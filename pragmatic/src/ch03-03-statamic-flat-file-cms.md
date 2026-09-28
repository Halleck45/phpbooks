# Statamic ($ for commercial use): A Flat-File CMS Built on Laravel

Statamic is what a content editor looks like when a Laravel developer builds it. **Content lives in flat Markdown and YAML files instead of a database**, so version control gives you content history for free. Underneath, it is still a Laravel application, and everything you know about Laravel (see [Shipping User Accounts](ch04-01-laravel-breeze-fortify.md), [Shipping Background Work](ch11-01-laravel-queues-horizon.md)) still applies.

```bash
composer create-project statamic/statamic my-site
cd my-site
php please make:user
php artisan serve
```

Content types ("collections" and "blueprints" in Statamic's vocabulary) are defined in YAML, and editors get a clean admin interface generated from that definition:

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

Templates use Statamic's own Antlers syntax or standard Blade. Your choice.

## Licensing

Statamic is free for personal, non-commercial projects. A commercial site needs a paid license, priced per site. You can evaluate it for free, but shipping it for a client is a line item in the budget.

## When to reach for this

A Laravel-comfortable team building a content-heavy site, one that wants Git-based content history and no separate database for pages and posts.

## When it's the wrong fit

A client who needs the WordPress plugin ecosystem specifically, or a project too small for the license cost to make sense.

> **Under the hood:** Storing content as flat files instead of database rows means Statamic leans on PHP's filesystem functions and its caching layer for performance instead of SQL queries. For most content sites, reading a cached, pre-parsed file is at least as fast as a database round trip, and `git diff` comes along as a free audit log.
