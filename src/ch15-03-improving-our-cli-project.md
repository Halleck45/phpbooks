# Improving Our CLI Project

Chapter 14 left `phpgrep` in working order, with `search()` doing the real work:

```php
<?php
declare(strict_types=1);

function search(GrepOptions $options): array
{
    $contents = file_get_contents($options->filename);

    if ($contents === false) {
        throw new RuntimeException("Could not read file: {$options->filename}");
    }

    $matches = [];

    foreach (explode("\n", $contents) as $line) {
        $haystack = $options->ignoreCase ? strtolower($line) : $line;
        $needle = $options->ignoreCase ? strtolower($options->query) : $options->query;

        if (str_contains($haystack, $needle)) {
            $matches[] = $line;
        }
    }

    return $matches;
}
```

It works, and for the log files you tested it against, it's fast enough that you never noticed anything wrong. Try it against a two-gigabyte log file, though, and you'll notice two things at once: `file_get_contents()` reads the *entire* file into a single string before `search()` does anything else, and `$matches` keeps growing for as long as the loop runs. If that file has half a million matching lines, `search()` doesn't hand back a single one of them until it has built an array holding all half million, and every line of the file, plus every matched line, is sitting in memory at the same time along the way.

## Rewriting `search()` as a generator

Now that you know `yield`, the fix is direct: stop building `$matches`, and `yield` each match as you find it. But there's a second change worth making at the same time: swap `file_get_contents()` (which reads the whole file up front) for `fopen()` and `fgets()`, which read it one line at a time. Otherwise you'd still be loading the entire file into memory before the generator even started producing anything, which defeats half the point:

```php
<?php
declare(strict_types=1);

function searchLines(GrepOptions $options): Generator
{
    $handle = fopen($options->filename, 'r');

    if ($handle === false) {
        throw new RuntimeException("Could not read file: {$options->filename}");
    }

    $needle = $options->ignoreCase ? strtolower($options->query) : $options->query;

    while (($line = fgets($handle)) !== false) {
        $haystack = $options->ignoreCase ? strtolower($line) : $line;

        if (str_contains($haystack, $needle)) {
            yield $line;
        }
    }

    fclose($handle);
}
```

Two things changed shape, not just syntax. The file itself is now read a line at a time via `fgets()`, instead of all at once via `file_get_contents()`. And instead of appending to an array and returning it once the whole file has been scanned, `searchLines()` yields each match the moment it's found, then goes right back to reading. Notice the exception check moved too: `fopen()` failing is now the thing that throws, since there's no `file_get_contents()` call left to fail. The `RuntimeException` (the same class you saw introduced back in [Chapter 9](ch09-02-exceptions.md)) still gets thrown before any `yield` happens, so a caller who never starts iterating never even attempts to open a file that doesn't exist... except that's not quite true, and it's worth being honest about why: because `searchLines()`'s body contains `yield`, calling it doesn't run any of this code yet, `fopen()` included. The exception won't actually fire until the caller starts iterating. We'll deal with that directly in the main script.

## Updating `phpgrep.php`

The main script's job barely changes: it still loops over whatever `search` gives it and prints each line, but the `try`/`catch` now has to wrap the loop itself, not just the call:

```php
<?php
declare(strict_types=1);

require __DIR__ . '/vendor/autoload.php';

$options = GrepOptions::fromArgv($argv);

try {
    foreach (searchLines($options) as $line) {
        echo $line;
    }
} catch (RuntimeException $e) {
    fwrite(STDERR, "Error: {$e->getMessage()}\n");
    exit(1);
}
```

That last point matters in practice, not just in theory: calling `searchLines($options)` on its own line, outside the `try`, would silently swallow the "file not found" case, because nothing would have actually tried to open the file yet. Wrapping the `foreach` instead of the call makes sure the exception, deferred as it is, still gets caught where you expect it.

## Why this is worth doing

Point `phpgrep` at that same two-gigabyte log file again. With the array-returning `search()`, you wait, however long it takes to scan the entire file, and then, all at once, half a million lines print in a burst, after the program has held every one of them in memory simultaneously. With `searchLines()`, the very first match appears on screen almost immediately, before the rest of the file has even been read, because `foreach` only needed the *first* yielded value to start printing. And the program's memory footprint stays flat throughout the whole run, regardless of file size or match count, because at any given moment it's holding exactly one line: never "all matches so far," never the whole file. That's the entire trade generators offer: earlier results, and a memory ceiling that doesn't move no matter how big the input gets.
