# Storing Keys with Associated Values in Associative Arrays

You already know, from the previous section, that there's no real difference between an indexed array and an associative array: they're the same underlying structure, PHP's ordered map, and the only thing that changes is what you use as the key. An associative array is just an array where you chose the keys yourself, usually strings, instead of letting PHP assign sequential integers:

```php
<?php

declare(strict_types=1);

$prices = [
    'apple' => 0.50,
    'banana' => 0.30,
    'cherry' => 3.20,
];

echo $prices['banana'] . "\n"; // 0.3
$prices['date'] = 4.10; // add a new key
```

Keys can be strings or integers (PHP will happily mix both in the same array), but they must be unique: assign to an existing key and you overwrite the old value rather than adding a second entry.

## `isset()` versus `array_key_exists()`, and the gotcha between them

Both functions answer a version of "is this key there," and they are not interchangeable: the difference has caused real bugs, so it's worth internalizing rather than half-remembering.

```php
<?php

declare(strict_types=1);

$user = [
    'name' => 'Alice',
    'nickname' => null,
];

var_dump(isset($user['name']));               // true
var_dump(isset($user['nickname']));           // false, surprising!
var_dump(array_key_exists('nickname', $user)); // true
```

`isset()` checks whether a value exists *and is not `null`*. `nickname` is a real key with a real entry, but its value happens to be `null`, and `isset()` treats that exactly like "not there." `array_key_exists()` doesn't care what the value is; it only asks whether the key was ever set, `null` or otherwise.

This matters in practice whenever `null` is a meaningful value rather than an absence: a user record where "no nickname" is legitimately stored as `null`, say. Reach for `isset()` for the common case (does this exist *and have a usable value*), and `array_key_exists()` when you specifically need to distinguish "never set" from "set to `null`." Mixing them up is one of those PHP surprises that costs you an hour the first time and never again after that. Trust me on this one.

## Iterating with `foreach`

You saw `foreach` in [Control Flow](ch03-05-control-flow.md) mostly on indexed arrays. On an associative array, the key-value form is where it earns its keep:

```php
<?php

declare(strict_types=1);

$prices = [
    'apple' => 0.50,
    'banana' => 0.30,
    'cherry' => 3.20,
];

foreach ($prices as $fruit => $price) {
    echo "{$fruit}: \${$price}\n";
}
// apple: $0.5
// banana: $0.3
// cherry: $3.2
```

Iteration order matches insertion order, always: another direct consequence of arrays being ordered maps rather than genuinely unordered hash tables. You never have to sort an associative array just to get a predictable iteration order; it already has one.

## Nesting: arrays of associative arrays

The shape you'll meet constantly in real code is a list of records: an indexed array where each element is itself an associative array, standing in for one row of data:

```php
<?php

declare(strict_types=1);

$books = [
    ['title' => 'The Pragmatic Programmer', 'author' => 'Hunt & Thomas', 'year' => 1999],
    ['title' => 'Refactoring', 'author' => 'Martin Fowler', 'year' => 2018],
    ['title' => 'Clean Code', 'author' => 'Robert C. Martin', 'year' => 2008],
];

foreach ($books as $book) {
    echo "{$book['title']} ({$book['year']}): {$book['author']}\n";
}

$recent = array_filter($books, fn (array $book) => $book['year'] >= 2008);
$titles = array_map(fn (array $book) => $book['title'], $books);

echo implode(', ', $titles) . "\n";
```

This is exactly the shape you get back from a database query, a JSON API response decoded with `json_decode($json, true)`, or a CSV file read row by row: a list of records, each one an associative array of fields. It looks almost too simple to call out, but it's worth naming explicitly: by the time you reach [Chapter 14](ch14-00-a-cli-project.md) and beyond, this pattern (indexed array outside, associative array inside) is how you'll represent most real-world data before it becomes anything more structured, like the objects from [Chapter 5](ch05-00-classes.md).
