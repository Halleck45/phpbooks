# Introduction

On vous a confié une base de code PHP, que vous l'ayez demandée ou non. Vous ouvrez le premier fichier, vous y trouvez `$this->`, des `->`, des `::` et une fonction qui s'appelle `htmlspecialchars`, et vous vous demandez si c'est bien le langage dont tout le monde vous a dit du mal.

En bonne partie, oui, mais pas celui d'aujourd'hui. **Le PHP dont on vous a parlé a existé, et il a presque entièrement disparu.** Ce qui reste est un langage typé, orienté objet, avec ramasse-miettes, un gestionnaire de paquets, un style de code standardisé, un écosystème d'analyse statique sérieux, une version par an chaque novembre, et un modèle d'exécution qui ne ressemble à rien de ce que vous avez utilisé jusqu'ici. Ce modèle d'exécution est la seule chose que vous ayez vraiment à apprendre.

## Ce qui était vrai

PHP est né en 1995 comme un jeu de gabarits avec un peu de logique dedans, et pendant sa première décennie il a été permissif jusqu'à l'absurde. Les variables apparaissaient de nulle part, `"abc" == 0` valait vrai, les erreurs s'imprimaient dans la page et l'exécution continuait, les requêtes SQL se construisaient par concaténation, et la bibliothèque standard s'est assemblée une fonction à la fois, au gré des besoins de chacun, ce qui explique que `strpos` voisine avec `str_replace` et `array_key_exists` avec `in_array`.

Toute une génération a appris à programmer sur ce PHP-là, en a écrit énormément, et une bonne partie de ce code tourne encore. C'est de ce PHP que parlent les blagues.

## Ce qui a changé

PHP 7 (2015) a doublé les performances et ajouté les déclarations de types scalaires. PHP 8 (2020) a apporté un vrai système de types avec les types union, `match`, les arguments nommés, les attributs, les énumérations, `readonly`, les callables de première classe et un compilateur JIT. PHP 8.4 a ajouté les hooks de propriété et la visibilité asymétrique, et PHP 8.5 un opérateur pipe. Dans le même mouvement, les règles de comparaison ont été corrigées, les propriétés dynamiques dépréciées, les vieilles fonctions `mysql_*` supprimées, et l'interpréteur lève désormais une `TypeError` là où il devinait.

<img src="images/ch00-two-phps.png" alt="Deux éléphants côte à côte : à gauche un vieil éléphant poussiéreux et rapiécé, assis sur un tas de code spaghetti emmêlé ; à droite un éléphant moderne et élancé, avec un nœud papillon, debout sur des boîtes bien étiquetées" width="560">

Autour du langage, la communauté a construit Composer, le gestionnaire de paquets que tout projet utilise ; les standards du PHP-FIG, pour que les bibliothèques d'auteurs différents s'emboîtent ; PHPUnit et Pest pour les tests ; PHPStan et Psalm, deux analyseurs statiques qui vous donnent l'essentiel de ce qu'un compilateur donnerait ; et Rector, qui réécrit le vieux code en syntaxe moderne. Depuis 2021, la PHP Foundation salarie des développeurs du cœur du langage, pour que son avenir ne dépende plus des soirées de bénévoles.

## Ce qui pique encore

Tout n'a pas été corrigé, et un livre pour gens pressés doit le dire d'emblée. Les chaînes sont des suites d'octets, donc `strlen('é')` vaut 2 et il vous faut les fonctions `mb_` dès qu'il s'agit de texte. La bibliothèque standard garde ses noms et ses ordres d'arguments incohérents, `==` convertit toujours ses opérandes, quoique bien moins sauvagement qu'avant, le typage strict est un interrupteur par fichier qu'il faut activer, les tableaux se copient à l'affectation, et le langage lui-même n'a pas de génériques. Chacun de ces points a une pratique moderne qui le neutralise, et chacun est traité au chapitre où vous le rencontrerez.

> La réputation de PHP est restée en 2010, alors que le langage a continué d'avancer.

## L'idée à saisir en premier

**Une requête web PHP démarre sans rien, exécute votre code de haut en bas, envoie sa réponse et jette tout.** Il n'y a pas de mémoire partagée entre les requêtes, pas d'objet application qui reste en vie, pas de boucle d'événements et pas de threads : le serveur web tend une requête à PHP, PHP produit une réponse, puis oublie tout ce qu'il vient de faire.

Si vous venez de Node, de Java, de Go ou d'un serveur Python ASGI, c'est la différence la plus importante, et la plupart des idiomes PHP en découlent : l'absence de pool de connexions par défaut, « l'état global » qui n'est qu'une notion par requête, le plantage qui n'affecte qu'un visiteur, la montée en charge par ajout de processus, l'existence d'OPcache, et les serveurs PHP persistants comme FrankenPHP ou RoadRunner qui forment un sujet à part entière. [Comment PHP s'exécute](ch01-how-php-runs.md) traite tout cela, et c'est le seul chapitre à ne pas sauter.

## Comment lire ce livre

Chaque chapitre répond à une question et se suffit à lui-même. Les phrases en gras portent le fil : en ne lisant que celles-là, vous obtenez le delta entre PHP et ce que vous connaissez déjà. Les blocs de code vous donnent la syntaxe, et le reste du texte est là pour le jour où un détail compte pour vous.

Les comparaisons avec Python, JavaScript, Java et quelques autres langages sont des points de repère, pas des traductions, et vous pouvez sauter celles des langages que vous ne connaissez pas sans rien perdre de l'explication.

Chaque exemple tourne sur une installation nue de PHP avec `php fichier.php`, sans framework ni bibliothèque, pour que la leçon porte sur PHP lui-même. Installez d'abord PHP : votre gestionnaire de paquets l'a, php.net liste les builds officiels, et l'image Docker officielle est `php:8.5-cli`. Gardez ensuite un terminal ouvert et exécutez ce que vous lisez.

Trois chapitres s'adressent à un lecteur en particulier. [Revenir à PHP après des années](ch14-returning-developer.md) fait correspondre les vieilles habitudes aux pratiques modernes, pour ceux qui reviennent au langage. [Venir de Python, JavaScript ou Java](appendix-01-cheat-sheet.md) est une table de correspondance, et [PHP 8.0 à 8.5 en un coup d'œil](appendix-02-versions.md) vous dit ce que la version PHP de votre projet sait faire.

Dans deux ou trois heures, la base de code que vous avez ouverte aura changé d'aspect : pas forcément plus simple, mais lisible.
