# Platform.sh ($): One Deploy Story for Several Frameworks

Platform.sh sells framework-agnostic infrastructure as code: **one configuration format, whether the project underneath is Laravel, Symfony, WordPress, TYPO3 or something else.** An agency shipping across several of the stacks in this book learns one deployment platform instead of five.

```yaml
# .platform.app.yaml
name: app
type: php:8.3
dependencies:
  php:
    composer/composer: "^2"
relationships:
  database: "db:mysql"
hooks:
  build: composer install --no-dev --optimize-autoloader
  deploy: php artisan migrate --force
```

```yaml
# .platform/services.yaml
db:
  type: mysql:8.0
```

```bash
git push platform main
```

Every push creates a full, isolated environment with its own database and its own storage, rather than deploying over a shared one. Previewing a feature branch as a running application becomes routine, not a special setup.

## Pricing

Platform.sh is a paid managed service, billed per project and environment, with no free tier for production use.

## When to reach for this

Agencies or teams running several projects across different PHP frameworks and CMSes, where one deployment workflow for all of them matters more than any single platform's framework-specific conveniences.

## When it's the wrong fit

A single project committed to one framework for the long term. A framework-native option like [Forge](ch16-01-laravel-forge-vapor.md) or [managed WordPress hosting](ch16-04-wordpress-managed-hosting.md) is simpler, and often cheaper, for that one case.

> **Under the hood:** The per-branch environment model works because Platform.sh treats infrastructure as versioned configuration next to your code. It is the instinct behind a `composer.lock` file pinning dependency versions, extended to the database and the services a deployment needs.
