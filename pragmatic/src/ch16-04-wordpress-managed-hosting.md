# WordPress: Managed Hosting Done Right (Kinsta, WP Engine $)

Generic hosting treats WordPress like any other PHP application. Managed WordPress hosting, from providers like Kinsta and WP Engine, is built around what WordPress is known to need: object and page caching tuned to its query patterns, one-click staging, core and plugin updates on a schedule you control, and malware scanning aimed at known plugin vulnerabilities.

```bash
# a typical managed-host workflow: staging, then push to production
wp @staging plugin update --all
wp @staging cache flush
# after review in the staging environment
wp @production deploy
```

**The difference from self-managed hosting shows up during an incident.** Managed hosts include automatic backups with one-click restore, and support staff who already know how WordPress fails, rather than generic server support learning the platform from your ticket.

## Pricing

Kinsta and WP Engine are paid, tiered by traffic and site count, with no free tier. The cost sits well above generic shared hosting and well below an in-house team doing the same reliability and performance work by hand.

## When to reach for this

Any client-facing, revenue-generating or otherwise important WordPress site, where downtime or a slow page has a cost and nobody in-house wants to own WordPress-specific server tuning and security monitoring.

## When it's the wrong fit

A low-stakes personal blog or an internal tool. Cheaper generic hosting is enough, and the specialized tooling would sit unused.

> **Under the hood:** Much of what these hosts sell is object caching: the results of expensive WordPress queries kept in memory, through Redis or Memcached, so a popular page does not re-run the same queries for every visitor. It is the caching instinct behind [TYPO3's caching framework](ch15-02-typo3-caching-framework.md), pre-configured for WordPress's usual query patterns.
