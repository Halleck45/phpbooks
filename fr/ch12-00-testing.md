# Écrire des tests automatisés

Jusqu'ici, vous avez vérifié chaque programme de ce livre de la même façon : vous le lancez, vous regardez la sortie, vous hochez la tête. Pour un jeu de devinette, ça suffit. Ça cesse de suffire le jour où votre projet compte trente fonctions et où vous modifiez une ligne, parce que la question n'est plus « cette ligne marche-t-elle ? » mais « qu'est-ce que je viens de casser d'autre ? », et cette réponse-là ne tient dans aucune tête.

**Un test automatisé est une vérification que vous écrivez une fois et que l'ordinateur refait pour vous, à chaque fois, sans se lasser et sans oublier.** Vous décrivez ce qu'un morceau de code doit faire, et PHP vous dit s'il le fait toujours. Mille exécutions plus tard, il est aussi attentif qu'à la première.

<img src="images/ch12-tireless-checker.png" alt="Un programmeur entouré de bulles inquiètes qui demandent ce qui a pu casser, à côté de l'éléphant PHP qui coche tranquillement la même liste pour la millième fois" width="600">

Pensez au détecteur de fumée de votre cuisine. Vous ne reniflez pas l'air toutes les minutes ; vous installez un appareil qui le fait, et il ne se manifeste qu'en cas de problème. Les tests jouent ce rôle pour votre code. Le silence veut dire que tout marche encore.

PHP a un outil par défaut pour ce travail, et un seul : [PHPUnit](https://phpunit.de/). Il est le standard depuis près de vingt ans, presque toutes les bibliothèques et tous les frameworks du monde PHP l'utilisent en interne, et c'est un paquet Composer, qui s'installe comme vous l'avez appris au [chapitre 7](ch07-01-hello-composer.md).

Un premier test tient en dix lignes, et vous écrirez le vôtre dans quelques minutes. Choisir lesquels lancer, puis garder de l'ordre quand ils se multiplient, demande un peu plus de réflexion, et c'est à cela que sert le reste du chapitre. À la fin, tester ne sera plus une étape collée après coup sur du code fini, mais une partie de la façon dont vous l'écrivez. C'est l'habitude sur laquelle s'appuie le [chapitre 14](ch14-00-a-cli-project.md) quand il construit un petit projet en écrivant les tests d'abord.

> Un test, c'est une question que vous posez une fois à votre code. L'ordinateur continue de la poser à votre place.
