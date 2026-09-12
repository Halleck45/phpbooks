# Recoverable Errors with Exceptions

<img src="images/ch09-icon.svg" alt="Recoverable Errors with Exceptions illustration" width="72">

Where the previous section was about bugs, this one is about situations your code should genuinely expect: a file that might not exist, an age that might be negative, an API that might reject the request you sent it. None of these mean your program is broken; they mean it needs to make a decision, and exceptions are PHP's mechanism for saying "here's a problem, and here's what I know about it" up the call stack to whoever is equipped to decide what happens next.

## `try`, `catch`, `finally`

The shape is the same as in most languages with exceptions:

```php
<?php

declare(strict_types=1);

function readConfig(string $path): array
{
    if (!file_exists($path)) {
        throw new \RuntimeException("Config file not found: {$path}");
    }

    return json_decode(file_get_contents($path), associative: true);
}

try {
    $config = readConfig('config.json');
    echo "Loaded " . count($config) . " settings.\n";
} catch (\RuntimeException $e) {
    echo "Couldn't load config: {$e->getMessage()}\n";
    $config = [];
} finally {
    echo "Config load attempt finished.\n";
}
```

`throw` raises an exception and immediately stops normal execution: nothing after the `throw` in `readConfig()` runs. Control jumps to the nearest enclosing `catch` block whose type matches, skipping everything in between, however many function calls deep that turns out to be. `finally` runs regardless of what happened (exception caught, exception not caught, or no exception at all), which makes it the right place for cleanup that has to happen no matter what: closing a file handle, releasing a lock.

## `Exception` versus `Error`, and `Throwable`

PHP's exception hierarchy has two parallel branches, both implementing the same interface, `Throwable`:

- `Exception` and its subclasses: for conditions a well-written program can reasonably anticipate and recover from. `InvalidArgumentException`, `RuntimeException`, `JsonException`.
- `Error` and its subclasses (covered in the previous section): for things that indicate a bug: `TypeError`, `DivisionByZeroError`.

`Throwable` is the interface both branches implement, and it's what lets `catch` blocks be precise: `catch (\Exception $e)` catches exceptions but lets an `Error` propagate past it; `catch (\Throwable $e)` catches either. Reach for `\Throwable` only at the very edges of an application (a top-level handler that logs anything unhandled before the process exits), never as a routine catch type in ordinary business logic. Catching it casually is how bugs quietly turn into "handled" cases that never get fixed.

## Catching several types at once

A single `catch` can list multiple types separated by `|`, when you genuinely want to handle more than one the same way:

```php
<?php

declare(strict_types=1);

try {
    $result = $client->send($request);
} catch (ConnectionException|TimeoutException $e) {
    echo "Network problem, retrying: {$e->getMessage()}\n";
    $result = retry($request);
}
```

If the handling logic actually differs between the two, use two separate `catch` blocks instead. Combining types is for when the response really is identical, not a shortcut to avoid writing a second block.

## Writing your own exception

Built-in exceptions like `RuntimeException` and `InvalidArgumentException` cover a lot of ground, but naming your own is one of the most common things you'll do in real PHP code: a specific exception type tells the caller precisely what went wrong, and lets them catch just that, instead of guessing from a string message:

```php
<?php

declare(strict_types=1);

class InvalidAgeException extends \Exception
{
    public function __construct(
        public readonly int $age,
    ) {
        parent::__construct("Invalid age: {$age}. Must be between 0 and 150.");
    }
}

function registerUser(string $name, int $age): void
{
    if ($age < 0 || $age > 150) {
        throw new InvalidAgeException($age);
    }

    echo "Registered {$name}, age {$age}.\n";
}

try {
    registerUser('Alice', -5);
} catch (InvalidAgeException $e) {
    echo "Registration failed: {$e->getMessage()}\n";
    echo "Offending value was: {$e->age}\n";
}
```

Extending `\Exception` gets you the whole standard machinery for free: `getMessage()`, `getCode()`, `getPrevious()`, a stack trace via `getTraceAsString()`. Calling `parent::__construct()` is what actually wires your custom message into that machinery; skip it and `getMessage()` comes back empty. Beyond that, the class is yours to shape: `InvalidAgeException` above stores the offending `$age` as a readonly property, so a `catch` block gets structured data to work with, not just a string to parse. This exact pattern (a small, specific exception class carrying the context that caused it) comes up again in [Chapter 14](ch14-00-a-cli-project.md), so it's worth being genuinely comfortable with it here.
