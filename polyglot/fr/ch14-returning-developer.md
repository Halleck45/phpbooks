# Revenir à PHP après des années

Vous avez écrit du PHP il y a des années, peut-être beaucoup, en 2008 ou en 2015 sur un projet qui était déjà vieux à l'époque. Vous vous souvenez de `mysql_query`, de `array()`, du `require_once` en tête de chaque fichier, et d'un langage qui laissait tout passer. Maintenant que vous y revenez, la première chose à savoir est que **presque toutes les habitudes dont vous vous souvenez ont un remplaçant moderne, et que la plupart des anciennes formes sont dépréciées ou supprimées.**

Ce chapitre est une liste de paires qui met en regard ce dont vous vous souvenez et ce que vous écrivez aujourd'hui. Le reste du livre détaille chaque remplaçant, et ce chapitre sert de carte pour s'y retrouver.

<img src="images/ch14-before-after.png" alt="Deux colonnes de code sur un tableau blanc. Colonne de gauche, barrée à l'encre : mysql_query, array(), require_once, global. Colonne de droite, en bleu : PDO, crochets, autoload de Composer, injection par le constructeur. Un petit éléphant tient le marqueur" width="560">

## La base de données

Vous vous souvenez d'avoir assemblé du SQL à la main pour le passer à `mysql_query()`. **Les fonctions `mysql_*` ont été supprimées en PHP 7.0**, si bien que le code qui les appelle ne tourne sur aucune version encore maintenue du langage. Le remplaçant est PDO avec des requêtes préparées, ce qui referme au passage la faille d'injection que l'ancien style ouvrait :

```php
<?php
declare(strict_types=1);

// then
// $result = mysql_query("SELECT * FROM users WHERE id = " . $_GET['id']);

// now
$pdo = new PDO('sqlite::memory:', options: [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
$stmt = $pdo->prepare('SELECT * FROM users WHERE id = :id');
$stmt->execute(['id' => (int) ($_GET['id'] ?? 0)]);
$user = $stmt->fetch(PDO::FETCH_ASSOC);
```

`mysqli` existe toujours et fonctionne très bien, mais PDO parle à toutes les bases avec une seule API. [Une requête web, sans framework](ch11-web-request.md) le montre en situation.

## Charger le code

Vous vous souvenez d'un mur de lignes `require_once`, ou d'une fonction `__autoload()` maison. **Aujourd'hui, une seule ligne charge tout : `require __DIR__ . '/vendor/autoload.php';`.** Composer génère ce fichier à partir d'une correspondance espace de noms vers dossier déclarée dans `composer.json`, et `__autoload()` elle-même a été supprimée en 8.0. Les classes vivent à raison d'une par fichier, nommé d'après la classe, et sont trouvées à la première utilisation. [Namespaces, Composer et autoloading](ch09-composer-and-namespaces.md) décrit la mise en place, qui prend cinq minutes.

Composer a aussi remplacé l'habitude de copier une bibliothèque dans son projet. Depuis 2012, `composer require vendor/package` la récupère sur Packagist, fige la version dans un fichier de verrouillage, et la met à jour quand vous le demandez.

## Une syntaxe qui a raccourci

Ce sont de petits changements, mais vous les verrez sur chaque ligne.

```php
// then
$list = array(1, 2, 3);
$name = isset($_GET['n']) ? $_GET['n'] : 'anon';
$double = function ($x) use ($factor) {
    return $x * $factor;
};
$callback = array($obj, 'method');
call_user_func_array($callback, array(1));
```

```php
// now
$list = [1, 2, 3];
$name = $_GET['n'] ?? 'anon';
$double = fn($x) => $x * $factor;
$callback = $obj->method(...);
$callback(1);
```

