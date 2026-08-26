# Adding Functionality with Test-Driven Development

`search()` and `GrepOptions` now live outside the entry script, in files that don't parse `$argv`, don't `echo`, and don't `exit`. That was the whole point of the last section's refactor, and it means, for the first time in this project, we can write a PHPUnit test against them directly, the way [Chapter 11](ch11-00-testing.md) taught. Let's use that to add a real feature: case-insensitive search.

Set up the project the same way you did there:

```console
$ composer require --dev phpunit/phpunit
```

## Red: write the test you wish already passed

Go back to `fruits.txt` from a couple of sections ago:

```text
Apple pie recipe
apple sauce for the win
Banana bread is better
cherry clafoutis
```

Searching for `apple` right now only finds the lowercase line: `str_contains()` doesn't fold case. Let's write down, as a test, the behavior we actually want: a `GrepOptions` with case-insensitivity turned on should match both `"Apple pie recipe"` and `"apple sauce for the win"`.

```php
<?php
// tests/SearchTest.php
declare(strict_types=1);

use PHPUnit\Framework\TestCase;

require_once __DIR__ . '/../src/GrepOptions.php';
require_once __DIR__ . '/../src/FileNotFoundException.php';
require_once __DIR__ . '/../src/search.php';

final class SearchTest extends TestCase
{
    private string $fixture;

    protected function setUp(): void
    {
        $this->fixture = tempnam(sys_get_temp_dir(), 'phpgrep');
        file_put_contents(
            $this->fixture,
            "Apple pie recipe\napple sauce for the win\nBanana bread is better\ncherry clafoutis\n"
        );
    }

    protected function tearDown(): void
    {
        unlink($this->fixture);
    }

    public function testSearchCanIgnoreCase(): void
    {
        $options = new GrepOptions(
            query: 'apple',
            filename: $this->fixture,
            ignoreCase: true,
        );

        $this->assertSame(
            ['Apple pie recipe', 'apple sauce for the win'],
            search($options)
        );
    }
}
```

`setUp()` and `tearDown()` are PHPUnit hooks that run before and after *every* test method in the class: perfect for building a fresh temporary fixture file per test and cleaning it up afterward, so tests never depend on leftover state from a previous run.

Run it:

```console
$ vendor/bin/phpunit tests
PHPUnit 10.5.0 by Sebastian Bergmann and contributors.

E                                                                   1 / 1 (100%)

Time: 00:00.014, Memory: 6.00 MB

1) SearchTest::testSearchCanIgnoreCase
Error: Unknown named parameter $ignoreCase
```

That's red. Good, for entirely the right reason. `GrepOptions` doesn't have an `ignoreCase` property at all yet, so PHP can't even construct the object the test asks for. This is the whole rhythm of test-driven development in one step: write the test for the behavior you want *before* the code that provides it exists, watch it fail, and let that failure tell you exactly what to build next.

## Green: make it pass

First, give `GrepOptions` the property the test is asking for:

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
            ignoreCase: false,
        );
    }
}
```

`fromArgv()` passes a hardcoded `false` for now: wiring it up to something the user can actually control is next section's job. Then teach `search()` to honor the flag:

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
    $query = $options->ignoreCase ? strtolower($options->query) : $options->query;

    $matches = [];
    foreach ($lines as $line) {
        $haystack = $options->ignoreCase ? strtolower($line) : $line;
        if (str_contains($haystack, $query)) {
            $matches[] = $line;
        }
    }

    return $matches;
}
```

Both `$line` and `$query` get lowercased for the *comparison* when `ignoreCase` is on, but notice it's the original, unmodified `$line` that gets pushed into `$matches`. We want case-insensitive matching, not case-mangled output.

```console
$ vendor/bin/phpunit tests
PHPUnit 10.5.0 by Sebastian Bergmann and contributors.

.                                                                   1 / 1 (100%)

Time: 00:00.013, Memory: 6.00 MB

OK (1 test, 1 assertion)
```

Green. That's the rhythm: red, then green, then (traditionally) refactor, though there's not much worth reshaping here yet. Worth adding one more test while you're in the file, just to pin down the behavior you're *not* changing:

```php
<?php

public function testSearchIsCaseSensitiveByDefault(): void
{
    $options = new GrepOptions(
        query: 'apple',
        filename: $this->fixture,
        ignoreCase: false,
    );

    $this->assertSame(['apple sauce for the win'], search($options));
}
```

That one passes immediately: it's not testing new behavior, it's guarding old behavior against a future regression. Both are worth having: the first proves the feature works, the second proves adding it didn't quietly break what was already there.
