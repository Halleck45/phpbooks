# Organizing a Multi-File Project

You now know how to declare a namespace and how to import from one. What's still missing is the connection between namespaces and the filesystem, because so far, PHP has no idea that `App\Models\Product` is supposed to live in any particular file at all. You could technically put it anywhere. You shouldn't, and in this section we'll set up the layout that makes "anywhere" stop being an option worth considering.

## One class, one file

The convention (not a language rule, but one followed closely enough across the PHP ecosystem that deviating from it will confuse the next person who opens your project) is one class, interface, trait, or enum per file, and the file name matches the class name exactly, including case. `Product` lives in `Product.php`. Not `product.php`, not `models.php` with three classes crammed into it.

This feels restrictive coming from scripts where everything lived in one file, but it pays for itself the moment a project has more than a handful of classes: you can find any class by its name alone, without grepping.

## A folder that mirrors the namespace

The second half of the convention is that your folder structure mirrors your namespace structure. A small project might look like this:

```console
$ find src -type f
src/Models/Product.php
src/Models/Category.php
src/Services/Cart.php
src/Services/PricingCalculator.php
```

And the namespace inside each file matches its path under `src/`:

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

```php
<?php

declare(strict_types=1);

namespace App\Models;

class Category
{
    public function __construct(
        public readonly string $name,
    ) {
    }
}
```

```php
<?php

declare(strict_types=1);

namespace App\Services;

use App\Models\Product;

class Cart
{
    /** @var Product[] */
    private array $items = [];

    public function add(Product $product): void
    {
        $this->items[] = $product;
    }

    public function total(): float
    {
        return array_sum(array_map(
            fn (Product $product) => $product->price,
            $this->items,
        ));
    }
}
```

`App\Models\Product` sits at `src/Models/Product.php`. `App\Services\Cart` sits at `src/Services/Cart.php`. The `App` prefix itself doesn't correspond to a folder named `App`: it corresponds to `src/` as a whole, a mapping you declare once, which is the subject of the next section.

## Putting it together from an entry point

With that layout in place, a small entry-point script (say `public/index.php`, or a one-off command you run with `php run.php`) just imports what it needs and gets on with it:

```php
<?php

declare(strict_types=1);

require __DIR__ . '/vendor/autoload.php';

use App\Models\Product;
use App\Services\Cart;

$cart = new Cart();
$cart->add(new Product('Keyboard', 49.00));
$cart->add(new Product('Mouse', 25.00));

echo $cart->total() . "\n";
```

No `require` for `Product.php` or `Cart.php` anywhere in sight: just `vendor/autoload.php`, the same line from [Chapter 1](ch01-03-hello-composer.md). That's not a coincidence, and it isn't automatic magic either: it works because of one small block of configuration connecting the `App\` namespace prefix to the `src/` folder, which is exactly what PSR-4 is, and exactly what's next.
