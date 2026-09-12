# Working with Environment Variables

<img src="images/ch14-icon.svg" alt="Working with Environment Variables illustration" width="72">

`GrepOptions` can carry an `ignoreCase` flag, and `search()` honors it, but `fromArgv()` still hardcodes it to `false`. There's no way for anyone running phpgrep from a terminal to actually turn it on. Let's fix that using an environment variable rather than a third command-line argument.

Why an environment variable and not just `$argv[3]`? Because case-insensitivity here is closer to a standing preference than a per-search decision: something you might want on for every search you run in a given shell session, without retyping a flag every time. Environment variables are exactly the tool for that: set once, inherited by every command you run afterward, until you close the terminal or unset it.

## Reading it with `getenv()`

```php
<?php
// src/GrepOptions.php
declare(strict_types=1);

final class GrepOptions
{
    public function __construct(
        public readonly string $query,
        public readonly string $filename,
        public readonly bool $ignoreCase,
    ) {
    }

    public static function fromArgv(array $argv): self
    {
        return new self(
            query: $argv[1],
            filename: $argv[2],
            ignoreCase: getenv('PHPGREP_IGNORE_CASE') !== false,
        );
    }
}
```

`getenv('PHPGREP_IGNORE_CASE')` returns the variable's value as a string if it's set, or the boolean `false` if it isn't set at all: that's why the check is `!== false` rather than something that tries to interpret the value as a boolean itself. It means `PHPGREP_IGNORE_CASE=1` turns the flag on, but so would `PHPGREP_IGNORE_CASE=` with nothing after the `=`: an empty string is still a value, and simply *setting the variable at all* is treated as "on." If that looseness bothers you, you're right to notice it, and tightening it (say, requiring the value to be exactly `"1"`) is a reasonable improvement to make on your own once the chapter's done.

## Trying it

```console
$ php phpgrep.php APPLE fruits.txt
```

No output at all: the query `APPLE` doesn't appear, case-sensitively, in either the `Apple` or `apple` line, so nothing matches and phpgrep prints nothing. Now flip the flag on:

```console
$ PHPGREP_IGNORE_CASE=1 php phpgrep.php APPLE fruits.txt
Apple pie recipe
apple sauce for the win
```

Setting `PHPGREP_IGNORE_CASE=1` immediately before the command, on the same line, sets it for that single invocation only: a common and useful shell idiom when you don't want a setting to outlive the command it's attached to. Export it instead, and it sticks around for the rest of the session:

```console
$ export PHPGREP_IGNORE_CASE=1
$ php phpgrep.php APPLE fruits.txt
Apple pie recipe
apple sauce for the win
```

## `getenv()` versus `$_ENV`

PHP also exposes environment variables through the `$_ENV` superglobal, and it's worth knowing why this chapter didn't reach for it. `$_ENV` is only populated according to the `variables_order` setting in `php.ini`: on plenty of default PHP installations, particularly ones tuned for web serving rather than CLI use, `E` is missing from that setting entirely, and `$_ENV` ends up empty regardless of what's actually in the process environment. `getenv()` has no such dependency: it asks the operating system directly, every time, and works consistently across CLI scripts, web requests, and every hosting configuration you're likely to encounter. For a command-line tool meant to run reliably wherever it's installed, that consistency is worth the slightly less fashionable syntax.
