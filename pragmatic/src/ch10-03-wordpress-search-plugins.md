# WordPress: Search Plugins and When to Reach for Elasticsearch

WordPress's built-in search is a `LIKE`-based SQL query against post titles and content, and it shows: no relevance ranking worth the name, no typo tolerance, and it slows down noticeably as a site's content grows into the thousands of posts.

The fastest fix is a plugin that replaces the built-in query with something better, without touching template code:

```bash
wp plugin install relevanssi --activate
```

Relevanssi reindexes existing content and takes over the search query, adding relevance scoring and fuzzy matching with essentially no code changes required.

For larger sites, or ones that need faceted filtering (search by category and price range together, for instance), an Elasticsearch-backed plugin swaps the search backend entirely:

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

The application code barely changes; `WP_Query` still works the same way, ElasticPress just answers it from Elasticsearch instead of MySQL underneath.

## When to reach for this

Relevanssi for most sites where search quality, not raw scale, is the complaint. ElasticPress once the site has enough content, or complex enough filtering needs, that even a smarter SQL query isn't going to be fast or flexible enough.

## When it's the wrong fit

A small site with a few dozen pages, where the default search is already fast enough and the complaint doesn't actually exist yet. Don't add search infrastructure ahead of an actual problem.

> **Under the hood:** `WP_Query` is WordPress's central abstraction for "get me some posts," used by nearly every theme and plugin. ElasticPress works by hooking into that same class and rerouting its query at the last moment, which is why adopting it rarely requires rewriting existing theme code.
