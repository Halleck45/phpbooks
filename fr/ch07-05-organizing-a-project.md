# Organiser un projet en plusieurs fichiers

Vous savez déclarer un espace de noms et importer depuis un autre. Ce qui manque encore, c'est le lien entre les espaces de noms et le système de fichiers : pour l'instant, rien ne dit à PHP que `App\Models\Product` vit dans un fichier plutôt qu'un autre. Vous pourriez le mettre n'importe où. Vous ne devriez pas, et l'organisation décrite ici est ce qui rend « n'importe où » définitivement moins tentant.

## Une classe, un fichier

**Une classe, interface, trait ou énumération par fichier, et le fichier porte son nom, à l'identique, casse comprise.** `Product` vit dans `Product.php`. Pas `product.php`, pas `models.php` avec trois classes entassées dedans. Le langage n'impose rien de tel. L'écosystème suit cette convention de si près que la contourner déroutera la prochaine personne qui ouvrira votre projet.

Ça paraît contraignant après des scripts où tout tenait dans un seul fichier. Ça se rentabilise dès qu'un projet dépasse une poignée de classes : vous retrouvez n'importe quelle classe à partir de son seul nom, sans grep.

## Un dossier qui reflète l'espace de noms

Seconde moitié de la convention : **l'arborescence des dossiers reflète celle des espaces de noms.** Un petit projet peut ressembler à ceci :

```console
$ find src -type f
src/Models/Product.php
src/Models/Category.php
src/Services/Cart.php
src/Services/PricingCalculator.php
```

<img src="images/ch07-mirror-tree.png" alt="L'arborescence du dossier src/ et celle de l'espace de noms App dessinées côte à côte comme dans un miroir : src/Models/Product.php reflète App\Models\Product, src/Services/Cart.php reflète App\Services\Cart" width="600">

Et l'espace de noms dans chaque fichier correspond à son chemin sous `src/` :

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

`App\Models\Product` se trouve dans `src/Models/Product.php`. `App\Services\Cart` se trouve dans `src/Services/Cart.php`. Remarquez que le préfixe `App` n'a pas de dossier `App` : il désigne `src/` dans son ensemble. C'est une correspondance unique, déclarée une seule fois, et c'est le sujet de la section suivante.

## Assembler le tout depuis un point d'entrée

Avec cette organisation en place, un script d'entrée (disons `public/index.php`, ou une commande ponctuelle que vous lancez avec `php run.php`) importe ce dont il a besoin et passe à l'action :

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

Pas un seul `require` pour `Product.php` ou `Cart.php`, rien que `vendor/autoload.php`, la ligne venue de [Hello, Composer!](ch07-01-hello-composer.md). Ce n'est pas une coïncidence, et ce n'est pas de la magie non plus. Ça fonctionne grâce à un petit bloc de configuration qui relie le préfixe `App\` au dossier `src/`. Ce bloc, c'est PSR-4, et une fois qu'il est en place ce script affiche `74`.
