# Cross-Ecosystem: SAST, Dependency Scanning, and CI Gates

Everything so far in this chapter depends on the framework. This page covers what works the same whichever stack you ship with, and how to wire it so **a broken or vulnerable build never quietly reaches production.**

**Static analysis as lightweight SAST**: PHPStan and Psalm, already covered per framework, double as a first line of static application security testing (SAST). They catch SQL built from unsanitized input, or a variable used before it is guaranteed to be set.

**GitHub CodeQL** goes deeper. It traces how untrusted input flows through the code toward a dangerous sink, a raw SQL query, an `eval()`, an unescaped output, instead of checking types.

```yaml
# .github/workflows/codeql.yml
- uses: github/codeql-action/init@v3
  with:
    languages: php
- uses: github/codeql-action/analyze@v3
```

**Dependabot** watches your `composer.lock` and opens a pull request the moment a dependency has a known vulnerability with a fix available.

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "composer"
    directory: "/"
    schedule: { interval: "weekly" }
```

**Snyk ($)** covers similar ground with a paid product's polish: a dashboard, license compliance checks, and coverage beyond Composer dependencies, for a subscription past its free tier.

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

If any step fails, the pull request cannot merge. That is the feature. Not that the tools exist, but that nobody has to remember to run them.

> **Under the hood:** CodeQL models data flow. It follows a value from where it enters the program (a `$_GET` parameter, a form field) to where it is used, instead of checking each line on its own. That is a different, and more expensive, kind of analysis than the type checking PHPStan and Psalm perform.
