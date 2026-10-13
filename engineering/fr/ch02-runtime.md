# Le runtime

**PHP exécute une requête par processus ou par thread, sur le Zend Engine, en mode *shared-nothing* par défaut : rien de ce que votre code met en mémoire ne survit à la réponse qu'il vient d'envoyer, sauf si vous changez explicitement de modèle de service pour garder l'application démarrée.** Cette phrase répond à la plupart des questions que vous vous posez sur le runtime. Elle mérite qu'on s'y arrête avant de lire la suite, car presque tout ce que PHP fait bien ou mal en découle.

Une exécution *shared-nothing*, où rien n'est partagé d'une requête à l'autre, signifie qu'une requête démarre l'application, exécute votre code et démonte le tout, à chaque fois. Une variable affectée, une connexion à la base ouverte, un cache réchauffé en mémoire : rien de cela n'existe pour la requête suivante, qui repart d'un démarrage propre. Ce n'est pas le retard d'un langage lent qui rattraperait son temps. C'est le modèle autour duquel PHP a été construit dès l'origine, et il vous apporte une propriété précise et précieuse. Une fuite mémoire dans une requête ne peut pas s'accumuler sur mille requêtes, puisqu'il n'existe aucune mémoire partagée où s'accumuler. Un plantage dans une requête ne peut pas corrompre l'état dont dépend la suivante, puisqu'il n'y a pas d'état partagé. Le prix est celui qu'on devine : rien n'est chaud. Chaque requête qui a besoin d'une connexion à la base en ouvre une, et chaque requête qui a besoin des routes et de la configuration de l'application les reconstruit, sauf si une couche située sous le langage met le résultat en cache.

Cette couche, c'est `opcache`. Le code source PHP est compilé en bytecode avant de s'exécuter, et par défaut cette compilation recommence à chaque requête, depuis zéro. Opcache, livré avec PHP depuis la version 5.5, garde le bytecode compilé en mémoire partagée pour que la requête suivante saute la recompilation. Dit précisément, et non comme on le décrit d'habitude : opcache est une `zend_extension`, et il faut le charger dans `php.ini` pour qu'il fasse quoi que ce soit. La plupart des distributions l'activent dans leurs paquets, mais PHP lui-même ne le fait pas. « PHP est rapide parce qu'il met le bytecode en cache » n'est donc vrai que pour une configuration précise et vérifiable, pas pour le langage tel qu'il s'installe.

<img src="images/ch02-runtime.png" alt="Un couloir d'hôtel avec trois chambres identiques : un client muni d'une enveloppe s'installe dans la première, un éléphant en tablier de femme de chambre défait et nettoie la deuxième, et la troisième, faite et vide, attend." width="560">

## Ce que le système de types impose vraiment

Les déclarations de types ajoutées depuis PHP 7 ne sont pas décoratives. Un fichier qui les active fait respecter ses contrats par le moteur lui-même, et pas seulement par un linter :

```php
<?php

declare(strict_types=1);

function total(float ...$prices): float
{
    return array_sum($prices);
}

total(9.99, "4.50"); // TypeError: total(): Argument #2 must be of type float, string given
```

Sans `declare(strict_types=1)`, PHP convertirait une chaîne numérique en nombre flottant et poursuivrait l'exécution. Avec, l'incohérence devient une `TypeError` à l'endroit exact où elle se produit, au lieu d'une corruption silencieuse trois fonctions plus loin. Voilà la version concrète et vérifiable de ce qu'annonçait [La réputation](ch01-introduction.md) : le système de types a changé. Il s'active fichier par fichier, et une fois activé, il est réel.

## Modèles de service : comment on contourne le *shared-nothing*

Trois façons de servir une application, par ordre alphabétique, couvrent l'essentiel de la production PHP aujourd'hui : FrankenPHP, PHP-FPM derrière un serveur web, et RoadRunner. PHP-FPM est le modèle historique. Un pool de processus workers traite chacun une requête à la fois, chaque processus est redémarré périodiquement, et aucun ne conserve l'état de l'application d'une requête à l'autre. C'est l'expression la plus pure du *shared-nothing*, et c'est encore le modèle que supposent par défaut la plupart des hébergements.

FrankenPHP et RoadRunner proposent tous deux un « mode worker » qui contourne volontairement ce comportement par défaut : l'application démarre une fois, reste en mémoire et traite de nombreuses requêtes à la suite sans redémarrage complet entre elles. La documentation de FrankenPHP le décrit sans détour, compromis compris. Les superglobales de PHP (`$_GET`, `$_POST`, `$_COOKIE`, `$_FILES`, `$_SERVER`, `$_REQUEST`) sont réinitialisées automatiquement entre deux requêtes, si bien qu'un worker ne laisse pas fuir les données de formulaire d'un visiteur dans la requête du suivant. En revanche, `$_ENV` n'est pas réinitialisée, et tout ce que votre propre code range délibérément hors d'une superglobale persiste tant que vous ne le videz pas vous-même. La documentation dit franchement pourquoi c'est important : selon ses termes, PHP « was not originally designed for long-running processes » (n'a pas été conçu à l'origine pour des processus de longue durée), et la parade habituelle consiste à redémarrer périodiquement les workers pour borner la mémoire qu'un processus de longue durée peut accumuler sans bruit. RoadRunner aborde la même idée par un autre côté : c'est un serveur d'applications écrit en Go qui gère un pool de workers PHP de longue durée, conservés d'une requête à l'autre au lieu d'être détruits après chacune.

