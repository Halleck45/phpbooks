# Les structures de contrôle

Réduisez le jeu de devinette à son squelette, et il reste deux mots : `if` et `while`. L'un décide, l'autre répète. **Tout ce qu'un programme fait au-delà de s'exécuter de haut en bas vient de ces deux gestes**, et PHP a quelques variantes de chacun.

## `if` / `elseif` / `else`

```php
<?php

$temperature = 18;

if ($temperature > 30) {
    echo "Hot.\n";
} elseif ($temperature > 15) {
    echo "Pleasant.\n";
} else {
    echo "Bring a jacket.\n";
}
```

Même forme que la comparaison du jeu : PHP exécute le premier bloc dont la condition est vraie et ignore les autres, ou se rabat sur `else`. C'est `elseif`, en un mot. `else if`, en deux mots, fonctionne aussi, mais seul `elseif` est un jeton unique pour PHP, c'est donc la convention à adopter.

**La condition n'a pas à être un booléen, mais écrivez-la comme si c'était le cas.** PHP convertit ce que vous lui donnez : `0`, `""`, `null` et `[]` comptent pour faux, tout le reste pour vrai. S'appuyer là-dessus, c'est exactement le genre de jonglage de types contre lequel [les types de données](ch03-02-data-types.md) vous ont mis en garde. Préférez une comparaison explicite dès que la valeur n'est pas déjà, à l'évidence, un booléen.

Une chaîne de `if`/`elseif` est à son meilleur quand chaque branche teste quelque chose de différent, comme `$temperature > 30` et `$temperature > 15` ci-dessus. Quand vous vous surprenez à écrire plusieurs branches qui comparent toutes la même valeur à une liste de possibilités, cette répétition est le signal de passer à l'outil suivant.

## `match`

PHP 8 a ajouté `match`, et une fois qu'on l'a utilisé, `switch` ressemble à une relique :

```php
<?php

$httpStatus = 404;

$message = match (true) {
    $httpStatus >= 200 && $httpStatus < 300 => "Success",
    $httpStatus >= 400 && $httpStatus < 500 => "Client error",
    $httpStatus >= 500 => "Server error",
    default => "Unknown",
};

echo $message; // Client error
```

<img src="images/ch03-match-arms.png" alt="Une valeur entre dans un bloc match dessiné comme un aiguillage de chemin de fer : plusieurs branches avec chacune une condition, et une seule allumée, qui mène à l'unique résultat qui en sort" width="520">

**`match` est une expression : il produit une valeur**, que vous affectez, comme ci-dessus, au lieu d'une instruction dans laquelle on bifurque. Deux autres choses en font une vraie amélioration par rapport à `switch`. Ses comparaisons sont strictes, `===`, donc aucun jonglage ne fait passer une mauvaise branche en douce. Et il n'a pas de fallthrough, donc pas de `break` à oublier. Le [chapitre 6](ch06-00-enums.md) associe `match` aux énumérations, et les deux se révèlent faits l'un pour l'autre.

## Les boucles

**`while` tourne tant que sa condition tient, et la vérifie avant chaque passage :**

```php
<?php

$count = 3;
while ($count > 0) {
    echo "{$count}...\n";
    $count--;
}
echo "Go!\n";
```

Le `while (true)` du jeu était le cas extrême : une condition qui ne devient jamais fausse, et `break` comme seule sortie.

**`do...while` vérifie la condition après chaque passage**, si bien que le corps s'exécute au moins une fois :

```php
<?php

do {
    echo "This runs once even if the condition is already false.\n";
} while (false);
```

<img src="images/ch03-while-vs-dowhile.png" alt="Deux portes : avec while, on contrôle le billet avant d'entrer, et on peut ne jamais entrer ; avec do while, on entre d'abord et le billet est contrôlé au retour, donc on entre toujours au moins une fois" width="560">

**`for` est la boucle classique en trois parties**, chez elle dès qu'il vous faut un compteur :

```php
<?php

for ($i = 0; $i < 5; $i++) {
    echo "{$i}\n";
}
```

Valeur de départ, condition, pas, le tout sur une ligne : `$i` part de 0, le corps tourne tant que `$i < 5`, et `$i++` ajoute un après chaque passage.

**`foreach` parcourt directement une collection, sans compteur à tenir**, et c'est la boucle que vous prendrez sans cesse dès que les tableaux arriveront au [chapitre 8](ch08-00-common-collections.md) :

```php
<?php

$fruits = ["apple", "banana", "cherry"];

foreach ($fruits as $fruit) {
    echo "{$fruit}\n";
}

$prices = ["apple" => 0.5, "banana" => 0.3];

foreach ($prices as $name => $price) {
    echo "{$name}: \${$price}\n";
}
```

La seconde forme, `as $name => $price`, extrait la clé et la valeur d'un coup. Elle est si fréquente dans le vrai code PHP qu'elle vaut d'être mémorisée dès maintenant.

## `break` et `continue`, encore une fois

Vous les avez rencontrés tous les deux dans le jeu : **`break` quitte la boucle sur-le-champ, `continue` saute au tour suivant.**

<img src="images/ch02-loop-track.png" alt="Une piste de course dessinée en boucle, avec une porte marquée break qui mène dehors et un raccourci marqué continue qui ramène à la ligne de départ" width="520">

```php
<?php

foreach ([1, 2, 3, 4, 5] as $n) {
    if ($n === 3) {
        continue; // skip 3, keep going
    }
    if ($n === 5) {
        break; // stop entirely once we hit 5
    }
    echo "{$n}\n";
}
// prints 1, 2, 4
```

Tous deux acceptent un nombre facultatif : `break 2` quitte deux boucles imbriquées d'un coup. N'y touchez que si c'est plus lisible que de restructurer les boucles. Les niveaux de break imbriqués sont évidents quand on les écrit et déroutants un mois plus tard.

Essayez : réécrivez la comparaison à trois branches du jeu sous la forme d'un `match (true)` qui produit le message, puis affichez-le. Le `break` doit rester hors du `match`, puisqu'un `match` produit une valeur et ne fait rien d'autre. Cette petite résistance, c'est la différence entre une expression et une instruction, sentie sous vos propres doigts.

Bifurquer, répéter, piloter. Le reste du livre n'ajoute jamais un nouveau geste, seulement des formes plus grandes faites de ceux-là.
