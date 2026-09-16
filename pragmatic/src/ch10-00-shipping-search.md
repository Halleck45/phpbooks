# Shipping Search That Feels Instant

A search box backed by `WHERE title LIKE '%query%'` works until it doesn't: no typo tolerance, no relevance ranking, and a full table scan waiting to happen as the data grows. Real search, the kind that feels instant and forgiving, is a solved problem with dedicated tools built for it. The trick is wiring your data into one without building a search engine yourself.

- [Laravel: Scout With Meilisearch or Algolia ($)](ch10-01-laravel-scout-meilisearch.md) covers Laravel's driver-based approach to full-text search.
- [TYPO3: Solr and Elasticsearch Integration](ch10-02-typo3-solr-elasticsearch.md) covers enterprise-grade search integration for large content sites.
- [WordPress: Search Plugins and When to Reach for Elasticsearch](ch10-03-wordpress-search-plugins.md) covers what's built in, and where its limits are.
