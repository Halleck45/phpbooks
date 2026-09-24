# D - Outils de développement utiles

Ce livre a déjà traité deux de ces outils en bonne et due forme. Les autres sont ceux à installer ensuite : pas une documentation exhaustive de chacun, juste de quoi savoir à quoi il sert et pourquoi les développeurs PHP en activité s'en donnent la peine.

## Composer

Traité à partir du [chapitre 7](ch07-01-hello-composer.md), puis en profondeur au [chapitre 16](ch16-00-more-about-composer.md). Gestion des dépendances et autoloading. Vous n'écrirez pas de PHP professionnellement sans lui et, arrivé à ce point du livre, vous ne l'avez d'ailleurs jamais fait.

## PHPUnit

Traité au [chapitre 12](ch12-00-testing.md). Le framework de test standard. Si un projet PHP a des tests, ce sont très probablement des tests PHPUnit.

## PHPStan et Psalm

Des outils d'analyse statique : ils lisent votre code sans l'exécuter et vous disent où il est faux, ou du moins où il est suspect. Tous deux comprennent le système de types de PHP plus strictement que PHP lui-même à l'exécution. Ils repèrent l'appel d'une méthode qui n'existe pas, un `null` passé là où le type dit qu'il ne peut pas l'être, un type de retour qui a discrètement cessé de correspondre à ce que la fonction renvoie. C'est exactement le territoire qu'effleure le [chapitre 11](ch11-03-generic-style-code.md) avec les génériques en docblock : le système de types de PHP ne sait pas exprimer « un tableau d'objets `User` », mais une annotation en docblock, lue par PHPStan ou Psalm, permet de vérifier cette promesse à votre place.

Aucun des deux n'est livré avec PHP. Les deux s'installent via Composer, tournent en intégration continue, et méritent d'être ajoutés à un projet dès le premier jour plutôt qu'après la mise en production des bugs qu'ils auraient attrapés.

```console
$ composer require --dev phpstan/phpstan
$ vendor/bin/phpstan analyse src
```

## PHP-CS-Fixer et PHP_CodeSniffer

Du contrôle de style : la question n'est pas « est-ce correct » mais « est-ce formaté comme l'équipe a décidé de formater ». Tous deux savent vérifier une base de code contre PSR-12 (le guide de style standard de PHP) et, plus utile encore, tous deux savent *corriger* les écarts automatiquement au lieu de simplement les lister.

```console
$ vendor/bin/php-cs-fixer fix src
```

Choisissez-en un, branchez-le dans votre éditeur ou dans un hook de pre-commit, et arrêtez les débats de style en revue de code : laissez l'outil se disputer à votre place.

## Xdebug

Un débogueur pas à pas et un profileur pour PHP. Au lieu de semer des `var_dump()` dans votre code et de le relancer, Xdebug vous laisse suspendre l'exécution sur un point d'arrêt, inspecter chaque variable en portée, et avancer ligne par ligne, depuis votre éditeur, en temps réel. Il profile aussi, en vous montrant exactement où une requête lente a passé son temps. Traité en détail, installation comprise, au [chapitre 13](ch13-02-xdebug.md).

## Éditeurs et IDE

PHP n'impose aucun éditeur, mais deux valent la peine d'être connus :

**PhpStorm** : un IDE conçu pour PHP, avec une compréhension profonde et intégrée du langage : refactoring, navigation, et une analyse statique en ligne qui rivalise avec PHPStan sans quitter l'éditeur. Commercial, gratuit pour les étudiants et les mainteneurs de projets open source.

**VS Code**, avec les extensions PHP (Intelephense ou le pack d'extensions PHP officiel) : gratuit, généraliste, et parfaitement capable une fois configuré. C'est vers lui que se tournent la plupart des développeurs PHP qui n'utilisent pas PhpStorm.

L'un comme l'autre est un bon choix. Ce qui compte, c'est d'en choisir un et de l'apprendre correctement, plutôt que de se battre avec un éditeur à moitié configuré en plus d'apprendre le langage.
