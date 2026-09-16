# Cross-Ecosystem: SAST, Dependency Scanning, and CI Gates

Everything so far in this chapter has been framework-specific. This page covers what works identically no matter which stack from this book you're shipping with, and how to wire it together so a broken or vulnerable build never quietly reaches production.

**Static analysis as lightweight SAST**: PHPStan and Psalm, already covered per-framework earlier in this chapter, double as a first line of static application security testing (SAST), catching things like SQL built from unsanitized input or a variable used before it's guaranteed to be set.

**GitHub CodeQL** performs deeper semantic security analysis, specifically tracing how untrusted input flows through the code toward a dangerous sink (a raw SQL query, an `eval()`, an unescaped output), rather than just checking types.

```yaml
# .github/workflows/codeql.yml
- uses: github/codeql-action/init@v3
  with:
    languages: php
- uses: github/codeql-action/analyze@v3
```

**Dependabot** watches your `composer.lock` and opens a pull request automatically the moment a dependency has a known vulnerability with a fix available.

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "composer"
    directory: "/"
    schedule: { interval: "weekly" }
```

**Snyk ($)** covers similar ground to Dependabot with a paid product's polish: a dashboard, license compliance checks, and coverage across more than just Composer dependencies, in exchange for a subscription past its free tier.

## Wiring it into CI

The point of all of this is a gate, not a report nobody reads:

```yaml
# .github/workflows/ci.yml
jobs:
  quality:
    steps:
      - run: composer audit
      - run: vendor/bin/phpstan analyse
      - run: vendor/bin/pest # or php bin/phpunit
```

If any step fails, the pull request can't merge. That's the actual feature: not that the tools exist, but that a broken or vulnerable build is structurally prevented from reaching production, rather than relying on someone remembering to run a check by hand.

> **Under the hood:** CodeQL's real strength is that it models data flow, tracing a value from where it enters the program (a `$_GET` parameter, a form field) to where it's used, rather than checking each line in isolation. That's a meaningfully different, and more expensive, kind of analysis than the type-checking PHPStan and Psalm perform.
