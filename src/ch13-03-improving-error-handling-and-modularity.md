# Refactoring to Improve Modularity and Error Handling

Everything phpgrep does still lives in one script, top to bottom: parse arguments, check the file, read it, loop over it, print matches. That's fine for thirty lines. It stops being fine the moment you want to test any single piece of it without running the whole program, which is exactly where this project is headed in a couple of sections. Let's split it up properly, and replace that clumsy `file_exists()` check with something PHP actually designed for this: an exception.

## A named exception

[Chapter 9](ch09-00-error-handling.md) made the case for throwing a specific, well-named exception instead of returning a sentinel value or printing an error and hoping the caller checks. PHP's built-in `RuntimeException` is the right base class for "something went wrong at runtime that the caller should have a chance to handle": extend it with a name that says exactly what happened:

```php
<?php
// src/FileNotFoundException.php
declare(strict_types=1);

final class FileNotFoundException extends RuntimeException
{
}
```

That's the entire class. It adds no new behavior; it doesn't need to. Its whole value is its name: catching `FileNotFoundException` specifically, rather than a generic `RuntimeException` or, worse, `Exception`, tells the reader of the `catch` block precisely what failure they're handling, without them needing to go read the code that threw it.

## Extracting `search()`

Now pull the reading-and-matching logic out of the top-level script and into a function with a real name and a real contract: it takes a `GrepOptions`, returns an array of matching lines, and throws if the file can't be read:

```php
<?php
// src/search.php
declare(strict_types=1);

require_once __DIR__ . '/FileNotFoundException.php';

function search(GrepOptions $options): array
{
    if (!is_readable($options->filename)) {
        throw new FileNotFoundException("Cannot read file: {$options->filename}");
    }

    $lines = file($options->filename, FILE_IGNORE_NEW_LINES);

    $matches = [];
    foreach ($lines as $line) {
        if (str_contains($line, $options->query)) {
            $matches[] = $line;
        }
    }

    return $matches;
}
```

`is_readable()` is a genuine improvement over `file_exists()`: it checks the file exists *and* that the current process has permission to read it, which is the actual precondition `file()` needs. Fail either check, and `search()` throws immediately, with a message that says exactly which file was the problem. No warning printed to a stream nobody's watching, no silent empty result, just a clear, catchable failure.

`GrepOptions` moves into its own file too, unchanged from the last section:

```php
<?php
// src/GrepOptions.php
declare(strict_types=1);

final class GrepOptions
{
    public function __construct(
        public readonly string $query,
        public readonly string $filename,
    ) {
    }

    public static function fromArgv(array $argv): self
    {
        return new self(
            query: $argv[1],
            filename: $argv[2],
        );
    }
}
```

## The entry script, now just wiring

With `GrepOptions` and `search()` living in `src/`, `phpgrep.php` shrinks down to what it should have been all along: the part that talks to the outside world, and nothing else.

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
        echo "Usage: php phpgrep.php <query> <filename>\n";
        return 1;
    }

    $options = GrepOptions::fromArgv($argv);

    try {
        $matches = search($options);
    } catch (FileNotFoundException $e) {
        echo "Error: {$e->getMessage()}\n";
        return 1;
    }

    foreach ($matches as $line) {
        echo $line . "\n";
    }

    return 0;
}

exit(main($argv));
```

Notice `main()` *returns* an exit code rather than calling `exit()` itself in the middle of the function: `exit()` only happens once, at the very last line of the file, wrapping whatever `main()` decided. That's a small discipline with a real payoff: a function that returns a value instead of unilaterally killing the process is a function you can call from anywhere, including, and this is the point, from a test, where you'd very much like `main()`'s mistakes to come back as a return value you can assert on, not as your test runner's process disappearing mid-suite.

```console
$ php phpgrep.php apple fruits.txt
apple sauce for the win

$ php phpgrep.php apple missing.txt
Error: Cannot read file: missing.txt
```

Same behavior from the outside as before: that's deliberate. Nothing about *what* phpgrep does changed in this section, only how it's built. That distinction is worth sitting with: a refactor that changes behavior isn't a refactor, it's a rewrite wearing a refactor's name. What did change is that `search()` and `GrepOptions` now live in files that never call `exit()`, never call `echo`, and never touch `$argv` directly, which means, as of this section, they're finally things a test can call directly and check, without launching the whole program to do it. That's exactly what the next section does.
