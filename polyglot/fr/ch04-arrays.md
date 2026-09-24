# Les tableaux

**Un tableau PHP est une table de hachage ordonnée, et c'est la seule collection native.** Il joue à la fois le rôle de la liste et du dictionnaire de Python, du tableau et de l'objet de JavaScript, de l'`ArrayList` et de la `LinkedHashMap` de Java. Les clés sont des entiers ou des chaînes, les valeurs sont n'importe quoi, et l'ordre d'insertion est toujours conservé.

```php
<?php
declare(strict_types=1);

$list = ['apple', 'pear'];                  // keys 0, 1
$map  = ['name' => 'Ada', 'born' => 1815];  // string keys
$mixed = [5 => 'five', 'six', 'x' => 'ex']; // keys 5, 6, 'x'

$list[] = 'plum';          // append, key 2
$map['died'] = 1852;       // insert, at the end

var_dump(array_is_list($list)); // true
var_dump(array_is_list($map));  // false
```

Il n'y a pas de type liste à part. Une « liste » est un tableau dont les clés se trouvent être 0, 1, 2 et ainsi de suite, dans cet ordre, et `array_is_list()` (PHP 8.1) vous dit si c'est le cas. La distinction compte quand le tableau quitte PHP : `json_encode()` produit `[...]` pour une liste et `{...}` pour tout le reste.

## Les clés sont normalisées

**Une clé est soit un `int`, soit une `string`, et PHP convertit tout le reste à l'entrée.** Une chaîne numérique devient l'entier qu'elle nomme, un flottant perd ses décimales, un booléen devient 0 ou 1, et `null` devient la chaîne vide :

```php
<?php
declare(strict_types=1);

$a = [];
$a['1'] = 'a';   // key 1, not '1'
$a[1.7] = 'b';   // key 1, overwrites (and a deprecation notice since 8.1)
$a[true] = 'c';  // key 1, overwrites again
$a[null] = 'd';  // key ''

var_dump($a); // [1 => 'c', '' => 'd']
```

Ces trois écritures visent la même clé. La règle rend service quand une base de données renvoie des identifiants sous forme de chaînes, et elle devient un piège quand vous comptiez sur `'1'` et `1` pour former deux entrées distinctes, ce qui n'arrive jamais.

## Lire une clé absente

Lire une clé absente émet un avertissement et renvoie `null`. Deux fonctions vous disent si une clé existe, et elles ne sont pas d'accord sur `null` :

```php
<?php
declare(strict_types=1);

$user = ['name' => 'Ada', 'email' => null];

var_dump(isset($user['email']));            // false: the value is null
var_dump(array_key_exists('email', $user)); // true: the key is there
var_dump(isset($user['phone']));            // false, no warning

$phone = $user['phone'] ?? 'unknown';       // no warning, default applied
```

**`isset()` répond « y a-t-il ici une valeur non nulle ? », `array_key_exists()` répond « la clé est-elle présente ? ».** Dans presque tous les cas, c'est `??` que vous voulez : il lit la clé si elle existe et n'est pas `null`, et se rabat sur la valeur par défaut sinon, en silence.

## Les tableaux sont des valeurs

Si vous ne retenez qu'une chose de ce chapitre, retenez celle-ci. **Affecter un tableau, le passer à une fonction ou le renvoyer produit à chaque fois une copie**, et l'original ne voit jamais ce qui arrive à cette copie.

```php
<?php
declare(strict_types=1);

function addItem(array $cart, string $item): array
{
    $cart[] = $item;
    return $cart;
}

$cart = ['book'];
$bigger = addItem($cart, 'pen');

var_dump(count($cart));   // 1
var_dump(count($bigger)); // 2
```

En JavaScript, en Python ou en Java, `cart` contiendrait maintenant deux éléments, parce que ces langages font circuler une référence vers une structure partagée. En PHP, la fonction a reçu son propre tableau, et pour vous donner le résultat elle doit le renvoyer.

<img src="images/ch04-copy-on-write.png" alt="Un tableau confié à une fonction : la fonction reçoit une photocopie de la feuille pendant que l'original reste intact sur le bureau de l'appelant ; ce n'est que lorsque la fonction écrit sur sa copie que les deux feuilles diffèrent vraiment" width="560">

