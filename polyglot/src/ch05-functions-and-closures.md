# Functions and Closures

**PHP functions look like TypeScript's with a `$` on every parameter, and closures capture by value, not by variable.** That second half is where the surprises live. The first half you can read at speed.

```php
<?php
declare(strict_types=1);

function greet(string $name, string $greeting = 'Hello', bool $shout = false): string
{
    $text = "$greeting, $name!";
    return $shout ? strtoupper($text) : $text;
}

echo greet('Ada');                       // Hello, Ada!
echo greet('Ada', shout: true);          // HELLO, ADA!
echo greet(greeting: 'Hi', name: 'Ada'); // Hi, Ada!
```

Parameters and return values carry types, checked at runtime as [Types](ch03-types.md) explained. Defaults work as everywhere. **Named arguments (PHP 8.0) let you skip the defaults you do not care about** and make a call with four booleans readable. Positional and named can mix, positional first.

## Variadics, references, and the odd return types

`...` on the last parameter collects the rest into an array; `...` in a call unpacks an array into arguments, string keys included, which turns an array into named arguments:

```php
<?php
declare(strict_types=1);

function sum(int ...$numbers): int
{
    return array_sum($numbers);
}

echo sum(1, 2, 3);        // 6
echo sum(...[4, 5]);      // 9

$options = ['greeting' => 'Hey', 'name' => 'Ada'];
// greet(...$options) would call greet(name: 'Ada', greeting: 'Hey')
```

A parameter declared `&$x` receives a reference: the function writes into the caller's variable. The standard library uses it for `sort()`, `preg_match()`'s `$matches` and a few others. In your own code, prefer returning the value. A function that changes its arguments is one your reader has to open to understand.

Parameter types take everything the type system offers: `?string $label = null` for an optional value, `int|string $id` for a union, `Countable&Traversable $items` for an intersection. Write the `?` explicitly; a plain `string $x = null` still works but has been deprecated since PHP 8.4. For a function that accepts a function, two declarations exist: `callable` accepts closures and also the string and array forms below, `Closure` accepts only real closure objects. New code tends to declare `Closure` and let callers convert with `(...)`, because a `Closure` can be type-checked and a string cannot.

Two return types describe functions that do not return normally. `void` means nothing comes back. `never` (PHP 8.1) means the function always throws or exits, so static analysers know that code after a `fail()` call is unreachable.

## Functions are not values, but you can grab a handle

A function name is not an expression. `$f = strlen;` is a syntax error, and the historical workaround was a string: `$f = 'strlen';` works because the `callable` type accepts a function name, a `[$object, 'method']` pair, or a `'Class::method'` string. That works, and nothing checks it until it runs.

**The modern way is the first-class callable syntax (PHP 8.1): the name followed by `(...)`.**

```php
<?php
declare(strict_types=1);

final class Mailer
{
    public function send(string $to): string
    {
        return "sent to $to";
    }
}

$length = strlen(...);                   // Closure wrapping strlen()
$send = (new Mailer())->send(...);       // Closure bound to that instance

echo $length('hello'); // 5
echo $send('ada@example.org');

var_dump(array_map(strtoupper(...), ['a', 'b'])); // ['A', 'B']
```

The result is a `Closure` object, PHP's only function value. It is type-safe, refactor-safe (rename the method and your editor follows), and it is what to pass to `array_map()` and friends. `Closure::fromCallable('strlen')` does the same from a string when you have one.

> A polyglot's reflex is `$this->send` without parentheses. In PHP that reads the property `send`, which does not exist. The method as a value is `$this->send(...)`.

## Closures capture by value

Anonymous functions exist, and you have to say what they capture:

```php
<?php
declare(strict_types=1);

$rate = 0.2;

$withTax = function (float $price) use ($rate): float {
    return $price * (1 + $rate);
};

$rate = 0.5; // too late, the closure already copied 0.2

echo $withTax(100.0); // 120
```

