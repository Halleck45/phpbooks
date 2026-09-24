# TYPO3: The Built-In Caching Framework

TYPO3's caching framework is worth studying even outside a TYPO3 project, because it solves caching as a genuinely layered problem rather than a single on/off switch: page output, individual content elements, database query results, and configuration each get their own cache, each with its own invalidation rules.

```php
# config/system/settings.php
$GLOBALS['TYPO3_CONF_VARS']['SYS']['caching']['cacheConfigurations']['pages'] = [
    'backend' => \TYPO3\CMS\Core\Cache\Backend\Typo3DatabaseBackend::class,
    'options' => ['defaultLifetime' => 86400],
];
```

Editors don't manage cache invalidation directly; TYPO3 clears exactly the affected caches automatically when content changes, rather than forcing a blunt "clear everything" after every edit:

```php
$cacheManager = GeneralUtility::makeInstance(CacheManager::class);
$cacheManager->getCache('pages')->flushByTag('pageId_' . $pageId);
```

That tag-based invalidation, flushing only what actually changed, is what makes aggressive caching safe on a large site: a typo fix on one page doesn't force every other page to be regenerated.

For high-traffic sites, TYPO3 layers a reverse proxy cache (typically Varnish) in front of all of this, serving fully rendered pages without PHP running at all for the common case of an anonymous visitor requesting unchanged content.

## When to reach for this

Large TYPO3 sites under real traffic, where page generation cost adds up across thousands of pages, and where content updates happen often enough that "just clear the whole cache" would defeat the purpose.

## When it's the wrong fit

A low-traffic site where the default caching is already fast enough; tuning cache lifetimes and tags for a site nobody's straining is effort spent on a problem that doesn't exist yet.

> **Under the hood:** Tag-based cache invalidation works by associating each cached item with one or more tags (a page ID, a content type) at write time, so flushing "everything tagged `pageId_42`" is a targeted operation rather than a full cache wipe, the same principle behind cache invalidation strategies in most well-designed caching systems, PHP or otherwise.