## Le JIT : une vraie fonctionnalité, un bénéfice étroit

PHP 8.0 a ajouté un compilateur Just-In-Time, et la RFC qui l'a introduit est d'une franchise inhabituelle sur ce qu'il aide et n'aide pas. Le compilateur traduit à l'exécution les portions de code les plus sollicitées en code machine, ce qui accélère nettement le travail numérique limité par le CPU. Il apporte peu à une requête web ordinaire, dont le temps se passe à attendre une base de données ou le réseau plutôt qu'à calculer, et la RFC fournit son propre benchmark qui montre exactement cet écart sur une charge réaliste.

<div class="chart">

{{#include charts/ch04-jit.svg}}

</div>

Trois cent vingt-six requêtes par seconde avec le JIT, trois cent quinze sans, sur une requête WordPress. C'est une différence réelle et mesurée, de quelques pour cent, sur la charge que font tourner la plupart des installations PHP, et elle vient de la RFC qui a livré la fonctionnalité, pas d'un détracteur. Le JIT n'est pas rien : c'est lui qui explique l'allure des comparaisons sur le code numérique dans [Performances](ch04-performance.md). Ce n'est simplement pas lui qui rend plus rapide une application web écrite en PHP.

## La concurrence sans threads

Quatre options, dans l'ordre que je garderai tout au long du livre, couvrent la manière dont du code PHP obtient de la concurrence à l'intérieur d'un seul processus : AMPHP, ReactPHP, Swoole (ou OpenSwoole) et, en tant que fonctionnalité du langage plutôt que bibliothèque, les Fibers. AMPHP est un ensemble de bibliothèques bâties sur le même modèle de boucle d'événements que les deux suivantes, et vise la même famille de problèmes de concurrence liés aux entrées-sorties : beaucoup de choses en attente en même temps, prises en charge par un seul processus qui ne se bloque jamais entièrement sur l'une d'elles. ReactPHP se présente, dans sa propre documentation, comme une bibliothèque bas niveau fondée sur une boucle d'événements, destinée aux serveurs et aux clients qui doivent garder ouvertes de nombreuses connexions simultanées. Swoole se décrit comme un moteur réseau événementiel à base de coroutines, écrit en C pour PHP, qui transforme les appels d'entrées-sorties normalement bloquants de PHP en appels non bloquants sous son propre ordonnanceur. Les Fibers, arrivées avec PHP 8.1, sont coopératives : une fiber se suspend et reprend via `Fiber::suspend()` et `Fiber::resume()`, et le code d'une seule fiber s'exécute à un instant donné. Tout cela relève de la concurrence, c'est-à-dire la capacité à mener de front de nombreuses tâches logiques et à passer de l'une à l'autre pendant qu'une attend une entrée-sortie. Rien de cela n'est du parallélisme, la capacité à faire réellement tourner deux tâches au même instant sur deux cœurs.

> **La limite.** PHP n'offre pas de multithreading natif dans le code utilisateur. Les extensions PECL `parallel` et `pthreads` existent et apportent un vrai parallélisme par threads du système, mais elles sont tierces, peu adoptées, et il faut les présenter honnêtement comme « existantes, mais de niche », sans les fondre en silence dans le récit sur la concurrence ci-dessus ni les en retirer. Si votre charge a besoin de deux tâches limitées par le CPU qui tournent littéralement au même instant dans un seul processus, rien dans la liste de ce chapitre ne le fait, et [Là où PHP est le mauvais choix](ch09-wrong-choice.md) traite cette limite en entier.

**À vérifier vous-même.** Sur n'importe quelle machine où PHP est installé, lancez :

```bash
php -v
php -i | grep -i opcache
```

La première commande vous indique la version de PHP et, en général, la SAPI (FPM, CLI ou autre) à laquelle vous avez affaire. La seconde vous dit si opcache est réellement chargé sur cette installation précise, et non s'il pourrait théoriquement l'être. La page commerciale d'un hébergeur n'est pas une preuve ; un grep sur la sortie de votre propre `phpinfo()`, si.

Le modèle d'exécution décrit ici, *shared-nothing* par défaut, contournable par certaines couches de service, concurrent mais pas parallèle, est le socle de tout ce qui suit. La question suivante ne porte plus sur la façon dont PHP exécute une requête, mais sur ceux qui le font tourner, à quelle échelle et sur quelles preuves. C'est le sujet de [Qui fait tourner PHP](ch03-who-runs-php.md).
