# Déstructuration de listes et de tableaux

Les vrais tableaux sont rarement des listes plates. Ils s'imbriquent, et le plus souvent ils portent des clés plutôt que des positions. **La déstructuration épouse la forme des données, quelle que soit cette forme.**

## Déstructuration imbriquée

Si un tableau contient d'autres tableaux, le motif reproduit cette structure telle quelle :

```php
<?php

$point = [[1, 2], 3];

[[$x, $y], $z] = $point;

echo "x={$x}, y={$y}, z={$z}\n"; // x=1, y=2, z=3
```

Mettez les deux côtés l'un à côté de l'autre : `[[$x, $y], $z]` et `[[1, 2], 3]`. Le motif est un calque des données. Cette symétrie fait tout l'intérêt. Passé un niveau de profondeur, une chaîne comme `$point[0][0]` commence à cacher ce que vous cherchez, alors que le motif dit « donne-moi exactement cette forme » en une ligne.

## Déstructuration par clé

Les coordonnées viennent par positions. Presque tout le reste de ce que vous déballerez dans une application vient avec des clés : une ligne de base de données, du JSON décodé, un formulaire soumis. Pour ceux-là, nommez les clés :

```php
<?php

$userData = [
    'name' => 'Priya',
    'age' => 29,
    'email' => 'priya@example.com',
];

['name' => $name, 'age' => $age] = $userData;

echo "{$name} is {$age}.\n"; // Priya is 29.
```

`email` n'est pas mentionné, donc on n'y touche pas. **Vous ne nommez que les clés que vous voulez, et le reste du tableau reste à sa place.**

<img src="images/ch19-keyed-pick.png" alt="Une commode aux tiroirs étiquetés name, age et email ; deux mains tirent les tiroirs name et age, dont le contenu s'écoule vers les variables $name et $age, tandis que le tiroir email reste fermé" width="520">

C'est ici que la déstructuration cesse d'être un raccourci et devient plus claire que l'alternative. Une ligne dit « ce code a besoin d'un nom et d'un âge » ; deux lignes de `$userData['name']` et `$userData['age']` le disent plus lentement.

Clés et imbrication se combinent :

```php
<?php

$response = [
    'status' => 'ok',
    'user' => ['name' => 'Priya', 'age' => 29],
];

['user' => ['name' => $name, 'age' => $age]] = $response;

echo "{$name}, {$age}\n"; // Priya, 29
```

## Échanger deux variables

La déstructuration a un petit tour de passe-passe très satisfaisant : échanger deux variables sans une troisième pour tenir la valeur en attente.

```php
<?php

$a = 1;
$b = 2;

[$a, $b] = [$b, $a];

echo "a={$a}, b={$b}\n"; // a=2, b=1
```

<img src="images/ch19-swap.png" alt="Deux boîtes étiquetées $a et $b contenant 1 et 2 ; un plateau à droite est d'abord rempli avec 2 et 1 dans l'ordre inverse, puis reversé dans les boîtes" width="560">

PHP construit d'abord le tableau `[$b, $a]` à droite, ce qui capture les deux valeurs d'origine, et seulement ensuite les reverse dans `$a` et `$b` à gauche. Quand `$a` est écrasé, l'ancienne valeur de `$b` a déjà été lue. C'est cet ordre qui rend l'échange sûr, et c'est la façon la plus propre d'échanger deux valeurs en PHP : aucune variable `$temp` nécessaire.

## Un mot de prudence

Déstructurez un tableau auquel il manque une clé ou une position que vous avez demandée, et rien n'est levé. L'élément manquant devient `null`, avec un avertissement si votre configuration de rapport d'erreurs est stricte. Essayez : retirez `'age'` de `$userData` ci-dessus et relancez le fichier.

> [!WARNING]
> **La déstructuration reconnaît une forme ; elle ne la vérifie jamais.** PHP vous laissera déballer un tableau de trois éléments comme s'il en avait cinq.

Prenez-la pour ce qu'elle est : une commodité pour du code où vous faites déjà confiance à la forme des données. Quand les données viennent de l'extérieur, validez d'abord, déstructurez ensuite.
