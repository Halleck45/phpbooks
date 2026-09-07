# Packages and Autoloading

You already know the mechanics of installing a package: `composer require` pulls it into `vendor/`, and `require 'vendor/autoload.php'` makes every class inside it available. What we skipped over a moment ago, on purpose, was *how* that second part actually works, because the answer explains why the rest of this chapter exists.

## The problem autoloading solves

Imagine PHP without any of this. You write a `Cart` class in one file and a `Product` class in another, and your entry-point script needs both:

```php
<?php

require 'Product.php';
require 'Cart.php';

$product = new Product('Keyboard', 49.00);
$cart = new Cart();
$cart->add($product);
```

Two classes, two `require` lines, kept in sync by hand. That's manageable. Now imagine forty classes, spread across a dozen packages you didn't write, each depending on others in an order you'd have to work out yourself. Nobody does this anymore, and for good reason: it's tedious and it breaks the moment you rename a file.

## `spl_autoload_register()`

PHP has a built-in escape hatch for exactly this: `spl_autoload_register()`. It lets you register a function that PHP calls automatically the first time it encounters a class name it doesn't recognize yet: instead of failing immediately, PHP gives your function a chance to go find and load it.

```php
<?php

spl_autoload_register(function (string $className): void {
    $file = __DIR__ . '/' . $className . '.php';

    if (file_exists($file)) {
        require $file;
    }
});

$cart = new Cart(); // Cart.php is loaded automatically, on first use
```

You could write your own version of this, and a lot of PHP projects did, before Composer existed. It works, but the moment a package you rely on ships its own hand-rolled autoloader with slightly different rules, you're back to coordinating things by hand.

## What Composer actually generates

Every time you run `composer install` or `composer require`, Composer regenerates the files inside `vendor/composer/`, including `autoload_psr4.php`, a plain PHP array mapping namespace prefixes to directories. `vendor/autoload.php` registers one autoloader, built from that map, via `spl_autoload_register()`, and from then on any class from any installed package resolves automatically, no matter which package declared it.

This works because packages don't just dump files into a shared folder: each one declares, in its own `composer.json`, which namespace prefix maps to which directory. A small preview of what that declaration looks like (we'll build one properly in [PSR-4](ch07-06-psr4.md)):

```json
{
    "autoload": {
        "psr-4": {
            "App\\": "src/"
        }
    }
}
```

That's really the whole trick: a namespace is a promise about where to find the file, and PSR-4 is the rule that turns the promise into a file path. Composer's autoloader just executes that rule fast.

## Why this needs namespaces at all

Here's the part that matters for the rest of the chapter: this scheme only works if class names stay unique across every package installed in your project. A `Product` class from your own code and a `Product` class from some e-commerce package would otherwise be indistinguishable: PHP wouldn't know which `Product.php` to load, and neither would you, reading the code six months later.

Namespaces are how PHP avoids that collision entirely, by making `Product` shorthand for something more specific: `App\Models\Product`, say, versus `Vendor\Ecommerce\Product`. Two different names, two different files, no ambiguity. That's what we cover next.
