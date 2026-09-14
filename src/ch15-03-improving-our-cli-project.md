# Improving Our CLI Project

Point `phpgrep` at a two-gigabyte log file and watch. Nothing happens for a long while. Then every matching line pours out at once. The `search()` you wrote in [Chapter 14](ch14-00-a-cli-project.md) is the reason:

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

Two things are happening at once. `file_get_contents()` reads the *entire* file into one string before `search()` does anything else, and `$matches` keeps growing for as long as the loop runs. With half a million matching lines, `search()` hands back nothing until it has built an array holding all of them. **The whole file and every match are sitting in memory at the same time**, and the user sees nothing until the last line has been checked.

## Rewriting `search()` as a generator

Now that you know `yield`, the first fix is direct: stop collecting into `$matches`, and `yield` each match the moment you find it. A second change goes with it. `file_get_contents()` would still load the whole file up front, so swap it for `fopen()` and `fgets()`, which read one line at a time. Otherwise the generator would be lazy about a file that was already entirely in memory, which defeats half the point:

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

<img src="images/ch15-grep-stream.png" alt="Before: the whole file is lifted into memory and matches pile up while the screen stays blank. After: lines flow one at a time through the function to the screen, and memory holds a single line" width="600">

The file is now read a line at a time, and each match leaves through `yield` as soon as it is found, before the next line is even read. **At any moment, the function holds one line and nothing else.** The error check moved as well: with no `file_get_contents()` left to fail, it is `fopen()` that reports a missing file, with the same `RuntimeException` you met in [Chapter 9](ch09-02-exceptions.md).

That exception hides a subtlety, and it deserves a straight explanation. Because the body of `searchLines()` contains `yield`, calling `searchLines($options)` runs none of it, `fopen()` included. **The exception does not fire when you call the function. It fires when someone starts iterating.** That changes where you have to catch it.

## Updating `phpgrep.php`

The main script barely changes: it still loops over what the search gives it and prints each line. But the `try`/`catch` must now wrap the loop, not just the call:

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

Try it the wrong way: keep the `try` around the call alone, put the `foreach` after the `catch`, and run `phpgrep` on a file that does not exist. The `try` block finishes without a complaint, since nothing has opened the file yet, and the exception bursts out of the `foreach` a few lines later, uncaught, with a stack trace instead of your tidy error message.

> With a generator, the error happens where the values are pulled, not where the function is called. Catch it there.

## Why this is worth doing

Point `phpgrep` at that two-gigabyte log again. With the array-returning `search()`, you wait for the entire file to be scanned, and then half a million lines print in one burst, after the program has held every one of them in memory. With `searchLines()`, **the first match appears almost immediately**, before the rest of the file has been read, because `foreach` only needed one value to start printing. And memory stays flat for the whole run, whatever the file size and the number of matches, because the program holds exactly one line at a time. Never "all matches so far", never the whole file.

That is the trade a generator offers: earlier results, and a memory ceiling that does not move no matter how big the input gets.
