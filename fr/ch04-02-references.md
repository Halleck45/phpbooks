# Passage par valeur et passage par référence

Copiez une variable, modifiez la copie, et l'original ne bouge pas. C'est le comportement par défaut de PHP, et il a un nom : **le passage par valeur**. C'est ce qui se passe partout en PHP tant que vous ne demandez pas autre chose. Cette section explique comment demander autre chose, et s'arrête sur le seul endroit où PHP vous donne autre chose sans que vous l'ayez demandé : les objets.

## Les références explicites avec `&`

Placez `&` devant une variable au moment de l'affecter, et les deux noms n'en font plus qu'un :

```php
<?php

$a = 10;
$b = &$a; // $b is now an alias for $a, not a copy of its value

$b = 20;

echo $a; // 20
```

Après `$b = &$a`, `$a` et `$b` ne sont pas deux variables contenant des valeurs égales. **Ce sont deux étiquettes collées sur la même boîte.** Changez la valeur par l'une ou l'autre étiquette, et vous l'avez changée pour les deux, puisqu'il n'y a jamais eu qu'une seule boîte.

<img src="images/ch04-two-labels.png" alt="Une seule boîte contenant la valeur 20, avec deux étiquettes collées dessus, $a et $b : une référence est un second nom pour le même emplacement" width="340">

> Une référence, c'est une deuxième étiquette sur la même boîte.

Le même `&` fonctionne sur un paramètre de fonction :

```php
<?php
declare(strict_types=1);

function addTax(array &$prices): void
{
    foreach ($prices as $key => $price) {
        $prices[$key] = round($price * 1.2, 2);
    }
}

$cart = ["book" => 10.00, "pen" => 2.00];
addTax($cart);

var_dump($cart); // book => 12.00, pen => 2.40, modified in place
```

Comparez avec le `addTax()` de la [section précédente](ch04-01-copy-on-write.md) : même corps, mais le `&` devant `$prices` change tout pour l'appelant. Sans lui, la fonction recevait une valeur qu'elle pouvait modifier sans conséquence. Avec lui, `$prices` à l'intérieur de la fonction *est* `$cart` à l'extérieur : pas de copie du tout, pas même paresseuse. **Un paramètre par référence permet à une fonction de modifier sur place la variable de l'appelant.** C'est exactement ainsi que travaille `sort()`, une vraie fonction native, qui réordonne votre tableau à travers une référence au lieu de vous en rendre un nouveau.

> [!WARNING]
> Le `&` se prête à l'abus. Une fonction dont la signature en porte un change discrètement son contrat, de « donne-moi des données, je t'en rends » à « laisse-moi entrer dans ta variable et la modifier », et c'est une promesse plus lourde qu'elle n'en a l'air. Réservez-le aux cas où la modification sur place est tout l'intérêt (trier, remplir un tampon) et renvoyez une valeur partout ailleurs. Le code qui renvoie son résultat se lit et se teste seul. Le code parsemé de paramètres `&` envoie le lecteur vérifier chaque appel pour savoir ce qui a pu changer.

## Les tableaux se copient, les objets non

Voici la surprise vers laquelle tout le chapitre avançait. Lisez-la lentement : elle piège presque tout le monde la première fois.

Vous savez que les tableaux se copient. Les objets, non. Affectez un objet à une variable, passez-le à une fonction, rangez-le dans un tableau : PHP ne duplique jamais l'objet lui-même. **Chaque variable qui « tient » un objet tient en réalité une poignée vers l'unique exemplaire qui vit en mémoire.** Copiez la variable tant que vous voulez, vous copiez la poignée, pas ce qu'il y a au bout.

```php
<?php
declare(strict_types=1);

class Cart
{
    public array $items = [];
}

$cartA = new Cart();
$cartA->items[] = "book";

$cartB = $cartA; // NOT a copy, $cartB points at the same Cart instance
$cartB->items[] = "pen";

var_dump($cartA->items); // ["book", "pen"], both items show up here too
var_dump($cartB->items); // ["book", "pen"]
```

