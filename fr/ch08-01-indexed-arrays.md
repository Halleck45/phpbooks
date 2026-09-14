# Stocker des listes de valeurs avec les tableaux indexés

Trois fruits, dans un ordre fixe, chacun accessible par sa position. C'est un tableau indexé, ce que la plupart des langages appellent simplement un tableau ou une liste, et il se construit avec des crochets :

```php
<?php

declare(strict_types=1);

$fruits = ['apple', 'banana', 'cherry'];

echo $fruits[0] . "\n"; // apple
echo $fruits[2] . "\n"; // cherry
echo count($fruits) . "\n"; // 3
```

**Les positions commencent à 0, pas à 1.** `$fruits[0]` est le premier élément, `$fruits[2]` le troisième et dernier.

`count()` donne le nombre d'éléments, et vous l'appellerez sans arrêt. C'est une lecture instantanée, pas un parcours du tableau, alors n'hésitez jamais à le mettre dans la condition d'une boucle.

## Ajouter à la fin

On construit rarement un tableau d'un bloc. Le plus souvent, on part de vide et on le fait grandir, et la façon de dire « ajoute ça à la fin » en PHP, c'est une paire de crochets vides :

```php
<?php

declare(strict_types=1);

$shoppingList = [];

$shoppingList[] = 'milk';
$shoppingList[] = 'eggs';
$shoppingList[] = 'bread';

print_r($shoppingList);
// Array
// (
//     [0] => milk
//     [1] => eggs
//     [2] => bread
// )
```

`$shoppingList[] = 'milk'` ressemble à un accès à rien du tout. Lisez-le comme un idiome à part entière : **« donne-lui la prochaine position libre et range-le là ».** PHP garde le compte de cette prochaine position ; vous n'avez jamais à le faire.

<img src="images/ch08-append.png" alt="Une rangée de trois boîtes numérotées 0, 1 et 2, et l'éléphant PHP qui glisse une quatrième boîte dans l'emplacement vide du bout, déjà étiqueté 3" width="520">

Essayez : affichez `count($shoppingList)` après chaque ligne. 1, 2, 3.

## Le modèle mental : un tableau est une table ordonnée

Voici le fait qui met en place tout le reste du chapitre. **Il n'existe pas de type liste à part en PHP.** `['apple', 'banana', 'cherry']` est un raccourci pour `[0 => 'apple', 1 => 'banana', 2 => 'cherry']` : un tableau indexé est un tableau dont les clés se trouvent être 0, 1, 2. En dessous, tous les tableaux PHP sont la même structure, une table de clés vers des valeurs qui retient l'ordre d'insertion.

Cela explique un comportement qui, sinon, passerait pour une bizarrerie. Filtrez un tableau indexé, et les survivants gardent leurs clés d'origine :

```php
<?php

declare(strict_types=1);

$numbers = [10, 15, 20, 25, 30];

$even = array_filter($numbers, fn (int $n) => $n % 2 === 0);

print_r($even);
// Array
// (
//     [0] => 10
//     [2] => 20
//     [4] => 30
// )
```

<img src="images/ch08-filter-gaps.png" alt="Trois rangées de boîtes : le tableau de départ avec les clés 0 à 4, le résultat de array_filter où les clés 1 et 3 ont disparu sans que les autres bougent, et le résultat de array_values renuméroté 0, 1, 2" width="560">

Les clés `1` et `3` ont disparu, elles n'ont pas été renumérotées. `array_filter()` a retiré deux entrées d'une table, et une table n'a aucune raison de rester contiguë. **S'il vous faut ensuite une suite propre `0, 1, 2`, `array_values()` renumérote :**

```php
<?php

$reindexed = array_values($even); // [10, 20, 30]
```

> Un tableau indexé est une table dont les clés se trouvent être 0, 1, 2. Retirez une entrée, les autres ne bougent pas.

## Les fonctions que vous utiliserez sans cesse

Une poignée de fonctions couvre l'essentiel de ce qu'on fait avec des listes au quotidien :

```php
<?php

declare(strict_types=1);

$scores = [88, 92, 74, 95, 60];

array_push($scores, 100);        // append (same as $scores[] = 100, but explicit)
$last = array_pop($scores);      // removes and returns the last element (100)

$passing = array_filter($scores, fn (int $s) => $s >= 60);
$grades = array_map(fn (int $s) => $s >= 90 ? 'A' : 'B', $passing);

sort($scores); // sorts in place, re-indexes from 0

$hasTopScore = in_array(95, $scores, strict: true);

echo implode(', ', $grades) . "\n";
```

`array_map()` transforme chaque élément et renvoie un tableau de même longueur. `array_filter()` garde les éléments qui passent un test et, vous venez de le voir, garde aussi leurs clés. `sort()` fait autrement : il modifie le tableau sur place et le renumérote à partir de 0, ce qui compte si vous teniez aux anciennes clés.

`in_array()` cherche une valeur. **Passez `strict: true`** pour qu'il compare avec `===` plutôt qu'avec la comparaison souple par défaut de PHP, pour la même raison qui a valu à `===` son propre encadré dans [Types de données](ch03-02-data-types.md). Faites-en une habitude.

`array_push()` et `$scores[] = ...` font le même travail pour une seule valeur. `array_push()` accepte plusieurs valeurs d'un coup, et « push » se lit bien quand on pense au tableau comme à une pile. Prenez celui qui se lit le mieux à l'endroit où vous l'écrivez.
