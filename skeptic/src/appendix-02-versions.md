# B - PHP Versions, 2015 to 2026

Each version has a section below, with its release date, its support window and its headline changes. The dates come from php.net. Active support means bug fixes and security fixes, and security support means security fixes only. Since the release cycle update voted in 2024, both windows end on 31 December of their final year.

| Version | Released | Active support until | Security support until |
|---|---|---|---|
| PHP 5.6 | 28 Aug 2014 | 19 Jan 2017 | 31 Dec 2018 |
| PHP 7.0 | 3 Dec 2015 | 3 Dec 2017 | 10 Jan 2019 |
| PHP 7.1 | 1 Dec 2016 | 1 Dec 2018 | 1 Dec 2019 |
| PHP 7.2 | 30 Nov 2017 | 30 Nov 2019 | 30 Nov 2020 |
| PHP 7.3 | 6 Dec 2018 | 6 Dec 2020 | 6 Dec 2021 |
| PHP 7.4 | 28 Nov 2019 | 28 Nov 2021 | 28 Nov 2022 |
| PHP 8.0 | 26 Nov 2020 | 26 Nov 2022 | 26 Nov 2023 |
| PHP 8.1 | 25 Nov 2021 | 25 Nov 2023 | 31 Dec 2025 |
| PHP 8.2 | 8 Dec 2022 | 31 Dec 2024 | 31 Dec 2026 |
| PHP 8.3 | 23 Nov 2023 | 31 Dec 2025 | 31 Dec 2027 |
| PHP 8.4 | 21 Nov 2024 | 31 Dec 2026 | 31 Dec 2028 |
| PHP 8.5 | 20 Nov 2025 | 31 Dec 2027 | 31 Dec 2029 |

The pattern to retain from the table is eleven consecutive yearly releases, each between 20 November and 8 December. The schedule of the next one is published on wiki.php.net months in advance, with its feature freeze and release candidate dates.

## PHP 7.0, December 2015

- New engine, with a large reduction in memory use and, on the interpreter's own work, about twice the speed of PHP 5.6; see [Throughput and Latency](ch03-throughput-and-latency.md) for the vendor claim and the independent synthetic measurement, with their caveats.
- Scalar type declarations (`int`, `float`, `string`, `bool`) for parameters, and return type declarations.
- `declare(strict_types=1)`.
- Null coalescing operator `??`, spaceship operator `<=>`.
- Anonymous classes.
- Engine errors became exceptions (`Error` hierarchy), so a fatal error can be caught.
- Removal of the `mysql_*` functions, `ereg_*` functions and PHP 4 style constructors.

## PHP 7.1 to 7.4, 2016 to 2019

- 7.1: nullable types (`?int`), `void` return type, `iterable`, class constant visibility.
- 7.2: `object` type, Argon2 password hashing, Libsodium in the core.
- 7.3: flexible heredoc syntax, `is_countable()`, JSON errors as exceptions.
- 7.4: typed properties, arrow functions (`fn`), OPcache preloading, the foreign function interface (FFI), the `??=` operator, covariant returns and contravariant parameters.

## PHP 8.0, November 2020

- Named arguments: `str_pad(string: 'a', length: 3)`.
- Attributes: `#[Route('/home')]` as structured metadata read by reflection.
- Constructor property promotion: `public function __construct(private int $x) {}`.
- Union types: `int|string $id`.
- `match` expression: strict comparison, no fallthrough, exhaustive.
- Nullsafe operator: `$user?->address?->city`.
- `mixed` and `static` as types.
- `throw` as an expression.
- `str_contains()`, `str_starts_with()`, `str_ends_with()`.
- `Stringable` interface, `WeakMap`.
- JIT compiler, inside OPcache.
- Saner string-to-number comparisons: `0 == 'foo'` is `false`.
- Internal functions throw `TypeError` and `ValueError` instead of warning and returning `null` or `false`.

## PHP 8.1, November 2021

- Enums, pure and backed.
- `readonly` properties.
- First-class callable syntax: `strlen(...)`.
- Fibers: stackful coroutines, the building block of async libraries.
- `new` in initializers.
- Pure intersection types: `Countable&Traversable`.
- `never` return type, `final` class constants, `array_is_list()`, explicit octal notation.

## PHP 8.2, December 2022

- `readonly` classes.
- Disjunctive normal form types: `(A&B)|null`.
- Standalone `true`, `false` and `null` types.
- Dynamic properties deprecated; `#[\AllowDynamicProperties]` opts a class back in.
- `#[\SensitiveParameter]` to redact an argument from stack traces.
- Constants in traits, `Random\Randomizer`.

## PHP 8.3, November 2023

- Typed class constants.
- `#[\Override]` attribute: the engine checks that a parent method exists.
- `json_validate()`.
- Dynamic class constant fetch: `Foo::{$name}`.
- `readonly` properties can be reinitialised inside `__clone()`.

## PHP 8.4, November 2024

- Property hooks: `get` and `set` logic declared on the property itself.
- Asymmetric visibility: `public private(set) int $x`.
- `new Foo()->bar()` without wrapping parentheses.
- Lazy objects through reflection (`newLazyGhost()`, `newLazyProxy()`).
- `#[\Deprecated]` attribute.
- `array_find()`, `array_find_key()`, `array_any()`, `array_all()`.
- `mb_trim()` and friends, `mb_ucfirst()`, `mb_lcfirst()`.
- New DOM extension with an HTML5 parser (`Dom\HTMLDocument`).
- BCMath object API (`BcMath\Number`), PDO driver subclasses (`Pdo\Sqlite`, `Pdo\Mysql`, `Pdo\Pgsql`).
- Implicitly nullable parameter types deprecated.

## PHP 8.5, November 2025

- Pipe operator: `$value |> trim(...) |> strtoupper(...)`.
- `clone` with property updates: `clone($obj, ['prop' => $value])`.
- `#[\NoDiscard]` attribute, with the `(void)` cast to silence it deliberately.
- `array_first()`, `array_last()`.
- Closures and first-class callables in constant expressions (attribute arguments, default values, constants).
- Attributes on constants.
- New `uri` extension (`Uri\Rfc3986\Uri`, `Uri\WhatWg\Url`).
- Fatal errors include a backtrace.
- `get_error_handler()`, `get_exception_handler()`.
- The backtick shell-execution operator is deprecated.
