# Un programme d'exemple avec des classes

Le meilleur moyen de voir ce qu'une classe apporte, c'est d'écrire deux fois le même petit problème, une fois avec un tableau, une fois avec une classe, et de regarder où la première version casse.

## Le problème, avec un tableau

Vous démarrez une boutique. Chaque produit a un nom, un prix et une quantité dans le panier, et il vous faut le total de la ligne. La version à base de tableau a l'air parfaitement raisonnable :

```php
<?php
declare(strict_types=1);

function lineTotal(array $product): float
{
    return $product['price'] * $product['quantity'];
}

$item = [
    'name' => 'Coffee mug',
    'price' => 8.50,
    'quantity' => 3,
];

echo lineTotal($item); // 25.5
```

Ça marche, jusqu'au jour où ça ne marche plus. Rien n'empêche une faute de frappe :

```php
<?php

$item = [
    'name' => 'Coffee mug',
    'prise' => 8.50, // typo, silently different key
    'quantity' => 3,
];

echo lineTotal($item); // Warning: Undefined array key "price"
```

**L'avertissement se déclenche au fond de `lineTotal()`, loin de l'endroit où l'erreur a été commise.** Rien dans `$item` ne disait quelles clés il devait contenir, et rien n'a vérifié que `price` était un nombre avant l'instant de la multiplication. Laissez la boutique grandir (remises, taux de TVA, niveaux de stock) et chaque fonction qui touche un tableau produit doit s'accorder, de son côté, sur les mêmes clés magiques. Chacune est à une faute de frappe d'échouer à l'exécution, loin du vrai bug.

## Le même problème, avec une classe

```php
<?php
declare(strict_types=1);

class Product
{
    public string $name;
    public float $price;
    public int $quantity;

    public function __construct(string $name, float $price, int $quantity)
    {
        $this->name = $name;
        $this->price = $price;
        $this->quantity = $quantity;
    }

    public function totalPrice(): float
    {
        return $this->price * $this->quantity;
    }
}
```

**`Product` nomme sa forme une fois, à un seul endroit.** Il ne reste rien à mal orthographier : `new Product(...)` exige exactement un nom, un prix et une quantité, dans cet ordre, chacun avec un type déclaré. Trompez-vous de type et, avec `strict_types` activé, PHP vous arrête sur-le-champ au lieu de laisser une chaîne se faire passer pour un prix :

```php
<?php

$mug = new Product('Coffee mug', 8.50, 3);

echo $mug->totalPrice(); // 25.5
```

Essayez : passez `'3'`, entre guillemets, comme quantité, dans un fichier où `strict_types` est activé. PHP refuse avec une `TypeError` avant même que l'objet existe.

<img src="images/ch05-logic-with-data.png" alt="Avant et après : à gauche, une boîte $item pleine d'étiquettes en vrac et une machine lineTotal lointaine reliées par une ficelle effilochée ; à droite, une seule valise Product avec les étiquettes imprimées dessus et une calculatrice totalPrice intégrée à la poignée" width="600">

`totalPrice()` vit maintenant sur `Product`, et non dans une fonction isolée à qui il faut expliquer la forme de son argument. **Quiconque tient un `Product`, n'importe où dans le code, peut appeler `$product->totalPrice()` et obtenir la bonne réponse, parce que la logique voyage avec les données sur lesquelles elle travaille.**

## L'utiliser dans un petit programme

Un panier minuscule, fait de quelques objets `Product` :

```php
<?php
declare(strict_types=1);

$cart = [
    new Product('Coffee mug', 8.50, 3),
    new Product('Notebook', 4.25, 2),
    new Product('Pen', 1.10, 5),
];

$total = 0.0;

foreach ($cart as $product) {
    echo "{$product->name}: \${$product->totalPrice()}\n";
    $total += $product->totalPrice();
}

echo "Total: \${$total}\n";
```

```console
$ php cart.php
Coffee mug: $25.5
Notebook: $8.5
Pen: $5.5
Total: $39.5
```

Regardez `$cart` : c'est toujours un tableau ordinaire. **Les classes ne remplacent pas les tableaux. Elles remplacent ce que vous seriez sinon forcé d'y entasser.** Ici, le tableau fait ce pour quoi il est bon, tenir une liste ordonnée de choses, et chaque chose est un `Product` qui connaît sa propre forme et sa propre arithmétique.

> Des tableaux pour les collections, des classes pour ce qu'elles collectionnent. Vous utiliserez ce duo jusqu'à la fin du livre.
