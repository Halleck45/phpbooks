# Writing to Standard Error

phpgrep has been printing everything the same way since the very first section: matches, usage messages, and error text all go through `echo`, all landing on the same output stream. That's been a quiet, low-grade problem the whole time, and this section is where it finally bites.

Every process has two separate output streams, not one: **standard output** (`STDOUT`), where a program's actual results belong, and **standard error** (`STDERR`), where diagnostics, warnings, and error messages belong. `echo` always writes to the first one. phpgrep's error messages have been going there too, right alongside legitimate matches, which is fine, as long as you only ever look at the terminal directly. It stops being fine the moment someone pipes phpgrep's output somewhere else, which is the entire reason command-line tools exist.

## Watch it go wrong

```console
$ php phpgrep.php apple missing.txt > results.txt
$ cat results.txt
Error: Cannot read file: missing.txt
```

That error message just landed *inside* `results.txt`. Whatever consumed that file next (another script, a report, a colleague trusting it contained only search results) now has to contend with a stray error line mixed into what should have been clean data, with nothing marking it as different from a real result. This is exactly the failure mode `STDOUT`/`STDERR` separation exists to prevent, and it's why every well-behaved command-line tool keeps the two apart.

## Fixing it with `fwrite(STDERR, ...)`

PHP exposes standard error as the constant `STDERR`, and `fwrite()` writes to it directly, bypassing `echo` entirely:

```php
<?php
// phpgrep.php
declare(strict_types=1);

require __DIR__ . '/src/GrepOptions.php';
require __DIR__ . '/src/FileNotFoundException.php';
require __DIR__ . '/src/search.php';

function main(array $argv): int
{
    if (count($argv) < 3) {
        fwrite(STDERR, "Usage: php phpgrep.php <query> <filename>\n");
        return 1;
    }

    $options = GrepOptions::fromArgv($argv);

    try {
        $matches = search($options);
    } catch (FileNotFoundException $e) {
        fwrite(STDERR, "Error: {$e->getMessage()}\n");
        return 1;
    }

    foreach ($matches as $line) {
        echo $line . "\n";
    }

    return 0;
}

exit(main($argv));
```

Only two lines changed: `echo` became `fwrite(STDERR, ...)` in both error paths, but the behavior at the boundary is completely different now:

```console
$ php phpgrep.php apple missing.txt > results.txt
Error: Cannot read file: missing.txt
$ cat results.txt
$
```

The error message still shows up on your terminal immediately: `STDERR` is not hidden, it's just a *different* stream, one that redirecting `STDOUT` with `>` doesn't touch. And `results.txt` is now empty, exactly as it should be: no matches were found because the search never ran, and no error text is masquerading as a result. Try it again against a file that actually has matches, and the split holds up the same way: real results go to `results.txt`, any error text stays on your terminal, and the two never mix regardless of what you redirect.

## Exit codes, one more time

`main()` still returns an `int` rather than calling `exit()` from inside itself, and the single `exit(main($argv))` at the bottom of the file is still the only place the process actually terminates. That discipline from a couple of sections ago is doing double duty now. It's what let `SearchTest` call `search()` directly without launching a process, and it's the same reason `main()`'s return value cleanly becomes the process's real exit code here: `1` on either failure path, `0` when it reaches the end having printed whatever it found, including printing nothing at all, which is a legitimate, successful outcome for a search tool, not a failure. A shell script or CI pipeline chaining phpgrep together with other commands can rely on that exit code exactly the way it relies on every other well-behaved Unix tool, without ever needing to parse phpgrep's output to figure out whether it worked.

That's phpgrep, for now: it accepts arguments properly, reads a file and searches it, fails loudly and specifically when it can't, is backed by tests that exercise its actual logic, respects an environment variable, and keeps its results and its errors on separate streams the way a command-line tool should. It's a small program, but there's very little about it left to apologize for.

One more improvement is coming. [Chapter 15](ch15-00-functional-features.md) introduces generators, and once it does, it comes back to this exact project for one last pass.
