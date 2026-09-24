# Le système de types

**PHP est typé dynamiquement, et chaque type que vous écrivez est vérifié à l'exécution**, pas à la compilation comme en Java, et pas effacé comme en TypeScript. Un paramètre déclaré `int` reçoit un `int`, sinon l'appel lève une `TypeError`, à chaque fois, y compris en production. Tout le modèle tient dans cette phrase, et la nuance se cache dans ce que « reçoit un `int` » veut dire, parce que cette nuance dépend d'un interrupteur.

## Les types que vous pouvez écrire

```php
<?php
declare(strict_types=1);

function describe(int|float $n, ?string $label, bool $verbose = false): string
{
    return ($label ?? 'value') . ': ' . $n . ($verbose ? ' (verbose)' : '');
}

echo describe(3, null), PHP_EOL;          // value: 3
echo describe(2.5, 'pi-ish', true), PHP_EOL; // pi-ish: 2.5 (verbose)
```

Les scalaires sont `int`, `float`, `string` et `bool`. Les types composés sont `array`, `object`, `callable`, `iterable`, et tout nom de classe ou d'interface. Par-dessus, PHP a une poignée de types qui n'ont de sens qu'à une position : `void` et `never` comme types de retour (`never` signifie que la fonction lève une exception ou quitte le programme), `static` comme type de retour d'une méthode fluide, `self` pour la classe courante, `mixed` quand vous acceptez vraiment n'importe quoi, et `null`, `true`, `false` comme types autonomes depuis PHP 8.2.

Ces types se combinent : `?string` est `string|null`, `int|string` est une union (PHP 8.0), `Countable&Traversable` est une intersection (PHP 8.1) qui exige que l'objet implémente les deux, et `(Countable&Traversable)|null` mélange les deux formes (PHP 8.2). La grammaire s'arrête là, sans génériques, sans tuples et sans typage structurel.

Les types se posent sur les paramètres, les valeurs de retour, les propriétés, et depuis PHP 8.3 sur les constantes de classe :

```php
<?php
declare(strict_types=1);

final class Temperature
{
    public const string UNIT = 'C';

    public function __construct(
        public readonly float $degrees,
    ) {
    }
}

$t = new Temperature(21.5);
var_dump($t->degrees); // float(21.5)
```

Les paramètres et propriétés non typés existent toujours et signifient `mixed`, mais le code moderne ne les laisse pas sans type.

## Ce que `int` accepte vraiment

C'est ici que PHP diffère de tout le reste. **Sans `strict_types`, PHP convertit les arguments scalaires vers le type déclaré quand il le peut.** Passez la chaîne `"12"` à un paramètre `int` et la fonction reçoit l'entier `12` ; passez `"12abc"` et vous obtenez une `TypeError` ; passez `1.5` et vous obtenez `1` avec un avertissement de dépréciation.

| Vous passez | paramètre `int`, mode coercitif | paramètre `int`, mode strict |
|---|---|---|
| `12` | `12` | `12` |
| `"12"` | `12` | `TypeError` |
| `"12abc"` | `TypeError` | `TypeError` |
| `12.0` | `12` | `TypeError` |
| `1.5` | `1`, déprécié depuis 8.1 | `TypeError` |
| `true` | `1` | `TypeError` |
| `null` | `TypeError` (`?int` l'accepte) | `TypeError` (`?int` l'accepte) |

La coercition ne concerne que les scalaires : un tableau n'est jamais transformé en chaîne, ni un objet en entier. Une seule conversion reste permise même en mode strict, celle d'un `int` là où un `float` est attendu, parce qu'elle ne perd jamais d'information.

<img src="images/ch03-strict-gate.png" alt="Un portail avec deux voies vers une fonction. Sur la voie souple, un petit éléphant remodèle une chaîne 12 en nombre 12 avant de la laisser passer. Sur la voie stricte, un éléphant sévère tient un panneau stop devant la même chaîne" width="560">

## L'interrupteur est par fichier, et côté appelant

```php
<?php
declare(strict_types=1);

function double(int $n): int
{
    return $n * 2;
}

echo double(21), PHP_EOL;    // 42
echo double('21'), PHP_EOL;  // TypeError: must be of type int, string given
```

Supprimez la ligne `declare` et le second appel affiche 42. Cet interrupteur a trois propriétés, et chacune surprend quelqu'un.

**Il est par fichier.** Il n'existe ni réglage global, ni option dans `php.ini`, ni paramètre à l'échelle du projet : chaque fichier annonce son propre mode, et un fichier sans la ligne est en mode coercitif.

**Il s'applique aux appels faits depuis le fichier, pas aux fonctions qui y sont définies.** Si `double()` vit dans un fichier strict et qu'un fichier coercitif l'appelle, `double('21')` convertit, parce que c'est l'appelant qui décide. Ce choix est voulu : l'auteur d'une bibliothèque ne peut pas imposer la rigueur au code qui l'appelle, et le code ancien continue de fonctionner quand il appelle une bibliothèque moderne.

**Il couvre aussi les valeurs de retour.** Une fonction en mode strict qui déclare `: int` et renvoie `"42"` lève une exception.

La règle pratique est courte : mettez `declare(strict_types=1);` en tête de chaque fichier que vous écrivez, laissez votre outil de style de code l'imposer, et n'y pensez plus.

> `strict_types` n'est pas « PHP avec les types activés », puisque PHP vérifie toujours les types. L'interrupteur décide seulement si une chaîne qui ressemble à un nombre compte comme un nombre.

