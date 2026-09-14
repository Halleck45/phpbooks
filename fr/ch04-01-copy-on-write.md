# Comment PHP gère les valeurs : la copie à l'écriture

Affectez un tableau à une seconde variable, ajoutez quelque chose à la seconde, et regardez la première :

```php
<?php

$original = [1, 2, 3];
$copy = $original;

$copy[] = 4;

var_dump($original); // array(3) { [0]=> int(1) [1]=> int(2) [2]=> int(3) }
var_dump($copy);     // array(4) { [0]=> int(1) [1]=> int(2) [2]=> int(3) [3]=> int(4) }
```

`$original` a toujours trois éléments. **Copier un tableau donne un tableau indépendant** : modifiez la copie autant que vous voulez, l'original ne bouge pas. Imaginez `$copy = $original` comme PHP parcourant le tableau et recopiant chaque élément dans une boîte neuve. C'est l'image à garder, et pour l'essentiel du PHP quotidien, elle suffit.

> Copiez un tableau, modifiez la copie : l'original ne bouge pas.

## Mais il ne copie pas vraiment tout de suite

Voici ce qui se passe réellement, et ça vaut la peine de le savoir même si ça change rarement la façon d'écrire du code. Dupliquer un tableau à l'instant où on l'affecte serait du gaspillage : beaucoup de tableaux circulent sans jamais être modifiés, et la copie serait du travail pour rien. **PHP attend, et ne copie le tableau qu'au moment où l'un des deux côtés essaie de le modifier.** Cette stratégie s'appelle la copie à l'écriture, copy-on-write en anglais.

L'affectation `$copy = $original` fait pointer les deux noms vers les mêmes données, et PHP tient un petit compte du nombre de variables qui les partagent. Lire par l'un ou l'autre nom ne coûte rien. La première écriture par l'un d'eux (`$copy[] = 4` ci-dessus) est le moment où PHP intervient : il fabrique une vraie copie, séparée, et applique la modification à cette copie seulement.

<img src="images/ch04-copy-on-write.png" alt="Avant l'écriture, $original et $copy sont deux étiquettes sur la même boîte de valeurs. La première écriture par $copy pousse PHP à dupliquer la boîte, et c'est seulement alors que chaque variable a son propre tableau" width="600">

```php
<?php

$original = ["apple", "banana"];
$copy = $original; // no copying has happened yet, both point at the same data

foreach ($copy as $fruit) {
    echo $fruit . "\n"; // just reading, still sharing
}

$copy[] = "cherry"; // *now* PHP actually duplicates the array
```

Rien de tout cela n'est visible depuis votre programme. Aucune fonction à appeler, aucun délai, rien qui se comporte différemment selon que la copie a « vraiment » eu lieu ou non. C'est une pure optimisation que le moteur fait pour vous. Le mot vaut quand même la peine d'être connu, parce que « copy-on-write » revient dans les discussions sur les performances de PHP, dans le texte des RFC et dans la sortie de certains profileurs, et il est bon de savoir que ça n'a rien d'exotique. C'est PHP qui paresse sur une copie qu'il allait de toute façon vous donner.

## Pourquoi ça compte pour les fonctions

Passez un tableau à une fonction, et la fonction reçoit ce qui se comporte comme sa propre copie :

```php
<?php
declare(strict_types=1);

function addTax(array $prices): array
{
    foreach ($prices as $key => $price) {
        $prices[$key] = round($price * 1.2, 2);
    }
    return $prices;
}

$cart = ["book" => 10.00, "pen" => 2.00];
$withTax = addTax($cart);

var_dump($cart);     // unchanged: book => 10.00, pen => 2.00
var_dump($withTax);  // book => 12.00, pen => 2.40
```

`addTax()` réécrit `$prices` à sa guise, et rien n'en ressort vers `$cart`. **Une fonction qui reçoit un tableau ne peut pas revenir réécrire les données de l'appelant**, sauf si celui-ci l'autorise explicitement. C'est en général exactement ce que vous voulez : vous confiez des données à une fonction, elle vous en rend, et ce que vous teniez est toujours ce que vous teniez. Essayez : ajoutez `$prices["hat"] = 5.00;` juste avant le `return` et affichez `$cart` à nouveau. Toujours deux articles.

Parfois, vous voulez vraiment qu'une fonction modifie sur place le tableau de l'appelant. La copie à l'écriture ne peut pas vous l'offrir. Les références, si, et c'est le sujet de la [section suivante](ch04-02-references.md).

Une chose à signaler avant d'y arriver : tout ce qui précède parle de tableaux. Affectez un objet à une autre variable et vous n'obtenez pas de copie indépendante, paresseuse ou non. Ce contraste mérite son propre traitement, juste après le `&`.
