# Defining an Enum

<img src="images/ch06-icon.svg" alt="Defining an Enum illustration" width="72">

## Pure enums

An enum defines a type with a fixed, closed set of possible values, called **cases**:

```php
<?php
declare(strict_types=1);

enum Suit
{
    case Hearts;
    case Diamonds;
    case Clubs;
    case Spades;
}

$card = Suit::Hearts;

var_dump($card);          // enum(Suit::Hearts)
var_dump($card === Suit::Hearts); // true
```

`Suit::Hearts` is a real, singleton value: there is exactly one `Suit::Hearts` in your entire program, ever, no matter how many variables point at it. That's a meaningfully stronger guarantee than a string constant ever gave you: a variable typed `Suit` genuinely cannot hold anything other than one of the four cases you declared. Try to assign it a typo'd value, or a plain string, and PHP stops you at the type level, not with a bug report three weeks later.

```php
<?php
declare(strict_types=1);

function describe(Suit $suit): string
{
    return "You drew a {$suit->name}.";
}

echo describe(Suit::Spades); // You drew a Spades.
```

Every case has a built-in `->name` property: the exact identifier you declared it with, as a string. Handy for logging or debugging; not something you should build serious program logic around, since it's really just the case's label.

## Backed enums

A pure enum's cases don't have an underlying value beyond themselves; they're not secretly strings or integers. Often, though, you need one: to store a status in a database column, to serialize it into JSON for an API response, to compare it against a value that arrived from outside your program entirely. For that, PHP gives you a **backed enum**, where every case is tied to a scalar value you choose:

```php
<?php
declare(strict_types=1);

enum Status: string
{
    case Pending = 'pending';
    case Shipped = 'shipped';
    case Cancelled = 'cancelled';
}

$status = Status::Shipped;

echo $status->value; // shipped
```

`: string` after the enum name declares it as backed by strings: every case must then declare a matching string value, and PHP enforces that at definition time. Integers work the same way (`enum Status: int`), but strings are by far the more common choice in practice, since a string like `'shipped'` is self-describing the moment you see it in a database row or a JSON payload, where a bare `2` tells you nothing without cross-referencing the enum definition.

Backed enums give you two extra ways to build a case from its underlying value:

```php
<?php

$status = Status::from('shipped');   // Status::Shipped
echo $status->name;                  // Shipped

$status = Status::tryFrom('bogus');  // null, no matching case
var_dump($status);
```

`from()` converts a raw value into the matching case, and throws a `ValueError` if nothing matches: reach for it when an unrecognized value genuinely represents a bug you want to know about immediately. `tryFrom()` is the forgiving sibling: it returns `null` instead of throwing, which is exactly what you want when the value is arriving from somewhere you don't fully trust, like user input or an external API, and "not a valid status" is a case you intend to handle rather than crash on.

## Enums can have methods

An enum isn't just a list of named values; it can carry behavior too, the same way a class can:

```php
<?php
declare(strict_types=1);

enum Status: string
{
    case Pending = 'pending';
    case Shipped = 'shipped';
    case Cancelled = 'cancelled';

    public function label(): string
    {
        return match ($this) {
            Status::Pending => 'Awaiting shipment',
            Status::Shipped => 'On its way',
            Status::Cancelled => 'Order cancelled',
        };
    }
}

echo Status::Shipped->label(); // On its way
```

`label()` behaves exactly like a method on any class: `$this` inside it refers to the specific case it was called on, just as it referred to a specific object back in [Chapter 5](ch05-03-methods.md). This is a genuinely good place to put presentation logic that would otherwise end up scattered across your codebase as a pile of `if ($status === 'shipped') { ... }` checks: the mapping from a case to a human-readable label lives in exactly one place, right next to the cases themselves. We'll look at `match` used this way (matching directly on an enum case rather than a loose condition) in real depth in the next section.
