# How PHP Manages Values: Copy-on-Write

Assign one array to another variable, and PHP behaves as though it made you a completely independent copy:

```php
<?php

$original = [1, 2, 3];
$copy = $original;

$copy[] = 4;

var_dump($original); // array(3) { [0]=> int(1) [1]=> int(2) [2]=> int(3) }
var_dump($copy);     // array(4) { [0]=> int(1) [1]=> int(2) [2]=> int(3) [3]=> int(4) }
```

`$original` is untouched. Modifying `$copy` had no effect on it whatsoever: exactly as if `$copy = $original` had walked through the array and duplicated every element into fresh memory on the spot. That's the mental model you should carry around, and for most day-to-day PHP it's all you need.

## But it doesn't actually copy on the spot

Here's the part that's worth knowing even though it rarely changes how you write code: PHP doesn't really duplicate the array the instant you write `$copy = $original`. That would be wasteful: plenty of arrays get assigned around and never modified at all, so copying eagerly would mean paying a cost for work that's frequently never needed. Instead, PHP uses a strategy called **copy-on-write**. The assignment just makes `$copy` and `$original` point at the same underlying array data, and PHP quietly counts how many variables are pointing at it. Only the moment you actually *modify* one of them (as `$copy[] = 4` does above) does PHP step in, make a real, separate copy first, and apply your change to that copy alone. Read from both variables without changing either, and they'll happily keep sharing the same underlying data behind the scenes:

```php
<?php

$original = ["apple", "banana"];
$copy = $original; // no copying has happened yet, both point at the same data

foreach ($copy as $fruit) {
    echo $fruit . "\n"; // just reading, still sharing
}

$copy[] = "cherry"; // *now* PHP actually duplicates the array
```

You can't observe this happening from inside your program: there's no function call, no visible delay, nothing that behaves differently depending on whether the copy has "really" happened yet. It's purely an optimization the engine performs for you. But the vocabulary matters, because you'll see "copy-on-write" mentioned in PHP performance discussions, RFC text, and the odd profiler output, and it helps to know it isn't some exotic caching layer. It's just PHP being lazy about a copy it was always going to make available to you, semantically, whether or not it does the work up front.

## Why this matters for functions

This is where copy-on-write stops being trivia and starts affecting how you write code. Pass an array into a function, and the function receives what behaves like its own independent copy:

```php
<?php
declare(strict_types=1);

function addTax(array $prices): array
{
    foreach ($prices as $key => $price) {
        $prices[$key] = round($price * 1.2, 2);
    }
    return $prices;
}

$cart = ["book" => 10.00, "pen" => 2.00];
$withTax = addTax($cart);

var_dump($cart);     // unchanged: book => 10.00, pen => 2.00
var_dump($withTax);  // book => 12.00, pen => 2.40
```

`addTax()` modifies `$prices` freely inside the function, and none of that leaks back out to `$cart`. This is usually exactly what you want: a function that takes an array shouldn't be able to reach back out and rewrite data the caller is still holding onto, unless you've explicitly asked for that. If you ever *do* want a function to modify the caller's array directly, that's not something copy-on-write gives you: it's what references are for, which is the whole subject of the [next section](ch04-02-references.md).

One thing worth flagging now, because the contrast is coming: this entire section has been about arrays. Objects play by a different set of rules: assigning one variable's object to another does *not* give you an independent copy, in any sense, lazy or otherwise. That distinction is important enough to earn its own careful treatment, which is where we're headed next.
