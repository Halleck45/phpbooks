# Livrer de la confiance

« Ça marche sur ma machine » n'est pas une fonctionnalité. Le bug que votre utilisateur trouve à 23 h était déjà là sur votre machine ; simplement, personne ne le cherchait. **La confiance est une fonctionnalité, et elle a sa place dans chaque projet de ce livre, pas seulement dans ceux où il reste du temps à la fin.** Elle vient de trois vérifications qui tournent sans vous : une suite de tests qui attrape les régressions, un analyseur statique qui attrape des familles entières de bugs avant que le code ne s'exécute, et un scan qui signale une dépendance vulnérable avant qu'elle ne parte en production.

<img src="images/ch14-gates.png" alt="Un tapis roulant fait passer des caisses sous trois portiques marqués d'une coche, d'une loupe et d'un cadenas, vers un camion de livraison ouvert. Un petit éléphant retire du tapis une caisse fissurée avant le premier portique" width="560">

Chaque écosystème a ses propres portiques. Les deux dernières pages sont celles qui marchent partout.

- [Laravel : Pest, Larastan et `composer audit`](ch14-01-laravel-pest-larastan.md) : des tests qui se lisent comme des phrases, un vérificateur de types qui connaît Laravel, et un scan de vulnérabilités en une commande.
- [Symfony : PHPUnit, PHPStan/Psalm et Rector](ch14-02-symfony-phpunit-phpstan-rector.md) : les trois mêmes, plus un outil qui réécrit votre code pour la prochaine version majeure.
- [WordPress : PHPUnit, PHPCS/WPCS et WPScan](ch14-03-wordpress-phpunit-phpcs-wpscan.md) : des tests contre un vrai WordPress, un linter qui repère les sorties non échappées, et un scanner des failles connues des extensions.
- [Tous écosystèmes : SAST, analyse des dépendances et barrières en CI](ch14-04-cross-ecosystem-sast-ci-gates.md) : ce qui tourne à l'identique quelle que soit la stack, câblé pour qu'un build cassé ne puisse pas être fusionné.
- [Attraper l'erreur en production : Sentry et Flare ($)](ch14-05-sentry-flare-error-tracking.md) : le moment où la confiance doit dépasser votre suite de tests et atteindre ce que rencontrent les vrais utilisateurs.
