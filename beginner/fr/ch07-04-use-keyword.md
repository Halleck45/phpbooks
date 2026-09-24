# Désigner du code avec le mot-clé `use`

Écrire `\App\Models\Product` chaque fois que vous avez besoin d'un `Product` lasse vite, et noie votre logique sous des chemins de fichiers. **Le mot-clé `use` importe un nom une seule fois, en tête de fichier, et le nom court fonctionne ensuite jusqu'à la fin de ce fichier.**

## Imports de base

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

Une ligne `use`, et `Product` signifie `App\Models\Product` jusqu'à la fin du fichier. Pas de barre oblique inverse, pas de chemin complet, pas d'ambiguïté. Les instructions `use` se placent juste sous la déclaration `namespace`, avant tout le reste.

<img src="images/ch07-use-sticky-note.png" alt="Un fichier source dessiné comme une feuille de papier avec un post-it en haut qui dit Product = App\Models\Product, et le nom court Product utilisé dans le code en dessous" width="520">

Voyez-le comme un post-it collé sur la première page : « quand je dis Product, je veux dire App\Models\Product ». Le post-it ne tient que sur ce fichier. **Importer une classe dans un fichier n'a aucun effet sur les autres fichiers**, si bien que chaque fichier qui a besoin de `Product` répète la même ligne `use`. Cette répétition est normale, ce n'est pas un signe que vous faites quelque chose de travers.

## Renommer avec `as`

Parfois, le nom court est déjà pris. Deux paquets exportent chacun une `Collection`, ou une bibliothèque a choisi un nom qui se lit mal dans votre code. `use ... as` renomme l'import, pour ce fichier seulement :

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

Hors de ce fichier, `App\Models\Product` et `Vendor\Ecommerce\Product` gardent leurs noms. Vous vous êtes simplement donné deux étiquettes locales bien distinctes, au seul endroit qui doit parler des deux à la fois.

## Importer plusieurs noms d'un coup

Quand un fichier s'appuie beaucoup sur un même espace de noms, regroupez les imports au lieu de répéter le préfixe :

```php
<?php

declare(strict_types=1);

namespace App\Services;

use App\Models\{Product, Category, Warehouse};
```

C'est exactement équivalent à trois lignes `use` séparées. Certaines équipes aiment la compacité, d'autres trouvent un import par ligne plus lisible dans un diff. Choisissez, et tenez-vous-y dans un même projet.

## Importer des fonctions et des constantes

`use` ne sert pas qu'aux classes. Une fonction utilitaire ou une constante placée dans un espace de noms (plus rare qu'une classe, la section précédente l'a dit, mais ça arrive) s'importe avec `use function` et `use const` :

```php
<?php

declare(strict_types=1);

namespace App\Services;

use function App\Helpers\slugify;
use const App\Helpers\DEFAULT_LOCALE;

$slug = slugify('Hello, Composer!');
```

Vous avez croisé cette forme au début du chapitre, dans [Hello, Composer!](ch07-01-hello-composer.md) : `use function Termwind\render;`. Elle ressemblait sans doute à un petit tour de magie à ce moment-là. C'est le même mécanisme que tout ce qui figure sur cette page, un import limité à un fichier, pour écrire un nom court à la place d'un nom long.

## Ce que vous y gagnez vraiment

Une instruction `use` est de la tenue de registre, pas du comportement. Rien ne change dans la classe, la fonction ou la constante concernée. Ce que vous obtenez, c'est du code qui se lit comme vous pensez : `new Product(...)` plutôt que `new \App\Models\Product(...)`, avec une ligne en tête de fichier qui porte toute la désambiguïsation. Avec `namespace`, vous avez maintenant tout ce qu'il faut pour écrire du code qui n'entre en collision avec celui de personne. Reste à le répartir entre fichiers et dossiers de manière sensée, et c'est la suite.
