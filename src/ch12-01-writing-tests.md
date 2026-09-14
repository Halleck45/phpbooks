# How to Write Tests with PHPUnit

Start a small project the way you did in [Chapter 7](ch07-01-hello-composer.md):

```console
$ composer init --no-interaction
$ composer require --dev phpunit/phpunit
```

That `--dev` matters: PHPUnit is a tool you use while building the project, not something the project needs to run in production. Composer keeps development-only dependencies separate for exactly this reason: they never ship.

## The code under test

Here's a small class worth testing, the kind of thing you've been writing since [Chapter 5](ch05-00-classes.md):

```php
<?php
// src/Rectangle.php

declare(strict_types=1);

final class Rectangle
{
    public function __construct(
        private readonly float $width,
        private readonly float $height,
    ) {
    }

    public function area(): float
    {
        return $this->width * $this->height;
    }

    public function isSquare(): bool
    {
        return $this->width === $this->height;
    }
}
```

Nothing new here: a readonly class with two properties and two methods. The question a test answers is simple: does it actually do what it claims to?

## Your first test

A test is a class extending PHPUnit's `TestCase`, with methods whose names start with `test`:

```php
<?php
// tests/RectangleTest.php

declare(strict_types=1);

use PHPUnit\Framework\TestCase;

final class RectangleTest extends TestCase
{
    public function testAreaOfARectangle(): void
    {
        $rectangle = new Rectangle(8.0, 7.0);

        $this->assertEquals(56.0, $rectangle->area());
    }
}
```

`assertEquals(expected, actual)` is the workhorse assertion: it fails the test, with a readable diff, if the two values aren't equal. Run the suite:

```console
$ vendor/bin/phpunit tests
PHPUnit 10.5.0 by Sebastian Bergmann and contributors.

.                                                                   1 / 1 (100%)

Time: 00:00.012, Memory: 6.00 MB

OK (1 test, 1 assertion)
```

One dot per passing test. That's it: that's the whole feedback loop you'll live in for the rest of this chapter.

## `#[Test]` as an alternative to the `test` prefix

PHP 8 attributes (covered properly in [Chapter 20](ch20-00-advanced-features.md)) give PHPUnit a second way to mark a method as a test, without the naming constraint:

```php
<?php

use PHPUnit\Framework\Attributes\Test;
use PHPUnit\Framework\TestCase;

final class RectangleTest extends TestCase
{
    #[Test]
    public function itCalculatesArea(): void
    {
        $rectangle = new Rectangle(8.0, 7.0);

        $this->assertEquals(56.0, $rectangle->area());
    }
}
```

Either style is fine, and most projects settle on one and stay consistent. This book will keep using the `test` prefix, since it needs no `use` statement and reads clearly enough on its own.

## More assertions: `assertTrue`, and `assertEquals` vs. `assertSame`

```php
<?php

final class RectangleTest extends TestCase
{
    public function testASquareIsDetected(): void
    {
        $square = new Rectangle(5.0, 5.0);

        $this->assertTrue($square->isSquare());
    }

    public function testEqualsVsSame(): void
    {
        $this->assertEquals(1, "1");   // passes, loose comparison, like ==
        $this->assertSame(1, "1");     // fails, strict comparison, like ===
    }
}
```

This distinction is not a PHPUnit quirk: it's the exact same `==` versus `===` distinction from [Chapter 3](ch03-02-data-types.md), wearing an assertion-shaped hat. `assertEquals()` allows type juggling: `1` and `"1"` are "equal enough." `assertSame()` refuses it, checking type and value together, the same way `===` does. Default to `assertSame()` when you can: it catches a category of bug (a function accidentally returning a string where you expected an int) that `assertEquals()` will let straight through without complaint. Reach for `assertEquals()` only when the loose comparison is genuinely what you mean to test.

A failing assertion tells you exactly what went wrong:

```console
$ vendor/bin/phpunit tests
1) RectangleTest::testEqualsVsSame
Failed asserting that 1 is identical to '1'.
```

That message is doing real work: it's telling you the types didn't match, not just that "something" was unequal. Read failure messages closely; PHPUnit is usually more specific than it looks at first glance.
