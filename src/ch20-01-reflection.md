# Magic Constants and Reflection

Most of the time, your code knows exactly what it is: you wrote it, you know the class name, the method name, the file it lives in. But sometimes code needs to ask itself questions at runtime: "what class am I currently in?", "what methods does this object have?", usually for logging, debugging, or building generic tools that operate on classes they've never seen before. PHP gives you two very different tools for that: a handful of constants that answer simple questions cheaply, and Reflection, a full API for interrogating your code's structure in detail.

## Magic constants

PHP defines several constants that expand, at compile time, to information about *where* they appear in your source. They're called "magic" because their value depends entirely on context: the same `__LINE__` means something different in every file:

```php
<?php

class Logger
{
    public function warn(string $message): void
    {
        echo __CLASS__ . '::' . __FUNCTION__ . " at line " . __LINE__ . ": {$message}\n";
    }
}

(new Logger())->warn('Disk space low');
```

```console
$ php logger.php
Logger::warn at line 7: Disk space low
```

`__CLASS__` gives you the current class name, `__FUNCTION__` the current function or method name (`__METHOD__` gives you both, as `Class::method`), `__LINE__` the current line number, and `__FILE__` the full path of the current file. None of them do anything clever, they're just filled in by the parser before your code runs, but that makes them cheap, reliable, and exactly what you want for log lines and debug output where you need to know where a message came from without hardcoding it.

## Reflection

Magic constants tell code about *itself*. Reflection lets code inspect *other* code: classes, methods, properties, parameters, even attributes (which you'll meet later in this chapter), as data you can query at runtime, rather than something only visible while reading source.

```php
<?php

class UserRepository
{
    public function find(int $id): ?string
    {
        return "User #{$id}";
    }

    public function save(string $name): void
    {
        // ...
    }

    private function connect(): void
    {
        // ...
    }
}

$reflection = new ReflectionClass(UserRepository::class);

foreach ($reflection->getMethods(ReflectionMethod::IS_PUBLIC) as $method) {
    echo $method->getName() . "\n";
}
```

```console
$ php reflect.php
find
save
```

`ReflectionClass` wraps a class and exposes everything about its shape: `getMethods()`, `getProperties()`, `getConstructor()`, and more, each returning further reflection objects (`ReflectionMethod`, `ReflectionProperty`) you can query in turn: a method's parameters, their types, whether a property is `readonly`, and so on. Passing `ReflectionMethod::IS_PUBLIC` above filters out `connect()`, PHP's private helper method, leaving just the public interface.

## Where you'll actually meet this

Be honest with yourself about how often you'll write code like the example above: rarely. What Reflection is *for*, in practice, is enabling other tools to work generically. A dependency injection container uses Reflection to look at a constructor's parameters and figure out what to pass in. PHPUnit uses it to find your test methods. Laravel and Symfony lean on it constantly under the hood. You'll use Reflection indirectly, through frameworks and libraries, far more often than you'll call `new ReflectionClass(...)` yourself, but knowing it's there, and roughly how it works, makes the "magic" those tools perform a lot less mysterious.
