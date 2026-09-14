# Un flux de contrôle concis avec `match` et `?->`

Certaines valeurs ne sont pas l'un de trois ou quatre cas. Elles sont l'un de deux : quelque chose, ou rien du tout. C'est le dernier ensemble fermé de ce chapitre, et il mérite une syntaxe à lui.

## L'opérateur nullsafe

`null` signifie « aucune valeur ici », comme le disait le [chapitre 3](ch03-02-data-types.md), et `->` va chercher une propriété ou une méthode dans un objet, comme au [chapitre 5](ch05-01-defining-classes.md). Assemblez les deux et vous obtenez une question que tout programme finit par se poser : que se passe-t-il quand on utilise `->` sur quelque chose qui pourrait être `null` ?

```php
<?php
declare(strict_types=1);

class Address
{
    public function __construct(
        public string $city,
    ) {
    }
}

class Customer
{
    public function __construct(
        public string $name,
        public ?Address $address = null,
    ) {
    }
}

$customer = new Customer('Ada');

echo $customer->address->city; // Error: Attempt to read property "city" on null
```

Ada n'a pas d'adresse enregistrée, donc `$customer->address` vaut `null`, et aller un cran plus loin avec `->city` échoue sur place : il n'y a aucune propriété à lire sur rien. La parade classique est une garde avant l'accès :

```php
<?php

$city = null;
if ($customer->address !== null) {
    $city = $customer->address->city;
}

echo $city ?? 'No address on file';
```

Ça fonctionne, et ça ne passe pas à l'échelle. Ajoutez quelques niveaux, `$order->customer->address->city` par exemple, et il faut soit imbriquer une garde par maillon, soit écrire une longue condition qui vérifie trois choses à la fois sans en nommer aucune.

**L'opérateur nullsafe, `?->`, fait la garde à votre place :**

```php
<?php
declare(strict_types=1);

$city = $customer->address?->city;

echo $city ?? 'No address on file';
```

`?->` regarde ce qui se trouve à sa gauche avant d'aller plus loin. Si c'est `null`, l'expression entière devient `null` à cet instant, sans erreur ni exception, prête pour `??` ou pour ce que vous faites d'habitude d'une valeur absente. Si ce n'est pas `null`, `?->` se comporte exactement comme `->`. Dans une chaîne plus longue, `$order?->customer?->address?->city` s'arrête au premier `null` rencontré et donne `null` pour toute l'expression, sans tenter les accès suivants.

<img src="images/ch06-nullsafe-chain.png" alt="Une chaîne de trois maillons, order, customer et address, menant à city ; le maillon address manque et, au lieu de casser, la chaîne rend un simple null" width="600">

> `?->` s'arrête au premier `null` et le rend. Tout ce qui suit est ignoré.

> [!WARNING]
> `?->` est fait pour les valeurs qui ont le droit d'être absentes : une adresse facultative, un enregistrement lié qui n'existe pas encore. Ce n'est pas un moyen d'éviter de décider si `null` a sa place à cet endroit. Semé partout par réflexe, il masque une conception qui n'a jamais tranché ce qui est facultatif. Là où l'absence n'est pas normale, gardez le `->` ordinaire et laissez l'erreur vous prévenir.

## `match`, l'alternative propre à une longue chaîne de `if`/`elseif`

Les énumérations sont le terrain où `match` est le plus à son avantage, mais il n'en a pas besoin. **`match` est la réponse de PHP à toute chaîne de `if`/`elseif` qui compare une valeur à plusieurs possibilités connues.** Voici une chaîne de ce genre :

```php
<?php
declare(strict_types=1);

function shippingCost(string $countryCode): float
{
    if ($countryCode === 'US') {
        return 5.00;
    } elseif ($countryCode === 'CA') {
        return 7.50;
    } elseif ($countryCode === 'FR' || $countryCode === 'DE') {
        return 9.00;
    } else {
        return 15.00;
    }
}
```

La même fonction en `match` :

```php
<?php
declare(strict_types=1);

function shippingCost(string $countryCode): float
{
    return match ($countryCode) {
        'US' => 5.00,
        'CA' => 7.50,
        'FR', 'DE' => 9.00,
        default => 15.00,
    };
}
```

Plus court, oui. Surtout, chaque branche est visiblement une alternative aux autres, d'un coup d'œil, là où la version à `elseif` doit être lue dans l'ordre pour s'assurer que rien ne se glisse entre deux étapes.

<img src="images/ch06-chain-vs-table.png" alt="Avant, après : à gauche, un escalier tortueux de questions if et elseif ; à droite, les mêmes décisions posées à plat dans une table de quatre lignes" width="600">

Vous tenez là une règle à garder pour toute la suite du livre. Prenez `if`/`elseif` quand les conditions sont réellement des vérifications de nature différente : un intervalle ici, une combinaison de deux drapeaux là. Prenez `match` dès que vous remarquez que la question est « laquelle de ces valeurs connues est-ce ? ». Les énumérations rendent cette question évidente. Elle se pose partout ailleurs aussi.
