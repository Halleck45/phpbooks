# Accepting Command Line Arguments

Create a new directory for the project and, inside it, a file called `phpgrep.php`. Every PHP script run from the command line has access to a superglobal array called `$argv`, holding everything typed after `php` on the command line:

```php
<?php
declare(strict_types=1);

var_dump($argv);
```

```console
$ php phpgrep.php apple fruits.txt
array(3) {
  [0]=>
  string(11) "phpgrep.php"
  [1]=>
  string(5) "apple"
  [2]=>
  string(9) "fruits.txt"
}
```

The first surprise, if you haven't met `$argv` before: `$argv[0]` is not your first argument, it's the name of the script itself. This trips up nearly everyone once. Your actual arguments start at index `1`. Here, `$argv[1]` is the word we're searching for, and `$argv[2]` is the file to search in: that's the whole interface phpgrep needs to expose.

## Reading two arguments, badly

The most direct way to grab them:

```php
<?php
declare(strict_types=1);

$query = $argv[1];
$filename = $argv[2];

echo "Searching for \"{$query}\" in \"{$filename}\"\n";
```

Run it right, and it works fine. Run it with too few arguments:

```console
$ php phpgrep.php apple
```

PHP raises a warning for the missing `$argv[2]`, then quietly treats it as `null`, and the program limps on with garbage input instead of stopping to tell you what went wrong. That's not acceptable for a tool anyone but you will ever run. Let's guard it:

```php
<?php
declare(strict_types=1);

if (count($argv) < 3) {
    echo "Usage: php phpgrep.php <query> <filename>\n";
    exit(1);
}

$query = $argv[1];
$filename = $argv[2];

echo "Searching for \"{$query}\" in \"{$filename}\"\n";
```

`exit(1)` stops the script immediately and sets the process's exit code to `1`: by Unix convention, `0` means "the program succeeded," and anything nonzero means "something went wrong." Every command-line tool you've ever chained together with `&&` or checked with `$?` in a shell relies on this convention; phpgrep should honor it too, from the very first version.

## Giving the arguments a home: `GrepOptions`

Two loose variables, `$query` and `$filename`, are fine for now, but this project is going to grow, and passing a pair of separate strings around every function we write gets unwieldy fast. Let's bundle them into a small, dedicated value object instead: a class whose entire job is holding "the options this run of the program was given," nothing more:

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

echo "Searching for \"{$options->query}\" in \"{$options->filename}\"\n";
```

Two readonly properties, set once through constructor promotion, exactly as you saw back in [Chapter 5](ch05-00-classes.md): a `GrepOptions` can't be modified after it's built, which is precisely right for something meant to represent "what the user asked for" for the lifetime of one run. `fromArgv()` is a static factory method: it takes the raw `$argv` array and hands back a fully-formed `GrepOptions`, keeping the "how do we parse arguments" question in exactly one place. Every future section in this chapter builds on this same class: you'll see it grow a third property soon enough, but its shape and its job stay the same.

Run it once more to confirm nothing changed from the reader's point of view:

```console
$ php phpgrep.php apple fruits.txt
Searching for "apple" in "fruits.txt"
```

Same behavior, better bones. That's the whole point of introducing the class this early: it costs almost nothing now, and it's exactly the seam the rest of this chapter needs.
