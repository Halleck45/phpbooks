# Storing Lists of Values with Indexed Arrays

An indexed array is what most languages just call an array or a list: an ordered sequence of values, each reachable by a numeric position starting at 0. In PHP, you build one with square brackets:

```php
<?php

declare(strict_types=1);

$fruits = ['apple', 'banana', 'cherry'];

echo $fruits[0] . "\n"; // apple
echo $fruits[2] . "\n"; // cherry
echo count($fruits) . "\n"; // 3
```

`count()` is the function you'll reach for constantly: it's O(1), an instant lookup, not a walk through the array, so never hesitate to call it inside a loop condition.

## Appending

You rarely build an array fully formed. More often you start empty and grow it, and PHP's syntax for "add this to the end" is `[]` with nothing inside the brackets:

```php
<?php

declare(strict_types=1);

$shoppingList = [];

$shoppingList[] = 'milk';
$shoppingList[] = 'eggs';
$shoppingList[] = 'bread';

print_r($shoppingList);
// Array
// (
//     [0] => milk
//     [1] => eggs
//     [2] => bread
// )
```

`$shoppingList[]` looks like indexing into nothing, but read it as its own idiom: "give this the next available index and put it there." PHP tracks that next index for you; you never have to.

## The mental model: arrays are ordered maps

Here's the fact that makes the rest of this chapter, and the next section on associative arrays, click into place: there's no separate "list" type in PHP. `['apple', 'banana', 'cherry']` is shorthand for `[0 => 'apple', 1 => 'banana', 2 => 'cherry']`: an indexed array *is* an associative array whose keys happen to be sequential integers starting at zero. Every PHP array, underneath, is the same ordered structure: a hash map that also remembers insertion order.

This explains behavior that otherwise looks like a quirk. Filter an indexed array and the surviving elements keep their *original* keys, not fresh ones:

```php
<?php

declare(strict_types=1);

$numbers = [10, 15, 20, 25, 30];

$even = array_filter($numbers, fn (int $n) => $n % 2 === 0);

print_r($even);
// Array
// (
//     [0] => 10
//     [2] => 20
//     [4] => 30
// )
```

Keys `1` and `3` are simply gone, not renumbered, because under the hood, `array_filter()` removed two entries from a map, and a map has no obligation to stay contiguous. If you need a clean `0, 1, 2, ...` sequence afterward, `array_values()` re-indexes:

```php
<?php

$reindexed = array_values($even); // [10, 20, 30]
```

## Functions you'll reach for constantly

A handful of functions cover most of what you do with indexed arrays day to day:

```php
<?php

declare(strict_types=1);

$scores = [88, 92, 74, 95, 60];

array_push($scores, 100);        // append (same as $scores[] = 100, but explicit)
$last = array_pop($scores);      // removes and returns the last element (100)

$passing = array_filter($scores, fn (int $s) => $s >= 60);
$grades = array_map(fn (int $s) => $s >= 90 ? 'A' : 'B', $passing);

sort($scores); // sorts in place, re-indexes from 0

$hasTopScore = in_array(95, $scores, strict: true);

echo implode(', ', $grades) . "\n";
```

`array_map()` transforms every element and returns a same-length array; `array_filter()` keeps elements that pass a test and, as you just saw, does not reindex; `sort()` mutates the array in place *and* renumbers it, which is worth remembering if you were relying on the original keys for anything. `in_array()` with `strict: true` uses `===` under the hood rather than PHP's looser default comparison, worth making a habit, for the same reason `===` earned its own callout back in [Data Types](ch03-02-data-types.md).

`array_push()` and `$scores[] = ...` do the same thing for a single value; `array_push()` exists mainly because it can take several values at once and because "push" reads clearly when you're thinking of the array as a stack. Either is fine: pick whichever reads better at the call site.
