# Control Flow

You've already seen `if`, `while`, `break`, and `continue` in the guessing game. This section makes them official and fills in the rest.

## `if` / `elseif` / `else`

```php
<?php

$temperature = 18;

if ($temperature > 30) {
    echo "Hot.\n";
} elseif ($temperature > 15) {
    echo "Pleasant.\n";
} else {
    echo "Bring a jacket.\n";
}
```

Note it's `elseif`, one word (`else if`, two words, also works), but only `elseif` reads as a single token to PHP, so it's the convention worth adopting. The condition doesn't need to be a boolean; PHP will convert whatever you hand it: `0`, `""`, `null`, and `[]` are all "falsy," everything else is "truthy," but relying on that too heavily is exactly the kind of type-juggling ambiguity [Chapter 3.2](ch03-02-data-types.md) warned you about. Prefer an explicit comparison when it isn't already obviously a boolean.

An `if`/`elseif` chain like this one is at its best when each branch tests something genuinely different, the way `$temperature > 30` and `$temperature > 15` do above. Once you catch yourself writing several branches that all compare the *same* value against a list of possibilities, that repetition is a sign to reach for the next tool instead.

## `match`

PHP 8 added `match`, and once you've used it, `switch` starts to feel like a relic:

```php
<?php

$httpStatus = 404;

$message = match (true) {
    $httpStatus >= 200 && $httpStatus < 300 => "Success",
    $httpStatus >= 400 && $httpStatus < 500 => "Client error",
    $httpStatus >= 500 => "Server error",
    default => "Unknown",
};

echo $message; // Client error
```

Two things make `match` a real upgrade over `switch`: it's an *expression* (it produces a value you can assign, as above, rather than a statement you branch inside of), and its comparisons are strict (`===`), so there's no accidental type juggling sneaking a wrong branch through. It also has no fallthrough to accidentally forget a `break` on. We'll give `match` a full chapter of its own once we pair it with enums in [Chapter 6](ch06-00-enums.md), where the two turn out to be made for each other.

## Loops

**`while`** runs as long as its condition holds, checked before each pass:

```php
<?php

$count = 3;
while ($count > 0) {
    echo "{$count}...\n";
    $count--;
}
echo "Go!\n";
```

**`do...while`** is the same idea, but checks *after* the first pass, guaranteeing the body runs at least once:

```php
<?php

do {
    echo "This runs once even if the condition is already false.\n";
} while (false);
```

**`for`** is the classic three-part loop, most at home when you need an index:

```php
<?php

for ($i = 0; $i < 5; $i++) {
    echo "{$i}\n";
}
```

**`foreach`** is the one you'll reach for constantly once arrays enter the picture in [Chapter 8](ch08-00-common-collections.md): it walks a collection directly, no index bookkeeping required:

```php
<?php

$fruits = ["apple", "banana", "cherry"];

foreach ($fruits as $fruit) {
    echo "{$fruit}\n";
}

$prices = ["apple" => 0.5, "banana" => 0.3];

foreach ($prices as $name => $price) {
    echo "{$name}: \${$price}\n";
}
```

That second form, `as $name => $price`, pulls out both the key and the value in one go, and it's used so often in real PHP code that it's worth committing to memory right now.

## `break` and `continue`, one more time

You met both in the guessing game: `break` exits a loop immediately, `continue` skips to the next iteration. Both accept an optional number (`break 2` exits two levels of nested loop at once), but reach for that only when it genuinely reads clearer than restructuring the loop; nested `break` levels are exactly the kind of thing that's obvious while you're writing it and baffling a month later.

```php
<?php

foreach ([1, 2, 3, 4, 5] as $n) {
    if ($n === 3) {
        continue; // skip 3, keep going
    }
    if ($n === 5) {
        break; // stop entirely once we hit 5
    }
    echo "{$n}\n";
}
// prints 1, 2, 4
```

That's the toolkit: branch with `if` or `match`, repeat with `while`, `do...while`, `for`, or `foreach`, and steer loops precisely with `break` and `continue`. Everything from here on in the book is built out of these same handful of pieces, arranged in more interesting shapes.
