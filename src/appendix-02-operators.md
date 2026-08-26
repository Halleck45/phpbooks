# B - Operators and Symbols

A reference table, grouped by what the operators actually do rather than alphabetically. Alphabetical order is great for dictionaries and terrible for remembering anything.

## Arithmetic

| Operator | Meaning |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulo (remainder) |
| `**` | Exponentiation |

## Assignment

| Operator | Meaning |
|---|---|
| `=` | Assign |
| `+=` `-=` `*=` `/=` | Arithmetic, then assign |
| `.=` | Concatenate, then assign |
| `%=` `**=` | Modulo / exponentiate, then assign |

Each compound assignment operator is shorthand: `$x += 1` is exactly `$x = $x + 1`, just shorter and, once you're used to it, easier to read at a glance.

## Comparison

| Operator | Meaning |
|---|---|
| `==` | Equal, after type juggling |
| `===` | Identical: same type and value, no juggling |
| `!=` `<>` | Not equal |
| `!==` | Not identical |
| `<` `>` `<=` `>=` | Less than, greater than, and their "or equal" variants |
| `<=>` | Spaceship |

The spaceship operator (`<=>`) compares two values and returns `-1`, `0`, or `1`, meaning less than, equal, or greater than, which is exactly the three-way answer sorting callbacks expect:

```php
<?php

$numbers = [5, 3, 8, 1];
usort($numbers, fn($a, $b) => $a <=> $b);
```

Before it existed, that comparison took three lines of `if`. Now it's one operator doing what it says.

Prefer `===` over `==` by default, for the reasons covered in [Chapter 3](ch03-02-data-types.md).

## Logical

| Operator | Meaning |
|---|---|
| `&&` | And |
| `\|\|` | Or |
| `!` | Not |
| `and` `or` `xor` | Word forms of and/or/exclusive-or |

`and`/`or` do the same job as `&&`/`||`, but at much lower precedence, low enough to lose to `=`. This compiles, and does not do what it looks like it does:

```php
<?php

$result = false or true;
var_dump($result); // bool(false)
```

`=` binds tighter than `or`, so that line is actually `($result = false) or true`: `$result` gets `false`, and the `or true` is discarded as an unused expression. Swap in `||` and it works as expected. Stick to `&&` and `||`; leave `and`/`or`/`xor` alone unless you have specifically memorized their precedence table, which is not a thing worth memorizing.

## String

| Operator | Meaning |
|---|---|
| `.` | Concatenation |
| `.=` | Concatenate and assign |

## Array

| Operator | Meaning |
|---|---|
| `+` | Union: keys from the left array win on conflict |
| `...` | Spread: unpacks one array's elements into another, or into a function call |

Array `+` is not array merging; see [Chapter 8](ch08-00-common-collections.md) for the difference between `+` and `array_merge()`, which handle duplicate keys in opposite ways.

## Null-related

| Operator | Meaning |
|---|---|
| `??` | Null coalescing: right side, only if left side is `null` or unset |
| `??=` | Null coalescing assignment |
| `?->` | Nullsafe method/property access |

```php
<?php

$name = $user->name ?? 'Anonymous';   // fall back if null
$config['retries'] ??= 3;             // set only if not already set

$city = $user?->address?->city;       // null, not a fatal error, if either is null
```

All three are covered properly in [Chapter 6](ch06-00-enums.md).

## Other symbols

| Symbol | Meaning |
|---|---|
| `$` | Marks a variable name |
| `->` | Access a property or method on an object instance |
| `::` | Access a static property, static method, class constant, or parent from within a class |
| `#[...]` | Attribute: structured metadata attached to a class, method, or property |

Attributes are the newest of the four, and get a full treatment in [Chapter 18](ch18-04-attributes.md).
