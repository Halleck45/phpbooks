# Les types de données

Le clavier a donné au jeu le texte « 42 », et le jeu avait besoin du nombre 42. Cet écart, et le `(int)` que vous avez écrit pour le combler, voilà le sujet de cette section. **PHP vous laisse écrire un programme entier sans nommer un seul type. Il peut aussi, si vous le lui demandez, vous tenir à vos types aussi strictement qu'un langage compilé.** Les deux sont vrais en même temps.

## Les types scalaires

Quatre types contiennent une seule valeur chacun :

```php
<?php

$age = 41;           // int
$price = 19.99;      // float
$name = "Damien";    // string
$isReady = true;     // bool
```

Un entier pour compter, un flottant pour mesurer, une chaîne de caractères pour le texte, un booléen pour oui ou non. Le jeu en a utilisé trois sans le dire : `$secretNumber` était un `int`, la saisie brute une `string`, et `is_numeric()` répondait par un `bool`.

Vous pouvez demander à PHP ce que contient une variable avec `gettype()`, ou, bien plus utile pour déboguer, avec `var_dump()` :

```php
<?php

var_dump($age);
// int(41)

var_dump($price);
// float(19.99)
```

**`var_dump()` affiche le type avec la valeur, ce qu'`echo` ne fait jamais.** Il deviendra l'un de vos outils les plus utilisés. Essayez : dans le jeu, ajoutez `var_dump($input);` juste après la ligne qui lit le clavier, tapez 42, et lisez la réponse. `string(2) "42"` : deux caractères de texte, pas un nombre.

## Les types composés

Deux types contiennent des collections d'autres choses.

**Les tableaux sont la structure à tout faire de PHP** : liste, dictionnaire, pile, file, un seul type sous-jacent qui change de chapeau :

```php
<?php

$fruits = ["apple", "banana", "cherry"];   // indexed
$prices = ["apple" => 0.5, "banana" => 0.3]; // associative
```

Tout le [chapitre 8](ch08-00-common-collections.md) leur est consacré, et ils le méritent : aucun programme PHP d'une taille respectable ne s'en passe.

**Les objets** sont des instances de classes, la manière qu'a PHP de réunir des données et le comportement qui les manipule. Les objets commencent vraiment au [chapitre 5](ch05-00-classes.md) ; d'ici là, vous n'en croiserez qu'un ou deux en passant.

## Les types spéciaux

`null` signifie « aucune valeur » : pas zéro, pas une chaîne vide, rien :

```php
<?php

$middleName = null;
```

Vous rencontrerez `null` sans arrêt, le plus souvent comme réponse à « cette fonction a-t-elle trouvé quelque chose, ou non ? ». PHP 8 a donné de vraies dents à `null` avec les énumérations et l'opérateur nullsafe (`?->`), tous deux au [chapitre 6](ch06-00-enums.md).

## Le jonglage de types, et comment cesser de s'en inquiéter

Voici ce qui a fait la réputation de PHP, méritée ou non : **quand un opérateur a besoin d'un certain type, PHP convertit la valeur sur place.**

```php
<?php

var_dump("5" + 3);      // int(8)
var_dump("5" . 3);      // string(2) "53"
var_dump(0 == "abc");   // false, as of PHP 8 (this used to be true!)
```

<img src="images/ch03-type-juggling.png" alt="Les deux mêmes valeurs, le texte 5 et le nombre 3, entrent dans un signe plus et ressortent en nombre 8, puis entrent dans un point et ressortent en texte 53 : c'est l'opérateur qui décide de la conversion" width="560">

`+` veut des nombres, donc la chaîne `"5"` devient un nombre. `.` (la concaténation) veut des chaînes, donc l'entier `3` devient du texte. C'est le *jonglage de types*, et les vieux tutoriels PHP en racontent des histoires d'horreur, surtout parce que la comparaison souple avec `==` avait des règles franchement surprenantes avant que PHP 8 ne les resserre. C'est aussi ce qui a transformé `"banana"` en un `0` silencieux dans le jeu.

Deux habitudes suffisent pour que le jonglage ne vous morde jamais.

**Préférez `===` à `==`.** La comparaison stricte vérifie le type *et* la valeur, sans conversion : `0 === "abc"` vaut simplement `false`, sans astérisque. Ne prenez `==` que lorsque vous voulez précisément la conversion.

**Activez les types stricts.** Placez ceci en toute première instruction du fichier, juste après `<?php` :

```php
<?php
declare(strict_types=1);

function double(int $n): int {
    return $n * 2;
}

double("4"); // TypeError: no silent conversion here
```

<img src="images/ch03-strict-types-door.png" alt="Une porte marquée strict_types=1 à l'entrée d'une fonction ; un videur laisse passer le nombre 4 et arrête à la porte le texte 4 entre guillemets" width="520">

Sans `declare(strict_types=1)`, PHP convertit discrètement `"4"` en `4` quand la valeur atteint un paramètre typé `int`. Avec, le même appel lève une `TypeError`. Le PHP moderne l'active presque toujours : « PHP a deviné ce que vous vouliez » devient « PHP vous a dit exactement ce qui n'allait pas », et le second est un bien meilleur rapport de bug.

> La comparaison souple et la conversion silencieuse sont le défaut de PHP. `===` et `strict_types` servent à les désactiver.

Les déclarations de types sur les paramètres, sur les valeurs de retour et, plus tard, sur les propriétés, apparaissent dans tous les exemples à partir d'ici. Elles sont facultatives en PHP. Traitez-les comme la règle, pas comme l'exception.
