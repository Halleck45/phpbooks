# Magic Methods

Put an object inside a string, and PHP has a decision to make. Read a property the class never declared, and it has another. **Magic methods are the hooks PHP looks for in those moments**: specially named methods, always starting with two underscores, that the language calls by itself when a specific situation comes up. You have already met two of them.

## `__construct` and `__destruct`, briefly

`__construct()` has been running under every `new` you have written since Chapter 5. PHP calls it as the object is created, and constructor promotion does its work there. `__destruct()` is the mirror image: PHP calls it when the object is about to disappear, typically when the last variable pointing to it goes out of scope. You will write it rarely. PHP's garbage collector, from [Chapter 4](ch04-03-scope-and-gc.md), frees memory on its own, so `__destruct()` is for the cases where something else must be released promptly, a file handle or a network connection, rather than waiting for the process to end.

## `__toString()`: letting an object act like a string

This is the one you will use most. Define it, and PHP calls it wherever your object lands in a string context: concatenation, interpolation, a bare `echo`.

```php
<?php
declare(strict_types=1);

final class Money
{
    public function __construct(
        private int $cents,
        private string $currency,
    ) {
    }

    public function __toString(): string
    {
        return sprintf('%.2f %s', $this->cents / 100, $this->currency);
    }
}

$price = new Money(4999, 'USD');

echo "Total: {$price}\n";
echo 'Total: ' . $price . "\n";
```

```console
$ php money.php
Total: 49.99 USD
Total: 49.99 USD
```

Neither `echo` names a method. PHP sees `$price` land in a string and calls `__toString()` on its own. **Any class with an obvious textual form (money, a name, an identifier) is a good candidate.** The return type must be `string`; returning anything else is a fatal error.

<img src="images/ch17-magic-buttons.png" alt="An object drawn as a box with three buttons on its side, __toString, __get and __call, and the PHP elephant pressing the __toString button itself as the object is dropped into a line of text" width="520">

> You write what the button does. PHP decides when to press it.

## `__get` and `__set`: dynamic property access

These fire when code reads or writes a property the class does not declare:

```php
<?php
declare(strict_types=1);

final class Config
{
    private array $values = [];

    public function __get(string $name): mixed
    {
        return $this->values[$name] ?? null;
    }

    public function __set(string $name, mixed $value): void
    {
        $this->values[$name] = $value;
    }
}

$config = new Config();
$config->debug = true;

var_dump($config->debug);      // true
var_dump($config->unset_key);  // null
```

`$config->debug = true` looks like an ordinary property write. `Config` has no `$debug` property, so PHP calls `__set('debug', true)` instead, and the value lands in the private `$values` array. Reading `$config->debug` triggers `__get('debug')` the same way. **The object behaves like a bag you can drop anything into.**

Now the cost. Read `$config->debug` at a call site and nothing tells you where the value comes from or whether it exists. Your editor cannot autocomplete it. A static analysis tool like PHPStan, from [Chapter 11](ch11-03-generic-style-code.md), cannot check it the way it checks a declared property. **Every magic accessor trades a little boilerplate for code that humans and tools follow less easily.** Keep them for the cases where the dynamic shape is the whole point, a config bag, a wrapper around external data of unpredictable shape, and declare real properties everywhere else.

## `__call`: intercepting method calls

`__call()` does for methods what `__get` does for properties: it fires when code calls a method the object does not have.

```php
<?php
declare(strict_types=1);

final class Logger
{
    public function __call(string $name, array $arguments): void
    {
        $level = strtoupper($name);
        echo "[{$level}] {$arguments[0]}\n";
    }
}

$logger = new Logger();
$logger->warning('Disk space is low.');
$logger->error('Connection refused.');
```

```console
$ php logger.php
[WARNING] Disk space is low.
[ERROR] Connection refused.
```

`Logger` has no `warning()` and no `error()`. Every call to a missing method lands in `__call()`, with the name as a `string` and the arguments as an `array`, and the method turns the name into a log level. This is a real technique; some libraries build their fluent-looking APIs on it. It also carries the `__get` caveat, doubled: the class definition says nothing about which methods exist or what they accept.

Try it: declare a real `warning()` method on `Logger`. The first call now goes to it, and only `error()` still reaches `__call()`. PHP looks for a declared method first and falls back to magic only when it finds none.

Reach for `__call` when that flexibility is worth the cost. Otherwise, a handful of plainly declared methods serves your reader, and your tools, better.
