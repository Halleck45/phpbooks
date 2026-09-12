# Data Types

<img src="images/ch03-icon.svg" alt="Data Types illustration" width="72">

PHP will let you write an entire program without ever mentioning a single type. It will also, if you ask it to, hold you to your types as strictly as any statically-typed language would refuse a mismatch. Both of these are true at once, and understanding why is most of what this section is about.

## Scalar types

Four types hold a single value each:

```php
<?php

$age = 41;           // int
$price = 19.99;      // float
$name = "Damien";    // string
$isReady = true;     // bool
```

Check what you're holding with `gettype()` or, more usefully while debugging, `var_dump()`:

```php
<?php

var_dump($age);
// int(41)

var_dump($price);
// float(19.99)
```

`var_dump()` will become one of your most-used tools. Get comfortable with it early: it tells you not just the value but the *type*, which `echo` never will.

## Compound types

Two types hold collections of other things.

**Arrays** are PHP's do-everything data structure: list, dictionary, stack, queue, all the same underlying type wearing different hats:

```php
<?php

$fruits = ["apple", "banana", "cherry"];   // indexed
$prices = ["apple" => 0.5, "banana" => 0.3]; // associative
```

We'll spend all of [Chapter 8](ch08-00-common-collections.md) on arrays, because they deserve it: there is no PHP program of any size that doesn't lean on them constantly.

**Objects** are instances of classes, PHP's building block for bundling data with the behavior that operates on it. We're not there yet ([Chapter 5](ch05-00-classes.md) is where objects properly start), but you'll see the odd one in passing before then.

## Special types

`null` represents "no value at all": not zero, not an empty string, genuinely nothing:

```php
<?php

$middleName = null;
```

You'll meet `null` constantly, usually in the form of "did this function find anything, or not." PHP 8.1 also gave `null` some real teeth with enums and the nullsafe operator (`?->`), both coming in [Chapter 6](ch06-00-enums.md).

## Type juggling, and how to stop worrying about it

Here's the thing PHP is famous for, fairly or not: it will convert between types automatically when an operator demands it.

```php
<?php

var_dump("5" + 3);      // int(8)
var_dump("5" . 3);      // string(2) "53"
var_dump(0 == "abc");   // false, as of PHP 8 (this used to be true!)
```

`+` expects numbers, so the string `"5"` gets converted; `.` (string concatenation) expects strings, so the integer `3` gets converted the other way. This is *type juggling*, and older PHP tutorials will tell you horror stories about it, mostly because loose comparison (`==`) used to have some genuinely surprising rules before PHP 8 tightened them up considerably.

Two habits keep this from ever biting you:

**Prefer `===` over `==`.** Strict comparison checks type *and* value, with no conversion: `0 === "abc"` is simply `false`, no asterisk needed. Reach for loose `==` only when you specifically want the conversion.

**Turn on strict types.** Put this as the very first statement in a file, right after `<?php`:

```php
<?php
declare(strict_types=1);

function double(int $n): int {
    return $n * 2;
}

double("4"); // TypeError: no silent conversion here
```

Without `declare(strict_types=1)`, PHP will happily convert `"4"` to `4` for you when it's passed into a typed parameter. With it, that same call throws a `TypeError` instead. Modern PHP code almost always turns this on: it turns "PHP quietly guessed what you meant" into "PHP told you exactly what went wrong," which is a much better bug report to receive.

We'll use type declarations (on parameters, return values, and eventually properties) throughout this book. They're optional in PHP, but treat them as the default, not the exception.
