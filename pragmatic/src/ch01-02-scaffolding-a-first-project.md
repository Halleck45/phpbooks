# Scaffolding a First Project in Under a Minute

Reading about a stack tells you what it claims. Running its scaffolding command for sixty seconds tells you what it actually feels like. Here's the fastest path into each of the main options this book covers.

## Laravel

```bash
composer create-project laravel/laravel my-app
cd my-app
php artisan serve
```

A running application at `http://localhost:8000`, with routing, a database connection, and an ORM already wired together.

## Symfony

```bash
composer create-project symfony/skeleton my-app
cd my-app
composer require webapp
symfony server:start
```

The `symfony/skeleton` starts nearly bare; `composer require webapp` pulls in the Twig, routing, and form components most sites end up needing anyway.

## WordPress

```bash
wp core download --path=my-site
cd my-site
wp config create --dbname=my_site --dbuser=root --dbpass=
wp core install --url=localhost:8080 --title="My Site" --admin_user=admin --admin_password=admin --admin_email=you@example.com
php -S localhost:8080
```

Or skip the command line entirely and use [Local](https://localwp.com), which does all four steps behind a GUI in about the same amount of time.

## API Platform

```bash
composer create-project api-platform/api-platform my-api
cd my-api
docker compose up -d
```

A running API skeleton with an interactive OpenAPI/Swagger docs page, ready for the next chapter's example of turning a single PHP class into a full CRUD API.

## What to actually compare

Don't compare these on install time alone; they're all under a minute. Compare what's already decided for you the moment the install finishes: Laravel and Symfony hand you an empty application and a lot of freedom, WordPress hands you a working, editable site with nothing custom yet, and API Platform hands you a fully documented, empty API. The one that feels closest to "done" for your actual brief is usually the right one to keep building on.

> **Under the hood:** All four of these are Composer projects: PHP's package manager resolves a dependency tree and generates an autoloader. WordPress is the outlier: it predates Composer's popularity and can run without it, though modern WordPress development almost always uses Composer for plugins and dependencies too.
