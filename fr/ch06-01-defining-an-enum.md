# Définir une énumération

## Énumérations pures

Quatre couleurs, ni plus ni moins. Les voici sous forme d'énumération :

```php
<?php
declare(strict_types=1);

enum Suit
{
    case Hearts;
    case Diamonds;
    case Clubs;
    case Spades;
}

$card = Suit::Hearts;

var_dump($card);          // enum(Suit::Hearts)
var_dump($card === Suit::Hearts); // true
```

`enum` ouvre la définition comme `class` le ferait, et chaque ligne `case` déclare une des valeurs permises. **Une énumération est un type doté d'une liste fermée de valeurs, et ces valeurs s'appellent des cas.** `Suit::Hearts` s'écrit comme une constante de classe : on atteint un cas par le nom de l'énumération.

La ligne `var_dump` montre quelque chose qu'une chaîne ne vous a jamais dit. `Suit::Hearts` est une valeur unique. Il n'en existe qu'un dans tout votre programme, quel que soit le nombre de variables qui pointent dessus, et c'est pourquoi le `===` de la ligne suivante répond `true` sans hésiter.

<img src="images/ch06-suit-singleton.png" alt="Quatre cartes à jouer épinglées sur un tableau, une par couleur, avec trois étiquettes de variables reliées par des ficelles à la même carte de cœur" width="480">

Cette unicité fait la sûreté du type. Un paramètre typé `Suit` ne peut rien contenir d'autre qu'un des quatre cas, et PHP arrête une valeur erronée au niveau du type, plutôt qu'avec un rapport de bogue trois semaines plus tard.

```php
<?php
declare(strict_types=1);

function describe(Suit $suit): string
{
    return "You drew a {$suit->name}.";
}

echo describe(Suit::Spades); // You drew a Spades.
```

Chaque cas porte une propriété intégrée `->name` : l'identifiant sous lequel vous l'avez déclaré, sous forme de chaîne. Pratique pour un journal, mais ce n'est qu'une étiquette. Y bâtir de la logique reviendrait à bâtir sur l'orthographe de votre propre code.

Essayez : appelez `describe('Spades')` avec une simple chaîne, et lisez le `TypeError`. Ce message, c'est l'énumération qui fait son travail.

## Énumérations adossées

Les cas d'une énumération pure ne sont rien d'autre qu'eux-mêmes : `Suit::Hearts` n'est pas secrètement une chaîne ou un nombre. Puis une commande doit être enregistrée dans une colonne de base de données, ou envoyée en JSON à un autre programme, et le monde extérieur ignore ce qu'est `Status::Shipped`. Il connaît `'shipped'`. **Une énumération adossée attache à chaque cas une valeur scalaire de votre choix**, une forme capable de quitter votre programme et d'y revenir.

```php
<?php
declare(strict_types=1);

enum Status: string
{
    case Pending = 'pending';
    case Shipped = 'shipped';
    case Cancelled = 'cancelled';
}

$status = Status::Shipped;

echo $status->value; // shipped
```

`: string` après le nom déclare l'énumération adossée à des chaînes, et dès lors chaque cas doit annoncer sa valeur : PHP le vérifie en lisant la définition. Les entiers marchent de la même façon (`enum Status: int`). Les chaînes restent le choix habituel, parce que `'shipped'` se comprend tout seul dans une ligne de base de données, là où un `2` nu vous renvoie à l'énumération pour savoir ce qu'il signifie.

Dans l'autre sens, d'une valeur brute vers un cas, il existe deux méthodes :

```php
<?php

$status = Status::from('shipped');   // Status::Shipped
echo $status->name;                  // Shipped

$status = Status::tryFrom('bogus');  // null, no matching case
var_dump($status);
```

`from()` convertit une valeur en cas correspondant et lève une `ValueError` si rien ne correspond. `tryFrom()` renvoie `null` à la place. Choisir entre les deux, c'est se demander d'où vient la valeur. Si une valeur inconnue ne peut être qu'un bogue dans votre propre code, utilisez `from()` et laissez-la échouer bruyamment. Si elle arrive d'une saisie utilisateur ou d'une API externe, « statut invalide » est une issue normale, et `tryFrom()` vous la remet sous la forme d'un `null` à gérer.

<img src="images/ch06-backed-bridge.png" alt="Une base de données et un document JSON, à l'extérieur, envoient la chaîne brute shipped à travers un poste de contrôle marqué from() et tryFrom() vers le programme, où elle devient le cas Status::Shipped ; une valeur inconnue, bogus, est renvoyée avec un null" width="600">

> `from()` lève une exception sur une valeur inconnue. `tryFrom()` renvoie `null`. Choisissez en vous demandant qui a produit la valeur.

## Une énumération peut avoir des méthodes

Une énumération n'est pas qu'une liste de noms. Elle peut porter du comportement, exactement comme une classe :

```php
<?php
declare(strict_types=1);

enum Status: string
{
    case Pending = 'pending';
    case Shipped = 'shipped';
    case Cancelled = 'cancelled';

    public function label(): string
    {
        return match ($this) {
            Status::Pending => 'Awaiting shipment',
            Status::Shipped => 'On its way',
            Status::Cancelled => 'Order cancelled',
        };
    }
}

echo Status::Shipped->label(); // On its way
```

`label()` fonctionne comme n'importe quelle méthode du [chapitre 5](ch05-03-methods.md) : à l'intérieur, `$this` désigne le cas sur lequel la méthode a été appelée. **La correspondance entre un cas et son libellé lisible vit désormais à un seul endroit, juste à côté des cas eux-mêmes**, au lieu d'être éparpillée dans le code sous forme de tests `if ($status === 'shipped')` qui finissent par diverger.

Le `match` à l'intérieur de `label()` compare `$this` à chaque cas et renvoie le texte inscrit à côté de celui qui convient. C'est `match` dans son meilleur rôle, et la section suivante le démonte pièce par pièce.
