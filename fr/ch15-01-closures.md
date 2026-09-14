# Closures et fonctions fléchées

Une closure est une fonction sans nom. Vous en avez rencontré une à la fin du chapitre 3, rangée dans une variable et appelée comme n'importe quelle fonction. Ce que le chapitre 3 a laissé de côté, c'est ce qui rend les closures utiles : **une closure peut emporter des variables du code qui l'entoure**, et PHP vous donne deux façons de les lui confier, avec deux résultats très différents.

## Capturer par valeur avec `use`

À l'intérieur d'une closure, les variables du code environnant sont invisibles par défaut. Vous devez nommer celles que vous voulez emporter, avec `use` :

```php
<?php
declare(strict_types=1);

function makeMultiplier(int $factor): callable
{
    return function (int $n) use ($factor): int {
        return $n * $factor;
    };
}

$double = makeMultiplier(2);
$triple = makeMultiplier(3);

echo $double(21) . "\n"; // 42
echo $triple(21) . "\n"; // 63
```

`makeMultiplier(2)` s'exécute, `$factor` vaut 2, et la closure est créée. **À cet instant précis, `use ($factor)` copie la valeur de `$factor` dans la closure**, et c'est cette copie que la closure utilisera pour le reste de sa vie. C'est la règle de la copie par valeur du [chapitre 4](ch04-02-references.md), appliquée à une fonction plutôt qu'à une variable.

Voilà pourquoi appeler `makeMultiplier()` deux fois donne deux closures qui se comporteront différemment pour toujours. `$double` est partie avec une copie de 2, `$triple` avec une copie de 3, et rien de ce qui arrivera plus tard à une variable nommée `$factor`, où que ce soit, ne peut les atteindre. Pensez à une photographie : la closure a pris `$factor` en photo en sortant, et une photo ne change pas quand le sujet change.

## Capturer par référence avec `use (&$var)`

Parfois, une photo ne suffit pas. Vous voulez que la closure partage une variable avec le code qui l'entoure, de sorte qu'un changement d'un côté se voie de l'autre. C'est `use (&$var)`, le même `&` que vous avez déjà vu sur des paramètres de fonction :

```php
<?php
declare(strict_types=1);

function makeCounter(): callable
{
    $count = 0;

    return function () use (&$count): int {
        $count++;
        return $count;
    };
}

$counter = makeCounter();
echo $counter() . "\n"; // 1
echo $counter() . "\n"; // 2
echo $counter() . "\n"; // 3
```

`$count` vit à l'intérieur de `makeCounter()`, et d'après tout ce que vous savez, elle devrait disparaître quand cette fonction se termine. Elle ne disparaît pas, parce que la closure en détient une référence. **La closure et la variable sont désormais deux étiquettes collées sur la même boîte**, et chaque appel à `$counter()` ajoute un à ce qu'elle contient. Plus personne d'autre ne voit `$count`, mais elle reste en vie aussi longtemps que la closure.

<img src="images/ch15-use-copy-vs-ref.png" alt="Deux façons pour une closure de capturer une variable : avec use, la closure repart avec une photo de la boîte ; avec use et une esperluette, elle reste reliée à la boîte d'origine par une corde" width="600">

Essayez : retirez le `&` et relancez le fichier. Chaque appel reçoit maintenant sa propre copie toute neuve de `$count`, qui part de 0, et le compteur affiche 1, 1, 1. Un seul caractère fait toute la différence entre un instantané et une boîte partagée.

## Fonctions fléchées : capturer sans demander

Écrire `use` pour chaque variable devient vite pénible, surtout pour les fonctions d'une ligne que vous passez à des fonctions comme `array_map()`. Les fonctions fléchées existent exactement pour ça :

```php
<?php
$factor = 3;
$triple = fn(int $n): int => $n * $factor;

echo $triple(14) . "\n"; // 42
```

Pas de `use` nulle part, et `$factor` est pourtant visible à l'intérieur. **Une fonction fléchée capture automatiquement, par valeur, chaque variable qu'elle mentionne dans le code environnant**, comme si PHP avait écrit `use ($factor)` à votre place. Cette commodité est la raison d'être de `fn`.

Elle vient avec deux limites. Le corps est une seule expression : ce qui suit `=>` est la valeur de retour, sans accolades, sans `return`, sans instruction avant. Et la capture est toujours par valeur. Il n'existe pas de version fléchée de `use (&$var)` ; quand il vous faut une référence, vous écrivez une closure complète.

> Une closure déclare ce qu'elle capture. Une fonction fléchée capture ce qu'elle utilise, toujours en copie.

## Là où on s'en sert vraiment

Vous écrirez beaucoup plus de fonctions fléchées que de closures, parce que la plupart des comportements que vous passez d'une fonction à l'autre sont courts. `array_map()`, `array_filter()` et `usort()` sont leur terrain naturel :

```php
<?php
declare(strict_types=1);

$prices = [10.00, 25.50, 3.99, 100.00];

$withTax = array_map(fn(float $p): float => round($p * 1.2, 2), $prices);

$expensive = array_filter($prices, fn(float $p): bool => $p > 20.00);

usort($prices, fn(float $a, float $b): int => $a <=> $b);
```

`array_map()` applique la fonction à chaque élément et renvoie un nouveau tableau avec les résultats. `array_filter()` garde les éléments pour lesquels la fonction renvoie `true`, ou tout ce que PHP considère comme vrai. `usort()` trie le tableau sur place en appelant la fonction pour comparer deux éléments à la fois ; `<=>`, l'opérateur vaisseau spatial, est la façon standard d'écrire cette comparaison, puisqu'il renvoie un nombre négatif, zéro ou un nombre positif selon le côté le plus grand.

Aucune des trois n'a eu besoin de plus qu'une fonction fléchée d'une ligne, et c'est précisément le cas pour lequel elles ont été conçues. **Réservez la closure complète aux moments où vous devez capturer par référence, ou quand la logique demande plus d'une expression.** Le reste du temps, la fonction fléchée est le meilleur choix par défaut.
