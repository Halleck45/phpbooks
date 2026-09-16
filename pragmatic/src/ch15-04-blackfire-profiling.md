# Blackfire ($): Finding the Actual Bottleneck

Every performance fix in this chapter, worker mode, caching, scaling infrastructure, assumes you already know what's slow. Guessing wrong wastes far more time than the fix itself: adding a cache in front of a query that was never the bottleneck fixes nothing. Blackfire profiles a real request and shows exactly where the time and memory went, function by function.

```bash
composer require blackfire/php-sdk --dev
blackfire run php artisan test
```

Or, for a live request, wrapping it directly:

```bash
blackfire curl https://example.com/checkout
```

The resulting profile shows a call graph: which function called which, how long each took, and how many times each ran, immediately surfacing the usual real-world culprits: an N+1 database query loop, an uncached external API call repeated needlessly, a template rendering step that turns out to dominate the request despite looking trivial in the code.

```php
// what profiling often reveals: 200 queries where one would do
foreach ($orders as $order) {
    echo $order->customer->name; // N+1: one query per order
}

// the fix, informed by the profile rather than a guess
$orders = Order::with('customer')->get();
```

## Pricing

Blackfire has a free tier for individual use, with paid plans for team collaboration and continuous profiling in CI, which is what earns it the `$` for anything beyond solo, occasional use.

## When to reach for this

The moment a specific page or endpoint is reported slow and the cause isn't obvious from reading the code. Profile first, then fix; fixing first and profiling to confirm it worked is backwards and usually wastes a cycle.

## When it's the wrong fit

Optimizing a page nobody has complained about and no metric has flagged. Profiling tools are for measured problems, not anxiety about hypothetical ones.

> **Under the hood:** Blackfire works via a PHP extension that hooks into the Zend Engine's function call mechanism, timing every function call transparently, which is why profiling adds measurable overhead and is normally run against a specific request on demand rather than left on for all production traffic.
