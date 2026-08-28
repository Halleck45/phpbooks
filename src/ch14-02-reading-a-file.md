# Reading a File

phpgrep can parse its arguments now, but it doesn't actually search anything yet. Time to fix that. Create a small file to search in, right next to `phpgrep.php`:

```console
$ cat fruits.txt
Apple pie recipe
apple sauce for the win
Banana bread is better
cherry clafoutis
```

## Reading the whole file into lines

PHP's `file()` function reads a file straight into an array, one element per line: exactly the shape we want:

```php
<?php

$lines = file($options->filename, FILE_IGNORE_NEW_LINES);
```

The `FILE_IGNORE_NEW_LINES` flag strips the trailing `\n` from each line as it reads, which saves you a `trim()` call on every single one afterward. You could reach for `file_get_contents()` followed by `explode("\n", ...)` instead (same result, two steps instead of one), and you'll see that combination plenty in real code, particularly when you need the raw file contents for something else too. For a line-by-line tool like this one, `file()` is the more direct match.

## Searching each line

With the lines in hand, `str_contains()` (introduced in PHP 8, and a welcome relief after years of everyone hand-rolling `strpos($haystack, $needle) !== false`) does the actual matching:

```php
<?php
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

if (count($argv) < 3) {
    echo "Usage: php phpgrep.php <query> <filename>\n";
    exit(1);
}

$options = GrepOptions::fromArgv($argv);

$lines = file($options->filename, FILE_IGNORE_NEW_LINES);

foreach ($lines as $line) {
    if (str_contains($line, $options->query)) {
        echo $line . "\n";
    }
}
```

```console
$ php phpgrep.php apple fruits.txt
apple sauce for the win
```

Only the lowercase `apple` line matched: `str_contains()` is case-sensitive, and `"Apple pie recipe"` doesn't contain the literal substring `"apple"`. Keep that fixture and that behavior in mind; it becomes the exact test case for case-insensitive matching a couple of sections from now.

## The file that isn't there

Try pointing phpgrep at a file that doesn't exist:

```console
$ php phpgrep.php apple missing.txt

Warning: file(missing.txt): Failed to open stream: No such file or directory in phpgrep.php on line 20
```

A warning, printed to the terminal, and then... nothing. `file()` returns `false` when it can't open the target, and our `foreach` silently iterates over `false` as if it were an empty array, producing no matches and no explanation. That's a genuinely bad failure mode: the tool looks like it ran successfully and simply found nothing, when what actually happened is it never read anything at all.

Let's patch that with the bluntest tool available: check first, and bail out if the file isn't there:

```php
<?php

if (!file_exists($options->filename)) {
    echo "Error: file \"{$options->filename}\" not found.\n";
    exit(1);
}

$lines = file($options->filename, FILE_IGNORE_NEW_LINES);
```

```console
$ php phpgrep.php apple missing.txt
Error: file "missing.txt" not found.
```

Better: at least it's honest now. But look at what this check actually buys you, and what it doesn't. `file_exists()` only answers "is there something at this path." It says nothing about whether *you* can read it: a file that exists but has permissions locked down still passes this check and then fails at `file()` exactly as before, warning and all. And every place in this program that might eventually open a file would need this same manual check copy-pasted in front of it, with every copy a chance to forget one. That's a clumsy, incomplete guard standing in for something PHP has a proper mechanism for. Time to reach for it.
