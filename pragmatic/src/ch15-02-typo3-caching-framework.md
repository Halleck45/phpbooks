# TYPO3: The Built-In Caching Framework

TYPO3's caching framework deserves a look even outside a TYPO3 project, because **it treats caching as a layered problem rather than an on/off switch.** Page output, individual content elements, database query results and configuration each get their own cache, with their own invalidation rules.

```php
# config/system/settings.php
$GLOBALS['TYPO3_CONF_VARS']['SYS']['caching']['cacheConfigurations']['pages'] = [
    'backend' => \TYPO3\CMS\Core\Cache\Backend\Typo3DatabaseBackend::class,
    'options' => ['defaultLifetime' => 86400],
];
```

Editors never manage invalidation. When content changes, TYPO3 clears the caches that depend on it and nothing else, instead of a blunt "clear everything" after every edit:

```php
$cacheManager = GeneralUtility::makeInstance(CacheManager::class);
$cacheManager->getCache('pages')->flushByTag('pageId_' . $pageId);
```

Tag-based invalidation is what makes aggressive caching safe on a large site. A typo fix on one page does not force every other page to be regenerated.

For high-traffic sites, TYPO3 adds a reverse proxy cache in front of all this, typically Varnish. An anonymous visitor asking for an unchanged page gets it fully rendered, without PHP running at all.

## When to reach for this

Large TYPO3 sites under load, where page generation adds up across thousands of pages and content changes often enough that clearing the whole cache would defeat the purpose.

## When it's the wrong fit

A low-traffic site where the default caching is already fast enough. Tuning lifetimes and tags for a site nobody is straining solves a problem that does not exist yet.

> **Under the hood:** Tag-based invalidation associates each cached item with one or more tags (a page ID, a content type) at write time. Flushing "everything tagged `pageId_42`" is then a targeted operation, not a full wipe. Most well-designed caching systems, PHP or otherwise, rest on the same principle.
