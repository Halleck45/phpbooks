# Closures and Arrow Functions

<img src="images/ch15-icon.svg" alt="Closures and Arrow Functions illustration" width="72">

You met the shape of a closure at the very end of Chapter 3: an anonymous function, assigned to a variable, callable just like any other. What we skipped over is the interesting part: how a closure gets at variables from the code around it, and the two very different ways PHP lets you control that.

## Capturing by value with `use`

A closure doesn't automatically see the variables in its enclosing scope. You have to tell it which ones to bring along, with `use`:

```php
<?php
declare(strict_types=1);

function makeMultiplier(int $factor): callable
{
    return function (int $n) use ($factor): int {
        return $n * $factor;
    };
}

$double = makeMultiplier(2);
$triple = makeMultiplier(3);

echo $double(21) . "\n"; // 42
echo $triple(21) . "\n"; // 63
```

`use ($factor)` copies the value of `$factor` into the closure at the moment the closure is created: the same by-value semantics you already know from [Chapter 4](ch04-02-references.md). `$double` and `$triple` each got their own frozen copy of `$factor` (2 and 3 respectively) when `makeMultiplier()` created them, and nothing that happens afterward to any variable named `$factor` anywhere else can touch either one. That's exactly why calling `makeMultiplier()` twice hands back two closures that behave differently forever, even though they came from the same code.

## Capturing by reference with `use (&$var)`

Sometimes you want the opposite: a closure that shares live storage with a variable in the enclosing scope, so a change on one side is visible on the other. That's `use (&$var)`, the same `&` you saw attached to function parameters:

```php
<?php
declare(strict_types=1);

function makeCounter(): callable
{
    $count = 0;

    return function () use (&$count): int {
        $count++;
        return $count;
    };
}

$counter = makeCounter();
echo $counter() . "\n"; // 1
echo $counter() . "\n"; // 2
echo $counter() . "\n"; // 3
```

`$count` lives inside `makeCounter()`, and by all rights should disappear the moment that function returns. It doesn't, because the closure holds a reference to it: the same aliasing mechanics from Chapter 4, just applied to a variable that only the closure can see. Each call to `$counter()` mutates the shared storage and hands back the new value. Without the `&`, every call would see its own fresh copy of `$count` starting at 0, and this counter would be stuck printing 1 forever.

## Arrow functions: capture without asking

Writing `use` for every variable a small closure needs gets tedious fast, especially for the one-liners you pass into things like `array_map()`. Arrow functions solve exactly that:

```php
<?php
$factor = 3;
$triple = fn(int $n): int => $n * $factor;

echo $triple(14) . "\n"; // 42
```

No `use` clause anywhere, and `$factor` is still visible inside. That's the whole point of `fn`: it automatically captures every variable it references from the enclosing scope, implicitly, by value, as if PHP had silently written `use ($factor)` for you. This is the main practical reason arrow functions exist. A regular closure makes you declare its captures; an arrow function just uses whatever's in scope, at the cost of two real restrictions: the body is a single expression (whatever follows `=>` is automatically the return value: no braces, no `return`, no statements before it), and the capture is always by value. If you need reference capturing, you need a full closure with `use (&$var)`; there's no arrow-function equivalent.

## Where this actually gets used

In practice, you'll write far more arrow functions than full closures, because most of the behavior you pass around is short. `array_map()`, `array_filter()`, and `usort()` are the classic homes for this:

```php
<?php
declare(strict_types=1);

$prices = [10.00, 25.50, 3.99, 100.00];

$withTax = array_map(fn(float $p): float => round($p * 1.2, 2), $prices);

$expensive = array_filter($prices, fn(float $p): bool => $p > 20.00);

usort($prices, fn(float $a, float $b): int => $a <=> $b);
```

`array_map()` applies the closure to every element and returns a new array of the results. `array_filter()` keeps only the elements for which the closure returns something truthy. `usort()` sorts an array in place using the closure to compare two elements at a time: `<=>`, the spaceship operator, is the standard way to write that comparison, returning a negative, zero, or positive number depending on order. None of these three functions needed anything more than a short arrow function, which is exactly the case they were designed for. Reach for a full closure with `use` when you need to capture by reference, or when the logic genuinely needs more than one expression; otherwise, the arrow function is almost always the better default.
