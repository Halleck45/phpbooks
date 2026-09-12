# Hello, World!

<img src="images/ch01-icon.svg" alt="Hello, World! illustration" width="72">

Create a file called `hello.php`, anywhere you like:

```php
<?php

echo "Hello, world!\n";
```

Then run it:

```console
$ php hello.php
Hello, world!
```

That's it. That's the whole program. Let's slow down and look at what's actually in those two lines, because every single one of them matters.

## `<?php`

PHP is, at heart, a templating language that grew a full programming language inside it. That opening tag is a leftover (and a permanent feature) of that history: everything *outside* `<?php ... ?>` tags is sent straight to output, untouched, as plain text or HTML. Everything *inside* is parsed as PHP code.

In a file that's pure PHP, like ours, you'll almost always see just the opening tag and nothing else: no closing `?>`, and definitely nothing before it. Skipping the closing tag at the end of a file is a deliberate convention, not an oversight: it's impossible to accidentally leak a stray blank line or space *after* a tag that was never closed. You'll thank this convention the first time a stray newline after `?>` breaks a redirect three files away from the one you edited.

## `echo`

`echo` prints its argument. It's not a function: no parentheses required, though `echo("...")` also works because PHP is relaxed about it. You'll see `echo` constantly; it's the workhorse of PHP output, alongside `print` (nearly identical, but a real expression that returns `1`) and `printf` (for when you need formatting).

## The string, and that `\n`

`"Hello, world!\n"` is a double-quoted string. Inside double quotes, PHP interprets escape sequences like `\n` (newline) and, as we'll see very soon, variables too. Single-quoted strings (`'Hello, world!'`) don't do either of those; they're closer to "what you typed is what you get." Neither is more "correct"; you'll pick between them constantly, usually based on whether you need PHP to look inside the string or leave it alone.

## The semicolon

PHP statements end with `;`. Forget one and PHP will, in typical fashion, wait until the *next* line to complain, pointing at code that was perfectly innocent. When you get a baffling parse error, the first thing worth checking is always the line *above* the one PHP is blaming.

## Running it

`php hello.php` runs the interpreter directly against your file: no compile step, no build artifact left behind. This is the single biggest difference in *feel* between PHP and a compiled language: you edit, you run, you see the result, immediately. We'll lean on that tight loop constantly throughout this book.

There's also a REPL, if you want to try one-liners without creating a file:

```console
$ php -a
Interactive shell

php > echo "Hello, world!\n";
Hello, world!
php > exit
```

Handy for quick experiments. Not something you'll build real programs in, but neither did anyone building real programs in a REPL for any other language.
