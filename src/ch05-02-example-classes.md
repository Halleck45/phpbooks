# An Example Program Using Classes

<img src="images/ch05-icon.svg" alt="An Example Program Using Classes illustration" width="72">

Let's see why you'd actually reach for a class, by writing the same small problem two ways.

## The problem, with loose arrays

Say you're building the start of a shop. Each product has a name, a price, and a quantity in the cart, and you need to compute a line total. The array-based version looks perfectly reasonable at first:

```php
<?php
declare(strict_types=1);

function lineTotal(array $product): float
{
    return $product['price'] * $product['quantity'];
}

$item = [
    'name' => 'Coffee mug',
    'price' => 8.50,
    'quantity' => 3,
];

echo lineTotal($item); // 25.5
```

It works, right up until it doesn't. Nothing stops a typo:

```php
<?php

$item = [
    'name' => 'Coffee mug',
    'prise' => 8.50, // typo, silently different key
    'quantity' => 3,
];

echo lineTotal($item); // Warning: Undefined array key "price"
```

That warning fires deep inside `lineTotal()`, far from where the actual mistake was made. Nothing in `$item`'s definition told you what keys it was supposed to have, and nothing checked that `price` was even a number until the moment it was multiplied. As the shop grows (discounts, tax rates, stock levels), every function touching a product array has to independently agree on the same set of magic string keys, and every one of them is a typo away from failing quietly or loudly, at runtime, nowhere near the actual bug.

## The same problem, with a class

```php
<?php
declare(strict_types=1);

class Product
{
    public string $name;
    public float $price;
    public int $quantity;

    public function __construct(string $name, float $price, int $quantity)
    {
        $this->name = $name;
        $this->price = $price;
        $this->quantity = $quantity;
    }

    public function totalPrice(): float
    {
        return $this->price * $this->quantity;
    }
}
```

`Product` now names its shape once, in one place. Try to build one with a typo'd property name, and there's nothing to typo: `new Product(...)` demands exactly `name`, `price`, and `quantity`, in that order, each with a declared type. Get the types wrong and, with `strict_types` on, PHP stops you immediately rather than letting a string quietly stand in for a price:

```php
<?php

$mug = new Product('Coffee mug', 8.50, 3);

echo $mug->totalPrice(); // 25.5
```

`totalPrice()` lives on `Product` itself now, not as a free-floating function somewhere else that has to be told the shape of its argument. Anyone holding a `Product`, anywhere in the codebase, written by anyone, can call `$product->totalPrice()` and get the right answer, because the logic for computing it travels with the data it operates on.

## Using it in a small program

A tiny cart, built from a handful of `Product` objects:

```php
<?php
declare(strict_types=1);

$cart = [
    new Product('Coffee mug', 8.50, 3),
    new Product('Notebook', 4.25, 2),
    new Product('Pen', 1.10, 5),
];

$total = 0.0;

foreach ($cart as $product) {
    echo "{$product->name}: \${$product->totalPrice()}\n";
    $total += $product->totalPrice();
}

echo "Total: \${$total}\n";
```

```console
$ php cart.php
Coffee mug: $25.5
Notebook: $8.5
Pen: $5.5
Total: $39.5
```

Notice `$cart` is still an ordinary array: classes don't replace arrays, they replace what you'd otherwise be forced to stuff *into* one. Here the array is doing exactly what it's good at, holding an ordered list of things, while each individual thing is a `Product` that knows its own shape and its own arithmetic. That combination, plain arrays for collections, classes for the things they collect, is the pattern you'll use constantly for the rest of this book.
