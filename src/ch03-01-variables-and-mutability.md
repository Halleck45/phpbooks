# Variables, Constants, and Mutability

## Variables

Every PHP variable starts with a dollar sign, and that's genuinely most of the syntax you need to know:

```php
<?php

$greeting = "Hello";
echo $greeting;

$greeting = "Goodbye";
echo $greeting;
```

No `let`, no `var` (well, there is `var`, but it's a fossil from PHP 4 that only means something inside a class, and you won't use it). You just assign, and the variable exists from that point on. There's no separate declaration step to forget.

That also means every variable is mutable by default: reassigning `$greeting` above isn't a special operation requiring permission, it's just... assignment, again. If you're coming from a language that makes you opt *into* mutability, this will feel like the opposite default. PHP's position is that mutability is the normal case and immutability is the thing you build deliberately, usually with objects (more on that once we reach classes).

## Naming

Variable names are case-sensitive, must start with a letter or underscore, and by convention use `camelCase`:

```php
<?php

$userName = "damien";
$total_price = 42.50; // valid, but not idiomatic PHP
```

Both lines above work. Only the first one is what you'll see in modern PHP code and in the standards (PSR-12) most projects follow. Function and class names have their own conventions we'll get to later. PHP's ecosystem cares more about consistency *within* a codebase than about any one style being objectively correct, but `camelCase` for variables is about as close to universal as PHP conventions get.

## Constants

When a value genuinely should never change during the program's execution (a configuration value, a mathematical constant, an API base URL), reach for a real constant instead of a variable you simply promise not to touch:

```php
<?php

define('MAX_RETRIES', 3);
echo MAX_RETRIES;

const APP_NAME = 'GuessingGame';
echo APP_NAME;
```

Two ways to write one, and both are common in the wild. `define()` is a function call, evaluated at runtime, and works anywhere. `const` is a language construct, resolved at compile time, and (this is the part that trips people up) can only be used at the top level of a file or inside a class; you can't `const` something inside an `if` block or a function body. Outside of a class, prefer `const`; it's slightly faster and reads more like what it is.

Notice constants have no `$`: that's deliberate, so you can tell at a glance, anywhere in a file, that `MAX_RETRIES` isn't going to change out from under you, unlike `$maxRetries`, which anyone downstream is free to reassign.

## A word about "mutability" versus what PHP actually does

If you've read about other languages that make a big deal out of ownership or borrowing, you might expect PHP's story here to be more complicated than "just assign to it." It genuinely isn't, at this level, but PHP does have its own, much gentler version of "who owns this data," which shows up once you start passing arrays and objects into functions rather than just printing strings. We'll get there in [Working with Variables and References](ch04-00-variables-and-references.md), once you've seen enough of the language for it to matter.
