# Platform.sh ($): One Deploy Story for Several Frameworks

Platform.sh's pitch is framework-agnostic infrastructure-as-code: one configuration format that works whether the project underneath is Laravel, Symfony, WordPress, TYPO3, or something else entirely, useful for an agency shipping across several of the stacks covered in this book without learning a different deployment platform for each one.

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

Every push creates a full, isolated environment (its own database, its own storage) rather than deploying over a shared one, which makes previewing a feature branch as a real, running application a routine part of the workflow rather than a special setup.

## Pricing

Platform.sh is a paid managed service, billed per project and environment, with no meaningful free tier for production use, which is what earns it the `$`.

## When to reach for this

Agencies or teams managing multiple projects across different PHP frameworks and CMSes, where one consistent deployment workflow across all of them is worth more than any single platform's framework-specific conveniences.

## When it's the wrong fit

A single project committed to one framework long-term, where a framework-native option like [Forge](ch16-01-laravel-forge-vapor.md) or [managed WordPress hosting](ch16-04-wordpress-managed-hosting.md) is simpler and often cheaper for that one use case.

> **Under the hood:** The per-branch environment model works because Platform.sh treats infrastructure itself as versioned configuration alongside your code, the same instinct as a `composer.lock` file pinning dependency versions, just extended to cover the database and services a deployment needs too.
