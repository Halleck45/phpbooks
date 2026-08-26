# Referring to Code with the `use` Keyword

Writing `\App\Models\Product` every single time you need a `Product` gets old fast, and it clutters up code that should be about your business logic, not about where files live. The `use` keyword lets you import a name once, at the top of a file, and then refer to it by its short name for the rest of that file.

## Basic imports

```php
<?php

declare(strict_types=1);

namespace App\Services;

use App\Models\Product;

function makeProduct(string $name, float $price): Product
{
    return new Product($name, $price);
}
```

One `use` statement, and `Product` means `App\Models\Product` for the rest of the file: no backslash, no full path, no ambiguity. `use` statements go directly under the `namespace` declaration, before anything else in the file. This is purely a per-file convenience: importing a class in one file has no effect on any other file, which also means you need the same `use` line again in every file that needs it. That repetition is normal, not a sign you're doing something wrong.

## Aliasing with `as`

Sometimes the short name is already taken: you're using two different packages that both happen to export something called `Collection`, or you want a locally clearer name than the one a library chose. `use ... as` renames the import for the current file only:

```php
<?php

declare(strict_types=1);

namespace App\Services;

use App\Models\Product;
use App\Models\Product as ProductModel;
use Vendor\Ecommerce\Product as ExternalProduct;

function convert(ExternalProduct $external): ProductModel
{
    return new ProductModel($external->title, $external->cost);
}
```

The alias only exists inside this file. `App\Models\Product` and `Vendor\Ecommerce\Product` haven't changed names anywhere else in the project; you've just given yourself two clearly distinct local labels to work with in the one place that needed to talk about both at once.

## Importing several names at once

When a file leans heavily on one namespace, you can group the imports instead of repeating the prefix on every line:

```php
<?php

declare(strict_types=1);

namespace App\Services;

use App\Models\{Product, Category, Warehouse};
```

This is equivalent to three separate `use` statements. It's a matter of taste: some teams like the compactness, others find one-import-per-line easier to scan in a diff. Either is fine; pick one and be consistent within a project.

## Importing functions and constants

`use` isn't only for classes. If you've namespaced a helper function or a constant (as mentioned in the previous section, this is rarer than namespacing classes, but it happens), you import them with `use function` and `use const`:

```php
<?php

declare(strict_types=1);

namespace App\Services;

use function App\Helpers\slugify;
use const App\Helpers\DEFAULT_LOCALE;

$slug = slugify('Hello, Composer!');
```

You already saw this exact form back in [Chapter 1](ch01-03-hello-composer.md), with `use function Termwind\render;`; at the time it probably looked like a small piece of magic. It's the same mechanism as everything else in this section: an import, scoped to one file, that lets you write a short name instead of a long, fully qualified one.

## What you're actually buying

None of this changes what any class, function, or constant *is*: a `use` statement is bookkeeping, not behavior. What it buys you is code that reads the way you think about it: `new Product(...)` instead of `new \App\Models\Product(...)`, everywhere it matters, with the one line at the top of the file doing all the work of disambiguation. Combined with the namespace declarations from the previous section, you now have everything you need to write code that won't collide with anyone else's. The next question is how to spread that code across files and folders sensibly, which is where we're headed.
