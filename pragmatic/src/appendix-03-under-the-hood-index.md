# C - Index of "Under the Hood" Boxes

Every optional aside in this book, in reading order, in case one of them stuck with you and you want to go find it again.

| Chapter | What it covers |
|---|---|
| [Framework, CMS, or Headless?](ch01-01-framework-cms-or-headless.md) | Why frameworks, CMSes, and API tools share the same underlying language features underneath different packaging |
| [Scaffolding a First Project](ch01-02-scaffolding-a-first-project.md) | Composer's dependency resolution and autoloading |
| [Symfony/Console](ch02-01-symfony-console-standalone.md) | Console commands as plain PHP classes, no special runtime |
| [Guzzle](ch02-02-guzzle-http-client.md) | PSR-7 and PSR-18, the interfaces that let HTTP clients interoperate |
| [League/Plates](ch02-03-league-plates-standalone.md) | Why plain-PHP templates need no compile step |
| [Monolog](ch02-04-monolog-standalone.md) | PSR-3, the standard logging interface |
| [Respect/Validation](ch02-05-respect-validation.md) | Validation libraries leaning on PHP's own type system |
| [League/Flysystem](ch02-06-league-flysystem-standalone.md) | Interface-based polymorphism applied to storage |
| [WordPress Block Themes](ch03-01-wordpress-block-themes.md) | Blocks stored as structured HTML, not PHP templates |
| [TYPO3 Structured Content](ch03-02-typo3-structured-content.md) | TCA as metadata-driven UI generation |
| [Statamic](ch03-03-statamic-flat-file-cms.md) | Flat files, PHP's filesystem functions, and caching instead of SQL |
| [Craft CMS](ch03-04-craft-cms.md) | Dynamic property access powering flexible content fields |
| [Laravel Breeze/Fortify](ch04-01-laravel-breeze-fortify.md) | Why password hashing is deliberately slow (bcrypt/argon2id) |
| [Symfony Security](ch04-02-symfony-security-bundle.md) | The `#[IsGranted]` attribute and reflection |
| [WordPress Roles](ch04-03-wordpress-roles-capabilities.md) | Capabilities as plain strings, not a formal permissions engine |
| [Laravel Filament](ch05-01-laravel-filament.md) | Fluent, chainable objects enabled by named arguments and enums |
| [Symfony EasyAdmin/Sonata](ch05-02-symfony-easyadmin.md) | Reading Doctrine entity metadata to infer field types |
| [API Platform Admin](ch05-03-api-platform-auto-admin.md) | Generating an OpenAPI/Hydra schema from attributes |
| [WordPress CPT as CRUD](ch05-04-wordpress-cpt-as-crud.md) | Every post type sharing one `wp_posts` table |
| [Laravel Nova](ch05-05-laravel-nova.md) | Why a paid license changes nothing about the underlying package mechanism |
| [API Platform from One Class](ch06-01-api-platform-from-one-class.md) | Attributes plus reflection generating routing, validation, and docs |
| [Laravel Sanctum](ch06-02-laravel-sanctum-resources.md) | Why tokens are hashed differently than passwords |
| [WordPress REST API](ch06-03-wordpress-rest-api.md) | The REST API built on WordPress's hooks and filters |
| [Laravel Reverb/Livewire](ch07-01-laravel-reverb-livewire.md) | PHP Fibers, and how they make a WebSocket server possible |
| [Symfony Mercure/Turbo](ch07-02-symfony-ux-turbo-mercure.md) | Server-Sent Events as a plain HTTP feature |
| [Nextcloud Talk](ch07-03-nextcloud-talk.md) | Nextcloud's app system and PHP's own autoloading conventions |
| [Pusher](ch07-04-pusher-managed-websockets.md) | Why a good abstraction makes "self-host or pay" a reversible decision |
| [Nextcloud Storage](ch08-01-nextcloud-ready-made-drive.md) | Chunked uploads and ETags for efficient sync |
| [Laravel Storage/S3](ch08-02-laravel-filesystem-s3.md) | Pre-signed URLs and cryptographic signatures |
| [WordPress Media Library](ch08-03-wordpress-media-library.md) | Eager thumbnail generation via GD/Imagick |
| [WooCommerce](ch09-01-woocommerce.md) | Commerce data modeled on the same `wp_posts`/`wp_postmeta` tables |
| [Sylius](ch09-02-sylius.md) | Built from reusable Symfony components, not invented from scratch |
| [Laravel Cashier/Stripe](ch09-03-laravel-cashier-stripe.md) | Verifying webhook signatures before trusting a payload |
| [Laravel Scout](ch10-01-laravel-scout-meilisearch.md) | A driver interface making search engines swappable |
| [TYPO3 Solr](ch10-02-typo3-solr-elasticsearch.md) | Mirroring page permissions into the search index |
| [WordPress Search](ch10-03-wordpress-search-plugins.md) | `WP_Query` as the hook point for smarter search backends |
| [Laravel Queues](ch11-01-laravel-queues-horizon.md) | Job serialization and why jobs should stay simple |
| [Symfony Messenger](ch11-02-symfony-messenger.md) | Routing messages to handlers via PHP's type system |
| [WordPress WP-Cron](ch11-03-wordpress-wp-cron-action-scheduler.md) | Why WP-Cron triggers on page loads instead of a system timer |
| [Laravel Prism](ch12-01-laravel-prism-llm-clients.md) | A provider interface, the same pattern as Flysystem's adapters |
| [Symfony AI Bundle](ch12-02-symfony-ai-bundle.md) | Dependency injection applied to an AI agent |
| [WordPress AI Plugins](ch12-03-wordpress-ai-plugins.md) | Why WordPress ships its own portable HTTP client |
| [TYPO3 Multilingual Trees](ch13-01-typo3-multilingual-trees.md) | Translations as linked records, not extra columns |
| [WordPress Multisite/WPML](ch13-02-wordpress-multisite-wpml.md) | Two different structural solutions to two different problems |
| [Symfony Translation](ch13-03-symfony-translation-component.md) | Translation files compiled into cached PHP arrays |
| [Laravel Pest/Larastan](ch14-01-laravel-pest-larastan.md) | Static analysis reasoning over type hints without running code |
| [Symfony PHPStan/Rector](ch14-02-symfony-phpunit-phpstan-rector.md) | Rector rewriting code by parsing and modifying its AST |
| [WordPress Testing](ch14-03-wordpress-phpunit-phpcs-wpscan.md) | Test isolation via database transaction rollback |
| [Cross-Ecosystem SAST](ch14-04-cross-ecosystem-sast-ci-gates.md) | Data-flow analysis versus type-checking |
| [Sentry/Flare](ch14-05-sentry-flare-error-tracking.md) | Hooking into PHP's own exception and error handlers |
| [FrankenPHP/Octane](ch15-01-frankenphp-laravel-octane.md) | Worker mode as the mirror image of Fibers |
| [TYPO3 Caching](ch15-02-typo3-caching-framework.md) | Tag-based cache invalidation |
| [Nextcloud Scaling](ch15-03-nextcloud-scaling.md) | Storage adapters again, this time under scaling pressure |
| [Blackfire](ch15-04-blackfire-profiling.md) | Profiling via a Zend Engine extension |
| [Laravel Forge/Vapor](ch16-01-laravel-forge-vapor.md) | Statelessness as the enabler of serverless deployment |
| [Cloud Hosting](ch16-02-cloud-hosting-aws-gcp-azure.md) | The same PHP process, regardless of which cloud runs it |
| [Platform.sh](ch16-03-platform-sh.md) | Infrastructure as versioned configuration |
| [WordPress Managed Hosting](ch16-04-wordpress-managed-hosting.md) | Object caching with Redis/Memcached |
| [Nextcloud AIO](ch16-05-nextcloud-aio-docker.md) | Container orchestration via the mastercontainer pattern |
