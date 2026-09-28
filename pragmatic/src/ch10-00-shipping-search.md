# Shipping Search That Feels Instant

"Can search find it even if I misspell it?" A search box backed by `WHERE title LIKE '%query%'` answers no. It has no typo tolerance, no relevance ranking, and it scans the whole table once the data grows. **Search that feels instant is a solved problem, and the job is to wire your data into a tool that solves it, not to build one.**

<img src="images/ch10-librarian.png" alt="A library counter. A person writes a request slip with a crossed-out squiggle on it. On the other side, a small elephant with reading glasses already holds out the right book, in front of a wall of card-catalog drawers" width="560">

- [Laravel: Scout With Meilisearch or Algolia ($)](ch10-01-laravel-scout-meilisearch.md): a search index kept in sync with your models, on a server you run or one you rent.
- [TYPO3: Solr and Elasticsearch Integration](ch10-02-typo3-solr-elasticsearch.md): search for thousands of pages that respects permissions and languages.
- [WordPress: Search Plugins and When to Reach for Elasticsearch](ch10-03-wordpress-search-plugins.md): what is built in, and the two plugins that replace it when it is not enough.
