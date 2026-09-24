# Les fonctions

Vous appelez des fonctions depuis les premières lignes du jeu. `random_int(1, 100)` a choisi le secret, `fgets(STDIN)` a lu une ligne, `trim()` l'a nettoyée, `is_numeric()` l'a vérifiée. Chacune est un morceau de travail qui porte un nom : vous lui donnez quelque chose, elle vous rend quelque chose. (`echo` y ressemble mais, comme le [chapitre 1](ch01-02-hello-world.md) le signalait, ce n'en est pas une.) Écrivons la vôtre.

```php
<?php

function greet($name) {
    return "Hello, {$name}!\n";
}

echo greet("Damien");
```

**`function`, un nom, des parenthèses pour les paramètres, et un corps entre accolades : c'est toute la forme.** Appelez `greet("Damien")`, et dans le corps `$name` contient `"Damien"`. Par convention, les noms de fonctions s'écrivent en `camelCase`. Ils sont aussi insensibles à la casse à l'appel, contrairement aux variables : `GREET("Damien")` fonctionnerait. Ne comptez pas dessus.

<img src="images/ch03-function-machine.png" alt="Une fonction dessinée comme une petite machine avec une plaque à son nom : une valeur entre par un entonnoir marqué du nom du paramètre, la machine travaille, et un résultat sort par une goulotte marquée return" width="560">

## Paramètres et types

Donnez un type à chaque paramètre, comme vous l'avez vu dans [les types de données](ch03-02-data-types.md), et donnez aussi un type de retour à la fonction :

```php
<?php

function greet(string $name): void {
    echo "Hello, {$name}!\n";
}
```

`: void` dit que cette fonction ne rend rien : on l'appelle uniquement pour son effet de bord, ici l'affichage. **Une fonction qui rend quelque chose doit dire quoi :**

```php
<?php

function add(int $a, int $b): int {
    return $a + $b;
}

$sum = add(2, 3);
```

Typez chaque paramètre et chaque valeur de retour de chaque fonction que vous écrivez, à partir de maintenant. Ça coûte quelques frappes et ça supprime toute une catégorie de bugs où une fonction reçoit, ou rend, discrètement quelque chose d'inattendu. Avec `declare(strict_types=1)`, PHP passe de « typé dynamiquement et un peu trop indulgent » à un langage qui vous arrête à la porte quand vous passez la mauvaise chose.

## Les valeurs par défaut

Un paramètre peut avoir une valeur par défaut, ce qui le rend facultatif à l'appel :

```php
<?php

function greet(string $name, string $greeting = "Hello"): string {
    return "{$greeting}, {$name}!\n";
}

echo greet("Damien");             // Hello, Damien!
echo greet("Damien", "Bonjour");  // Bonjour, Damien!
```

Les paramètres avec défaut viennent après ceux qui n'en ont pas. PHP lit les arguments de gauche à droite : il lui faut d'abord régler les obligatoires.

## Les arguments nommés

L'ordre des arguments cesse de compter dès que vous les passez par leur nom, et **nommer les arguments est un vrai confort dès qu'une fonction a plus de deux ou trois paramètres :**

```php
<?php

echo greet(name: "Damien", greeting: "Bonjour");
echo greet(greeting: "Bonjour", name: "Damien"); // order no longer matters
```

C'est surtout précieux avec les fonctions qui ont plusieurs paramètres facultatifs : vous allez droit à celui que vous voulez changer, au lieu d'épeler tous les défauts intermédiaires pour l'atteindre par sa position.

## `return` sort immédiatement

**`return` quitte la fonction sur-le-champ, avec une valeur.** Rien de ce qui suit ne s'exécute :

```php
<?php

function classify(int $n): string {
    if ($n < 0) {
        return "negative";
    }

    if ($n === 0) {
        return "zero";
    }

    return "positive";
}
```

Pas de « la dernière expression est le résultat » implicite, comme dans certains langages. PHP veut toujours un `return` explicite. Oubliez-le, et la fonction renvoie `null`, en silence. C'est en général un bug plutôt qu'un choix, et c'est pourquoi déclarer `: void` sur les fonctions qui ne renvoient vraiment rien mérite de devenir une habitude : PHP, et tout outil d'analyse statique qui lit votre code, peut alors signaler une valeur qui s'échappe par accident.

## Les fonctions sont des valeurs

Une dernière chose, bonne à savoir tôt même si elle ne prend tout son sens qu'au [chapitre 15](ch15-00-functional-features.md) : **une fonction est une valeur, elle aussi.** Vous pouvez la garder dans une variable et l'appeler depuis là :

```php
<?php

$operation = 'add';
echo $operation(2, 3); // calls add(2, 3), if add() is defined above
```

Et PHP a de vraies fonctions anonymes, les [closures](ch15-01-closures.md), pour quand vous devez faire circuler un comportement sans lui donner de nom :

```php
<?php

$double = function (int $n): int {
    return $n * 2;
};

echo $double(21); // 42
```

Rangez ça dans un coin. Ça comptera beaucoup plus tard, quand vous confierez de petits morceaux de comportement aux fonctions de tableaux et aux générateurs.
