# Méthodes et promotion des propriétés

**Une méthode est une fonction qui vit à l'intérieur d'une classe.** Vous en avez déjà écrit une, `totalPrice()` sur `Product`. Ce qui la distingue d'une fonction ordinaire tient dans une seule variable, `$this`, et une fois ce point clair, la façon la plus courte d'écrire un constructeur en PHP n'est plus qu'à un pas.

## `$this`

**Dans une méthode, `$this` est l'objet sur lequel la méthode a été appelée.** C'est par lui qu'une méthode atteint les données de cette instance précise, et non d'une autre instance de la même classe :

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

    public function applyDiscount(float $percentage): void
    {
        $this->price -= $this->price * ($percentage / 100);
    }
}

$mug = new Product('Coffee mug', 8.50, 3);
$mug->applyDiscount(10);

echo $mug->price; // 7.65
```

`applyDiscount()` ne prend pas le produit en paramètre. Elle n'en a pas besoin : `$this` est déjà le produit sur lequel on l'a appelée. Appelez `$mug->applyDiscount(10)`, et dans la méthode, `$this` est `$mug`. Appelez la même méthode sur un autre `Product`, et `$this` est celui-là.

<img src="images/ch05-this.png" alt="Deux caisses de produits côte à côte, $mug et $pen ; un appel à applyDiscount(10) envoie une flèche marquée $this vers la caisse $mug seulement, dont l'étiquette de prix passe de 8.50 à 7.65, tandis que la caisse $pen reste intacte" width="560">

`$this` est implicite, et toujours disponible dans toute méthode non statique. C'est lui qui garde les méthodes d'un objet en phase avec les données de ce même objet, sans que vous ayez à passer l'objet à chacune de ses propres méthodes.

> Appelez une méthode sur un objet, et `$this` est cet objet. Rien à passer, rien à déclarer.

Essayez : créez un second produit, `$pen = new Product('Pen', 1.10, 5);`, appelez `$mug->applyDiscount(10)`, puis affichez `$pen->price`. Le stylo n'a pas bougé. La remise n'a atteint que l'objet vers lequel `$this` pointait.

## Le constructeur, version longue

Regardez à nouveau le constructeur de `Product`. Trois paramètres en entrée, trois affectations en face, une ligne chacune, aucune logique au-delà de « range ça là où ça va ». **Ce motif est si courant en PHP, et si répétitif, qu'il a gagné son propre raccourci.**

## La promotion des propriétés

Depuis PHP 8, **ajouter un mot-clé de visibilité à un paramètre du constructeur déclare la propriété et l'affecte d'un seul geste :**

```php
<?php
declare(strict_types=1);

class Product
{
    public function __construct(
        public string $name,
        public float $price,
        public int $quantity,
    ) {
    }

    public function totalPrice(): float
    {
        return $this->price * $this->quantity;
    }
}

$mug = new Product('Coffee mug', 8.50, 3);
echo $mug->totalPrice(); // 25.5
```

Mettez cette version à côté de celle du début de la section. Vues de l'extérieur, les deux classes sont identiques : mêmes propriétés, mêmes types, même signature de constructeur. À l'intérieur, la version promue n'a plus de déclarations de propriétés séparées, plus de `$this->name = $name;` répété trois fois, et un corps de constructeur vide. **Écrire `public string $name` en paramètre fait trois choses à la fois : déclarer la propriété, la typer, et y ranger l'argument reçu.**

C'est la façon idiomatique et moderne d'écrire un constructeur dont le seul travail est « garde ce qu'on m'a donné », et cela décrit une bonne part des constructeurs que vous écrirez en PHP. Vous le verrez partout à partir de maintenant.

## Les propriétés `readonly`, en bref

Un mot-clé de plus, parce qu'il va si naturellement avec la promotion. **Marquez une propriété promue `readonly`, et elle ne peut être affectée qu'une fois, à la construction, et plus jamais ensuite :**

```php
<?php
declare(strict_types=1);

class Product
{
    public function __construct(
        public readonly string $name,
        public float $price,
        public int $quantity,
    ) {
    }
}

$mug = new Product('Coffee mug', 8.50, 3);
$mug->name = 'Travel mug'; // Error: Cannot modify readonly property Product::$name
```

Un prix et une quantité sont faits pour changer ; c'est tout l'intérêt de `applyDiscount()`. Le nom d'un produit, lui, a rarement une bonne raison de bouger. `readonly` vous permet de le dire dans la définition même de la classe, et PHP le fait respecter, au lieu que la règle vive dans un commentaire ou une convention que quelqu'un finira par oublier. Il reviendra plus loin dans le livre, quand les enums et les objets-valeurs entreront en scène.
