# Processing a Series of Items with Generators

<img src="images/ch15-icon.svg" alt="Processing a Series of Items with Generators illustration" width="72">

Every function you've written so far that hands back a series of values has done it the same way: build an array, fill it up, `return` it. That's fine right up until the series is big enough that building the whole thing before anyone looks at a single item stops being fine. Generators are PHP's answer: a function that produces values one at a time, on demand, instead of all at once.

## The array way, and its limit

Here's an ordinary function that returns the first `$max` square numbers:

```php
<?php
declare(strict_types=1);

function squaresUpTo(int $max): array
{
    $result = [];
    for ($i = 1; $i <= $max; $i++) {
        $result[] = $i * $i;
    }
    return $result;
}

foreach (squaresUpTo(5) as $square) {
    echo $square . "\n";
}
```

For five squares, nobody cares that `squaresUpTo()` builds the entire array before the `foreach` sees a single value. For five million, that's five million integers sitting in memory before anything gets printed, and if all you actually needed was to look at the first three, you paid to build all five million anyway.

## The same function, rewritten with `yield`

Change `return` into a series of `yield` statements, and change the return type to `Generator`:

```php
<?php
declare(strict_types=1);

function squaresUpTo(int $max): Generator
{
    for ($i = 1; $i <= $max; $i++) {
        yield $i * $i;
    }
}

foreach (squaresUpTo(5) as $square) {
    echo $square . "\n";
}
```

The call site didn't change at all: `foreach` doesn't know or care whether it's iterating an array or a generator. What changed is *when* the work happens. A function whose body contains `yield` doesn't run that body when you call it. Calling `squaresUpTo(5)` returns a `Generator` object immediately, with nothing inside it computed yet. The loop only runs, one `$i` at a time, as `foreach` asks for the next value, and at any given moment, exactly one square exists, not all of them.

## Watching the laziness happen

It's worth seeing this directly, because "runs lazily" is easy to accept as a fact and much more convincing as something you watch happen:

```php
<?php
function countUp(): Generator
{
    echo "starting\n";
    for ($i = 1; $i <= 3; $i++) {
        echo "about to yield {$i}\n";
        yield $i;
        echo "resumed after {$i}\n";
    }
}

$gen = countUp();
echo "generator created, nothing has run yet\n";

foreach ($gen as $value) {
    echo "got {$value}\n";
}
```

```console
$ php lazy.php
generator created, nothing has run yet
starting
about to yield 1
got 1
resumed after 1
about to yield 2
got 2
resumed after 2
about to yield 3
got 3
resumed after 3
```

Look at the order. Calling `countUp()` produces nothing, not even the `"starting"` line, because the body hasn't run yet. Only when `foreach` starts pulling values does execution begin, and it stops the instant it hits `yield`, handing that value to the loop. `"resumed after 1"` doesn't print until `foreach` comes back for the *next* value, at which point `countUp()` picks up exactly where it left off, mid-loop, with all its local state (`$i` included) intact. That pause-and-resume is the whole mechanism. A generator function is really a function that can be suspended and continued, and `yield` is where the suspending happens.

## Associative generators

`yield` can produce key-value pairs too, using the same `key => value` syntax you'd use to build an associative array:

```php
<?php
function statusCodes(): Generator
{
    yield 200 => 'OK';
    yield 404 => 'Not Found';
    yield 500 => 'Internal Server Error';
}

foreach (statusCodes() as $code => $message) {
    echo "{$code}: {$message}\n";
}
```

Everything else works the same way: the pairs are still produced lazily, one at a time, as `foreach` asks for them. This is a small feature, but a genuinely convenient one whenever the natural shape of what you're generating already has an obvious key, the way an associative array often would.

Generators aren't a replacement for arrays; plenty of code genuinely needs a real array it can index into, count, or pass to `array_map()`. What they're for is exactly the case above: a series of values, produced by some logic, where nobody actually needs them all in memory at the same time. We'll put that to real use in the next section, on a file that's a good deal bigger than five squares.
