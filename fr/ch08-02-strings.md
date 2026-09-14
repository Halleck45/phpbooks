# Stocker du texte encodé en UTF-8 avec les chaînes de caractères

Demandez à PHP la longueur du mot `café`, et il répond cinq.

Vous avez rencontré les chaînes de caractères dans [Hello, World!](ch01-02-hello-world.md) et utilisé l'interpolation dans le [jeu de devinette](ch02-00-guessing-game-tutorial.md) sans cérémonie. Ce que nous avons passé sous silence, à raison, c'est la partie qui finit par mordre tous ceux qui manipulent des chaînes en PHP. **Une chaîne PHP n'est pas faite de caractères. Elle est faite d'octets.** La plupart du temps, la différence est invisible. Jusqu'au jour où elle ne l'est plus.

## Les guillemets, en bref

Vous utiliserez les deux sortes sans arrêt, alors voici la règle une fois encore. Les guillemets simples sont ce que PHP a de plus littéral : pas d'interpolation, pas de séquence d'échappement en dehors de `\'` et `\\`. Les guillemets doubles remplacent les variables par leur valeur et comprennent les séquences comme `\n` et `\t` :

```php
<?php

declare(strict_types=1);

$name = 'Damien';

echo 'Hello, $name\n';   // Hello, $name\n  (literal, no processing)
echo "Hello, $name\n";   // Hello, Damien  (interpolated, newline applied)
```

**Choisissez les guillemets simples quand il n'y a rien à interpoler.** C'est un peu plus rapide, PHP ne parcourt pas le texte à la recherche de `$` ou de `\`, mais le vrai bénéfice est pour le prochain lecteur : les guillemets simples disent « rien de malin ici ».

## Octets et caractères

Voici le fait qui compte. **Les fonctions classiques de PHP sur les chaînes (`strlen()`, `strtoupper()`, `substr()` et leurs cousines) travaillent sur des octets, point.** C'était une hypothèse raisonnable dans un monde ASCII, où un octet est un caractère. Elle s'effondre dès que le texte n'est plus de l'ASCII, et en UTF-8, ce que produit à peu près tout le PHP moderne, ça arrive vite :

```php
<?php

declare(strict_types=1);

$name = 'café';

echo strlen($name) . "\n";     // 5, not 4!
echo mb_strlen($name) . "\n";  // 4, correct
```

<img src="images/ch08-bytes-vs-chars.png" alt="Le mot café en quatre tuiles de lettres au-dessus d'une règle de cinq cases d'octets, le é occupant deux cases : strlen compte les cases, mb_strlen compte les tuiles" width="560">

`café` a quatre caractères, mais UTF-8 range le é sur deux octets, si bien que `strlen()`, qui compte des octets, dit cinq. Ce n'est pas faux, à proprement parler. C'est la réponse à une question que vous ne vouliez pas poser. `mb_strlen()` (`mb` pour multibyte, multi-octets) comprend UTF-8 et compte des caractères, ce que vous vouliez dire.

Essayez : remplacez `café` par un seul emoji. `strlen()` dit quatre, `mb_strlen()` dit un.

La règle pratique tient en une phrase. **Si une chaîne peut un jour contenir quelque chose tapé par un utilisateur (un nom, un commentaire, une recherche), utilisez la variante `mb_`.** `strlen()` reste juste pour le travail réellement orienté octets : la taille du contenu d'un fichier, ou une chaîne que vous avez construite vous-même en ASCII connu. Dans le doute, `mb_strlen()` ne vous coûte rien, et il vous épargne un bug qui n'apparaît que chez certains de vos utilisateurs, en général ceux qui ont un accent dans leur nom. C'est le genre qui fait honte.

> [!WARNING]
> `strlen()` compte des octets. `mb_strlen()` compte des caractères. Pour tout ce qu'un humain a tapé, ce sont des caractères que vous voulez.

## Les fonctions de tous les jours

Une poignée de fonctions couvre le gros du travail réel sur les chaînes :

```php
<?php

declare(strict_types=1);

$message = 'PHP is not dead, it just smells funny.';

if (str_contains($message, 'not dead')) {
    echo "Reassuring.\n";
}

$corrected = str_replace('not dead', 'thriving', $message);
echo $corrected . "\n";

$excerpt = substr($message, 0, 12);
echo $excerpt . "...\n"; // PHP is not d...

$formatted = sprintf('%s scored %d%% on the test.', 'Alice', 92);
echo $formatted . "\n"; // Alice scored 92% on the test.
```

`str_contains()` (PHP 8.0 et suivants) demande si une chaîne apparaît dans une autre et renvoie un booléen, sans plus. Elle a remplacé le vieil idiome `strpos($haystack, $needle) !== false` que vous croiserez encore dans du code ancien, avec son `false` à part qui n'attend que de vous faire trébucher. `str_replace()` remplace chaque occurrence d'une sous-chaîne. `substr()` découpe une portion par position de départ et longueur, et comme `strlen()`, elle a une jumelle `mb_substr()` qui compte des caractères, selon la même règle que plus haut.

**`sprintf()` construit une chaîne à partir d'un modèle et d'une liste de valeurs.** Passé une ou deux valeurs, c'est bien plus lisible qu'une suite de concaténations, et cela donne un contrôle que l'interpolation n'offre pas : `%d%%` ci-dessus force `92` à être traité comme un entier, puis affiche un `%` littéral. `printf()` fait la même chose, moins la partie « renvoyer une chaîne » : il affiche directement.

<img src="images/ch08-sprintf-template.png" alt="Un modèle sprintf dessiné comme un formulaire à trous, où les valeurs Alice et 92 tombent dans les deux blancs pour former la phrase finale" width="520">

## L'interpolation, une dernière fois

Vous connaissez les bases depuis le [chapitre 2](ch02-00-guessing-game-tutorial.md). La forme complète mérite d'être sous la main : **`{$expr}` entre guillemets doubles accepte plus qu'une simple variable**, un accès de tableau, une propriété, un appel de méthode, tout ce qui se résout en une valeur :

```php
<?php

declare(strict_types=1);

$user = ['name' => 'Alice', 'age' => 30];

echo "{$user['name']} is {$user['age']} years old.\n";
```

Sans les accolades, `"$user['name']"` ne fait pas ce que vous attendez : PHP s'arrêterait à `$user` en lisant le nom de la variable et afficherait le reste tel quel. Les accolades lèvent l'ambiguïté, alors faites-en votre réflexe dès qu'une interpolation dépasse une simple `$variable`.