Le coût est plus faible qu'il n'y paraît, parce que PHP partage la mémoire sous le capot et ne duplique les données qu'à la première écriture, un mécanisme appelé copie à l'écriture. Passer un tableau de dix mille éléments à une fonction qui se contente de le lire ne coûte donc rien.

Vous pouvez y renoncer avec une référence, `&`, sur le paramètre :

```php
function addItemInPlace(array &$cart, string $item): void
{
    $cart[] = $item;
}
```

Réservez cette écriture à la rare boucle critique où la copie se mesure. Une fonction qui renvoie un nouveau tableau se lit, se teste et se type plus facilement, et si la famille `sort()` modifie sur place par référence, c'est une exception héritée de l'histoire du langage plutôt qu'un modèle à suivre.

Les objets se comportent à l'inverse : **une variable objet est un identifiant, et les copies de cet identifiant désignent le même objet**, comme dans tous les langages que vous connaissez. Quand il vous faut une sémantique de référence pour une collection, enveloppez-la dans une classe, ce que le chapitre [Les classes](ch06-classes.md) détaille.

## foreach, par valeur et par référence

`foreach` itère sur une copie, donc modifier `$item` dans la boucle ne change rien :

```php
<?php
declare(strict_types=1);

$prices = [10, 20, 30];

foreach ($prices as $price) {
    $price *= 2; // local copy, the array is untouched
}

foreach ($prices as &$price) {
    $price *= 2; // writes through
}
unset($price); // break the reference

var_dump($prices); // [20, 40, 60]
```

Le `unset()` qui suit la boucle par référence a une vraie fonction : sans lui, `$price` pointe toujours vers le dernier élément, et un `$price = 0;` innocent plus loin dans le fichier écrase `$prices[2]`. La plupart des développeurs PHP se sont fait prendre une fois. Un `foreach` avec `$key => $value` et une écriture dans `$prices[$key]` évite la question, et `array_map()` l'évite tout autant.

## Démonter et remonter des tableaux

La déstructuration fonctionne sur les listes et sur les dictionnaires :

```php
<?php
declare(strict_types=1);

[$x, $y] = [3, 4];
['id' => $id, 'name' => $name] = ['id' => 7, 'name' => 'Ada'];
[, $second] = ['skip', 'keep']; // holes are allowed

$defaults = ['color' => 'blue', 'size' => 'M'];
$order = [...$defaults, 'size' => 'L']; // string keys spread since 8.1

var_dump($order); // ['color' => 'blue', 'size' => 'L']
```

Le dépliage avec des clés chaînes se comporte comme `{...defaults, size: 'L'}` en JavaScript : les dernières entrées gagnent. Avec des clés entières, le dépliage renumérote, donc `[...[1, 2], ...[3]]` vaut `[1, 2, 3]`, et non un dictionnaire avec des clés en double.

## Le trio fonctionnel et ses cousins

`array_map()`, `array_filter()` et `array_reduce()` font ce que leur nom dit, avec chacun sa subtilité :

```php
<?php
declare(strict_types=1);

$orders = [
    ['id' => 1, 'total' => 40, 'paid' => true],
    ['id' => 2, 'total' => 15, 'paid' => false],
    ['id' => 3, 'total' => 90, 'paid' => true],
];

$totals = array_map(fn(array $o) => $o['total'], $orders);       // [40, 15, 90]
$paid   = array_filter($orders, fn(array $o) => $o['paid']);      // keys 0 and 2
$sum    = array_reduce($totals, fn(int $carry, int $t) => $carry + $t, 0); // 145

echo json_encode($paid);                // {"0":{...},"2":{...}}  an object!
echo json_encode(array_values($paid));  // [{...},{...}]          a list
```

**`array_filter()` conserve les clés d'origine.** Après le filtrage d'une liste, les clés ont des trous, `array_is_list()` répond `false` et `json_encode()` produit un objet ; `array_values()` renumérote et remet tout en ordre. Notez aussi l'ordre des arguments, qui place le tableau en premier pour `array_filter()` et `array_reduce()` mais la fonction de rappel en premier pour `array_map()`. Cette incohérence a trente ans, et la complétion de votre éditeur reste le meilleur remède.

