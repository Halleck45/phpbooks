# Appendix A: Sources

Every figure and sourced claim in this book is listed below, grouped by the chapter it appears in, with the publisher, the URL, and the date the underlying data refers to or was checked. Where a figure comes from a page that recomputes continuously (W3Techs, Packagist), the date is a retrieval date, not a publication date, and the chapter text says so at the point the figure is used.

A small number of entries below are marked **pending direct verification**. Each one was confirmed through a search-engine snippet or a secondary account rather than a direct fetch of the primary page at the time of writing, and each one is written into its chapter in a form narrow enough not to depend on a precise figure that has not yet been directly confirmed. They are listed here rather than silently dropped so that whoever finishes this book's production knows exactly what remains to be checked before publication.

## Chapter 1: The Reputation

- PHP's share of websites with a known server-side language: 69.9 percent, checked 2026-09-17; 71.8 percent in March 2026; 70.2 percent on 2026-09-03. W3Techs, [w3techs.com/technologies/details/pl-php](https://w3techs.com/technologies/details/pl-php).

## Chapter 2: The Runtime

- PHP's execution model (Zend Engine, request-per-process or thread, shared-nothing by default). The PHP manual, current, checked 2026-09-17.
- Opcache bundled since PHP 5.5; loaded as a `zend_extension` via `php.ini`, not active by default from core alone. [php.net/manual/en/opcache.installation.php](https://php.net/manual/en/opcache.installation.php), checked 2026-09-17.
- JIT RFC's own WordPress benchmark: 326 requests/second with the JIT enabled versus 315 without. PHP JIT RFC, [wiki.php.net/rfc/jit](https://wiki.php.net/rfc/jit), checked 2026-09-17.
- `declare(strict_types=1)` and scalar/return type enforcement behavior. The PHP manual, current, checked 2026-09-17.
- FrankenPHP worker mode: superglobals reset automatically between requests except `$_ENV`; the project's own documentation states "PHP was not originally designed for long-running processes" and recommends periodic worker restarts. [frankenphp.dev/docs/worker/](https://frankenphp.dev/docs/worker/), checked 2026-09-17.
- RoadRunner as a Go-based application server managing a pool of long-lived PHP workers. **Pending direct verification** of [docs.roadrunner.dev](https://docs.roadrunner.dev); the current description traces to a third-party comparison, not the project's own documentation.
- AMPHP as an event-loop-based library family for I/O-bound concurrency, described generically rather than quoted. **Pending direct verification** of [github.com/amphp/amp](https://github.com/amphp/amp) README; not independently re-checked this pass.
- ReactPHP's self-description as a low-level, event-loop-based library for event-driven programming. [github.com/reactphp/reactphp](https://github.com/reactphp/reactphp) README, checked 2026-09-17.
- Swoole's self-description as an event-driven, coroutine-based concurrency engine written in C for PHP. [github.com/swoole/swoole-src](https://github.com/swoole/swoole-src) README, checked 2026-09-17.
- Fibers (PHP 8.1): cooperative, single-stack coroutines via `Fiber::suspend()` and `Fiber::resume()`, concurrency without OS-level parallelism. [php.net/manual/en/language.fibers.php](https://php.net/manual/en/language.fibers.php), checked 2026-09-17.
- `parallel` and `pthreads` as third-party PECL extensions offering real OS-thread parallelism. PECL and the PHP manual, general reference, checked 2026-09-17.

## Chapter 3: Who Runs PHP

- W3Techs adoption figure: see Chapter 1 entry above.
- Stack Overflow Developer Survey 2025: PHP 19.1 percent, JavaScript 68.8 percent, Python 54.8 percent, TypeScript 48.8 percent, C# 29.9 percent, Java 29.6 percent, Go 17.4 percent, Ruby 6.9 percent, among 24,759 professional-developer respondents. [survey.stackoverflow.co/2025/technology](https://survey.stackoverflow.co/2025/technology), checked 2026-09-17.
- MediaWiki as roughly 70 percent PHP, close to two million lines of Wikimedia-maintained PHP, running across seven data centers (three United States, two Europe, one Asia, one South America) behind Varnish, Apache Traffic Server, and Apache HTTP Server, with APCu and Memcached caching. Wikimedia, [wikitech.wikimedia.org/wiki/MediaWiki_at_WMF](https://wikitech.wikimedia.org/wiki/MediaWiki_at_WMF) and [wikitech.wikimedia.org/wiki/Wikimedia_infrastructure](https://wikitech.wikimedia.org/wiki/Wikimedia_infrastructure), living pages, retrieved 2026-09-17.
- Meta and Slack run Hack on HHVM, not PHP. **Pending direct verification** against each company's own current engineering material; treated as established background fact for the purpose of this book's exclusion rule.

## Chapter 4: Performance

- TechEmpower Framework Benchmarks discontinued 24 March 2026, repository archived; last completed Round 23 published 17 March 2025, covering more than 330 framework implementations. [techempower.com/blog/2025/03/17/framework-benchmarks-round-23/](https://techempower.com/blog/2025/03/17/framework-benchmarks-round-23/) and [github.com/TechEmpower/FrameworkBenchmarks](https://github.com/TechEmpower/FrameworkBenchmarks) (archived), checked 2026-09-17.
- JIT RFC WordPress benchmark: see Chapter 2 entry above.
- Computer Language Benchmarks Game: PHP 8.4.1 versus Python 3.13, suite version 25.03, PHP faster on fannkuch-redux, n-body, and spectral-norm by roughly 1.5 to 2 times. [benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/python3-php.html](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/python3-php.html), checked 2026-09-17.

## Chapter 5: Scale

- PHP-FPM's worker-based, shared-nothing process model. [php.net/manual/en/install.fpm.php](https://php.net/manual/en/install.fpm.php), checked 2026-09-17.
- Wikimedia data-center distribution: see Chapter 3 entry above.

## Chapter 6: Who Maintains It

- JetBrains "The State of PHP 2025": 1,720 PHP-specific respondents of 24,534 developers surveyed overall, fielded April-June 2025, with the survey's own caveat that results may skew toward JetBrains product users. Figures used: 88 percent with 3+ years of PHP experience; 58 percent not planning to migrate away within a year (Go and Python most-cited among those who would); self-reported version split 89 percent PHP 8.x, 33 percent 7.x, 8 percent 5.6 or earlier; PHPStan usage 36 percent, up 9 points year over year; PHPUnit 50 percent; Pest 17 percent; 32 percent report no automated testing; 42 percent report no static analysis. [blog.jetbrains.com/phpstorm/2025/10/state-of-php-2025/](https://blog.jetbrains.com/phpstorm/2025/10/state-of-php-2025/), checked 2026-09-17.
- Composer's lockfile-based dependency resolution as a reproducibility guarantee. [getcomposer.org](https://getcomposer.org) documentation, general reference, checked 2026-09-17.

## Chapter 7: Cost

- PHP License version 3.01 applies to PHP 8.4 and 8.5; License version 4 (Modified BSD / BSD-3-Clause) applies from PHP 8.6 onward. [php.net/license/index.php](https://php.net/license/index.php), checked 2026-09-17.
- Packagist statistics: approximately 468,201 published packages, 5,822,307 published versions, and approximately 199.8 billion cumulative installs since 13 April 2012. [packagist.org/statistics](https://packagist.org/statistics), checked 2026-09-17, live counter.
- Composer's hash-based install verification against the project lockfile. [getcomposer.org](https://getcomposer.org) documentation, general reference, checked 2026-09-17.
- PHP-FPM's minimal hosting requirements: see Chapter 5 entry above.
- `password_hash` and `password_verify` as the standard password-hashing API. [php.net/manual/en/function.password-hash.php](https://php.net/manual/en/function.password-hash.php), current, checked 2026-09-17.
- Libsodium bindings bundled with PHP since version 7.2. [php.net/manual/en/book.sodium.php](https://php.net/manual/en/book.sodium.php), current, checked 2026-09-17.
- PDO prepared statements separating query structure from data. [php.net/manual/en/pdo.prepared-statements.php](https://php.net/manual/en/pdo.prepared-statements.php), current, checked 2026-09-17.

## Chapter 8: Governance and Versions

- Release cadence and support windows: one feature release per year in late November; two years of active support followed by two years of security-only support. PHP 8.2 released 8 Dec 2022 (active support ended 31 Dec 2024, security support ends 31 Dec 2026); PHP 8.3 released 23 Nov 2023 (active until 31 Dec 2025, security until 31 Dec 2027); PHP 8.4 released 21 Nov 2024 (active until 31 Dec 2026, security until 31 Dec 2028); PHP 8.5 released 20 Nov 2025 (active until 31 Dec 2027, security until 31 Dec 2029). [php.net/supported-versions.php](https://php.net/supported-versions.php), checked 2026-09-17.
- RFC process: proposed and voted on the public wiki, with a two-thirds majority required for a language change. **Pending direct verification** of [wiki.php.net/rfc/change_required_votes_to_two_thirds](https://wiki.php.net/rfc/change_required_votes_to_two_thirds) for exact wording and adoption date.
- The PHP Foundation established November 2021. **Pending direct verification** of the Foundation's own founding account at [thephp.foundation](https://thephp.foundation); the account used here was traced through a sponsor's blog post rather than the Foundation's own history page.
- A public funding ledger recording ongoing contributions from multiple independent organizations. **Pending direct verification** of current cumulative totals at [opencollective.com/phpfoundation](https://opencollective.com/phpfoundation); this book states the ledger's existence and transparency without printing specific dollar figures that were not directly confirmed.
- A dedicated process for handling security reports against the core language, separate from the feature RFC process. **Pending direct verification** of [php.net/security](https://php.net/security).
- W3Techs version fragmentation: PHP 8.x 64.1 percent, 7.x 28.1 percent, 5.x 7.8 percent, 4.x 0.1 percent of PHP-running websites. [w3techs.com/technologies/details/pl-php](https://w3techs.com/technologies/details/pl-php), checked 2026-09-17.

## Chapter 9: Where PHP Is the Wrong Choice

- Fibers, `parallel`, and `pthreads`: see Chapter 2 entries above.
- PHP-versus-Python CPU-bound comparison: see Chapter 4 entry above.
- NativePHP as a community project built on Laravel, packaging PHP applications for desktop and mobile app stores, with the project's own documentation claiming production deployments as of 2026. [nativephp.com/docs/](https://nativephp.com/docs/), checked 2026-09-17.
- Absence of a PHP equivalent to NumPy, pandas, PyTorch, or TensorFlow: an ecosystem-density observation, checkable directly via Packagist's own category search and PHP's extension index rather than a single dated citation.
- FrankenPHP's own statement on long-running processes: see Chapter 2 entry above.
- PHPStan and Psalm both approximating generics through a shared `@template` docblock convention, enforced only by static analysis, not the language engine. **Pending direct verification** of [phpstan.org/writing-php-code/generics](https://phpstan.org/writing-php-code/generics) and [psalm.dev/docs/annotating_code/templated_annotations/](https://psalm.dev/docs/annotating_code/templated_annotations/); current sourcing is secondary.
- W3Techs version fragmentation: see Chapter 8 entry above.

## Chapter 10: The Evaluation

No new figures. This chapter reruns the live sources already listed above: [w3techs.com/technologies/details/pl-php](https://w3techs.com/technologies/details/pl-php), [survey.stackoverflow.co](https://survey.stackoverflow.co), [benchmarksgame-team.pages.debian.net/benchmarksgame](https://benchmarksgame-team.pages.debian.net/benchmarksgame), [github.com/php/php-src](https://github.com/php/php-src), [packagist.org/statistics](https://packagist.org/statistics), and [php.net/supported-versions.php](https://php.net/supported-versions.php). The runtime-status code sample uses `PHP_VERSION`, `PHP_SAPI`, and `opcache_get_status()`, all documented in the PHP manual, current, checked 2026-09-17.
