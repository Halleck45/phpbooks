# L'expression `match`

`match` a fait une courte apparition au [chapitre 3](ch03-05-control-flow.md) sous la forme `match(true)`, testant une condition après l'autre sur un code de statut HTTP. Une astuce utile, mais pas `match` à son meilleur. **`match` brille quand une valeur est comparée à un petit ensemble connu de possibilités**, et une énumération est précisément cet ensemble.

## Comparer directement à un cas de l'énumération

```php
<?php
declare(strict_types=1);

enum Status: string
{
    case Pending = 'pending';
    case Shipped = 'shipped';
    case Cancelled = 'cancelled';
}

function nextAction(Status $status): string
{
    return match ($status) {
        Status::Pending => 'Pack the order',
        Status::Shipped => 'Notify the customer',
        Status::Cancelled => 'Issue a refund',
    };
}

echo nextAction(Status::Pending); // Pack the order
```

Pas de `true`, pas d'opérateur de comparaison, pas de test d'intervalle. `match ($status)` compare la valeur entre parenthèses à chaque branche avec une comparaison stricte `===`, et renvoie ce qui se trouve à droite de la flèche sur la première branche qui convient. Lue de haut en bas, la fonction est une table : une ligne par cas, une réponse par ligne.

<img src="images/ch06-match-table.png" alt="La valeur Status::Pending arrive devant une table à deux colonnes, où la ligne Pending est surlignée et sa réponse, Pack the order, ressort à droite" width="560">

Remarquez le `return` devant `match`. **`match` est une expression : il produit une valeur** que vous pouvez renvoyer ou ranger dans une variable, là où `switch` et `if` se contentent d'exécuter du code. C'est pour cela que le corps entier de la fonction tient en une seule instruction.

## Plusieurs conditions par branche

Une branche peut lister plusieurs valeurs, séparées par des virgules, et une seule suffit :

```php
<?php
declare(strict_types=1);

function isFinal(Status $status): bool
{
    return match ($status) {
        Status::Shipped, Status::Cancelled => true,
        Status::Pending => false,
    };
}

var_dump(isFinal(Status::Shipped));   // true
var_dump(isFinal(Status::Cancelled)); // true
var_dump(isFinal(Status::Pending));   // false
```

`Status::Shipped, Status::Cancelled => true` se lit « l'un ou l'autre, même réponse ». C'est mieux que d'écrire la branche deux fois, et mieux qu'un `||` glissé dans un `match(true)`.

## L'exhaustivité est imposée

Voici ce qui fait de `match` plus qu'un `switch` mieux rangé. **Chaque valeur possible doit être traitée, nommément ou par une branche `default`. Si aucune ne convient, `match` lève une exception.** Supposons que la boutique se mette à accepter les retours :

```php
<?php
declare(strict_types=1);

enum Status: string
{
    case Pending = 'pending';
    case Shipped = 'shipped';
    case Cancelled = 'cancelled';
    case Returned = 'returned'; // added later
}

function nextAction(Status $status): string
{
    return match ($status) {
        Status::Pending => 'Pack the order',
        Status::Shipped => 'Notify the customer',
        Status::Cancelled => 'Issue a refund',
        // forgot to add a Returned arm
    };
}

nextAction(Status::Returned); // UnhandledMatchError: Unhandled match case Status::Returned
```

L'énumération a grandi, le `match` non, et la première fois qu'une commande retournée atteint `nextAction()`, PHP lève une `UnhandledMatchError` sur cette ligne précise.

<img src="images/ch06-unhandled-case.png" alt="Un nouveau cas nommé Returned se présente devant une table match qui n'a que des lignes pour Pending, Shipped et Cancelled, n'y trouve pas de place, et une UnhandledMatchError est levée" width="560">

Cela paraît sévère, et c'est justement l'intérêt. Ajoutez un cas à une énumération dans six mois, oubliez l'une des expressions `match` qui la lisent, et PHP nomme l'endroit à corriger. Un `switch` sans branche correspondante ne fait rien et continue. Une chaîne de `if` exécute tranquillement son `else` pour une valeur que personne n'avait prévue. Un `match` refuse.

Essayez : ajoutez une branche `Status::Returned => 'Restock the item'` et relancez le fichier.

Quand la plupart des cas partagent vraiment un même comportement de repli, ajoutez une branche `default`, comme `switch` en a toujours eu. Elle récupère tout ce qui n'est pas nommé au-dessus, et dit au lecteur que vous avez choisi de traiter le reste de la même façon, plutôt qu'oublié.

> Un `match` sans `default` est une promesse de traiter chaque cas. PHP vous tient à cette promesse.