**The `use` clause copies the variables at the moment the closure is created.** Nothing in the enclosing scope is visible unless listed, and later changes to the outer variable do not reach the closure. JavaScript and Python close over the variable itself and would print 150 here. PHP hands the closure a snapshot.

<img src="images/ch05-closure-snapshot.png" alt="A closure being created takes a photograph of the variable rate showing 0.2; afterwards the outer rate is changed to 0.5 on the desk, but the closure still holds the photo reading 0.2" width="560">

To capture the variable rather than its value, add `&`: `use (&$rate)`. Now the closure and the outer scope share it, in both directions. The usual need for it is an accumulator, or a recursive closure that must see itself:

```php
$fact = function (int $n) use (&$fact): int {
    return $n <= 1 ? 1 : $n * $fact($n - 1);
};
```

Arrow functions (PHP 7.4) drop the ceremony. **`fn` captures the whole enclosing scope automatically, by value, and holds a single expression:**

```php
$withTax = fn(float $price): float => $price * (1 + $rate);
```

No `use`, no `return`, no braces, and the same snapshot semantics. Most callbacks you write will be arrow functions. Reach for `function () use ()` when you need statements, or a by-reference capture.

Inside a class, a closure keeps `$this` automatically, which is what you expect. Mark it `static fn` or `static function` when it does not need the instance; that avoids holding the object alive from inside a long-lived callback. `Closure::bind()` and `$closure->call($object)` rebind `$this` to another object, and are how frameworks reach private state from outside. You will rarely write them yourself.

## Generators

A function containing `yield` returns a `Generator` without running its body. Each `foreach` step runs it to the next `yield`. This is Python's generator, nearly line for line:

```php
<?php
declare(strict_types=1);

/** @return Generator<int, string> */
function lines(string $path): Generator
{
    $handle = fopen($path, 'r');
    try {
        while (($line = fgets($handle)) !== false) {
            yield rtrim($line, "\n");
        }
    } finally {
        fclose($handle);
    }
}

foreach (lines('/etc/hosts') as $number => $line) {
    echo "$number: $line", PHP_EOL;
}
```

The file is read one line at a time, however large it is, and closed when the loop ends or breaks. **A generator is `iterable`, so any function accepting `iterable` takes it without knowing.** `yield $key => $value` sets explicit keys, `yield from` delegates to another generator or array, and a `return` inside a generator sets a value readable through `getReturn()` once iteration is over. Generators run once; to iterate again, call the function again.

## Pipelines

PHP 8.5 adds the pipe operator. **`$x |> f(...)` calls `f($x)`, and chains read top to bottom instead of inside out:**

```php
// PHP 8.5
$slug = ' Hello World '
    |> trim(...)
    |> strtolower(...)
    |> (fn(string $s) => str_replace(' ', '-', $s));

echo $slug; // hello-world
```

Each stage is any callable taking one argument, which is exactly what the first-class callable syntax and arrow functions produce. Before 8.5 the same code is three nested calls or three temporary variables; both still work, and both are still common.

PHP 8.5 also brings `#[\NoDiscard]`, an attribute for functions whose return value must not be dropped. Call such a function as a bare statement and PHP emits a warning; cast the call to `(void)` to say you meant it. Libraries use it on methods returning a new immutable object, the classic `$date->modify()` bug where the result is thrown away.

## Legacy shapes you will recognise

`func_get_args()` and `func_num_args()` read the arguments of a function declared without parameters. They predate `...$args` and survive in old code. `call_user_func()` and `call_user_func_array()` invoke a callable; `$callable(...$args)` does the same today. `create_function()` built closures from strings and was removed in 8.0. When you meet these, the modern replacement is one line away, and Rector can make the edit for you.

> Closures snapshot their `use` variables, arrow functions snapshot everything, and a method becomes a value with `(...)`. Keep those three straight and PHP callbacks hold no further surprises.

Functions carry behaviour. The data they act on is mostly objects, and PHP's object model has changed more in the last five years than in the fifteen before. [Classes](ch06-classes.md) shows what it looks like now.
