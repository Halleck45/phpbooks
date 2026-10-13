# Annexe A : Sources

Chaque chiffre et chaque affirmation sourcée de ce livre figure ci-dessous, rangé sous le chapitre où il apparaît, avec son éditeur, son URL et la date à laquelle la donnée se rapporte ou a été vérifiée. Quand un chiffre vient d'une page recalculée en continu (W3Techs, Packagist), la date est celle de la consultation et non celle d'une publication, et le chapitre le précise à l'endroit où il cite le chiffre.

Quelques entrées portent la mention **en attente de vérification directe**. Au moment de l'écriture, chacune n'avait été confirmée que par un extrait de moteur de recherche ou par un récit de seconde main, sans lecture directe de la page d'origine, et chacune est rédigée dans son chapitre de façon assez étroite pour ne pas dépendre d'un chiffre précis encore non confirmé. Je les laisse ici plutôt que de les supprimer en silence, pour que la personne qui achèvera la production du livre sache exactement ce qui reste à vérifier avant publication.

## Chapitre 1 : La réputation

- Part de PHP parmi les sites dont le langage côté serveur est connu : 69,9 %, vérifié le 17 septembre 2026 ; 71,8 % en mars 2026 ; 70,2 % le 3 septembre 2026. W3Techs, [w3techs.com/technologies/details/pl-php](https://w3techs.com/technologies/details/pl-php).

## Chapitre 2 : Le runtime

- Modèle d'exécution de PHP (Zend Engine, une requête par processus ou par thread, shared-nothing par défaut). Le manuel PHP, version courante, vérifié le 17 septembre 2026.
- Opcache livré avec PHP depuis la version 5.5 ; chargé comme `zend_extension` dans `php.ini`, inactif par défaut avec le seul cœur. [php.net/manual/en/opcache.installation.php](https://php.net/manual/en/opcache.installation.php), vérifié le 17 septembre 2026.
- Benchmark WordPress de la RFC du JIT elle-même : 326 requêtes par seconde avec le JIT, contre 315 sans. RFC JIT de PHP, [wiki.php.net/rfc/jit](https://wiki.php.net/rfc/jit), vérifié le 17 septembre 2026.
- `declare(strict_types=1)` et comportement du contrôle des types scalaires et des types de retour. Le manuel PHP, version courante, vérifié le 17 septembre 2026.
- Mode worker de FrankenPHP : superglobales réinitialisées automatiquement entre deux requêtes, sauf `$_ENV` ; la documentation du projet indique elle-même « PHP was not originally designed for long-running processes » et recommande de redémarrer périodiquement les workers. [frankenphp.dev/docs/worker/](https://frankenphp.dev/docs/worker/), vérifié le 17 septembre 2026.
- RoadRunner, serveur d'applications écrit en Go qui gère un pool de workers PHP de longue durée. **En attente de vérification directe** de [docs.roadrunner.dev](https://docs.roadrunner.dev) ; la description actuelle vient d'un comparatif tiers, pas de la documentation du projet.
- AMPHP, famille de bibliothèques fondées sur une boucle d'événements pour la concurrence limitée par les entrées-sorties, décrite en termes généraux et non citée. **En attente de vérification directe** du README de [github.com/amphp/amp](https://github.com/amphp/amp) ; pas revérifié de façon indépendante lors de cette passe.
- ReactPHP, qui se décrit comme une bibliothèque bas niveau fondée sur une boucle d'événements, pour la programmation événementielle. README de [github.com/reactphp/reactphp](https://github.com/reactphp/reactphp), vérifié le 17 septembre 2026.
- Swoole, qui se décrit comme un moteur de concurrence événementiel à base de coroutines, écrit en C pour PHP. README de [github.com/swoole/swoole-src](https://github.com/swoole/swoole-src), vérifié le 17 septembre 2026.
- Fibers (PHP 8.1) : coroutines coopératives à pile unique via `Fiber::suspend()` et `Fiber::resume()`, de la concurrence sans parallélisme au niveau du système d'exploitation. [php.net/manual/en/language.fibers.php](https://php.net/manual/en/language.fibers.php), vérifié le 17 septembre 2026.
- `parallel` et `pthreads`, extensions PECL tierces qui offrent un vrai parallélisme par threads du système. PECL et le manuel PHP, référence générale, vérifiés le 17 septembre 2026.

## Chapitre 3 : Qui fait tourner PHP

- Chiffre d'adoption de W3Techs : voir l'entrée du chapitre 1 ci-dessus.
- Stack Overflow Developer Survey 2025 : PHP 19,1 %, JavaScript 68,8 %, Python 54,8 %, TypeScript 48,8 %, C# 29,9 %, Java 29,6 %, Go 17,4 %, Ruby 6,9 %, sur 24 759 répondants développeurs professionnels. [survey.stackoverflow.co/2025/technology](https://survey.stackoverflow.co/2025/technology), vérifié le 17 septembre 2026.
- MediaWiki, écrit à environ 70 % en PHP, soit près de deux millions de lignes de PHP maintenues par Wikimedia, réparti sur sept centres de données (trois aux États-Unis, deux en Europe, un en Asie, un en Amérique du Sud) derrière Varnish, Apache Traffic Server et Apache HTTP Server, avec APCu et Memcached comme caches. Wikimedia, [wikitech.wikimedia.org/wiki/MediaWiki_at_WMF](https://wikitech.wikimedia.org/wiki/MediaWiki_at_WMF) et [wikitech.wikimedia.org/wiki/Wikimedia_infrastructure](https://wikitech.wikimedia.org/wiki/Wikimedia_infrastructure), pages tenues à jour en continu, consultées le 17 septembre 2026.
- Meta et Slack font tourner Hack sur HHVM, pas PHP. **En attente de vérification directe** auprès des publications techniques actuelles de chacune des deux entreprises ; tenu pour un fait établi pour appliquer la règle d'exclusion du livre.

## Chapitre 4 : Performances

- TechEmpower Framework Benchmarks arrêté le 24 mars 2026, dépôt archivé ; dernière édition complète, le Round 23, publiée le 17 mars 2025, couvrant plus de 330 implémentations de frameworks. [techempower.com/blog/2025/03/17/framework-benchmarks-round-23/](https://techempower.com/blog/2025/03/17/framework-benchmarks-round-23/) et [github.com/TechEmpower/FrameworkBenchmarks](https://github.com/TechEmpower/FrameworkBenchmarks) (archivé), vérifiés le 17 septembre 2026.
- Benchmark WordPress de la RFC du JIT : voir l'entrée du chapitre 2 ci-dessus.
- Computer Language Benchmarks Game : PHP 8.4.1 contre Python 3.13, version 25.03 de la suite, PHP plus rapide sur fannkuch-redux, n-body et spectral-norm d'un facteur 1,5 à 2 environ. [benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/python3-php.html](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/python3-php.html), vérifié le 17 septembre 2026.

## Chapitre 5 : Montée en charge

- Modèle de processus de PHP-FPM, à base de workers et shared-nothing. [php.net/manual/en/install.fpm.php](https://php.net/manual/en/install.fpm.php), vérifié le 17 septembre 2026.
- Répartition des centres de données de Wikimedia : voir l'entrée du chapitre 3 ci-dessus.

## Chapitre 6 : Qui fait vivre PHP

- JetBrains, « The State of PHP 2025 » : 1 720 répondants spécifiquement PHP sur 24 534 développeurs interrogés au total, enquête menée d'avril à juin 2025, avec la réserve de l'enquête elle-même : les résultats peuvent pencher vers les utilisateurs des produits JetBrains. Chiffres utilisés : 88 % ont au moins trois ans d'expérience en PHP ; 58 % ne prévoient pas de migrer vers un autre langage dans l'année (Go et Python sont les plus cités par ceux qui le feraient) ; versions déclarées : 89 % PHP 8.x, 33 % 7.x, 8 % 5.6 ou antérieure ; PHPStan utilisé par 36 %, soit 9 points de plus en un an ; PHPUnit 50 % ; Pest 17 % ; 32 % déclarent ne pas avoir de tests automatisés ; 42 % déclarent ne pas faire d'analyse statique. [blog.jetbrains.com/phpstorm/2025/10/state-of-php-2025/](https://blog.jetbrains.com/phpstorm/2025/10/state-of-php-2025/), vérifié le 17 septembre 2026.
- Résolution des dépendances de Composer par fichier de verrouillage, comme garantie de reproductibilité. Documentation de [getcomposer.org](https://getcomposer.org), référence générale, vérifiée le 17 septembre 2026.

## Chapitre 7 : Coût

- La licence PHP version 3.01 s'applique à PHP 8.4 et 8.5 ; la licence version 4 (BSD modifiée, BSD-3-Clause) s'applique à partir de PHP 8.6. [php.net/license/index.php](https://php.net/license/index.php), vérifié le 17 septembre 2026.
- Statistiques de Packagist : environ 468 201 paquets publiés, 5 822 307 versions publiées et environ 199,8 milliards d'installations cumulées depuis le 13 avril 2012. [packagist.org/statistics](https://packagist.org/statistics), vérifié le 17 septembre 2026, compteur en direct.
- Contrôle des installations de Composer par empreinte, à partir du fichier de verrouillage du projet. Documentation de [getcomposer.org](https://getcomposer.org), référence générale, vérifiée le 17 septembre 2026.
- Exigences d'hébergement minimales de PHP-FPM : voir l'entrée du chapitre 5 ci-dessus.
- `password_hash` et `password_verify`, l'API standard de hachage des mots de passe. [php.net/manual/en/function.password-hash.php](https://php.net/manual/en/function.password-hash.php), version courante, vérifié le 17 septembre 2026.
- Liaisons Libsodium livrées avec PHP depuis la version 7.2. [php.net/manual/en/book.sodium.php](https://php.net/manual/en/book.sodium.php), version courante, vérifié le 17 septembre 2026.
- Requêtes préparées de PDO, qui séparent la structure de la requête des données. [php.net/manual/en/pdo.prepared-statements.php](https://php.net/manual/en/pdo.prepared-statements.php), version courante, vérifié le 17 septembre 2026.

## Chapitre 8 : Gouvernance et versions

- Rythme de publication et durées de support : une version porteuse de nouvelles fonctionnalités par an, fin novembre ; deux ans de support actif, puis deux ans de correctifs de sécurité seulement. PHP 8.2 sorti le 8 décembre 2022 (support actif terminé le 31 décembre 2024, support de sécurité jusqu'au 31 décembre 2026) ; PHP 8.3 sorti le 23 novembre 2023 (actif jusqu'au 31 décembre 2025, sécurité jusqu'au 31 décembre 2027) ; PHP 8.4 sorti le 21 novembre 2024 (actif jusqu'au 31 décembre 2026, sécurité jusqu'au 31 décembre 2028) ; PHP 8.5 sorti le 20 novembre 2025 (actif jusqu'au 31 décembre 2027, sécurité jusqu'au 31 décembre 2029). [php.net/supported-versions.php](https://php.net/supported-versions.php), vérifié le 17 septembre 2026.
- Processus RFC : proposition et vote sur le wiki public, majorité des deux tiers requise pour un changement du langage. **En attente de vérification directe** de [wiki.php.net/rfc/change_required_votes_to_two_thirds](https://wiki.php.net/rfc/change_required_votes_to_two_thirds) pour la formulation exacte et la date d'adoption.
- Création de la PHP Foundation en novembre 2021. **En attente de vérification directe** du récit fondateur publié par la Foundation sur [thephp.foundation](https://thephp.foundation) ; le récit utilisé ici vient du billet de blog d'un sponsor, pas de la page d'histoire de la Foundation.
- Un registre public des financements, qui enregistre les contributions régulières de plusieurs organisations indépendantes. **En attente de vérification directe** des totaux cumulés actuels sur [opencollective.com/phpfoundation](https://opencollective.com/phpfoundation) ; le livre mentionne l'existence et la transparence du registre sans imprimer de montants qui n'ont pas été confirmés directement.
- Un processus propre au traitement des signalements de sécurité sur le cœur du langage, distinct du processus RFC des fonctionnalités. **En attente de vérification directe** de [php.net/security](https://php.net/security).
- Fragmentation des versions selon W3Techs : PHP 8.x 64,1 %, 7.x 28,1 %, 5.x 7,8 %, 4.x 0,1 % des sites sous PHP. [w3techs.com/technologies/details/pl-php](https://w3techs.com/technologies/details/pl-php), vérifié le 17 septembre 2026.

## Chapitre 9 : Là où PHP est le mauvais choix

- Fibers, `parallel` et `pthreads` : voir les entrées du chapitre 2 ci-dessus.
- Comparaison PHP contre Python sur des calculs limités par le CPU : voir l'entrée du chapitre 4 ci-dessus.
- NativePHP, projet communautaire construit sur Laravel, qui empaquette des applications PHP pour les boutiques d'applications de bureau et mobiles ; sa documentation revendique des déploiements en production en 2026. [nativephp.com/docs/](https://nativephp.com/docs/), vérifié le 17 septembre 2026.
- Absence d'équivalent PHP à NumPy, pandas, PyTorch ou TensorFlow : un constat sur la densité de l'écosystème, que l'on vérifie directement avec la recherche par catégorie de Packagist et l'index des extensions de PHP plutôt qu'avec une citation datée unique.
- Position de FrankenPHP lui-même sur les processus de longue durée : voir l'entrée du chapitre 2 ci-dessus.
- PHPStan et Psalm simulent tous deux les génériques par une convention commune de docblock `@template`, que seule l'analyse statique fait respecter, pas le moteur du langage. **En attente de vérification directe** de [phpstan.org/writing-php-code/generics](https://phpstan.org/writing-php-code/generics) et de [psalm.dev/docs/annotating_code/templated_annotations/](https://psalm.dev/docs/annotating_code/templated_annotations/) ; la source actuelle est de seconde main.
- Fragmentation des versions selon W3Techs : voir l'entrée du chapitre 8 ci-dessus.

## Chapitre 10 : L'évaluation

Aucun chiffre nouveau. Ce chapitre refait les mesures à partir des sources vivantes déjà listées ci-dessus : [w3techs.com/technologies/details/pl-php](https://w3techs.com/technologies/details/pl-php), [survey.stackoverflow.co](https://survey.stackoverflow.co), [benchmarksgame-team.pages.debian.net/benchmarksgame](https://benchmarksgame-team.pages.debian.net/benchmarksgame), [github.com/php/php-src](https://github.com/php/php-src), [packagist.org/statistics](https://packagist.org/statistics) et [php.net/supported-versions.php](https://php.net/supported-versions.php). Le script de contrôle du runtime utilise `PHP_VERSION`, `PHP_SAPI` et `opcache_get_status()`, tous documentés dans le manuel PHP, version courante, vérifié le 17 septembre 2026.
