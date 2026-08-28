# Generic-Style Code with Docblocks and Static Analysis

Here's something to say plainly, because plenty of documentation dances around it: PHP does not have generics. In a language that does (Java's `List<String>`, TypeScript's `Array<Product>`), the compiler itself refuses to let the wrong type into a typed container. PHP's type system stops at the array boundary. You can type-hint a parameter as `array`, but "an array of what" is not something the language will check for you, ever, at runtime.

```php
<?php

function totalPrice(array $products): float
{
    $total = 0.0;
    foreach ($products as $product) {
        $total += $product->price;
    }
    return $total;
}
```

Nothing here stops you from calling `totalPrice([1, 2, 3])` or `totalPrice(['not', 'products'])`. PHP will happily run the loop and blow up on `$product->price` the moment it hits something that isn't an object with a `price` property, at runtime, in production if you're unlucky, instead of the moment you wrote the bug.

## The workaround: docblocks static analysis tools understand

The PHP ecosystem's answer isn't a language feature; it's a convention. You annotate what an array actually contains in a docblock comment, and a separate tool, run before you ship, checks that annotation against how the code is actually used.

```php
<?php

/**
 * @param Product[] $products
 */
function totalPrice(array $products): float
{
    $total = 0.0;
    foreach ($products as $product) {
        $total += $product->price;
    }
    return $total;
}
```

`@param Product[] $products` means nothing to the PHP interpreter; it's a comment, and `php totalPrice.php` runs identically with or without it. What it means something to is [PHPStan](https://phpstan.org/) or [Psalm](https://psalm.dev/), the two dominant static analysis tools in the PHP world. Run one of them against this file, and it will trace every call site: if some other function passes an array containing an `int`, or a `Refund` object instead of a `Product`, the analyzer flags it: the same category of error a generics-checking compiler would catch, just caught by a separate program instead of the language itself.

## `@template`: closer to real generics

For genuinely generic structures (a collection class that could hold any single type, consistently), both tools understand a more expressive annotation modeled directly on how generics read in other languages:

```php
<?php

/**
 * @template T
 */
final class TypedCollection
{
    /** @var T[] */
    private array $items = [];

    /**
     * @param T $item
     */
    public function add(mixed $item): void
    {
        $this->items[] = $item;
    }

    /**
     * @return T[]
     */
    public function all(): array
    {
        return $this->items;
    }
}
```

Used with a matching `@var` annotation at the call site:

```php
<?php

/** @var TypedCollection<Product> $products */
$products = new TypedCollection();
$products->add(new Product('Keyboard', 49.90));
```

PHPStan will track `T` as `Product` through the rest of that variable's life, and complain the moment you `add()` something that isn't one. `mixed` in the actual method signature is doing the honest work here: it's what PHP itself sees and permits at runtime, anything at all. The `@template T` annotation is the layer above it, understood only by the analyzer, that narrows `mixed` down to something specific for as long as static analysis is watching.

## Where this leaves you

This isn't a workaround you should feel apologetic about; it's simply how PHP's type system works today, and the ecosystem has settled comfortably around it. Real projects run PHPStan or Psalm as a required step in CI, often at a strict analysis level, and treat a docblock type mismatch exactly like a compiler error: something that fails the build, not a suggestion. The runtime stays permissive by design (that's a PHP trait as old as the language), but nothing forces you to *ship* code that only the runtime has checked. Add these annotations wherever an `array` parameter's contents matter, install one of the two tools, and you get most of what a generics-checking language gives you, just delivered a step earlier in your workflow instead of built into `php` itself.
