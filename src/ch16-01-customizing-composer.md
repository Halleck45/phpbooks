# Customizing Autoload and Scripts

The `composer.json` you've written so far has had two jobs: list dependencies, and map a namespace to a folder via PSR-4. It can do more than that with barely any extra effort, and two features are worth adding to your everyday habits right away: scripts, and a second flavor of autoloading for code that isn't a class.

## Scripts: shortcuts for commands you run constantly

Every PHP project accumulates a handful of commands you type over and over: running the test suite, running a linter, clearing a cache. Composer lets you name them, in the `"scripts"` section of `composer.json`:

```json
{
    "name": "you/phpgrep",
    "require": {},
    "require-dev": {
        "phpunit/phpunit": "^11.0"
    },
    "scripts": {
        "test": "phpunit",
        "check": "phpstan analyse src"
    }
}
```

Run either one with `composer run`, or, for a `"scripts"` entry with no colliding built-in Composer command, just `composer` followed by the name directly:

```console
$ composer test
$ composer check
```

This isn't just a shorter way to type `phpunit`. The real value shows up on a team: everyone runs `composer test`, regardless of whether the underlying tool is PHPUnit, Pest, or something else entirely, and regardless of what flags it needs. Change the command, and every developer, and every CI pipeline calling `composer test`, picks up the change automatically, with nothing to update on their end. A script entry can also be an array of commands, run in sequence, if a task genuinely needs more than one step:

```json
{
    "scripts": {
        "check": [
            "phpstan analyse src",
            "phpunit"
        ]
    }
}
```

## `"files"` autoloading: for code that isn't a class

PSR-4 autoloading, from [Chapter 7](ch07-06-psr4.md), maps a namespace to a directory and loads classes from it on demand: one class, one file, found by name. That works perfectly for classes. It has nothing to say about a file full of plain functions, because there's no class name for Composer to map to a file path. For that, `composer.json` has a second autoloading mechanism, `"files"`, which just lists files to load unconditionally, every time the autoloader runs:

```json
{
    "autoload": {
        "psr-4": {
            "PhpGrep\\": "src/"
        },
        "files": [
            "src/helpers.php"
        ]
    }
}
```

Anything defined at the top level of `src/helpers.php` (functions, constants) becomes available everywhere in your project the moment `vendor/autoload.php` is included, with no `use` statement needed to reach it, the same way a built-in function like `strtolower()` needs none. This is the right tool for a small set of standalone helper functions that don't belong to any particular class. It's also easy to overuse: a `"files"` entry loads its file's contents on *every single request*, unconditionally, unlike PSR-4 classes, which only load when something actually references them. Keep it for genuinely small, genuinely global helpers, and let PSR-4 handle everything that reasonably belongs on a class.

One last step, after editing either section by hand: run `composer dump-autoload` so Composer regenerates the autoloader files to match what you just wrote. `composer install` and `composer require` do this automatically; a manual edit to `composer.json` doesn't, until you tell it to.
