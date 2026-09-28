# WordPress: Search Plugins and When to Reach for Elasticsearch

WordPress's built-in search is a `LIKE` query against post titles and content, and it shows. No relevance ranking to speak of, no typo tolerance, and it slows down once a site has thousands of posts.

**The fastest fix is a plugin that replaces the built-in query without touching template code.**

```bash
wp plugin install relevanssi --activate
```

Relevanssi reindexes existing content and takes over the search query. You get relevance scoring and fuzzy matching, with no code changes to speak of.

For larger sites, or ones that need faceted filtering (category and price range together, for instance), an Elasticsearch-backed plugin swaps the search backend entirely:

```bash
wp plugin install elasticpress --activate
wp elasticpress index --setup
```

```php
$args = [
    's' => 'wireless mouse',
    'post_type' => 'product',
];
$query = new WP_Query($args); // ElasticPress intercepts this transparently
```

The application code barely changes. `WP_Query` works as before, and ElasticPress answers it from Elasticsearch instead of MySQL.

## When to reach for this

Relevanssi for most sites where the complaint is search quality, not scale. ElasticPress once the site has enough content, or complex enough filtering, that even a smarter SQL query will not be fast or flexible enough.

## When it's the wrong fit

A small site with a few dozen pages, where the default search is fast enough and nobody has complained. Do not add search infrastructure ahead of a problem.

> **Under the hood:** `WP_Query` is WordPress's central abstraction for "get me some posts," used by nearly every theme and plugin. ElasticPress hooks into that same class and reroutes its query at the last moment, which is why adopting it rarely means rewriting theme code.
