# List and Array Destructuring

The previous section showed destructuring in its simplest, flat form. Arrays are rarely that tidy in real code: they nest, and they're often associative rather than positional. Destructuring handles both.

## Nested destructuring

If an array contains other arrays, the destructuring pattern can mirror that shape directly:

```php
<?php

$point = [[1, 2], 3];

[[$x, $y], $z] = $point;

echo "x={$x}, y={$y}, z={$z}\n"; // x=1, y=2, z=3
```

The pattern on the left literally looks like the data on the right: `[[$a, $b], $c]` next to `[[1, 2], 3]`. That symmetry is the whole appeal: once an array's shape gets more than one level deep, destructuring lets you say "give me exactly this shape" in one line instead of chaining index access like `$point[0][0]`.

## Keyed destructuring

Positional unpacking works fine for tuples like coordinates, but most arrays you'll destructure in real applications are associative: rows from a database, decoded JSON, form input. For those, match by key instead of position:

```php
<?php

$userData = [
    'name' => 'Priya',
    'age' => 29,
    'email' => 'priya@example.com',
];

['name' => $name, 'age' => $age] = $userData;

echo "{$name} is {$age}.\n"; // Priya is 29.
```

Notice `email` is simply ignored: you only need to name the keys you actually want, and the rest of the array is left alone. This is where destructuring stops being a shorthand and starts being genuinely more readable than the alternative: compare `['name' => $name, 'age' => $age] = $userData;` to two separate lines of `$userData['name']` and `$userData['age']`. The keyed form also self-documents which fields a function actually cares about, right at the point of use.

You can combine keyed and nested destructuring too:

```php
<?php

$response = [
    'status' => 'ok',
    'user' => ['name' => 'Priya', 'age' => 29],
];

['user' => ['name' => $name, 'age' => $age]] = $response;

echo "{$name}, {$age}\n"; // Priya, 29
```

## Swapping two variables

Destructuring has one small, satisfying party trick: swapping the values of two variables without a temporary third one.

```php
<?php

$a = 1;
$b = 2;

[$a, $b] = [$b, $a];

echo "a={$a}, b={$b}\n"; // a=2, b=1
```

PHP builds the array `[$b, $a]` on the right-hand side first (capturing both original values) and only then assigns into `$a` and `$b` on the left. That ordering is exactly what makes the swap safe: by the time `$a` gets overwritten, `$b`'s original value has already been read. It's a small idiom, but it's the kind of line that makes you look like you know the language, and it genuinely is the cleanest way to swap two values in PHP: no `$temp` variable required.

## A word of caution

Destructuring an array that doesn't have the keys or positions you expect doesn't throw: missing elements just become `null`, with a warning in strict error-reporting setups. It's a pattern match in shape only; PHP won't stop you from destructuring a three-element array as if it had five. Treat it as a convenience for code where you already trust the shape of the data; validate first, when the data comes from outside your control.
