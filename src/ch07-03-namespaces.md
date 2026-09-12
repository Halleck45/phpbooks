# Controlling Scope and Visibility with Namespaces

<img src="images/ch07-icon.svg" alt="Controlling Scope and Visibility with Namespaces illustration" width="72">

A namespace is a prefix. That's the whole concept, and it's worth saying plainly before the syntax makes it look more complicated than it is: `App\Models\Product` is just the name `Product`, living inside the namespace `App\Models`, the same way `/home/damien/notes.txt` is just `notes.txt`, living inside `/home/damien`. Nothing about the class itself changes. What changes is how you, and PHP, refer to it unambiguously.

## Declaring a namespace

A namespace declaration is the first statement in a file: before it, only a docblock or `declare(strict_types=1)` is allowed:

```php
<?php

declare(strict_types=1);

namespace App\Models;

class Product
{
    public function __construct(
        public readonly string $name,
        public readonly float $price,
    ) {
    }
}
```

Everything declared in this file (the `Product` class, and any other class, interface, or function you add to it) now lives under `App\Models`. Its full, unambiguous name is `App\Models\Product`. Within this same file, and within any other file that also declares `namespace App\Models;`, you can still refer to it as plain `Product`: PHP resolves unqualified names against the current namespace first.

## Why bother

Here's the scenario this is built for. Say your project uses a third-party library that ships its own `Collection` class: plenty of packages do, it's a natural name for "a bunch of things with some helper methods." You also want a `Collection` class of your own, for a stamp-collecting app, say. Without namespaces, PHP would see two classes both trying to be called `Collection` and refuse to load the second one: a fatal error, and not a subtle one.

With namespaces, there's no conflict at all:

```php
<?php

namespace App\Models;

class Collection
{
    // your Collection, entirely unrelated to anyone else's
}
```

```php
<?php

// Illuminate\Support\Collection, from a package you installed
namespace Illuminate\Support;

class Collection
{
    // their Collection
}
```

Two classes, same short name, no collision: `App\Models\Collection` and `Illuminate\Support\Collection` are simply different identifiers. This is the actual reason namespaces exist. It has nothing to do with "organizing code" in the abstract and everything to do with the fact that your project will, almost immediately, contain code from people you've never met, and none of you coordinated on naming in advance.

## Fully qualified names

You can always refer to a class by its full path, regardless of what namespace you're currently in, by writing it out completely: a *fully qualified name*:

```php
<?php

namespace App\Services;

function makeProduct(): \App\Models\Product
{
    return new \App\Models\Product('Keyboard', 49.00);
}
```

Notice the leading backslash. Inside a namespace, an unqualified name like `Product` is resolved relative to the current namespace: PHP would look for `App\Services\Product`, which doesn't exist. A leading `\` says "start from the very top, the global namespace"; it's the same trick you need for PHP's own built-in classes when you're inside a namespace:

```php
<?php

namespace App\Services;

function now(): \DateTimeImmutable
{
    return new \DateTimeImmutable();
}
```

`DateTimeImmutable` isn't namespaced; it lives in the global namespace, same as `Exception`, `ArrayObject`, and every other built-in class. Once your file declares its own namespace, you need that leading backslash to reach them, or the `use` keyword to import them once and skip the backslash everywhere else, which is exactly where we're headed next.

## A note on functions and constants

Namespaces apply to functions and constants too, not just classes: `namespace App\Helpers;` followed by `function slugify(string $s): string { ... }` gives you `App\Helpers\slugify()`. In practice this comes up less often than you'd expect: PHP falls back to the global namespace automatically for unqualified function and constant names if no namespaced version exists, which is why you can keep calling `strlen()` and `array_map()` from inside a namespaced file without a second thought. Classes get no such fallback: get the namespace wrong for a class and PHP simply won't find it.
