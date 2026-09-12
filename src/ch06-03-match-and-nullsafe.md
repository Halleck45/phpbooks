# Concise Control Flow with `match` and `?->`

<img src="images/ch06-icon.svg" alt="Concise Control Flow with match and ?-> illustration" width="72">

We'll close this chapter with a piece of syntax that has nothing to do with enums directly, but solves a closely related problem: handling a value that might be *nothing at all*, without burying the code that actually matters under a stack of defensive checks.

## The nullsafe operator

Recall from [Data Types](ch03-02-data-types.md) that `null` means "no value at all," and recall from [Chapter 5](ch05-01-defining-classes.md) that `->` reaches into an object to get at a property or call a method. Combine the two, and you get a genuinely common problem: what happens when you try to use `->` on something that might be `null`?

```php
<?php
declare(strict_types=1);

class Address
{
    public function __construct(
        public string $city,
    ) {
    }
}

class Customer
{
    public function __construct(
        public string $name,
        public ?Address $address = null,
    ) {
    }
}

$customer = new Customer('Ada');

echo $customer->address->city; // Error: Attempt to read property "city" on null
```

`$customer` has no address on file, so `$customer->address` is `null`, and reaching further with `->city` blows up immediately. The traditional fix is a guard before every such access:

```php
<?php

$city = null;
if ($customer->address !== null) {
    $city = $customer->address->city;
}

echo $city ?? 'No address on file';
```

That works, but it doesn't scale: chain a few more levels (`$order->customer->address->city`, say) and you either nest a guard for every link in the chain, or write one large condition that's checking three different things at once and calling none of them out individually.

The nullsafe operator, `?->`, does this in one step:

```php
<?php
declare(strict_types=1);

$city = $customer->address?->city;

echo $city ?? 'No address on file';
```

`?->` checks whether the thing on its left is `null` before attempting the access. If it is, the whole expression short-circuits to `null` immediately: no error, no exception, just `null`, ready to be handled with `??` or however else you'd handle a missing value. If it isn't `null`, `?->` behaves exactly like ordinary `->`. Chain several together, and the short-circuiting propagates through the whole chain: `$order?->customer?->address?->city` stops at the first `null` it finds and returns `null` for the entire expression, without ever attempting the accesses after it.

One thing worth being deliberate about: `?->` is for "this might legitimately be absent, and that's fine" situations, an optional address, an optional related record. It's not a substitute for thinking about whether `null` should be possible at all. Sprinkling `?->` everywhere out of habit tends to paper over a design that hasn't decided what's actually optional and what genuinely shouldn't ever be missing. Use it where absence is an expected, normal outcome; let a real type error surface anywhere else.

## `match` as the clean alternative to a long `if`/`elseif` chain

We've spent this chapter pairing `match` with enums, but it's worth stepping back to the broader point: `match` is PHP's answer to a long `if`/`elseif` chain checking one thing against several discrete possibilities, enum or not.

```php
<?php
declare(strict_types=1);

function shippingCost(string $countryCode): float
{
    if ($countryCode === 'US') {
        return 5.00;
    } elseif ($countryCode === 'CA') {
        return 7.50;
    } elseif ($countryCode === 'FR' || $countryCode === 'DE') {
        return 9.00;
    } else {
        return 15.00;
    }
}
```

Rewritten as a `match`, the same logic reads as a table rather than a sequence of decisions to follow one after another:

```php
<?php
declare(strict_types=1);

function shippingCost(string $countryCode): float
{
    return match ($countryCode) {
        'US' => 5.00,
        'CA' => 7.50,
        'FR', 'DE' => 9.00,
        default => 15.00,
    };
}
```

Shorter, and, more importantly, every branch is visibly an alternative to every other one, at a glance, rather than a chain of `elseif`s you have to read sequentially to be sure you understand the fallthrough. That's the instinct to carry forward: reach for `if`/`elseif` when your conditions are genuinely different kinds of checks (ranges, combinations, unrelated booleans), and reach for `match` the moment you notice you're really just asking "which one of these known values is it": enums included, but far from the only place that question comes up.