## Convertir volontairement

Quand vous voulez une conversion, dites-le :

```php
<?php
declare(strict_types=1);

var_dump((int) '42');        // int(42)
var_dump((int) '42 apples'); // int(42): a cast takes the leading digits
var_dump((int) 'apples');    // int(0)
var_dump((string) 3.0);      // string(1) "3"
var_dump((bool) '0');        // bool(false): "0" is falsy, "0.0" is not
var_dump(intval('0x1A', 16)); // int(26)
```

Les transtypages ne lèvent jamais d'exception et n'émettent jamais d'avertissement : ils font de leur mieux avec ce qu'ils reçoivent. Cela en fait le bon outil pour une entrée utilisateur déjà validée, et le mauvais pour tout ce qui ne l'est pas. Pour vérifier avant de convertir, `is_int()`, `is_string()`, `is_numeric()` et leurs cousines renvoient des booléens, et `filter_var($x, FILTER_VALIDATE_INT)` renvoie l'entier ou `false`.

Pour voir ce que vous tenez, `var_dump()` affiche le type et la valeur. `get_debug_type()` (PHP 8.0) renvoie le nom que vous écririez dans une déclaration (`int`, `string`, `App\User`), là où l'ancien `gettype()` renvoie `integer` et `object`.

## Null et la bibliothèque standard

Vos propres fonctions refusent `null` pour un paramètre non nullable, dans les deux modes. **Les fonctions natives sont plus tolérantes, et cette tolérance est en voie de disparition.** `strlen(null)` renvoie `0` aujourd'hui avec un avertissement de dépréciation (depuis PHP 8.1), et la prochaine version majeure devrait lever une exception. Un code qui lit `strlen($_GET['q'])` sur un paramètre absent vit donc en sursis, alors que `strlen($_GET['q'] ?? '')` continuera de fonctionner.

La même tolérance se voit dans l'autre sens. Là où une fonction renvoyait `false` en cas d'échec, les plus récentes lèvent une `ValueError` (PHP 8.0), et celles qui renvoient encore `false` sont documentées ainsi. Quand la documentation dit `string|false`, testez `false` avec `===` et jamais avec `if (!$result)`, parce que `"0"` et `""` sont faux au sens large, eux aussi.

## Les nombres, brièvement

Un `int` fait 64 bits sur toutes les plateformes que vous rencontrerez, et le dépassement ne boucle pas : **un entier qui déborde devient un flottant**, en silence.

```php
<?php
declare(strict_types=1);

var_dump(PHP_INT_MAX + 1); // float(9.223372036854776E+18)
var_dump(0.1 + 0.2 === 0.3); // bool(false), as in every IEEE 754 language
var_dump(intdiv(7, 2), 7 / 2); // int(3), float(3.5)
```

La division produit toujours un flottant, sauf si les deux opérandes sont des entiers et que le résultat est exact. `intdiv()` donne la division entière, `%` est le modulo entier et `fmod()` celui des flottants. Pour la monnaie ou tout ce qui est décimal, l'extension `bcmath` et sa classe `BcMath\Number` (PHP 8.4) font de l'arithmétique à précision arbitraire.

## Où sont passés les génériques

Le langage n'en a pas. `array` est le type de tout tableau, quel que soit son contenu, et une classe `Collection` ne peut pas dire ce qu'elle collectionne. **L'écosystème a répondu avec des docblocks lus par les analyseurs statiques**, et sur un projet maintenu cette réponse a autant de poids qu'un compilateur :

```php
<?php
declare(strict_types=1);

/**
 * @template T
 * @param list<T> $items
 * @param callable(T): bool $keep
 * @return list<T>
 */
function keep(array $items, callable $keep): array
{
    return array_values(array_filter($items, $keep));
}

/** @var list<int> $evens */
$evens = keep([1, 2, 3, 4], fn (int $n) => $n % 2 === 0);
```

PHP lit `array` et `callable`, tandis que PHPStan et Psalm lisent `list<T>` et `callable(T): bool`, en déduisent que `$evens` contient des entiers, et font échouer le build si vous passez des chaînes. Avec `list<int>`, `array<string, User>`, `non-empty-string` ou `int<1, max>`, le vocabulaire est plus riche que le langage, et les deux outils s'accordent sur l'essentiel. [Tests, analyse statique et outillage](ch12-tooling.md) montre comment en installer un.

<img src="images/ch03-two-readers.png" alt="Une ligne de code avec un docblock au-dessus. Le moteur PHP, dessiné en éléphant, ne lit que la ligne de code. Un second personnage avec une loupe lit le docblock et hoche la tête" width="560">

## Le piège

La première erreur est d'écrire `function f(int $n)` dans un fichier sans `strict_types`, de passer `"12"` dans un test, de voir que ça marche, et d'en conclure que PHP ne vérifie rien, alors qu'il a vérifié et converti dans la foulée. La seconde est l'inverse : ajouter `declare(strict_types=1)` à un fichier et s'attendre à ce que toute l'application devienne stricte, alors que seuls les appels de ce fichier ont changé.

Les deux ont le même remède. La ligne va dans chaque fichier, une règle de style de code l'impose, et un analyseur statique attrape au build les cas que le moteur attraperait en production.

Les tableaux ont été mentionnés trois fois dans ce chapitre sans un mot sur ce qu'ils sont, parce qu'ils ne sont pas ce que votre langage appelle un tableau. [Les tableaux](ch04-arrays.md) remet les choses en place.
