# Laravel: Pest, Larastan, and `composer audit`

**Pest** is a testing framework built on PHPUnit, designed so a test reads close to plain English. Tests that are easy to read get written.

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

**Larastan** wraps PHPStan (see [Symfony's PHPStan/Psalm](ch14-02-symfony-phpunit-phpstan-rector.md) for the framework-agnostic version) with Laravel-specific type knowledge. It catches a call to a method that does not exist on a model, or the wrong type passed to a job, without running the code.

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

**`composer audit`** checks your installed dependencies against a database of known vulnerabilities. The day a package you depend on gets a CVE, this command tells you, before an attacker does.

```bash
composer audit
```

## When to reach for this

Every Laravel project past the prototype stage. **Tests and static analysis are cheapest on day one and most expensive to retrofit** onto a codebase that has already grown without them.

## When it's the wrong fit

There is no wrong fit here. The failure mode is skipping this page under deadline pressure.

> **Under the hood:** PHPStan, and Larastan with it, reads your type hints, including union types, `readonly` properties and enums, and reasons about what is possible without executing anything. The stricter your types, the more bugs it catches before a single test runs.
