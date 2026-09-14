# Where `match` and Destructuring Can Be Used

Destructuring is assignment that unpacks. Instead of assigning one value to one variable, you assign several values from an array to several variables, in a single statement, by describing the shape you expect on the left-hand side. It shows up in more places than you'd guess once you start looking for it.

## The two spellings

The original syntax uses `list()`:

```php
<?php

$coordinates = [4, 7];

list($x, $y) = $coordinates;

echo "x={$x}, y={$y}\n";
```

PHP later added a shorter form using square brackets, which does exactly the same thing and is the one you'll see in modern code:

```php
<?php

$coordinates = [4, 7];

[$x, $y] = $coordinates;

echo "x={$x}, y={$y}\n";
```

Both forms match values positionally: the first element of the array goes to the first variable named, the second to the second, and so on. `list()` still appears in older codebases and a handful of PHP's own documentation examples, so it's worth recognizing, but there's no reason to reach for it in new code: the bracket form is shorter and reads the same.

## Inside a foreach

Destructuring becomes genuinely useful when you combine it with `foreach`, unpacking each element of a collection as you iterate:

```php
<?php

$pairs = [
    ['Alice', 30],
    ['Bob', 25],
    ['Carol', 35],
];

foreach ($pairs as [$name, $age]) {
    echo "{$name} is {$age} years old.\n";
}
```

```console
$ php pairs.php
Alice is 30 years old.
Bob is 25 years old.
Carol is 35 years old.
```

Without destructuring, you'd write `$pair[0]` and `$pair[1]` inside the loop body: it works, but it tells the reader nothing about what those positions *mean*. `foreach ($pairs as [$name, $age])` documents the shape of the data right there in the loop header.

## Skipping elements

Sometimes you only want some of the values an array offers. Leaving a slot empty skips it, without shifting the positions of the ones you do want:

```php
<?php

$row = [1, 'Second', 'Third'];

[, $second, $third] = $row;

echo "{$second}, {$third}\n"; // Second, Third
```

The leading comma with nothing before it says "skip the first element": the variable list has a gap where a name would normally go. This is a small thing, but it reads better than assigning a value to `$unused` you'll never touch.

That covers where destructuring shows up. The next section goes deeper into the array-unpacking syntax itself: nesting, matching by key instead of position, and a genuinely useful one-liner for swapping two variables.
