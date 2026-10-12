# C - Index des encadrés « Sous le capot »

Chaque aparté optionnel de ce livre, dans l'ordre de lecture, pour le jour où l'un d'eux vous est resté en tête et où vous voulez le retrouver.

| Chapitre | Ce qu'il explique |
|---|---|
| [Framework, CMS ou headless ?](ch01-01-framework-cms-or-headless.md) | Pourquoi frameworks, CMS et outils d'API partagent les mêmes traits du langage sous des emballages différents |
| [Un premier projet](ch01-02-scaffolding-a-first-project.md) | La résolution des dépendances et l'autoloading de Composer |
| [Symfony/Console](ch02-01-symfony-console-standalone.md) | Les commandes console comme simples classes PHP, sans runtime spécial |
| [Guzzle](ch02-02-guzzle-http-client.md) | PSR-7 et PSR-18, les interfaces qui font coopérer les clients HTTP |
| [League/Plates](ch02-03-league-plates-standalone.md) | Pourquoi des templates en PHP pur n'ont pas besoin d'étape de compilation |
| [Monolog](ch02-04-monolog-standalone.md) | PSR-3, l'interface standard de journalisation |
| [Respect/Validation](ch02-05-respect-validation.md) | Des bibliothèques de validation qui s'appuient sur le système de types de PHP |
| [League/Flysystem](ch02-06-league-flysystem-standalone.md) | Le polymorphisme par interface appliqué au stockage |
| [Thèmes de blocs WordPress](ch03-01-wordpress-block-themes.md) | Des blocs stockés en HTML structuré, pas en templates PHP |
| [Contenu structuré TYPO3](ch03-02-typo3-structured-content.md) | Le TCA comme génération d'interface pilotée par des métadonnées |
| [Statamic](ch03-03-statamic-flat-file-cms.md) | Des fichiers plats, les fonctions de fichiers de PHP et du cache à la place du SQL |
| [Craft CMS](ch03-04-craft-cms.md) | L'accès dynamique aux propriétés derrière des champs de contenu flexibles |
| [Laravel Breeze/Fortify](ch04-01-laravel-breeze-fortify.md) | Pourquoi le hachage des mots de passe est lent exprès (bcrypt/argon2id) |
| [Symfony Security](ch04-02-symfony-security-bundle.md) | L'attribut `#[IsGranted]` et la réflexion |
| [Rôles WordPress](ch04-03-wordpress-roles-capabilities.md) | Des capacités qui sont de simples chaînes, pas un moteur de permissions formel |
| [Laravel Filament](ch05-01-laravel-filament.md) | Des objets fluides et chaînables rendus possibles par les arguments nommés et les enums |
| [Symfony EasyAdmin/Sonata](ch05-02-symfony-easyadmin.md) | Lire les métadonnées d'entité Doctrine pour déduire les types de champs |
| [API Platform Admin](ch05-03-api-platform-auto-admin.md) | Générer un schéma OpenAPI/Hydra à partir d'attributs |
| [WordPress CPT en CRUD](ch05-04-wordpress-cpt-as-crud.md) | Tous les types de contenu dans une seule table `wp_posts` |
| [Laravel Nova](ch05-05-laravel-nova.md) | Pourquoi une licence payante ne change rien au mécanisme des paquets |
| [API Platform depuis une classe](ch06-01-api-platform-from-one-class.md) | Attributs et réflexion qui engendrent routage, validation et documentation |
| [Laravel Sanctum](ch06-02-laravel-sanctum-resources.md) | Pourquoi les jetons ne sont pas hachés comme les mots de passe |
| [API REST WordPress](ch06-03-wordpress-rest-api.md) | L'API REST construite sur les hooks et les filtres de WordPress |
| [Laravel Reverb/Livewire](ch07-01-laravel-reverb-livewire.md) | Les Fibers de PHP, et comment elles rendent possible un serveur WebSocket |
| [Symfony Mercure/Turbo](ch07-02-symfony-ux-turbo-mercure.md) | Les Server-Sent Events, une simple fonctionnalité HTTP |
| [Nextcloud Talk](ch07-03-nextcloud-talk.md) | Le système d'applications de Nextcloud et les conventions d'autoloading de PHP |
| [Pusher](ch07-04-pusher-managed-websockets.md) | Pourquoi une bonne abstraction rend réversible le choix « héberger ou payer » |
| [Stockage Nextcloud](ch08-01-nextcloud-ready-made-drive.md) | Envois par morceaux et ETags pour une synchronisation efficace |
| [Laravel Storage/S3](ch08-02-laravel-filesystem-s3.md) | URL présignées et signatures cryptographiques |
| [Médiathèque WordPress](ch08-03-wordpress-media-library.md) | La génération immédiate des vignettes avec GD/Imagick |
| [WooCommerce](ch09-01-woocommerce.md) | Des données de commerce modélisées dans les mêmes tables `wp_posts`/`wp_postmeta` |
| [Sylius](ch09-02-sylius.md) | Assemblé à partir de composants Symfony réutilisables, pas réinventé |
| [Laravel Cashier/Stripe](ch09-03-laravel-cashier-stripe.md) | Vérifier la signature d'un webhook avant de faire confiance à son contenu |
| [Laravel Scout](ch10-01-laravel-scout-meilisearch.md) | Une interface de pilote qui rend les moteurs de recherche interchangeables |
| [TYPO3 Solr](ch10-02-typo3-solr-elasticsearch.md) | Reproduire les permissions des pages dans l'index de recherche |
| [Recherche WordPress](ch10-03-wordpress-search-plugins.md) | `WP_Query` comme point d'accroche pour des moteurs de recherche plus malins |
| [Files d'attente Laravel](ch11-01-laravel-queues-horizon.md) | La sérialisation des jobs, et pourquoi ils doivent rester simples |
| [Symfony Messenger](ch11-02-symfony-messenger.md) | Router les messages vers leurs handlers grâce au système de types de PHP |
| [WP-Cron WordPress](ch11-03-wordpress-wp-cron-action-scheduler.md) | Pourquoi WP-Cron se déclenche au chargement des pages et non sur une horloge système |
| [Laravel Prism](ch12-01-laravel-prism-llm-clients.md) | Une interface de fournisseur, le même motif que les adaptateurs de Flysystem |
| [Symfony AI Bundle](ch12-02-symfony-ai-bundle.md) | L'injection de dépendances appliquée à un agent IA |
| [Extensions IA WordPress](ch12-03-wordpress-ai-plugins.md) | Pourquoi WordPress embarque son propre client HTTP portable |
| [Arbres multilingues TYPO3](ch13-01-typo3-multilingual-trees.md) | Des traductions comme enregistrements liés, pas comme colonnes supplémentaires |
| [WordPress Multisite/WPML](ch13-02-wordpress-multisite-wpml.md) | Deux réponses structurelles à deux problèmes différents |
| [Symfony Translation](ch13-03-symfony-translation-component.md) | Des fichiers de traduction compilés en tableaux PHP mis en cache |
| [Laravel Pest/Larastan](ch14-01-laravel-pest-larastan.md) | L'analyse statique qui raisonne sur les types déclarés sans exécuter le code |
| [Symfony PHPStan/Rector](ch14-02-symfony-phpunit-phpstan-rector.md) | Rector qui réécrit le code en analysant et modifiant son AST |
| [Tests WordPress](ch14-03-wordpress-phpunit-phpcs-wpscan.md) | L'isolation des tests par annulation de transaction |
| [SAST tous écosystèmes](ch14-04-cross-ecosystem-sast-ci-gates.md) | Analyse des flux de données contre vérification des types |
| [Sentry/Flare](ch14-05-sentry-flare-error-tracking.md) | Se brancher sur les gestionnaires d'exceptions et d'erreurs de PHP |
| [FrankenPHP/Octane](ch15-01-frankenphp-laravel-octane.md) | Le mode worker, image inversée des Fibers |
| [Cache TYPO3](ch15-02-typo3-caching-framework.md) | L'invalidation de cache par étiquettes |
| [Montée en charge Nextcloud](ch15-03-nextcloud-scaling.md) | Les adaptateurs de stockage, cette fois sous la pression de la croissance |
| [Blackfire](ch15-04-blackfire-profiling.md) | Le profilage par une extension du Zend Engine |
| [Laravel Forge/Vapor](ch16-01-laravel-forge-vapor.md) | L'absence d'état comme condition du déploiement serverless |
| [Hébergement cloud](ch16-02-cloud-hosting-aws-gcp-azure.md) | Le même processus PHP, quel que soit le cloud qui l'exécute |
| [Platform.sh](ch16-03-platform-sh.md) | L'infrastructure comme configuration versionnée |
| [Hébergement WordPress infogéré](ch16-04-wordpress-managed-hosting.md) | Le cache objet avec Redis/Memcached |
| [Nextcloud AIO](ch16-05-nextcloud-aio-docker.md) | L'orchestration de conteneurs par le motif du mastercontainer |
