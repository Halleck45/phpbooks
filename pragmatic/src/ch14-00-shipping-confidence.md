# Shipping Confidence

"It works on my machine" is not a feature. Confidence, the actual, checkable kind that comes from a test suite that catches regressions, a static analyzer that catches whole categories of bugs before they run, and a scan that flags a known-vulnerable dependency before it ships, is a feature too. It's the one where the bug gets caught before your user finds it, and it belongs in every project in this book, not just the ones with time left over at the end.

- [Laravel: Pest, Larastan, and `composer audit`](ch14-01-laravel-pest-larastan.md) covers Laravel's testing and static analysis stack.
- [Symfony: PHPUnit, PHPStan/Psalm, and Rector](ch14-02-symfony-phpunit-phpstan-rector.md) covers Symfony's equivalent, plus automated upgrades.
- [WordPress: PHPUnit, PHPCS/WPCS, and WPScan](ch14-03-wordpress-phpunit-phpcs-wpscan.md) covers testing and security scanning for plugins and themes.
- [Cross-Ecosystem: SAST, Dependency Scanning, and CI Gates](ch14-04-cross-ecosystem-sast-ci-gates.md) covers what works the same everywhere, regardless of framework.
- [Catching It in Production: Sentry and Flare ($)](ch14-05-sentry-flare-error-tracking.md) covers the moment confidence has to extend past your own test suite, into what's actually happening for real users.
