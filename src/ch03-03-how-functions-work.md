# Functions

You've already used a handful of PHP's built-in functions: `trim()`, `echo` (which, as noted earlier, technically isn't one), `random_int()`. Let's write your own.

```php
<?php

function greet($name) {
    echo "Hello, {$name}!\n";
}

greet("Damien");
```

`function`, a name, parentheses for parameters, and a body in braces: that's the whole shape. PHP function names are, like variables, case-insensitive at the call site (please don't rely on that) and conventionally `camelCase`.

## Parameters and types

Add type declarations to parameters the same way you saw in the previous section, and give the function a return type too:

```php
<?php

function greet(string $name): void {
    echo "Hello, {$name}!\n";
}
```

`: void` says this function doesn't return a value: it's called purely for its side effect (printing, here). Every function that *does* hand something back should declare what:

```php
<?php

function add(int $a, int $b): int {
    return $a + $b;
}

$sum = add(2, 3);
```

Type every parameter and every return value, on every function you write, from here on. It costs you a few extra keystrokes and saves you from an entire category of bugs where a function silently receives, or returns, something you didn't expect. Combined with `declare(strict_types=1)` from the previous section, this turns PHP from "dynamically typed and a little too forgiving about it" into something that will actually stop you at the door when you pass the wrong thing.

## Default values

Parameters can have defaults, which makes them optional at the call site:

```php
<?php

function greet(string $name, string $greeting = "Hello"): void {
    echo "{$greeting}, {$name}!\n";
}

greet("Damien");             // Hello, Damien!
greet("Damien", "Bonjour");  // Bonjour, Damien!
```

Parameters with defaults must come after parameters without them: PHP reads arguments left to right, so it needs the required ones settled first.

## Named arguments

Speaking of argument order: PHP lets you pass arguments by name instead of position, which is a genuine quality-of-life feature once a function has more than two or three parameters:

```php
<?php

greet(name: "Damien", greeting: "Bonjour");
greet(greeting: "Bonjour", name: "Damien"); // order no longer matters
```

This is especially welcome with functions that have several optional parameters: you can skip straight to the one you actually want to override, instead of passing every default in between just to reach it positionally.

## Return values are expressions, not just for `void` functions

`return` immediately exits the function with a value:

```php
<?php

function classify(int $n): string {
    if ($n < 0) {
        return "negative";
    }

    if ($n === 0) {
        return "zero";
    }

    return "positive";
}
```

There's no implicit "last expression is the return value" the way some languages work: PHP always wants an explicit `return`. Leave it off, and a function returns `null` by default, silently. That's usually a bug, not a choice, which is exactly why declaring `: void` on functions that truly return nothing is worth the habit: it lets PHP (and any static analysis tool checking your code) flag it if you accidentally do return something from one.

## Functions as values

One more thing worth knowing early, even though we won't use it in earnest until [Chapter 14](ch14-00-functional-features.md): functions in PHP are values too. You can hold one in a variable and call it:

```php
<?php

$operation = 'add';
echo $operation(2, 3); // calls add(2, 3), if add() is defined above
```

And PHP has genuine anonymous functions, closures, for when you need to pass behavior around without giving it a name at all:

```php
<?php

$double = function (int $n): int {
    return $n * 2;
};

echo $double(21); // 42
```

File that away for now. It'll matter a great deal later, once we start passing small pieces of behavior into array functions and generators.
