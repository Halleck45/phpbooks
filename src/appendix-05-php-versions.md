# E - PHP Versions and Backward Compatibility

## Release cadence

PHP ships a new minor version roughly once a year. Each version gets about two years of active support (new features, bug fixes, security patches) followed by roughly one more year of security-only support before it reaches end of life. After that, running it in production is running unpatched software, full stop.

Check what you're running:

```console
$ php -v
PHP 8.3.0 (cli) (built: ...)
```

Or from inside a running script:

```php
<?php

echo phpversion(); // "8.3.0"
```

## A short history

PHP 5 to PHP 7 was a genuinely huge leap: a rewritten engine, roughly double the performance, and the introduction of scalar type declarations. PHP 7 to PHP 8 was smaller in raw performance terms but denser in language features: the JIT compiler, union types, enums, attributes, named arguments, the nullsafe operator, constructor promotion, `match`. Most of what this book leans on (enums in [Chapter 6](ch06-00-enums.md), attributes in [Chapter 20](ch20-04-attributes.md), and constructor promotion in [Chapter 5](ch05-03-methods.md)) didn't exist before PHP 8. This book targets PHP 8.1 and later for exactly that reason.

## Pin a minimum version

Tell Composer, and anyone installing your package, what it actually needs:

```json
{
    "require": {
        "php": ">=8.1"
    }
}
```

This isn't a formality. Without it, Composer will happily let your package install on a PHP version that doesn't have the features you're using, and the failure will happen at runtime instead of install time, which is a much worse place to discover it.

## Don't fear upgrading

PHP takes backward compatibility within a major version seriously. Code written for PHP 8.0 runs, largely unmodified, on PHP 8.3. Deprecation notices generally show up one or two versions before something is actually removed, giving you real warning rather than a surprise. Upgrading is rarely the ordeal older reputations about PHP suggest: the bigger risk, in practice, is staying on an unsupported version and quietly losing security patches.
