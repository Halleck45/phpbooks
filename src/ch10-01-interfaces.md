# Defining Shared Behavior with Interfaces

Suppose you're writing something that needs to print a human-readable summary of an object: an invoice line, a product, a log entry, whatever it happens to be that week. You could give every class you write a `describe()` method and hope everyone remembers the naming convention. Or you could make it a rule the language itself checks. That's what an interface is for.

```php
<?php

interface Formattable
{
    public function format(): string;
}
```

An interface looks like a class with all the bodies removed. `format(): string` here is a *signature*, not an implementation: no braces, no logic, just a promise. Any class that says it implements `Formattable` must have a public `format()` method that returns a string. PHP enforces this at the language level. Leave the method out, or return the wrong type, and your code won't run.

## Implementing it

A class opts in with `implements`:

```php
<?php

readonly class Product
{
    public function __construct(
        public string $name,
        public float $price,
    ) {
    }
}

readonly class InvoiceLine implements Formattable
{
    public function __construct(
        private Product $product,
        private int $quantity,
    ) {
    }

    public function format(): string
    {
        $total = $this->product->price * $this->quantity;
        return sprintf('%dx %s, $%.2f', $this->quantity, $this->product->name, $total);
    }
}
```

`InvoiceLine implements Formattable` is a claim PHP will verify for you: if `format()` were missing, or typed to return an `int`, you'd get a fatal error the moment PHP tried to load the class, not buried three calls deep in production. A class can implement more than one interface, separated by commas, which is one of the ways PHP works around not having multiple inheritance for classes.

## Why bother: programming against the interface

Here's the part that actually pays for itself. Write a function that type-hints the interface, not the concrete class:

```php
<?php

function printSummary(Formattable $item): void
{
    echo $item->format() . "\n";
}

printSummary(new InvoiceLine(new Product('Keyboard', 49.90), 2));
```

`printSummary()` doesn't know or care that it received an `InvoiceLine`. It only knows it received *something* that can `format()`. Add a second class tomorrow (`Refund`, `Discount`, `ShippingFee`, whatever), implement `Formattable` on it, and `printSummary()` needs no changes at all. It already works, because it was never written against a specific class in the first place.

This matters even more once tests enter the picture. If `printSummary()` had type-hinted `InvoiceLine` directly, testing it in isolation would mean constructing a real `InvoiceLine` with a real `Product` behind it. Type-hint `Formattable` instead, and a test can hand it any object that satisfies the contract, including a deliberately fake one built just for the test, with no `Product` in sight. We'll put that to direct use once we reach [Chapter 11](ch11-00-testing.md).

## `instanceof`

Occasionally you need to ask, at runtime, whether an object satisfies an interface:

```php
<?php

if ($item instanceof Formattable) {
    echo $item->format() . "\n";
}
```

Reach for this rarely. If you find yourself writing a lot of `instanceof` checks before calling a method, that's usually a sign the method belongs on an interface you should be type-hinting against instead, not a sign you need more `instanceof`.

## A note on naming

PHP has no special syntax to mark an interface as "just" a contract versus something more structural: `Formattable`, `Countable`, `Stringable`, `ArrayAccess` are all ordinary interfaces, some built into the language itself, some yours. Convention favors an adjective ending in *-able* for a single-capability contract (`Formattable`, `Comparable`, `Sortable`), which signals intent to the next reader even though PHP itself doesn't require it. We'll meet several of PHP's own built-in interfaces later, in [Chapter 18](ch18-00-advanced-features.md).
