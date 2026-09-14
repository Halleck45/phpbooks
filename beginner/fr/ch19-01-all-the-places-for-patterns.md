# Où utiliser `match` et la déstructuration

Une affectation range d'ordinaire une valeur dans une variable. **La déstructuration est une affectation qui déballe : plusieurs valeurs sorties d'un tableau, dans plusieurs variables, en une seule instruction.** Vous décrivez à gauche la forme que vous attendez, et PHP remplit les noms.

## Les deux orthographes

PHP sait faire ça depuis longtemps, sous le nom de `list()` :

```php
<?php

$coordinates = [4, 7];

list($x, $y) = $coordinates;

echo "x={$x}, y={$y}\n";
```

La forme entre crochets est arrivée plus tard et fait exactement la même chose :

```php
<?php

$coordinates = [4, 7];

[$x, $y] = $coordinates;

echo "x={$x}, y={$y}\n";
```

<img src="images/ch19-shape-stencil.png" alt="Le motif [$x, $y] dessiné comme un pochoir posé sur le tableau [4, 7], chaque valeur tombant par son trou dans la variable du même nom" width="560">

Les deux formes associent par position : le premier élément va au premier nom, le deuxième au deuxième, et ainsi de suite. `list()` survit dans les vieilles bases de code et dans quelques exemples de la documentation officielle, donc reconnaissez-le quand vous le croisez, mais écrivez la forme entre crochets. Elle est plus courte, et elle ressemble au tableau qu'elle démonte.

Essayez : remplacez le tableau par `[4, 7, 9]` et relancez. Rien ne casse. La troisième valeur n'a simplement aucun nom où atterrir, alors elle reste où elle est.

## Dans un foreach

Le premier endroit où la déstructuration rapporte vraiment, c'est `foreach`, où vous déballez chaque élément au moment où la boucle vous le tend :

```php
<?php

$pairs = [
    ['Alice', 30],
    ['Bob', 25],
    ['Carol', 35],
];

foreach ($pairs as [$name, $age]) {
    echo "{$name} is {$age} years old.\n";
}
```

```console
$ php pairs.php
Alice is 30 years old.
Bob is 25 years old.
Carol is 35 years old.
```

Sans elle, le corps de la boucle dirait `$pair[0]` et `$pair[1]`, et celui qui lit le code devrait deviner ce que signifie la position 0. **`foreach ($pairs as [$name, $age])` annonce la forme des données dans l'en-tête de la boucle**, la première ligne que tout le monde regarde.

## Sauter des éléments

Parfois un tableau offre plus que ce que vous voulez. Laissez une case vide et PHP la saute, sans décaler celles qui suivent :

```php
<?php

$row = [1, 'Second', 'Third'];

[, $second, $third] = $row;

echo "{$second}, {$third}\n"; // Second, Third
```

La virgule sans rien devant dit « saute le premier » : la liste des noms a un trou là où un nom irait normalement. Un détail, mais qui se lit mieux qu'une variable `$unused` remplie pour ne jamais servir.

Les tableaux plats sont le cas facile. Les vrais s'imbriquent, la plupart portent des clés plutôt que des positions, et la déstructuration les suit jusque-là, tour de passe-passe compris.