`[]` est arrivé en 5.4, `??` en 7.0, les fonctions fléchées `fn` en 7.4, et la syntaxe de callable de première classe `$obj->method(...)` en 8.1. Les callables sous forme de chaîne comme `'Class::method'` et `call_user_func()` fonctionnent toujours ; plus personne ne les écrit, parce que la nouvelle forme est vérifiée par l'éditeur et par l'analyseur, et qu'un callable s'appelle tout simplement avec des parenthèses.

## Les types

Vous vous souvenez de fonctions qui acceptaient n'importe quoi et renvoyaient ce qui venait. **Aujourd'hui les fonctions déclarent leurs types, et une ligne par fichier oblige PHP à les faire respecter.**

```php
<?php
declare(strict_types=1);

// then
// function total($items, $rate) { ... }

// now
function total(array $items, float $rate): float
{
    return array_sum($items) * $rate;
}

total([10, 20], '1.2'); // TypeError: must be of type float, string given
```

Les types scalaires sont arrivés en 7.0, les types de retour avec eux, le nullable `?int` en 7.1, les types union en 8.0, et les propriétés typées en 7.4. `declare(strict_types=1)` désactive la conversion silencieuse pour les appels faits depuis ce fichier. [Le système de types](ch03-types.md) donne les règles précises.

## Flux de contrôle et constantes

Vous vous souvenez de `switch`, de son fallthrough et de sa comparaison lâche, et d'une classe remplie de `const STATUS_ACTIVE = 'active';`. **`match` a remplacé le premier, les énumérations le second.**

```php
<?php
declare(strict_types=1);

enum Status: string
{
    case Active = 'active';
    case Archived = 'archived';
}

function label(Status $status): string
{
    return match ($status) {
        Status::Active => 'In use',
        Status::Archived => 'Put away',
    };
}
```

`match` (8.0) compare avec `===`, ne traverse pas les branches, et lève une exception si aucune ne convient. Les énumérations (8.1) sont de vrais types : une fonction typée `Status` ne peut pas recevoir la chaîne `'deleted'`. [Énumérations et match](ch07-enums-and-match.md) va plus loin.

## Les classes

Vous vous souvenez d'une propriété privée, d'un getter et d'un setter, multipliés par dix dans chaque classe. **La promotion de propriétés dans le constructeur et `readonly` ramènent tout cela à une ligne par propriété.**

```php
<?php
declare(strict_types=1);

final class Money
{
    public function __construct(
        public readonly int $cents,
        public readonly string $currency,
    ) {
    }
}

$price = new Money(1999, 'EUR');
echo $price->cents; // 1999
$price->cents = 0;  // Error: Cannot modify readonly property
```

La promotion est arrivée en 8.0, `readonly` en 8.1. Les hooks de propriété (PHP 8.4) couvrent le cas où un getter calculait vraiment quelque chose, en attachant des blocs `get` et `set` à la propriété elle-même. [Les classes](ch06-classes.md) montre tout cela.

Parmi ce dont vous vous souvenez, deux pratiques sont désormais supprimées ou dépréciées. Les constructeurs à la PHP 4, où la méthode portait le nom de la classe, ont été supprimés en 8.0. Les propriétés dynamiques, affecter `$obj->whatever` sans l'avoir déclarée, sont dépréciées depuis 8.2 et doivent devenir une erreur dans la prochaine version majeure.

## Les erreurs

Vous vous souvenez de `@mysql_connect(...) or die('no db')`, et d'avertissements imprimés au beau milieu de la page. **Aujourd'hui les erreurs sont des exceptions, et vous les rattrapez.** Les fonctions internes lèvent `TypeError` et `ValueError` au lieu de renvoyer `false` avec un avertissement, la division par zéro lève une exception, et les frameworks convertissent les avertissements restants en exceptions avec un gestionnaire d'erreurs. `@` existe toujours, mais considérez-le comme le signe d'un problème à corriger. [Erreurs et exceptions](ch08-errors-and-exceptions.md) explique la hiérarchie.

## Les globales

