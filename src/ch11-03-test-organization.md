# Test Organization

Where tests live matters less for correctness than it does for whether anyone (including future you) can find them. PHP's convention here is simple enough to state in one sentence: a `tests/` directory that mirrors the shape of `src/`, with one test class per class, named after the thing it tests plus `Test`.

```text
src/
    Rectangle.php
    GrepOptions.php
tests/
    RectangleTest.php
    GrepOptionsTest.php
```

`src/Rectangle.php` gets `tests/RectangleTest.php`. `src/Http/Client.php` would get `tests/Http/ClientTest.php`, keeping the directory structure lined up on both sides. This isn't enforced by PHPUnit (you could name things however you like and point `phpunit.xml` at whatever directory you chose), but it's the convention nearly every PHP project follows, and deviating from it without a good reason just makes your codebase slightly harder for the next person to navigate. Composer's PSR-4 autoloading, from [Chapter 7](ch07-00-namespaces-and-composer.md), usually maps a `Tests\` namespace onto this `tests/` directory the same way it maps your application namespace onto `src/`.

## Unit tests vs. integration tests

A **unit test** exercises one class or function, in isolation, with nothing outside it involved: no database, no filesystem, no network. `RectangleTest` is a unit test: it constructs a `Rectangle` directly and checks its own methods, nothing more. Unit tests are fast (thousands of them can run in a few seconds), which is exactly what lets you run the whole suite constantly without it slowing you down.

An **integration test** checks that several pieces work correctly *together*: your code talking to a real database, a real file on disk, a real HTTP call to another service. They catch a category of bug unit tests structurally cannot: the assumptions two pieces make about each other turning out to be wrong, even though each piece is individually correct. They're also slower, often by orders of magnitude, and more prone to flaking for reasons that have nothing to do with your code: a slow disk, a network blip.

```php
<?php

use PHPUnit\Framework\TestCase;

final class FindMatchingLinesIntegrationTest extends TestCase
{
    public function testFindsLinesInARealFile(): void
    {
        $path = tempnam(sys_get_temp_dir(), 'lines');
        file_put_contents($path, "apple\nbanana\ncherry\n");

        $lines = findMatchingLines($path, 'banana');

        $this->assertSame(['banana'], $lines);

        unlink($path);
    }
}
```

Nothing here is exotic (it's still a PHPUnit `TestCase`, still full of assertions), but notice it touches the real filesystem, creating and cleaning up an actual temporary file, rather than faking one. That's the distinguishing feature, not the syntax.

## A practical split

Most projects keep both kinds of test in the same `tests/` tree but separate them by directory or by PHPUnit group (`tests/Unit/` and `tests/Integration/`, or the `#[Group('integration')]` attribute from the previous section), so you can run the fast unit suite constantly while you work, and save the slower integration suite for before a commit or for CI. Neither kind replaces the other: unit tests tell you a piece works on its own; integration tests tell you the pieces still work once they're talking to each other, which is, after all, the only way your program actually runs.
