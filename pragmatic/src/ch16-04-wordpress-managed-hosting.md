# WordPress: Managed Hosting Done Right (Kinsta, WP Engine $)

Generic hosting treats WordPress like any other PHP application. Managed WordPress hosting, from providers like Kinsta and WP Engine, is built around WordPress's specific, well-known needs: aggressive object and page caching tuned for WordPress's query patterns, one-click staging environments, automatic core and plugin updates on a schedule you control, and malware scanning specific to known WordPress plugin vulnerabilities.

```bash
# a typical managed-host workflow: staging, then push to production
wp @staging plugin update --all
wp @staging cache flush
# after review in the staging environment
wp @production deploy
```

The practical difference from self-managed hosting shows up during an incident: managed hosts typically include automatic backups with one-click restore, and support staff who already know WordPress's failure modes specifically, rather than generic server support that has to learn the platform from your ticket.

## Pricing

Both Kinsta and WP Engine are paid, tiered by traffic and site count, with no meaningful free tier, which is what earns this the `$`. The cost typically sits well above generic shared hosting and below the cost of an in-house team operating the same reliability and performance work manually.

## When to reach for this

Any client-facing, revenue-generating, or otherwise important WordPress site, where downtime or a slow page has a real cost, and where nobody in-house wants to own WordPress-specific server tuning and security monitoring.

## When it's the wrong fit

A low-stakes personal blog or an internal tool, where generic, cheaper hosting is entirely sufficient and the specialized tooling of managed WordPress hosting goes largely unused.

> **Under the hood:** Much of what these hosts offer is object caching, storing the results of expensive WordPress database queries in memory (via Redis or Memcached) so a popular page doesn't re-run the same queries for every visitor, the same caching instinct behind [TYPO3's caching framework](ch15-02-typo3-caching-framework.md), pre-configured specifically for WordPress's common query patterns.
