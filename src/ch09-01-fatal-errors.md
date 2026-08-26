# Unrecoverable Errors: Fatal Errors and `Error`

Some problems aren't a matter of unlucky input or a missing file: they're a matter of your code being wrong. You called a method that doesn't exist. You passed a string where a function demanded an integer, with strict types on. You divided by zero. None of these are things a well-behaved program should be designed to "handle" gracefully, because there's nothing sensible to do in response except fix the bug.

PHP represents this category with the `Error` class and its subclasses. A few you'll meet constantly:

```php
<?php

declare(strict_types=1);

function half(int $n): int
{
    return $n / 0; // DivisionByZeroError
}

function double(int $n): int
{
    return $n * 2;
}

double("four"); // TypeError: strict_types is on, no silent conversion

$user = null;
$user->getName(); // Error: Call to a member function getName() on null
```

`DivisionByZeroError`, `TypeError`, and the generic `Error` you get from calling a method on `null` are all doing the same job: telling you, as precisely as possible, that the program reached a state it has no business being in. This is exactly the kind of situation `declare(strict_types=1)` was designed to surface loudly rather than let slide; you met the mechanism in [Data Types](ch03-02-data-types.md), and this is where it pays off.

## Why this used to be worse

If you look at PHP code written before version 7, you'll find a lot of manual `null` checks and `is_int()` guards scattered defensively through function bodies, because back then, many of these situations didn't throw anything catchable at all. Calling a method on `null` was a fatal error that simply halted the script, full stop, no `try`/`catch` in the world could intervene. A type mismatch might silently coerce, or emit a warning to a log nobody was watching, and keep going with garbage data.

PHP 7 introduced `Error` (and PHP 8 sharpened it further) specifically to fix this: nearly everything in this category is now a real object implementing `Throwable`, the same interface `Exception` implements. That means you technically *can* write `catch (Error $e)` and keep your program running. It also means you very often shouldn't.

## Catchable doesn't mean "should catch"

The distinction that matters here isn't "can PHP represent this as an object" (as of PHP 8, it almost always can); it's "does catching this actually fix anything." Compare:

```php
<?php

declare(strict_types=1);

// Reasonable: the input is genuinely unpredictable, and there's a sensible fallback.
try {
    $config = json_decode($configJson, associative: true, flags: JSON_THROW_ON_ERROR);
} catch (\JsonException $e) {
    $config = [];
}

// Unreasonable: papering over a bug instead of fixing it.
try {
    $total = $order->getTotal(); // $order might be null due to a bug upstream
} catch (\Error $e) {
    $total = 0; // now every bug in this code path just... returns zero, silently
}
```

The first case catches a genuinely recoverable situation: malformed JSON from an external source is a normal thing to happen, and falling back to an empty config is a defensible choice. The second case catches a symptom of a bug and hides it behind a plausible-looking number. Six months later, someone is debugging why totals are occasionally zero, with no exception, no log entry, no clue, because the `catch` block ate the only evidence that something went wrong.

The rule worth keeping: catch `Error` and its subclasses only when you have a genuinely good reason and a narrow, specific type; never a broad `catch (\Error $e)` used as a safety net. If your own code is producing a `TypeError`, the fix is almost always to correct the code that's calling the function wrong, not to wrap the call in a `try` block. We'll draw this line more precisely in [To Throw or Not to Throw](ch09-03-to-throw-or-not-to-throw.md); for now, treat `Error` as PHP telling you something is broken, and exceptions, covered next, as PHP telling you something needs a decision.
