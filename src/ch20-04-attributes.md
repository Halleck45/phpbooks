# Attributes

For years, PHP developers who wanted to attach metadata to a class or method ("this method is a test," "this property maps to a database column," "this route handles `GET /users`") had exactly one tool: a specially formatted comment, a docblock, that some framework would parse at runtime with a regular expression. It worked, but it was always a little uneasy: the metadata lived in a comment, which the language itself didn't understand or check, and a typo in it failed silently.

PHP 8 replaced that convention with a real language feature: **attributes**, written as `#[SomethingLikeThis]` directly above the thing they describe.

## Defining and attaching an attribute

An attribute is just a class, marked with PHP's own `#[Attribute]` attribute so PHP knows it's meant to be used this way:

```php
<?php

#[Attribute]
class Route
{
    public function __construct(
        public readonly string $method,
        public readonly string $path,
    ) {
    }
}
```

Once defined, attach it to a method with the `#[...]` syntax:

```php
<?php

class UserController
{
    #[Route(method: 'GET', path: '/users')]
    public function index(): string
    {
        return 'List of users';
    }

    #[Route(method: 'POST', path: '/users')]
    public function store(): string
    {
        return 'User created';
    }
}
```

At this point, nothing runs differently: `#[Route(...)]` doesn't call anything on its own. It's inert metadata, attached to the method, waiting for something to go looking for it.

## Reading attributes back with Reflection

That "something" is Reflection, from earlier in this chapter. `ReflectionMethod` (and `ReflectionClass`, `ReflectionProperty`) can list the attributes attached to whatever they're reflecting, and construct the actual attribute object on demand:

```php
<?php

$reflection = new ReflectionClass(UserController::class);

foreach ($reflection->getMethods() as $method) {
    foreach ($method->getAttributes(Route::class) as $attribute) {
        $route = $attribute->newInstance();
        echo "{$route->method} {$route->path} -> {$method->getName()}()\n";
    }
}
```

```console
$ php routes.php
GET /users -> index()
POST /users -> store()
```

`getAttributes(Route::class)` finds every `Route` attribute on a method, and `newInstance()` actually constructs it: running the constructor, with the arguments you wrote in `#[Route(...)]`, and handing you back a real `Route` object with `method` and `path` properties. This is genuinely how simple routing systems are built: scan a controller's methods, read off their `Route` attributes, and build a routing table from what you find, all without a separate configuration file to keep in sync.

## Where you've already seen this

If you've read [Chapter 12](ch12-00-testing.md), this pattern should look familiar: PHPUnit's `#[Test]` attribute marks a method as a test case the same way `#[Route]` marks one as a handler here: a plain class, read back through Reflection, driving real behavior. Frameworks lean on attributes constantly now: Symfony uses them for routes and dependency injection configuration, Doctrine uses them to map properties to database columns, and PHPUnit uses them for test metadata generally, not just marking a method as a test. You won't necessarily write many custom attributes of your own day to day, but you'll read `#[...]` above methods and classes constantly in modern PHP code, and now you know exactly what's happening when you do: a plain object, waiting to be read back through Reflection.
