# First-Class Callable Syntax and Advanced Closures

You met closures and arrow functions in [Chapter 14](ch14-01-closures.md). This section covers two more recent additions worth having in your toolkit: a cleaner syntax for turning existing functions and methods into callables, and a couple of `Closure` tricks that come up once you're writing more deliberate, defensive code.

## The old way of passing a function around

Before PHP 8.1, if you wanted to pass an existing function or method as a value (to `array_map()`, for instance) you reached for a string or an array:

```php
<?php

$lengths = array_map('strlen', ['a', 'bb', 'ccc']);

class Greeter
{
    public function greet(string $name): string
    {
        return "Hello, {$name}!";
    }
}

$greeter = new Greeter();
$greetCallable = [$greeter, 'greet'];

echo $greetCallable('Sam'), "\n"; // Hello, Sam!
```

This works, and you'll still see it in plenty of existing code, but it has a real downside: `'strlen'` and `[$greeter, 'greet']` are just a string and an array as far as your tools are concerned. Your editor can't reliably jump to the definition, and a typo in the method name isn't caught until the callable is actually invoked.

## First-class callable syntax

PHP 8.1 added a direct syntax for the same thing: write the function or method's name followed by `(...)` (three literal dots, not a real argument list) and PHP hands you a proper `Closure` pointing at it.

```php
<?php

$lengths = array_map(strlen(...), ['a', 'bb', 'ccc']);

class Greeter
{
    public function greet(string $name): string
    {
        return "Hello, {$name}!";
    }
}

$greeter = new Greeter();
$greetCallable = $greeter->greet(...);

echo $greetCallable('Sam'), "\n"; // Hello, Sam!
```

Same behavior, but now `strlen(...)` and `$greeter->greet(...)` are real references your tooling understands: go-to-definition works, static analysis can check the signature, and a rename of `greet()` gets caught immediately rather than failing silently at runtime. It reads better too: `$greeter->greet(...)` says "the `greet` method, as a value," which is exactly what's happening, without a string that happens to be a method name.

## `Closure::fromCallable()`

Sometimes you're handed something callable (a string, an array pair) from outside your control (a configuration value, perhaps) and want it as a real `Closure` object so you can call methods like `bindTo()` on it. `Closure::fromCallable()` converts any of PHP's callable shapes into one:

```php
<?php

$callableFromConfig = 'strtoupper';

$closure = Closure::fromCallable($callableFromConfig);

echo $closure('hello'), "\n"; // HELLO
```

In new code, first-class callable syntax replaces most of the reasons you'd reach for this directly, but you'll still see `Closure::fromCallable()` in library code that has to accept a callable in any of its traditional forms and normalize it.

## Static closures

By default, a closure defined inside a method silently captures `$this`, letting it call back into the surrounding object. Occasionally you want the opposite guarantee: a closure that *cannot* touch the object it was defined in, because it's going to be handed off somewhere else and you want it to stay self-contained. Mark it `static`:

```php
<?php

class Report
{
    private string $secret = 'internal data';

    public function makeFormatter(): Closure
    {
        return static function (string $line): string {
            return strtoupper($line);
        };
    }
}

$formatter = (new Report())->makeFormatter();

echo $formatter('quarterly summary'), "\n"; // QUARTERLY SUMMARY
```

A `static function` closure behaves exactly like an ordinary one except that `$this` is unavailable inside it: trying to use it is a compile-time error, not a runtime surprise. It's a small guarantee, but a meaningful one: it tells the reader, and PHP itself, that this closure is genuinely standalone, with no hidden dependency on the object that created it.
