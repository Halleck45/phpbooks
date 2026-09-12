# Magic Methods

<img src="images/ch17-icon.svg" alt="Magic Methods illustration" width="72">

PHP calls a small set of specially named methods automatically, in response to specific situations, rather than waiting for you to call them by name: using an object in a string, reading a property that doesn't exist, calling a method that isn't there. These are magic methods, always prefixed with a double underscore, and you've already met the first two.

## `__construct` and `__destruct`, briefly

`__construct()` has been running quietly under every `new` you've written since Chapter 5: it's the method PHP calls automatically when an object is created, and it's where constructor promotion does its work. `__destruct()` is its counterpart: PHP calls it automatically when an object is about to be destroyed, typically when the last variable referencing it goes out of scope. You'll see it far less often; most PHP objects don't need cleanup logic, since PHP's garbage collector, covered in [Chapter 4](ch04-03-scope-and-gc.md), handles memory on its own. `__destruct()` earns its keep mainly for things like closing a file handle or a network connection explicitly, rather than waiting for the process to end.

## `__toString()`: letting an object act like a string

This is the magic method you'll reach for most often. Define it, and PHP will call it automatically anywhere your object is used in a string context: string concatenation, interpolation, a plain `echo`:

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

Neither line calls `format()` or anything else by name; PHP sees `$price` land in a string context and calls `__toString()` on its own. This genuinely earns its place: any class representing something that has an obvious, sensible textual form (money, a name, an identifier) is a good candidate. Note the return type must be `string`; `__toString()` returning anything else is a fatal error.

## `__get` and `__set`: dynamic property access

These fire when code reads or writes a property that isn't declared on the class at all:

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

`$config->debug = true` looks like a normal property write. `Config` has no `$debug` property, so PHP calls `__set('debug', true)` instead, which stores the value in the internal `$values` array. Reading `$config->debug` back triggers `__get('debug')` the same way. This can be a genuinely convenient way to build something that behaves like a flexible bag of properties.

It's also worth being honest about the cost. Code that reads `$config->debug` gives no hint, at the call site, of where that value actually comes from or whether it exists: your editor can't autocomplete it, and a static analysis tool like PHPStan, from [Chapter 11](ch11-03-generic-style-code.md), can't verify it the way it can verify a real declared property. Overuse `__get`/`__set` and you've traded a small amount of boilerplate for code that's harder for both humans and tools to follow. Use them sparingly, for cases where the dynamic behavior is genuinely the point (a config bag, a data-transfer object wrapping an unpredictable external shape), not as a general substitute for declaring real properties.

## `__call`: intercepting method calls

`__call()` is the method equivalent of `__get`/`__set`: it fires when code calls a method that doesn't exist on the object:

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

`Logger` has no `warning()` or `error()` method at all; every call to a missing method lands in `__call()`, with the method name and its arguments handed to you as `string` and `array`. This is a real technique, it's how some libraries build fluent, flexible-looking APIs, but it comes with the same honest caveat as `__get`/`__set`, doubled: nothing about `Logger`'s class definition tells you `warning()` or `error()` exist, or what they accept. Reach for it when the flexibility is worth that cost; otherwise, a handful of ordinary, explicitly declared methods will almost always serve your reader, and your tooling, better.
