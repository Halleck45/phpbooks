# Passing by Value vs. by Reference

The previous section showed you PHP's default: assign an array to a new variable, modify the new one, and the original is untouched. That default is called **passing (or assigning) by value**, and it's what happens everywhere in PHP unless you explicitly ask for something else. This section covers how to ask for something else. More importantly, it covers the one place where PHP quietly gives you "something else" whether you asked for it or not: objects.

## Explicit references with `&`

PHP lets you make two variables refer to the *same* underlying value on purpose, using `&`:

```php
<?php

$a = 10;
$b = &$a; // $b is now an alias for $a, not a copy of its value

$b = 20;

echo $a; // 20
```

After `$b = &$a`, there's no meaningful sense in which `$a` and `$b` are two separate variables holding equal values: they're two names for the same storage. Change either one, and you've changed both, because there was only ever one thing to change.

You can pass this behavior into a function too, by declaring the parameter with `&`:

```php
<?php
declare(strict_types=1);

function addTax(array &$prices): void
{
    foreach ($prices as $key => $price) {
        $prices[$key] = round($price * 1.2, 2);
    }
}

$cart = ["book" => 10.00, "pen" => 2.00];
addTax($cart);

var_dump($cart); // book => 12.00, pen => 2.40, modified in place
```

Compare this to the `addTax()` from the previous section: same body, but the `&` before `$prices` changes everything about how the caller experiences it. Without `&`, the function received a value it could freely mutate without consequence to the caller. With `&`, `$prices` inside the function *is* `$cart` outside it: there's no copy at all, not even a lazy one. This is genuinely useful when a function's whole job is to modify something in place: think `sort()`, which is a real built-in PHP function that works exactly this way, rearranging your array through a reference rather than handing you back a new one.

It's also easy to overuse. A function signature with `&` in it is quietly changing the contract of the function from "give me data, get data back" to "let me reach into your variable and change it," and that's a bigger promise than it looks like on the page. Reach for it when in-place mutation is genuinely the point (sorting, filling a buffer, that kind of thing) and prefer an ordinary return value everywhere else. Code that returns its result is easier to read, easier to test, and easier to trust at a glance; code sprinkled with `&` parameters requires the reader to go check every call site to know what might have changed.

## Arrays copy, objects don't

Here's the gotcha this whole chapter has been building toward, and it's worth reading slowly, because it trips up almost everyone the first time they meet it.

You already know arrays copy by value: copy-on-write, but functionally a copy. Objects don't. When you assign an object to a variable, pass it into a function, or store it in an array, PHP never duplicates the object itself. Every variable that ends up "holding" that object is really just holding a handle to the one instance living in memory. Copy the variable all you like: you're copying the handle, not the thing it points to.

```php
<?php
declare(strict_types=1);

class Cart
{
    public array $items = [];
}

$cartA = new Cart();
$cartA->items[] = "book";

$cartB = $cartA; // NOT a copy, $cartB points at the same Cart instance
$cartB->items[] = "pen";

var_dump($cartA->items); // ["book", "pen"], both items show up here too
var_dump($cartB->items); // ["book", "pen"]
```

`$cartB = $cartA` looks exactly like `$copy = $original` did with arrays. It behaves nothing like it. There is only one `Cart` object here; `$cartA` and `$cartB` are two labels stuck on the same box. Modify the box through either label, and anyone holding the other label sees the change immediately, because there's nothing else to see: it's the same object.

This is the single most common source of "why did my function change something it wasn't supposed to touch" bugs in beginner PHP code, and it runs in exactly the opposite direction of the array confusion: people expect objects to copy like arrays do, get burned once, and then overcorrect by assuming *everything* aliases like objects do. Neither assumption is right. The rule is simple once it's explicit: **arrays copy, objects alias.** Passing an object into a function never protects the caller's data the way passing an array does: the function receives a handle to the very same instance, and anything it does through that handle is visible the moment the function returns, no `&` required.

```php
<?php
declare(strict_types=1);

function addItem(Cart $cart, string $item): void
{
    $cart->items[] = $item; // this mutates the caller's actual Cart
}

$cart = new Cart();
addItem($cart, "notebook");

var_dump($cart->items); // ["notebook"], visible outside the function, no & needed
```

No `&` appears anywhere in `addItem()`'s signature, and none is needed. Objects are always "passed by handle" (sometimes described loosely as "passed by reference," though that's not quite the precise PHP term), since you *can* reassign `$cart` inside the function to point it at a different object entirely without affecting the caller's variable. What you can't do is mutate the object it points to without that mutation being visible everywhere else that same object is referenced.

## `clone`, the escape hatch

Sometimes you genuinely want an independent copy of an object: a second `Cart` with the same starting items that can then diverge from the original. That's what `clone` is for:

```php
<?php
declare(strict_types=1);

$cartA = new Cart();
$cartA->items[] = "book";

$cartB = clone $cartA; // a genuine, separate copy
$cartB->items[] = "pen";

var_dump($cartA->items); // ["book"], untouched
var_dump($cartB->items); // ["book", "pen"]
```

`clone` creates a new object with the same property values as the original, and from that point on the two instances are fully independent, exactly the behavior you might have mistakenly expected from plain assignment. One caveat worth flagging now and revisiting later: `clone` copies properties one level deep. If one of `Cart`'s properties were itself an object rather than a plain array, the clone and the original would still share *that* nested object, handle and all, unless you do something about it. PHP gives classes a `__clone()` magic method for exactly this situation, which we'll cover once we've spent more time with classes in general, starting in [Chapter 5](ch05-00-classes.md).
