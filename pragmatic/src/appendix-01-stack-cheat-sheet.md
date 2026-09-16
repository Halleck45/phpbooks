# A - The Stack Cheat Sheet

One page, use case on the left, recommended pick on the right. A `$` marks anything that isn't open source. Where two picks appear, the first is usually the faster start.

| You need to ship... | Reach for | Chapter |
|---|---|---|
| A custom application with real business logic | Laravel or Symfony | [Ch. 1](ch01-01-framework-cms-or-headless.md) |
| A marketing site or blog a client edits themselves | WordPress | [Ch. 3](ch03-01-wordpress-block-themes.md) |
| A large, multi-department, multilingual institutional site | TYPO3 | [Ch. 3](ch03-02-typo3-structured-content.md) / [Ch. 13](ch13-01-typo3-multilingual-trees.md) |
| A one-off script or CLI tool, no framework | Symfony/Console, Guzzle, Monolog | [Ch. 2](ch02-00-standalone-components.md) |
| Login, sign-up, password reset | Laravel Breeze/Fortify, Symfony Security, or WordPress roles | [Ch. 4](ch04-00-shipping-user-accounts.md) |
| An internal admin panel | Laravel Filament, Symfony EasyAdmin, or Nova `$` | [Ch. 5](ch05-00-shipping-an-admin-back-office.md) |
| A REST/GraphQL API with docs | API Platform | [Ch. 6](ch06-01-api-platform-from-one-class.md) |
| Live updates without a page refresh | Laravel Reverb, Symfony Mercure, or Pusher `$` | [Ch. 7](ch07-00-shipping-real-time-features.md) |
| File sharing and sync ("our own Dropbox") | Nextcloud | [Ch. 8](ch08-01-nextcloud-ready-made-drive.md) |
| Ordinary file uploads in an existing app | Laravel Storage / League/Flysystem | [Ch. 8](ch08-02-laravel-filesystem-s3.md) |
| A product catalog and checkout | WooCommerce, Sylius, or Cashier + Stripe `$` | [Ch. 9](ch09-00-shipping-a-storefront.md) |
| Search that tolerates typos and ranks by relevance | Laravel Scout + Meilisearch (or Algolia `$`) | [Ch. 10](ch10-01-laravel-scout-meilisearch.md) |
| Background jobs and scheduled tasks | Laravel Queues, Symfony Messenger, or Action Scheduler | [Ch. 11](ch11-00-shipping-background-work.md) |
| An AI-powered feature added to an existing app | Laravel Prism or Symfony AI Bundle | [Ch. 12](ch12-00-shipping-an-ai-feature.md) |
| Multiple languages or multiple regional sites | TYPO3, WPML, or Symfony Translation | [Ch. 13](ch13-00-shipping-multi-language-multi-site.md) |
| Tests, static analysis, and vulnerability scanning | Pest/Larastan, PHPStan/Psalm, `composer audit` | [Ch. 14](ch14-00-shipping-confidence.md) |
| Production error visibility | Sentry (or Flare `$`) | [Ch. 14](ch14-05-sentry-flare-error-tracking.md) |
| More throughput without rewriting the app | FrankenPHP / Laravel Octane | [Ch. 15](ch15-01-frankenphp-laravel-octane.md) |
| Finding an actual performance bottleneck | Blackfire `$` | [Ch. 15](ch15-04-blackfire-profiling.md) |
| Deploying a Laravel app | Forge or Vapor `$` | [Ch. 16](ch16-01-laravel-forge-vapor.md) |
| Deploying onto an existing AWS/GCP/Azure contract | App Runner, Cloud Run, or App Service | [Ch. 16](ch16-02-cloud-hosting-aws-gcp-azure.md) |
| Deploying across several different frameworks consistently | Platform.sh `$` | [Ch. 16](ch16-03-platform-sh.md) |
| Deploying WordPress at real, revenue-generating scale | Kinsta or WP Engine `$` | [Ch. 16](ch16-04-wordpress-managed-hosting.md) |
| Self-hosting Nextcloud in production | The All-in-One Docker image | [Ch. 16](ch16-05-nextcloud-aio-docker.md) |
