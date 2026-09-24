# D - Useful Development Tools

This book has already covered two of these properly. The rest are what to go install next: not exhaustive documentation of any one of them, just enough to know what each one is for and why working PHP developers bother.

## Composer

Covered from [Chapter 7](ch07-01-hello-composer.md) onward, and again in depth in [Chapter 16](ch16-00-more-about-composer.md). Dependency management and autoloading. You will not write PHP professionally without it, and by this point in the book you already haven't.

## PHPUnit

Covered in [Chapter 12](ch12-00-testing.md). The standard testing framework. If a PHP project has tests, they are very likely PHPUnit tests.

## PHPStan and Psalm

Static analysis tools: they read your code without running it and tell you where it's wrong, or at least where it's suspicious. Both understand PHP's type system more strictly than PHP itself does at runtime; they'll catch a call to a method that doesn't exist, a `null` passed where the type says it can't be, a return type that quietly stopped matching what the function returns. This is exactly the territory [Chapter 11](ch11-03-generic-style-code.md) touches on with docblock-based generics: PHP's own type system can't express "an array of `User` objects," but a docblock annotation combined with PHPStan or Psalm reading it can check that promise for you.

Neither ships with PHP. Both install via Composer, both run in CI, and both are worth adding to a project on day one rather than after the bugs they'd have caught have already shipped.

```console
$ composer require --dev phpstan/phpstan
$ vendor/bin/phpstan analyse src
```

## PHP-CS-Fixer and PHP_CodeSniffer

Code style enforcement: not "is this correct" but "is this formatted the way the team agreed to format it." Both can check a codebase against PSR-12 (PHP's standard style guide) and, more usefully, both can *fix* violations automatically rather than just listing them.

```console
$ vendor/bin/php-cs-fixer fix src
```

Pick one, wire it into your editor or a pre-commit hook, and stop having style debates in code review; let the tool have that argument instead.

## Xdebug

A step debugger and profiler for PHP. Instead of scattering `var_dump()` calls through your code and rerunning it, Xdebug lets you pause execution at a breakpoint, inspect every variable in scope, and step through line by line, from your editor, in real time. It also profiles, showing you exactly where a slow request spent its time. Covered properly, installation and all, in [Chapter 13](ch13-02-xdebug.md).

## Editors and IDEs

PHP doesn't require any particular editor, but two are worth knowing about:

**PhpStorm**: a dedicated PHP IDE with deep, built-in understanding of the language (refactoring, navigation, and inline static analysis that rivals PHPStan without leaving the editor). Commercial, free for students and open source maintainers.

**VS Code**, with the PHP extensions (Intelephense or the official PHP extension pack): free, general-purpose, and perfectly capable once configured. What most PHP developers who don't use PhpStorm reach for.

Either is a fine choice. What matters is picking one and learning it properly, rather than fighting a half-configured editor on top of learning the language.
