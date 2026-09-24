# Statamic ($ for commercial use): A Flat-File CMS Built on Laravel

Statamic is what a content editor looks like when a Laravel developer builds it: content lives in flat Markdown and YAML files instead of a database, version control gets you free content history, and the whole thing is still a real Laravel application underneath, so anything you already know about Laravel (see [Shipping User Accounts](ch04-01-laravel-breeze-fortify.md), [Shipping Background Work](ch11-01-laravel-queues-horizon.md)) still applies.

```bash
composer create-project statamic/statamic my-site
cd my-site
php please make:user
php artisan serve
```

Content types ("collections" and "blueprints" in Statamic's vocabulary) are defined in YAML, and editors get a clean admin interface generated straight from that definition:

```yaml
# resources/blueprints/collections/posts/post.yaml
title: Post
sections:
  main:
    fields:
      - handle: title
        field: { type: text, required: true }
      - handle: content
        field: { type: markdown }
      - handle: featured_image
        field: { type: assets, container: images }
```

Templates use Statamic's own Antlers syntax or standard Blade, developer's choice.

## Licensing

Statamic is free for personal, non-commercial projects. Any commercial site needs a paid license, priced per site, which is what earns it the `$` in this book: it's open enough to evaluate for free, but shipping it for a client is a real line item.

## When to reach for this

A Laravel-comfortable team building a content-heavy site, one that wants Git-based content history and doesn't want to run a separate database just for pages and posts.

## When it's the wrong fit

A client who needs the WordPress plugin ecosystem specifically, or a project where the license cost isn't justified by the smaller scope.

> **Under the hood:** Storing content as flat files instead of database rows means Statamic leans heavily on PHP's filesystem functions and caching layer for performance instead of SQL queries. For most content sites, reading a cached, pre-parsed file is at least as fast as a database round trip, and it comes with `git diff` as a free audit log.
