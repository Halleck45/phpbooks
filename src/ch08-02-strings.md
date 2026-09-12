# Storing UTF-8 Encoded Text with Strings

<img src="images/ch08-icon.svg" alt="Storing UTF-8 Encoded Text with Strings illustration" width="72">

You met strings back in [Hello, World!](ch01-02-hello-world.md), and used interpolation without much ceremony in the [guessing game](ch02-00-guessing-game-tutorial.md). What we skipped, reasonably, was the part that eventually bites everyone who works with PHP strings: they're not really made of characters. They're made of bytes. Most of the time that distinction is invisible, right up until it isn't.

## Quotes, briefly revisited

A quick recap, since you'll use both constantly: single quotes are as literal as PHP gets, with no interpolation and no escape sequences beyond `\'` and `\\`. Double quotes interpolate variables and understand escape sequences like `\n` and `\t`:

```php
<?php

declare(strict_types=1);

$name = 'Damien';

echo 'Hello, $name\n';   // Hello, $name\n  (literal, no processing)
echo "Hello, $name\n";   // Hello, Damien  (interpolated, newline applied)
```

Reach for single quotes when a string has nothing to interpolate: it's marginally faster (PHP doesn't have to scan the string looking for `$` or `\`), but mostly it signals to the next reader "nothing clever happening here."

## Bytes versus characters

Here's the fact that matters: PHP's classic string functions (`strlen()`, `strtoupper()`, `substr()`, and their relatives) operate on bytes, full stop. That was a perfectly fine assumption in an ASCII world, where one byte is one character. It falls apart the moment your text isn't ASCII, which in a UTF-8 world (essentially all modern PHP output) is often:

```php
<?php

declare(strict_types=1);

$name = 'café';

echo strlen($name) . "\n";     // 5, not 4!
echo mb_strlen($name) . "\n";  // 4, correct
```

`café` has four *characters*, but the é is encoded in UTF-8 as two bytes, so `strlen()`, which counts bytes, reports five. It isn't wrong, exactly; it's answering a question you didn't mean to ask. `mb_strlen()` (the `mb_` stands for multibyte) understands UTF-8 encoding and counts actual characters, which is almost always what you want when the string might contain anything beyond plain English.

The practical rule: if a string could ever contain a name, a comment, a search term, an emoji, anything a user typed, use the `mb_` variant. `strlen()` is still fine for genuinely byte-oriented work: measuring the size of a file's contents, or a string you built yourself out of known ASCII. When in doubt, `mb_strlen()` costs you nothing and saves you from a bug that only shows up for some of your users, usually the ones with accented names, which is exactly the kind of bug that's embarrassing to ship.

## Everyday string functions

A handful of functions cover the bulk of real-world string work:

```php
<?php

declare(strict_types=1);

$message = 'PHP is not dead, it just smells funny.';

if (str_contains($message, 'not dead')) {
    echo "Reassuring.\n";
}

$corrected = str_replace('not dead', 'thriving', $message);
echo $corrected . "\n";

$excerpt = substr($message, 0, 12);
echo $excerpt . "...\n"; // PHP is not d...

$formatted = sprintf('%s scored %d%% on the test.', 'Alice', 92);
echo $formatted . "\n"; // Alice scored 92% on the test.
```

`str_contains()` (PHP 8.0+) replaced the old, awkward `strpos($haystack, $needle) !== false` idiom you'll still see in older code. It does exactly what its name says and returns a plain boolean, no special-case `false` to trip over. `str_replace()` swaps every occurrence of a substring. `substr()` extracts a portion by start position and length. Like `strlen()`, it has an `mb_substr()` counterpart that counts characters instead of bytes, worth reaching for under the same rule as above.

`sprintf()` deserves particular attention: it builds a formatted string from a template and a list of values, which reads far more clearly than a chain of concatenations once more than one or two values are involved, and it gives you control interpolation doesn't: `%d%%` above forces `92` to be treated as an integer and prints a literal `%` sign afterward. `printf()` is the same thing, minus the "return a string" part; it prints directly instead.

## Interpolation, one more time

You already know the basics from Chapter 2, but the full form is worth having on hand: `{$expr}` inside a double-quoted string accepts more than a bare variable, including property access, method calls, array access, anything that resolves to a value:

```php
<?php

declare(strict_types=1);

$user = ['name' => 'Alice', 'age' => 30];

echo "{$user['name']} is {$user['age']} years old.\n";
```

Without the braces, `"$user['name']"` doesn't do what you'd expect: PHP would stop parsing the variable name at `$user` and print the rest literally. The `{$...}` form removes that ambiguity entirely, which is why it's worth using as your default the moment interpolation gets more complex than a single bare `$variable`.
