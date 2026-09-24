# Blackfire ($): Finding the Actual Bottleneck

Every fix in this chapter assumes you already know what is slow. Guess wrong and you lose more time than the fix would have cost: a cache in front of a query that was never the bottleneck fixes nothing. **Blackfire profiles a real request and shows where the time and memory went, function by function.**

```bash
composer require blackfire/php-sdk --dev
blackfire run php artisan test
```

Or, for a live request, wrap it directly:

```bash
blackfire curl https://example.com/checkout
```

The profile is a call graph: which function called which, how long each took, how many times it ran. The usual culprits surface at once. An N+1 query loop. An external API called on every iteration when once would do. A template step that dominates the request despite looking trivial in the code.

```php
// what profiling often reveals: 200 queries where one would do
foreach ($orders as $order) {
    echo $order->customer->name; // N+1: one query per order
}

// the fix, informed by the profile rather than a guess
$orders = Order::with('customer')->get();
```

## Pricing

Blackfire has a free tier for individual use. Team collaboration and continuous profiling in CI are paid, hence the `$` for anything beyond solo, occasional use.

## When to reach for this

The moment a page or an endpoint is reported slow and the cause is not obvious from reading the code. Profile first, then fix. The other order wastes a cycle.

## When it's the wrong fit

A page nobody has complained about and no metric has flagged. Profiling tools are for measured problems, not for anxiety about hypothetical ones.

> **Under the hood:** Blackfire is a PHP extension that hooks into the Zend Engine's function call mechanism and times every call transparently. That is why profiling adds measurable overhead, and why it runs against one request on demand rather than on all production traffic.
