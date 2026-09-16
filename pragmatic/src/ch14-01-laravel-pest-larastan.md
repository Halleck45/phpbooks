# Laravel: Pest, Larastan, and `composer audit`

**Pest** is a testing framework built on top of PHPUnit, designed so tests read close to plain English, lowering the barrier to actually writing them.

```bash
composer require pestphp/pest --dev --with-all-dependencies
php artisan pest:install
```

```php
it('rejects an order with no items', function () {
    $order = Order::factory()->create();

    expect(fn () => $order->submit())
        ->toThrow(EmptyOrderException::class);
});

it('applies a discount code correctly', function () {
    $order = Order::factory()->create(['total' => 100]);

    $order->applyDiscount('SAVE10');

    expect($order->total)->toBe(90.0);
});
```

```bash
php artisan test
```

**Larastan** wraps PHPStan (see [Symfony's PHPStan/Psalm](ch14-02-symfony-phpunit-phpstan-rector.md) for the framework-agnostic version) with Laravel-specific type knowledge, catching bugs like calling a method that doesn't exist on a model, or passing the wrong type to a job, without ever running the code.

```bash
composer require larastan/larastan --dev
```

```neon
# phpstan.neon
includes:
    - vendor/larastan/larastan/extension.neon
parameters:
    level: 6
    paths: [app]
```

```bash
vendor/bin/phpstan analyse
```

**`composer audit`** checks installed dependencies against a database of known vulnerabilities, catching the moment a package you depend on gets a CVE, before an attacker finds it first.

```bash
composer audit
```

## When to reach for this

Every Laravel project past the prototype stage. Tests and static analysis are cheapest to add early and most expensive to retrofit onto a codebase that's already grown without them.

## When it's the wrong fit

There isn't really one here; the honest failure mode is skipping this chapter under deadline pressure, not a case where it's the wrong tool.

> **Under the hood:** PHPStan (and by extension Larastan) works by reading your code's type hints, including PHP's union types, `readonly` properties, and enums, and reasoning about what's possible without executing anything. The stricter your type hints, the more bugs it can catch before a single test runs.
