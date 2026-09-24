# Scaffolding a First Project in Under a Minute

Reading about a stack tells you what it claims. **Running its scaffolding command for sixty seconds tells you what it feels like.** Here is the fastest path into each of the main options this book covers.

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

The skeleton starts nearly bare. `composer require webapp` pulls in Twig, routing, and the form component, which most sites end up needing anyway.

## WordPress

```bash
wp core download --path=my-site
cd my-site
wp config create --dbname=my_site --dbuser=root --dbpass=
wp core install --url=localhost:8080 --title="My Site" --admin_user=admin --admin_password=admin --admin_email=you@example.com
php -S localhost:8080
```

Or skip the command line and use [Local](https://localwp.com), which does the same four steps behind a GUI in about the same time.

## API Platform

```bash
composer create-project api-platform/api-platform my-api
cd my-api
docker compose up -d
```

A running API skeleton with an interactive OpenAPI docs page, ready for the moment a single PHP class becomes a full CRUD API.

## What to compare

Not install time: they are all under a minute. Compare what is already decided for you when the install finishes. Laravel and Symfony hand you an empty application and a lot of freedom. WordPress hands you a working, editable site with nothing custom in it yet. API Platform hands you a fully documented, empty API. The one that feels closest to "done" for your brief is usually the one to keep building on.

> **Under the hood:** All four are Composer projects: PHP's package manager resolves a dependency tree and generates an autoloader. WordPress is the outlier. It predates Composer's popularity and can run without it, though WordPress development today almost always uses Composer for plugins and dependencies too.
