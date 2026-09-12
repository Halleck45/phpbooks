# Performance: Loops vs. Generators vs. Array Functions

<img src="images/ch15-icon.svg" alt="Performance: Loops vs. Generators vs. Array Functions illustration" width="72">

You now have three ways to process a series of values in PHP: a plain `for` or `foreach` loop, a generator, or one of the built-in array functions like `array_map()` and `array_filter()`. They can often solve the same problem. They don't cost the same, and "cost" here means two different things (time and memory) that don't always move together. Let's actually measure it instead of guessing.

## A small benchmark

Here's the same task (square two million integers and sum the results) done three ways:

```php
<?php
declare(strict_types=1);

const N = 2_000_000;

// 1. plain loop
$sum = 0;
for ($i = 1; $i <= N; $i++) {
    $sum += $i * $i;
}

// 2. array functions
$numbers = range(1, N);
$squares = array_map(fn(int $n): int => $n * $n, $numbers);
$sum = array_sum($squares);

// 3. generator
function squares(int $max): Generator {
    for ($i = 1; $i <= $max; $i++) {
        yield $i * $i;
    }
}
$sum = 0;
foreach (squares(N) as $square) {
    $sum += $square;
}
```

Run each version in its own process (so one doesn't inflate another's peak-memory reading) and measure with `hrtime()` and `memory_get_peak_usage()`. On the machine this book was written on:

```console
loop              ~100 ms   peak memory:   2 MB
array functions   ~140 ms   peak memory:  66 MB
generator         ~170 ms   peak memory:   2 MB
```

Take the exact numbers with a grain of salt: they'll shift with your PHP version, your hardware, and what else is running. The *shape* of the result is the part worth trusting: the plain loop is fastest and leanest, full stop. The array-function version is the slowest and by far the hungriest, because `range()` builds a two-million-element array, then `array_map()` builds a *second* two-million-element array to hold the squares, and both exist in memory at once before `array_sum()` even starts. The generator lands in between on time (there's real overhead to suspending and resuming a function two million times) but matches the loop's flat, minimal memory use, because it never materializes anything bigger than one value.

## Reading that honestly

None of this means "always use loops." It means the three tools are optimized for different things, and picking one is about which of those things you actually need:

**A `for`/`foreach` loop** is the fastest and most explicit option, and often the clearest to read besides: there's no framework to understand, just a variable changing on every pass. Reach for it when performance matters, when the logic is more than a one-line transformation, or honestly, whenever you're not sure; it's rarely the wrong default.

**A generator** trades a bit of raw speed for a flat memory ceiling on data that's large, streaming, or expensive to produce all at once: a huge file, an API you're paging through, an infinite sequence. You saw this pay off directly in the previous section: `phpgrep` printing its first match before finishing the file, instead of waiting to build one giant array of results. If the whole series would comfortably fit in memory anyway, a generator's suspend-and-resume overhead is buying you nothing.

**`array_map()` and `array_filter()`** are often the most *readable* option for small-to-medium in-memory transformations: a one-line `array_map(fn($x) => ..., $items)` reads better than the equivalent five-line loop, and that's a genuine win worth having. What they are not is a memory optimization: each one builds a brand-new array to hold its result, on top of whatever you passed in. For a hundred items, that's irrelevant. For millions, it's the difference you just watched in the benchmark above.

## A decision rule, not a table

If the data is small enough that you'd never think twice about holding it all in memory, reach for whichever reads best at the call site: usually an array function for a simple transformation, a loop for anything with real logic in it. If the data is large, unbounded, or expensive to produce (a big file, a database cursor, anything you're paging through), reach for a generator, and accept the modest overhead in exchange for memory usage that doesn't grow with the input. And if you're chasing raw speed on a hot path and you've actually measured that it matters, the plain loop is still, quietly, the fastest thing PHP gives you. Don't guess which of these applies: the benchmark above took about a dozen lines of code to write. Measure your own case if it matters enough to ask the question at all.