PHP 8.4 a ajouté les recherches que vous réécriviez à la main : `array_find()` renvoie le premier élément qui correspond, `array_find_key()` sa clé, `array_any()` et `array_all()` renvoient des booléens. PHP 8.5 a ajouté `array_first()` et `array_last()`, qui renvoient la première et la dernière valeur quelles que soient les clés, à côté des plus anciennes `array_key_first()` et `array_key_last()`.

```php
// PHP 8.4
$firstBig = array_find($orders, fn(array $o) => $o['total'] > 50);
$allPaid  = array_all($orders, fn(array $o) => $o['paid']);   // false
```

Le tri modifie sur place et, depuis PHP 8.0, est stable. `usort()` avec l'opérateur vaisseau spatial est l'idiome :

```php
usort($orders, fn(array $a, array $b) => $b['total'] <=> $a['total']);
```

`sort()` et `usort()` renumérotent les clés ; `asort()` et `uasort()` les conservent ; `ksort()` trie par clé. `array_column($orders, 'total', 'id')` extrait un champ d'une liste de lignes et, avec le troisième argument, indexe le résultat par un autre. `array_combine()`, `array_flip()`, `array_unique()`, `array_slice()` et `array_splice()` sont là aussi, avec `count()` pour la longueur.

Vous croiserez aussi `compact()` et `extract()`, qui transforment des variables locales en tableau et inversement. Il suffit de savoir les reconnaître, parce qu'elles mettent en échec l'analyse statique comme votre éditeur et qu'aucun code récent ne les écrit.

## Itérer sur n'importe quoi

`foreach` ne se limite pas aux tableaux. **Tout ce qui est `iterable` fonctionne : tableaux, générateurs, et objets implémentant `Iterator` ou `IteratorAggregate`.** Une fonction qui accepte `iterable` peut recevoir un générateur d'un million de lignes sans charger le million de lignes, ce que [Fonctions et closures](ch05-functions-and-closures.md) reprend.

```php
<?php
declare(strict_types=1);

function total(iterable $amounts): int
{
    $sum = 0;
    foreach ($amounts as $amount) {
        $sum += $amount;
    }
    return $sum;
}

echo total([1, 2, 3]); // 6
```

## Quand un tableau ne suffit pas

Un tableau ne peut pas dire ce qu'il contient : `array $orders` n'apprend rien au lecteur, et le langage n'a pas d'`array<Order>`. La réponse légère est un docblock, `@param list<Order> $orders`, que PHPStan et Psalm imposent comme un vrai type et que votre éditeur utilise pour la complétion. La réponse plus lourde est une petite classe, une `final class Orders` qui détient un tableau privé, expose exactement les opérations dont vous avez besoin, et implémente les interfaces qui lui permettent de se comporter comme un tableau là où c'est utile : `Countable` pour `count()`, `ArrayAccess` pour `$orders[0]` et `IteratorAggregate` pour `foreach`.

<img src="images/ch04-array-vs-collection.png" alt="À gauche, une caisse ouverte étiquetée array où l'on a jeté n'importe quoi ; à droite, une boîte étiquetée avec une fente typée sur le dessus qui n'accepte que des pièces en forme d'Order, avec un petit compteur et une poignée sur le côté" width="560">

Pour les cas qu'un tableau ne couvre pas, la bibliothèque standard fournit `SplObjectStorage`, qui associe des objets à des données en utilisant l'objet lui-même comme clé, et `WeakMap` (PHP 8.0), qui fait de même sans garder l'objet en vie, ce qui permet aux caches indexés par entité de ne pas fuir.

> Les deux habitudes à perdre ici sont d'attendre d'une fonction qu'elle modifie le tableau que vous lui passez, et d'oublier qu'`array_filter()` laisse des trous. Renvoyez le nouveau tableau, et passez par `array_values()` avant d'encoder.

Les tableaux sont ce que la plupart du code PHP fait circuler, et les fonctions sont ce à quoi il les confie. Comme les closures de PHP capturent leur contexte autrement que celles que vous connaissez, elles méritent leur propre chapitre, [Fonctions et closures](ch05-functions-and-closures.md).
