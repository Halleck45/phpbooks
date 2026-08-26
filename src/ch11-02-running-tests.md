# Controlling How Tests Are Run

`vendor/bin/phpunit tests` runs everything, every time, which is fine for a handful of tests and increasingly annoying once you have hundreds. This section covers narrowing that down, plus the config file that makes the whole thing repeatable.

## Filtering by name

`--filter` runs only tests whose method name matches a pattern:

```console
$ vendor/bin/phpunit --filter testAreaOfARectangle tests
```

It matches against the method name as a regular expression, so `--filter Area` would catch `testAreaOfARectangle` along with anything else containing "Area": useful while you're heads-down on one feature and don't want the whole suite's noise on every run.

## Grouping tests

For a coarser cut than one test at a time, tag tests with a group, using either the older docblock annotation or the modern attribute:

```php
<?php

use PHPUnit\Framework\Attributes\Group;
use PHPUnit\Framework\TestCase;

final class RectangleTest extends TestCase
{
    #[Group('geometry')]
    public function testAreaOfARectangle(): void
    {
        $rectangle = new Rectangle(8.0, 7.0);

        $this->assertSame(56.0, $rectangle->area());
    }
}
```

Then run just that group:

```console
$ vendor/bin/phpunit --group geometry tests
```

A common real-world use: mark slow tests (ones that hit a database, or the filesystem, or the network) with `#[Group('slow')]`, and exclude them from your everyday inner loop with `--exclude-group slow`, saving the full run for CI where a few extra seconds don't cost you anything.

## `phpunit.xml`

Typing `tests` and remembering your preferred flags on every single invocation gets old fast. A `phpunit.xml` file at your project root fixes that: PHPUnit reads it automatically, no flag needed:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit bootstrap="vendor/autoload.php"
         colors="true">
    <testsuites>
        <testsuite name="default">
            <directory>tests</directory>
        </testsuite>
    </testsuites>
</phpunit>
```

`bootstrap` tells PHPUnit which file to load before anything else: almost always Composer's autoloader, so your test files can reference `Rectangle` without a manual `require`. `testsuites` defines what "the test suite" even means: here, everything under `tests/`. With this file in place, the invocation shrinks back down to the bare command:

```console
$ vendor/bin/phpunit
```

You can still layer `--filter` or `--group` on top of it whenever you need a narrower run. Generate a starting version of this file with `vendor/bin/phpunit --generate-configuration` if you'd rather answer a few prompts than hand-write the XML: either way, commit the resulting file. It's project configuration, not a personal preference, and everyone on the team (plus your CI pipeline) should be running the same suite the same way.
