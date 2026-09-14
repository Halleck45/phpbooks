# Gérer la fin du script et le nettoyage

Tout script PHP se termine. La plupart du temps, il se termine en exécutant sa dernière ligne. Parfois, il se termine sur une erreur fatale que personne n'avait prévue. Dans les deux cas, il y a souvent quelque chose dont vous voulez être sûr en sortant : fermer un fichier, noter dans un journal que la requête est finie, envoyer une écriture en attente à la base de données. `try`/`finally`, vu au [chapitre 9](ch09-00-error-handling.md), couvre les cas ordinaires. Il ne couvre pas la vraie erreur fatale, celle qui arrête l'exécution net, sans exception à attraper. **Pour celle-là, PHP vous donne une prise sur le tout dernier instant de la vie du script.**

## `register_shutdown_function()`

```php
<?php

register_shutdown_function(function (): void {
    echo "Cleaning up before the script ends.\n";
});

echo "Doing regular work.\n";

// Simulate something going badly wrong.
strlen(); // fatal error: too few arguments
```

```console
$ php shutdown_demo.php
Doing regular work.
Cleaning up before the script ends.
Fatal error: Uncaught ArgumentCountError: strlen() expects exactly 1 argument, 0 given...
```

Regardez l'ordre de cette sortie : le message de nettoyage arrive avant l'erreur fatale. **La fonction de shutdown s'exécute à la toute fin de la requête, quelle que soit la façon dont le script y est arrivé** : après un retour normal, après une exception non attrapée, après la plupart des erreurs fatales. Vous enregistrez le callback une fois, vers le haut de votre application (en vrai, dans le code d'amorçage d'un framework), et PHP promet de l'exécuter en sortant. C'est ce que PHP a de plus proche de « quoi qu'il arrive, exécute ceci en dernier ».

Essayez : remplacez la ligne `strlen();` par `exit;`, puis par `throw new RuntimeException('boom');`. La ligne de nettoyage apparaît à chaque fois.

<img src="images/ch21-shutdown-hook.png" alt="Trois façons pour un script de finir, sa dernière ligne, une exception non attrapée ou une erreur fatale, convergent vers la même porte marquée shutdown, où le nettoyage s'exécute avant que la requête ne disparaisse" width="600">

## Là où la vie d'un script se termine vraiment

C'est le modèle de requête sans partage du [chapitre 18](ch18-01-request-model.md), vu depuis la fin. Dans le cycle de vie traditionnel de PHP, la « fin » d'un script est un instant précis : la réponse a été envoyée, et le processus (ou le thread) qui a pris en charge cette requête est sur le point d'être recyclé ou démonté pour la suivante. Tout ce que le script a alloué (variables, objets, descripteurs de fichiers gérés par PHP lui-même) est nettoyé dans ce démontage, fonctions de shutdown comprises. Il n'y a pas de processus qui dure et dans lequel la mémoire pourrait fuir, comme peut le faire un serveur Node.js qui tourne depuis des semaines. **Chaque requête part d'une page blanche, et le désordre de chaque requête, nettoyé ou non, meurt avec elle.**

C'est aussi pour cela que `register_shutdown_function()` veut dire plus, en PHP, que « s'exécute à la fin ». Ce n'est pas une tâche de fond, et ce n'est pas remis à plus tard comme l'est une tâche mise en file d'attente au chapitre 18. Elle s'exécute de manière synchrone, en ligne, avant que l'histoire de cette requête précise ne soit close. Voilà ce qui en fait le bon endroit pour « noter que cette requête s'est terminée » ou « libérer le verrou que cette requête tenait », et le mauvais endroit pour tout ce qui devrait se passer indépendamment de cette requête.

> Une fonction de shutdown, c'est la dernière chose que fait cette requête. Pas quelque chose qui se passe plus tard.

## Où vous en êtes

Regardez ce que ce projet a utilisé : un routeur fait d'un tableau et d'une poignée de `if`, des contrôleurs qui sont de simples classes avec des méthodes, une couche de vues dans le même style PHP-dans-du-HTML que la première page du livre, et une fonction de shutdown qui boucle le cycle de vie d'une requête. Rien de tout cela n'a demandé de framework. **Tout cela est, en miniature, ce qu'un framework fournit à grande échelle.**

Vous avez commencé ce livre avec `echo "Hello, world!\n";`, à peu près le plus petit programme qui existe. Vous le terminez en assemblant des classes, des espaces de noms, des interfaces, la gestion des erreurs et le cycle de vie d'une requête en quelque chose qui sert des pages web. La syntaxe entre les deux n'a jamais été le sujet. Le sujet, c'était le discernement qui fait prendre la bonne pièce au bon moment, et ce discernement est la seule chose qu'aucun livre ne peut finir pour vous. Il vient en écrivant plus de PHP que vous n'en avez écrit jusqu'ici.

Allez en écrire.
