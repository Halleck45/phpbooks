# Step Debugging with Xdebug

<img src="images/ch13-icon.svg" alt="Step Debugging with Xdebug illustration" width="72">

Xdebug is a PHP extension, not a separate program: once it's installed, it changes how PHP itself behaves, rather than being something you call from your code the way you call `var_dump()`. That's a bit more setup than the previous section needed, but it buys you something print debugging can't: the ability to pause a running script at an exact line and look at everything in scope, without having guessed in advance what to print.

## Installing it

Xdebug isn't bundled with PHP, so it needs installing separately, and the exact command depends on your platform:

```console
$ pecl install xdebug
```

Most package managers offer it too (`apt install php-xdebug` on Debian and Ubuntu, `brew install php` followed by `pecl install xdebug` on macOS with Homebrew's PHP). Whichever route you take, it needs to be enabled in `php.ini` afterward with a line resembling:

```ini
zend_extension=xdebug
```

Confirm it loaded:

```console
$ php -v
PHP 8.3.0 (cli) (built: ...)
    with Xdebug v3.3.0, Copyright (c) 2002-2024, by Derick Rethans
```

If Xdebug's name shows up in that output, it's active.

## `xdebug.mode`: turning on what you need

Xdebug does several unrelated things, and a single setting, `xdebug.mode`, controls which of them are switched on, as a comma-separated list in `php.ini`:

```ini
xdebug.mode=develop,debug
```

`develop` is worth having on by default: it doesn't require any tooling at all, and it quietly improves output you're already producing. With it enabled, `var_dump()` prints with color and includes the file and line it was called from, and an uncaught exception's output grows a full stack trace, arguments included, instead of PHP's terser default. `debug` is the mode that enables the part this section is really about: pausing execution for an external tool to inspect.

## Connecting an editor

Step debugging needs two ends talking to each other: PHP, running your script, and an editor or IDE, listening for it to say "I've paused, come look." Both PhpStorm and VS Code (with the "PHP Debug" extension) support this out of the box, over a protocol called DBGp, on port 9003 by default. Set up in either is roughly the same shape:

1. Start "listening for Xdebug connections" in the editor.
2. Click in the gutter next to a line of code to set a breakpoint: a red dot marking "pause here."
3. Run the script (`php your_script.php` from the terminal, or reload a page served by `php -S`, with `xdebug.mode` including `debug`).
4. Execution stops the moment it reaches that line, before running it, and the editor shows every variable in scope at that exact point.

From there you step **over** a line (run it, stop again at the next one), step **into** a function call (follow execution inside it instead of running it as a block), or step **out** of the current function back to its caller, watching variables change as you go.

## Trying it on the guestbook

The validation code from [Chapter 10](ch10-02-validation-and-xss.md) is a good place to practice on, since it's small enough to hold in your head but has a real branch worth watching:

```php
if ($name === '') {
    $errors[] = 'Name cannot be empty.';
} elseif (mb_strlen($name) > 60) {
    $errors[] = 'Name is too long.';
}
```

Set a breakpoint on the `if ($name === '')` line, start the built-in server with `xdebug.mode=debug` set, start listening in your editor, and submit the guestbook form with the name field left blank. Execution pauses right there, and the variables pane shows `$name` as an empty string, `$errors` as an empty array, exactly as they stood at that instant, before a single line of the `if` block has run. Step over it, and watch `$errors` gain its first entry in real time. That's the entire value of step debugging in one small example: no `var_dump()` call had to be written, moved, or removed to see it.

## Profiling, briefly

`xdebug.mode=profile` turns on a third capability: instead of pausing execution, it records how long each function call took, writing the result to a "cachegrind" file (`xdebug.output_dir` controls where). Tools like QCachegrind or the profiler built into PhpStorm read that file and show you, visually, exactly where a slow request spent its time: which function, called how many times, accounting for what fraction of the total. It's a different job from debugging a wrong answer, closer to what [Chapter 15](ch15-04-performance.md) discusses for loops versus generators, but it's the same extension and worth knowing it's there.

## Choosing between the two tools

Reach for `var_dump()` and `print_r()` first, honestly: they need no setup, and for most of the bugs you'll hit, especially early on, "print the value and look at it" finds the problem in seconds. Reach for Xdebug once printing stops narrowing things down, once a bug depends on a sequence of calls rather than a single value, or once you find yourself adding and removing `var_dump()` calls three or four times chasing the same problem. That's the point where pausing the program and just looking around costs less time than guessing again.
