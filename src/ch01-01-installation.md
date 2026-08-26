# Installation

## Checking whether you already have PHP

Open a terminal and try this:

```console
$ php -v
PHP 8.3.6 (cli) (built: ...) (NTS)
```

If you get a version number, and it starts with an 8, you're basically done. Skip ahead to the next section. If it starts with a 7 or lower, or the command isn't found at all, read on.

## Installing PHP

**macOS.** The system used to ship an ancient PHP for internal use; recent macOS versions ship none at all. Either way, install a current one with Homebrew:

```console
$ brew install php
```

**Linux.** Your distribution's package manager has it, though the version lagging behind can be a year or two out of date depending on the release. On Ubuntu or Debian, the [Ondřej Surý PPA](https://launchpad.net/~ondrej/+archive/ubuntu/php) keeps up with new releases faster than the default repositories:

```console
$ sudo apt install php-cli
```

**Windows.** Grab the "Non Thread Safe" zip from [windows.php.net](https://windows.php.net/download/), unzip it somewhere sane like `C:\php`, and add that folder to your `PATH`. If you'd rather not manage this by hand, [Laragon](https://laragon.org/) or [WampServer](https://www.wampserver.com/) bundle PHP with a friendlier installer.

**Anywhere, with Docker.** If you don't want to install anything system-wide:

```console
$ docker run --rm -it php:8.3-cli bash
```

This drops you into a shell with PHP ready to go. It's a fine way to follow along with this book without touching your machine's configuration at all.

## Verifying the install

Run `php -v` again. You should see a version number this time. While you're there, run this too: it lists which optional pieces (called *extensions*) are compiled into your PHP:

```console
$ php -m
```

Don't worry about the list. We'll come back to extensions when we actually need one.

One last thing worth knowing: PHP has both a command-line version (`php-cli`, what you just installed) and versions meant to run inside a web server (`php-fpm`, mod_php). They're the same language underneath, but this book only needs the CLI one: the version that runs scripts directly from your terminal, the way Python or Ruby would.