Si `class` et `new` sont nouveaux pour vous, le [chapitre 5](ch05-00-classes.md) les explique posément. Pour l'instant, lisez `new Cart()` comme « fabrique un panier » et `->items` comme « sa liste d'articles ».

`$cartB = $cartA` ressemble trait pour trait au `$copy = $original` des tableaux. Il ne se comporte pas du tout pareil. Il n'y a qu'un seul `Cart` ici, et `$cartA` et `$cartB` sont deux étiquettes dessus. Ajoutez un stylo par l'une ou l'autre, et l'autre le voit aussitôt, parce qu'il n'y a rien d'autre à voir.

<img src="images/ch04-arrays-copy-objects-alias.png" alt="Côte à côte : deux variables de tableau sont deux boîtes séparées au même contenu, tandis que deux variables d'objet sont deux étiquettes nouées au même caddie" width="600">

C'est la cause la plus fréquente des « pourquoi ma fonction a-t-elle modifié quelque chose qu'elle n'était pas censée toucher » dans le code PHP des débutants, et elle joue dans le sens inverse de la confusion sur les tableaux. On s'attend à ce que les objets se copient comme les tableaux, on se brûle une fois, puis on surcorrige en supposant que tout se partage comme les objets. Aucune des deux hypothèses n'est bonne.

> Les tableaux se copient, les objets se partagent.

Passer un objet à une fonction ne protège jamais les données de l'appelant comme le fait un tableau. La fonction reçoit une poignée vers le même exemplaire, et tout ce qu'elle fait à travers cette poignée est visible dès qu'elle rend la main, sans `&` :

```php
<?php
declare(strict_types=1);

function addItem(Cart $cart, string $item): void
{
    $cart->items[] = $item; // this mutates the caller's actual Cart
}

$cart = new Cart();
addItem($cart, "notebook");

var_dump($cart->items); // ["notebook"], visible outside the function, no & needed
```

Pas de `&` dans `addItem()`, et pas besoin. Les objets sont toujours « passés par poignée ». Vous entendrez dire « passés par référence », ce qui est proche mais pas le terme exact en PHP : à l'intérieur de la fonction, vous pouvez toujours réaffecter `$cart` à un autre objet sans toucher la variable de l'appelant. Essayez : mettez `$cart = new Cart();` en première ligne de `addItem()`. Le carnet part dans un panier que personne d'autre ne tient, et le `$cart->items` de l'appelant reste vide. Ce que vous ne pouvez pas faire, c'est modifier l'objet au bout de la poignée sans que la modification apparaisse partout où cet objet est tenu.

## `clone`, la porte de sortie

Parfois, vous voulez bel et bien un second `Cart` indépendant, qui démarre avec les mêmes articles puis suit son propre chemin. C'est le rôle de `clone` :

```php
<?php
declare(strict_types=1);

$cartA = new Cart();
$cartA->items[] = "book";

$cartB = clone $cartA; // a genuine, separate copy
$cartB->items[] = "pen";

var_dump($cartA->items); // ["book"], untouched
var_dump($cartB->items); // ["book", "pen"]
```

**`clone` crée un nouvel objet avec les mêmes valeurs de propriétés, et à partir de là les deux sont pleinement indépendants**, le comportement que vous auriez pu attendre d'une simple affectation. Une réserve, à noter dès maintenant : `clone` copie sur un seul niveau. Si l'une des propriétés de `Cart` était elle-même un objet plutôt qu'un simple tableau, le clone et l'original partageraient encore cet objet imbriqué, poignée comprise, à moins d'y remédier. PHP donne aux classes une méthode `__clone()` exactement pour ça, et le livre y revient une fois que vous aurez passé plus de temps avec les classes, à partir du [chapitre 5](ch05-00-classes.md).
