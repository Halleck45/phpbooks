# Livrer vite, à grande échelle

La plupart des fonctionnalités de ce livre tournent très bien sur du PHP ordinaire : un processus neuf par requête, une requête en base, une réponse, terminé. Puis le trafic grandit, ou une page se révèle lente, et « ça marche » cesse discrètement de suffire. **Ce chapitre s'adresse à la seconde phase, celle où la performance est devenue une exigence mesurée et non plus une inquiétude.**

<img src="images/ch15-bottleneck.png" alt="Une suite de larges tuyaux avec un court tronçon étroit devant lequel des gouttes font la queue. Un petit éléphant muni d'un chronomètre pointe le tronçon étroit, pendant qu'une personne s'apprête à resserrer une vanne sur une partie large du tuyau" width="560">

Trois des quatre pages sont des remèdes. Lisez la quatrième en premier : elle vous dit de quel remède vous avez besoin.

- [FrankenPHP et Laravel Octane : les performances du mode worker](ch15-01-frankenphp-laravel-octane.md) : garder l'application démarrée en mémoire entre les requêtes au lieu de la reconstruire à chaque fois.
- [TYPO3 : le framework de cache intégré](ch15-02-typo3-caching-framework.md) : un cache en couches avec invalidation ciblée, livré avec une grande plateforme de contenu.
- [Nextcloud : faire grandir une plateforme auto-hébergée](ch15-03-nextcloud-scaling.md) : ce qui change quand une application PHP auto-hébergée passe d'une équipe à toute une organisation.
- [Blackfire ($) : trouver le vrai goulot d'étranglement](ch15-04-blackfire-profiling.md) : mesurer où part le temps avant de corriger quoi que ce soit.
