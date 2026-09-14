# B - PHP 8.0 to 8.5 at a Glance

One section per version, headline features only. Find your project's version, then read down from there to see what you can use.

## PHP 8.0, November 2020

- Named arguments: `str_pad(string: 'a', length: 3)`.
- Attributes: `#[Route('/home')]` as structured metadata read by reflection.
- Constructor property promotion: `public function __construct(private int $x) {}`.
- Union types: `int|string $id`.
- `match` expression: strict comparison, no fallthrough, exhaustive.
- Nullsafe operator: `$user?->address?->city`.
- `mixed` and `static` as types.
- `throw` as an expression: `$x = $y ?? throw new Exception();`.
- `str_contains()`, `str_starts_with()`, `str_ends_with()`.
- `Stringable` interface, implemented automatically by any class with `__toString()`.
- `WeakMap`.
- JIT compiler, inside OPcache.
- Saner string-to-number comparisons: `0 == 'foo'` is `false`.
- Trailing comma allowed in parameter lists.
- Internal functions throw `TypeError` and `ValueError` instead of warning and returning `null` or `false`.

## PHP 8.1, November 2021

- Enums, pure and backed: `enum Suit: string { case Hearts = 'H'; }`.
- `readonly` properties: `public readonly int $x`.
- First-class callable syntax: `strlen(...)`.
- Fibers: stackful coroutines, the building block of async libraries.
- `new` in initializers: `public function __construct(private Logger $l = new NullLogger()) {}`.
- Pure intersection types: `Countable&Traversable`.
- `never` return type.
- `final` class constants.
- Array unpacking with string keys: `[...$defaults, ...$options]`.
- `array_is_list()`.
- Explicit octal notation: `0o16`.

## PHP 8.2, December 2022

- `readonly` classes: `final readonly class Point {}`.
- Disjunctive normal form types: `(A&B)|null`.
- Standalone `true`, `false` and `null` types.
- Dynamic properties deprecated; `#[\AllowDynamicProperties]` opts a class back in.
- `#[\SensitiveParameter]` to redact an argument from stack traces.
- Constants in traits.
- `Random\Randomizer` and the `random` extension.
- Enum cases usable in constant expressions.

## PHP 8.3, November 2023

- Typed class constants: `const string NAME = 'x';`.
- `#[\Override]` attribute: the engine checks that a parent method exists.
- `json_validate()`.
- Dynamic class constant fetch: `Foo::{$name}`.
- `readonly` properties can be reinitialised inside `__clone()`.
- `Randomizer::getBytesFromString()`, `Randomizer::getFloat()`.
- Negative array indices behave consistently.
- `mb_str_pad()`.

## PHP 8.4, November 2024

- Property hooks: `public string $name { get => ...; set => ...; }`.
- Asymmetric visibility: `public private(set) int $x`.
- `new` without parentheses when chaining: `new Foo()->bar()`.
- Lazy objects: `ReflectionClass::newLazyGhost()`, `newLazyProxy()`.
- `#[\Deprecated]` attribute for your own code.
- `array_find()`, `array_find_key()`, `array_any()`, `array_all()`.
- `mb_trim()`, `mb_ltrim()`, `mb_rtrim()`, `mb_ucfirst()`, `mb_lcfirst()`.
- New DOM extension with an HTML5 parser: `Dom\HTMLDocument`.
- BCMath object API: `BcMath\Number`.
- PDO driver subclasses: `Pdo\Sqlite`, `Pdo\Mysql`, `Pdo\Pgsql`, via `Pdo::connect()`.
- `request_parse_body()` for form bodies on any HTTP method.
- Implicitly nullable parameters (`Foo $x = null` without `?`) deprecated.
- `exit` and `die` are now functions.

## PHP 8.5, November 2025

- Pipe operator: `$slug = $title |> trim(...) |> strtolower(...);`.
- `clone` with property updates: `clone($point, ['x' => 3])`.
- `#[\NoDiscard]` attribute, warning when a return value is ignored; `(void)` cast to silence it on purpose.
- `array_first()`, `array_last()`.
- Closures and first-class callables in constant expressions (attribute arguments, default values, constants).
- Attributes on constants.
- New `uri` extension: `Uri\Rfc3986\Uri`, `Uri\WhatWg\Url`.
- Fatal errors now include a backtrace.
- `get_error_handler()`, `get_exception_handler()`.
- `#[\DelayedTargetValidation]`.
- `PHP_BUILD_DATE` constant.
- The backtick shell-execution operator is deprecated.

## Support policy

Each version gets two years of active support (bug fixes) followed by two years of security fixes only. A version released in November 2025 is therefore active until late 2027 and patched until late 2029. Dates move with each release; [php.net/supported-versions](https://www.php.net/supported-versions) has the current table. Running a version past its security window is a risk you take knowingly or not at all.

## Finding your project's version

`php -v` prints the interpreter you run locally. `composer.json` declares what the project supports under `require.php` (`"php": "^8.3"`), and `config.platform.php` pins the version Composer resolves against, which is the one to trust when the two differ. Production may run something else again; `phpinfo()` or `php -v` on the server settles it.
