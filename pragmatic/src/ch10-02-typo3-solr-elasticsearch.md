# TYPO3: Solr and Elasticsearch Integration

A large TYPO3 site (see [Structured Content at Enterprise Scale](ch03-02-typo3-structured-content.md)) has the search problem dedicated engines exist for. Thousands of pages, several languages, and editors who expect results to respect the same permissions and page tree as the rest of the site.

**The Solr extension indexes the page tree with its access restrictions, so a search never surfaces a page a visitor is not allowed to see.**

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

Faceted search, where visitors filter results by content type, department or date, is configuration once Solr is connected. No custom PHP.

## When to reach for this

Enterprise TYPO3 sites where search correctness matters to the organisation: multilingual content, page permissions, faceted filtering. Not a nice-to-have search box.

## When it's the wrong fit

A smaller TYPO3 site where the built-in indexed search extension is enough. A separate Solr or Elasticsearch cluster is infrastructure the project does not need yet.

> **Under the hood:** The Solr integration mirrors TYPO3's own permission model when indexing, storing which user groups can see each document alongside its content. That is what keeps search from becoming an accidental way to leak restricted content, a detail generic search integrations sometimes miss.