Vous vous souvenez de `global $db;` en tête de chaque fonction. **Aujourd'hui la dépendance entre par le constructeur.**

```php
<?php
declare(strict_types=1);

final class UserRepository
{
    public function __construct(private readonly PDO $pdo)
    {
    }
}
```

L'objet qui a besoin d'une base de données en reçoit une, ce qui permet de le tester avec une autre. Les frameworks automatisent ce câblage avec un conteneur, mais l'idée elle-même n'en a pas besoin.

`register_globals`, qui transformait chaque paramètre de requête en variable, a été supprimé en 5.4. `$_REQUEST` existe toujours et personne ne s'en sert : lisez `$_GET` ou `$_POST` et dites lequel vous voulez. `extract()` et les variables variables (`$$name`) restent légales et n'apparaissent dans aucune base de code moderne.

## Texte et dates

Vous vous souvenez de `date('Y-m-d', $timestamp)` et de `utf8_encode()`. **Les dates sont des objets `DateTimeImmutable`, et le texte est en UTF-8 partout.**

```php
<?php
declare(strict_types=1);

$due = new DateTimeImmutable('2026-03-01', new DateTimeZone('UTC'));
echo $due->modify('+30 days')->format('Y-m-d'); // 2026-03-31
```

`utf8_encode()` et `utf8_decode()` n'ont jamais géré que le Latin-1 et sont dépréciées depuis 8.2 ; `mb_convert_encoding()` fait le travail pour n'importe quel encodage. `ereg_*` a été supprimé en 7.0, `preg_*` est resté. La forme `${var}` d'interpolation dans les chaînes est dépréciée depuis 8.2 ; écrivez `{$var}`. [Chaînes, nombres, dates et JSON](ch10-standard-library.md) a le reste.

## Petites choses disparues

- `each()` et `create_function()`, supprimées en 8.0. Utilisez `foreach` et les closures.
- Le cast `(unset)`, supprimé en 8.0.
- Les paramètres implicitement nullables, `Foo $x = null` sans le `?`, dépréciés en 8.4. Écrivez `?Foo $x = null`.
- `split()`, supprimée en 7.0. Utilisez `explode()` ou `preg_split()`.
- `mb_internal_encoding('UTF-8')` en tête des fichiers. Le défaut est UTF-8 depuis 5.6.

## Faire passer une base de code PHP 5 sur PHP 8

Elle ne tournera pas telle quelle, les appels `mysql_*` à eux seuls le garantissent. La partie mécanique, au moins, est automatisée : **Rector réécrit l'ancienne syntaxe en syntaxe nouvelle**, version par version, à partir d'une configuration qui nomme votre cible. Pointez-le sur le code, relisez le diff, lancez les tests que vous avez, espérons-le, et recommencez. PHPStan ou Psalm trouvent ensuite ce que Rector n'a pas pu faire. [Tests, analyse statique et outillage](ch12-tooling.md) présente les deux.

Prévoyez ce travail dans votre planning, car un site qui tourne encore sous PHP 5 aujourd'hui utilise une version qui ne reçoit plus de correctifs de sécurité depuis 2018, et il représente un risque avant même d'être une base de code.

## Le rythme des versions

PHP publie désormais une version mineure chaque novembre : 8.0 en 2020, 8.1 en 2021, et ainsi de suite jusqu'à 8.5 en 2025. Chaque version reçoit deux ans de support actif puis deux ans de correctifs de sécurité ; [php.net/supported-versions](https://www.php.net/supported-versions) donne les dates. Une version par an, c'est une petite liste de dépréciations à lire chaque année, et une base de code qui ne s'éloigne jamais beaucoup du présent.

> Jugez le langage sur ses notes de version plutôt que sur la base de code que vous retrouvez, parce que cette base de code est une photo de l'époque où elle a été écrite, alors que le langage a continué d'avancer.

[Pour aller plus loin](ch15-where-to-go.md) liste les endroits où vous tenir à jour.
