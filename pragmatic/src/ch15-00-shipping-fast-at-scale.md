# Shipping It Fast, At Scale

Most features in this book ship fine on ordinary PHP: a fresh process per request, a database query, a response, done. Then traffic grows, or a specific page turns out to be slow, and "it works" quietly stops being enough. This chapter is about that second phase: not premature optimization, but the concrete tools for when performance becomes a real, measured requirement.

- [FrankenPHP and Laravel Octane: Worker Mode Performance](ch15-01-frankenphp-laravel-octane.md) covers keeping your application booted in memory between requests instead of rebuilding it from scratch every time.
- [TYPO3: The Built-In Caching Framework](ch15-02-typo3-caching-framework.md) covers a mature, layered caching system built into a large content platform.
- [Nextcloud: Scaling a Self-Hosted Platform](ch15-03-nextcloud-scaling.md) covers what changes when a self-hosted PHP application grows from a team to an organization.
- [Blackfire ($): Finding the Actual Bottleneck](ch15-04-blackfire-profiling.md) covers measuring where the time actually goes, instead of guessing.
