# Defining and Instantiating Classes

A class is a blueprint. It describes what data an object of that type holds and, eventually, what it can do. On its own, though, a class produces nothing. You have to ask PHP to build one, with `new`.

## Defining a class

```php
<?php
declare(strict_types=1);

class Rectangle
{
    public float $width;
    public float $height;
}
```

`class Rectangle { ... }` declares the blueprint. Inside it, `public float $width;` declares a **typed property**: a named slot every `Rectangle` object will have, and a type PHP will enforce whenever something tries to assign to it. This should feel familiar: it's the same type declarations you've been putting on function parameters since [Chapter 3](ch03-02-data-types.md), applied to a piece of data that lives on an object instead of a variable that lives in a function call.

## Instantiating a class

`new` creates an actual object, an **instance**, from the blueprint:

```php
<?php

$rect = new Rectangle();
$rect->width = 10.0;
$rect->height = 4.0;

echo $rect->width;  // 10
echo $rect->height; // 4
```

`new Rectangle()` gives you a real `Rectangle` object, with its own independent `$width` and `$height`, and assigns it to `$rect`. The `->` operator reaches into an object to read or write one of its properties: think of it as the object equivalent of `[]` on an array, though we'll see shortly that objects are usually better behaved about what you're allowed to put in there. Create a second `Rectangle`, and it's a genuinely separate object, with its own storage:

```php
<?php

$rect2 = new Rectangle();
$rect2->width = 3.0;
$rect2->height = 3.0;

echo $rect->width;  // 10, untouched by $rect2
echo $rect2->width; // 3
```

This is worth pausing on, given what [Chapter 4](ch04-02-references.md) taught you about objects sharing handles: `$rect` and `$rect2` aren't two names for the same object; they're two separate `new` calls, producing two separate instances. The "objects alias, not copy" rule from Chapter 4 is about what happens when you *assign an existing object to another variable* (`$a = $b`), not about what happens every time you write `new`. Each `new` genuinely builds a fresh object.

## Constructing with `__construct`

Setting each property by hand after `new`, as above, works, but it's easy to forget one, and there's a window where a half-built `Rectangle` exists with some properties still unset. PHP lets you define a special method, `__construct()`, that runs automatically the moment an object is created, so you can guarantee it's fully and correctly initialized from the start:

```php
<?php
declare(strict_types=1);

class Rectangle
{
    public float $width;
    public float $height;

    public function __construct(float $width, float $height)
    {
        $this->width = $width;
        $this->height = $height;
    }
}

$rect = new Rectangle(10.0, 4.0);

echo $rect->width;  // 10
echo $rect->height; // 4
```

Whatever arguments you pass to `new Rectangle(...)` are handed straight to `__construct()`. Inside it, `$this` refers to the object currently being built: `$this->width = $width` takes the incoming parameter and stores it on the object's own `$width` property. We'll look at `$this` more closely, and at a much shorter way to write exactly this constructor, in [Methods and Constructor Promotion](ch05-03-methods.md).

## Visibility: `public`, `private`, `protected`

Every property and method in PHP has a **visibility**, and so far everything above has been `public`: reachable from anywhere, including code entirely outside the class. That's often not what you want. Mark a property `private`, and only code inside the class itself can read or write it:

```php
<?php
declare(strict_types=1);

class Rectangle
{
    private float $width;
    private float $height;

    public function __construct(float $width, float $height)
    {
        $this->width = $width;
        $this->height = $height;
    }
}

$rect = new Rectangle(10.0, 4.0);
echo $rect->width; // Error: Cannot access private property Rectangle::$width
```

This is a deliberate restriction, not a bug to work around. Once `$width` is private, the *only* way anything outside `Rectangle` can learn or change it is through methods `Rectangle` itself chooses to expose, which means `Rectangle` gets to enforce its own rules about what a valid width even looks like, rather than trusting every caller everywhere to behave. `protected` sits in between: invisible from outside the class, but visible to any class that later extends it, a distinction that matters once we reach inheritance in [Chapter 15](ch15-00-object-oriented-php.md). For now, a reasonable default: reach for `private` unless you have a specific reason a property needs to be `public`, and expose access through methods when outside code genuinely needs it.
