# Hello, Composer!

A single-file script like `hello.php` doesn't need help managing dependencies, because it has none. Real projects do, almost immediately: a testing library here, an HTTP client there. And PHP's answer to "how do I pull in someone else's code without copy-pasting it into my repo" is [Composer](https://getcomposer.org/).

If you've used `npm`, `pip`, or `cargo` before, you already understand Composer's job. If you haven't, don't worry: we'll build the intuition from scratch.

## Installing Composer

On macOS or Linux, the quickest path is usually your package manager:

```console
$ brew install composer
```

Everywhere else, or if you want the canonical method, the [official download page](https://getcomposer.org/download/) has a short install script. Either way, confirm it worked:

```console
$ composer --version
Composer version 2.7.6 2024-...
```

## Starting a project

Inside an empty directory, run:

```console
$ composer init
```

Composer will ask you a handful of questions: package name, description, author, license, and so on. For now, you can accept the defaults on most of them or just press Enter through the whole thing; none of it is permanent. What matters is what it leaves behind: a `composer.json` file.

```json
{
    "name": "you/hello-composer",
    "require": {}
}
```

This file is the source of truth for your project's dependencies: think of it as an ingredients list. `composer.json` is meant to be committed to version control. What it *pulls in*, on the other hand, is not.

## Requiring your first package

Let's add something real. [`nunomaduro/termwind`](https://github.com/nunomaduro/termwind) is a small library for styling terminal output, nothing essential, just enough to prove the mechanism works:

```console
$ composer require nunomaduro/termwind
```

Two things appear: a `vendor/` directory, containing the actual downloaded code, and a `composer.lock` file, which pins the *exact* versions installed, down to the last commit, so that everyone on your team, and your production server, installs identically. `composer.json` says what you're willing to accept; `composer.lock` says what you actually got. Commit the lock file too.

Now use it:

```php
<?php

require 'vendor/autoload.php';

use function Termwind\render;

render('<div class="p-1 bg-green-400">Hello, Composer!</div>');
```

That `require 'vendor/autoload.php';` line is the one that matters most. Composer generates an autoloader: a bit of PHP that knows how to find and load any class from any package you've installed, on demand, without you writing a single `require` for each one. Include that one file, once, at the top of your entry point, and every dependency you add from here on just... works.

## What we'll do with this

Everything so far has lived in a single file, so Composer's autoloader hasn't had much to do beyond loading Termwind. That changes immediately: the rest of this chapter is about splitting code across files and packages, and that same autoloader is also how *your own* classes get found, not just third-party ones.
