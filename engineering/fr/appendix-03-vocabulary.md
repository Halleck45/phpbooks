# Annexe C : Vocabulaire

Les termes sont définis au sens où je les emploie, en langage courant, avec un renvoi au chapitre qui les explique en situation.

**Analyse statique.** Rechercher les erreurs d'un code, dont les incohérences de types, sans l'exécuter. PHPStan et Psalm sont les deux outils d'analyse statique cités dans ce livre ; tous deux simulent aussi les types génériques grâce à une convention commune de docblocks que le moteur du langage, lui, ne fait pas respecter. Voir [Qui fait vivre PHP](ch06-who-maintains-it.md) et [Là où PHP est le mauvais choix](ch09-wrong-choice.md).

**Composer.** Le gestionnaire de dépendances de PHP. Il résout les paquets demandés par un projet à partir de Packagist, note dans un fichier de verrouillage les versions exactes installées, et contrôle chaque installation par une empreinte, si bien qu'une dépendance ne peut pas changer en silence sous un projet après sa revue. Voir [Coût](ch07-cost.md).

**Coroutine.** Une unité d'exécution qui peut se mettre en pause et rendre la main, puis reprendre plus tard au même endroit, sans que le système d'exploitation la détruise et la reconstruise. Les Fibers de PHP et des bibliothèques comme ReactPHP et Swoole reposent sur cette idée. Voir [Le runtime](ch02-runtime.md).

**Fibers.** Une fonctionnalité du langage arrivée avec PHP 8.1, qui apporte la concurrence coopérative : une fiber se suspend avec `Fiber::suspend()` et reprend avec `Fiber::resume()`. Le code d'une seule fiber s'exécute à un instant donné ; c'est de la concurrence, pas du parallélisme. Voir [Le runtime](ch02-runtime.md).

**FPM (FastCGI Process Manager).** Le gestionnaire de processus standard de PHP : un pool de processus, chacun traitant une requête à la fois, chacun ne partageant rien avec les autres. C'est la façon classique, et la plus répandue, de servir une application PHP. Voir [Le runtime](ch02-runtime.md) et [Montée en charge](ch05-scale.md).

**JIT (compilation à la volée).** Arrivé avec PHP 8.0. Il traduit en code machine, pendant l'exécution, les portions de code les plus sollicitées. Le gain est net sur les calculs numériques limités par le CPU ; sur une requête web ordinaire, qui passe l'essentiel de son temps à attendre des entrées-sorties, il reste faible. Voir [Le runtime](ch02-runtime.md) et [Performances](ch04-performance.md).

**Mode worker.** Une façon de servir l'application, proposée par FrankenPHP et RoadRunner, qui garde l'application PHP démarrée en mémoire d'une requête à l'autre au lieu de la détruire après chacune. Les superglobales sont réinitialisées automatiquement entre deux requêtes ; tout ce que votre code conserve délibérément ne l'est pas, et c'est pourquoi le redémarrage périodique des workers est la parade standard, documentée, contre la mémoire qui grossit au fil d'un long processus. Voir [Le runtime](ch02-runtime.md).

**Opcache.** Une `zend_extension` livrée avec PHP depuis la version 5.5, qui garde en mémoire partagée le bytecode compilé pour ne pas le recompiler à chaque requête. Elle doit être chargée explicitement dans `php.ini` ; le cœur de PHP ne l'active pas tout seul. Voir [Le runtime](ch02-runtime.md).

**Packagist.** Le registre public de paquets dans lequel Composer résout les dépendances. Publier y est gratuit, s'en servir aussi. Voir [Coût](ch07-cost.md).

**PSR (PHP Standards Recommendation).** Une convention commune, que les auteurs de frameworks et de bibliothèques adoptent volontairement au terme d'un processus de normalisation, et que le langage n'impose pas. Les PSR couvrent par exemple le chargement automatique des classes, les interfaces de journalisation ou la forme des messages HTTP, pour que des bibliothèques écrites séparément fonctionnent ensemble à coup sûr. Voir [La réputation](ch01-introduction.md).

**RFC (Request for Comments).** Le processus public par lequel on propose puis vote une modification du langage lui-même, sur un wiki prévu à cet effet. Un changement du langage doit réunir une majorité des deux tiers. Voir [Gouvernance et versions](ch08-governance-and-versions.md).

**SAPI (Server API).** L'interface entre le moteur PHP et ce qui le fait tourner : FPM, la ligne de commande ou un autre module de serveur. `PHP_SAPI` indique sous laquelle tourne un processus donné. Voir [L'évaluation](ch10-the-evaluation.md).

**Shared-nothing.** Le modèle d'exécution par défaut de PHP, où rien n'est partagé d'une requête à l'autre : chaque requête démarre l'application, s'exécute, envoie sa réponse puis disparaît, sans transmettre ni mémoire ni état à la suivante. C'est ce qui rend la montée en charge horizontale si simple, et c'est pour cela que tout ce qui doit durer vit hors du processus PHP. Voir [Le runtime](ch02-runtime.md) et [Montée en charge](ch05-scale.md).
