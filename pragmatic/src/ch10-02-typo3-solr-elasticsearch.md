# TYPO3: Solr and Elasticsearch Integration

Large TYPO3 sites (see [Structured Content at Enterprise Scale](ch03-02-typo3-structured-content.md)) tend to have exactly the search problem dedicated engines exist for: thousands of pages, multiple languages, and content editors who expect search results to respect the same permissions and page tree structure as the rest of the site.

The `apache-solr-for-typo3` extension indexes the page tree directly, respecting access restrictions so a search never surfaces a page a given visitor shouldn't see:

```bash
composer require apache-solr-for-typo3/solr
```

```yaml
plugin.tx_solr {
  solr {
    host = solr.example.com
    port = 8983
    scheme = https
  }
  search {
    faceting = 1
    faceting.facets {
      contentType {
        field = type
      }
    }
  }
}
```

Faceted search, letting visitors filter results by content type, department, or date without writing custom filtering logic, is largely configuration once Solr is connected, not custom PHP.

## When to reach for this

Enterprise TYPO3 sites where search quality and correctness (respecting multilingual content, page permissions, and faceted filtering) genuinely matters to the organization, not just a nice-to-have search box.

## When it's the wrong fit

A smaller TYPO3 site where the built-in indexed search extension is sufficient, and running a separate Solr or Elasticsearch cluster would be infrastructure the project doesn't need yet.

> **Under the hood:** The Solr integration mirrors TYPO3's own permission model when indexing, storing which user groups can see each document alongside its content. That's what prevents search from becoming an accidental way to leak restricted content, a detail generic search integrations sometimes miss entirely.
