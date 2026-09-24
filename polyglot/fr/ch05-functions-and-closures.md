# Fonctions et closures

**Les fonctions PHP ressemblent à celles de TypeScript avec un `$` devant chaque paramètre, et les closures capturent par valeur, pas par variable.** La première moitié de cette phrase se lit en vitesse, et c'est dans la seconde que se cachent les surprises de ce chapitre.

```php
<?php
declare(strict_types=1);

function greet(string $name, string $greeting = 'Hello', bool $shout = false): string
{
    $text = "$greeting, $name!";
    return $shout ? strtoupper($text) : $text;
}

echo greet('Ada');                       // Hello, Ada!
echo greet('Ada', shout: true);          // HELLO, ADA!
echo greet(greeting: 'Hi', name: 'Ada'); // Hi, Ada!
```

Paramètres et valeurs de retour portent des types, vérifiés à l'exécution comme l'explique [Le système de types](ch03-types.md). Les valeurs par défaut fonctionnent comme partout. **Les arguments nommés (PHP 8.0) permettent de sauter les valeurs par défaut qui ne vous intéressent pas** et rendent lisible un appel à quatre booléens. Positionnels et nommés se mélangent, les positionnels d'abord.

## Variadiques, références et types de retour particuliers

`...` sur le dernier paramètre rassemble le reste dans un tableau ; `...` dans un appel déplie un tableau en arguments, clés de chaîne comprises, ce qui transforme un tableau en arguments nommés :

```php
<?php
declare(strict_types=1);

function sum(int ...$numbers): int
{
    return array_sum($numbers);
}

echo sum(1, 2, 3);        // 6
echo sum(...[4, 5]);      // 9

$options = ['greeting' => 'Hey', 'name' => 'Ada'];
// greet(...$options) would call greet(name: 'Ada', greeting: 'Hey')
```

Un paramètre déclaré `&$x` reçoit une référence, et la fonction écrit alors directement dans la variable de l'appelant. La bibliothèque standard s'en sert pour `sort()`, pour le `$matches` de `preg_match()` et pour quelques autres. Dans votre propre code, préférez renvoyer la valeur, parce qu'une fonction qui modifie ses arguments oblige le lecteur à l'ouvrir pour comprendre ce qu'elle fait.

Les types de paramètres acceptent tout ce que le système de types propose : `?string $label = null` pour une valeur optionnelle, `int|string $id` pour une union, `Countable&Traversable $items` pour une intersection. Écrivez le `?` explicitement, car un simple `string $x = null` fonctionne encore mais est déprécié depuis PHP 8.4. Pour une fonction qui accepte une fonction, vous avez le choix entre `callable`, qui accepte les closures ainsi que les formes chaîne et tableau décrites plus bas, et `Closure`, qui n'accepte que de vrais objets closure. Le code récent tend à déclarer `Closure` et à laisser l'appelant convertir avec `(...)`, parce qu'une `Closure` se vérifie par le typage alors qu'une chaîne échappe à toute vérification.

Les fonctions qui ne reviennent pas normalement disposent de leurs propres types de retour : `void` signifie que rien ne revient, et `never` (PHP 8.1) signifie que la fonction lève toujours une exception ou termine le script, de sorte que les analyseurs statiques savent que le code placé après un appel à `fail()` est inaccessible.

## Les fonctions ne sont pas des valeurs, mais on peut en obtenir une référence

Un nom de fonction n'est pas une expression, et `$f = strlen;` est une erreur de syntaxe. Le contournement historique passait par une chaîne : `$f = 'strlen';` fonctionne parce que le type `callable` accepte un nom de fonction, une paire `[$object, 'method']` ou une chaîne `'Class::method'`. Cette forme marche encore, mais rien ne la vérifie avant l'exécution.

**La façon moderne est la syntaxe de callable de première classe (PHP 8.1) : le nom suivi de `(...)`.**

```php
<?php
declare(strict_types=1);

final class Mailer
{
    public function send(string $to): string
    {
        return "sent to $to";
    }
}

$length = strlen(...);                   // Closure wrapping strlen()
$send = (new Mailer())->send(...);       // Closure bound to that instance

echo $length('hello'); // 5
echo $send('ada@example.org');

var_dump(array_map(strtoupper(...), ['a', 'b'])); // ['A', 'B']
```

Le résultat est un objet `Closure`, la seule valeur de type fonction en PHP. Il est sûr pour le typage comme pour le refactoring, puisque votre éditeur suit le renommage de la méthode, et c'est la forme à passer à `array_map()` et consorts. Quand vous tenez une chaîne plutôt qu'un nom, `Closure::fromCallable('strlen')` produit le même objet.

> Le réflexe du développeur venu d'ailleurs est d'écrire `$this->send` sans parenthèses, ce qui en PHP lit la propriété `send`, qui n'existe pas. La méthode en tant que valeur s'écrit `$this->send(...)`.

## Les closures capturent par valeur

Les fonctions anonymes existent, et vous devez dire ce qu'elles capturent :

```php
<?php
declare(strict_types=1);

$rate = 0.2;

$withTax = function (float $price) use ($rate): float {
    return $price * (1 + $rate);
};

$rate = 0.5; // too late, the closure already copied 0.2

echo $withTax(100.0); // 120
```

**La clause `use` copie les variables au moment où la closure est créée.** Rien de la portée englobante n'est visible sans être listé, et les changements ultérieurs de la variable extérieure n'atteignent pas la closure. Là où JavaScript et Python se referment sur la variable elle-même et afficheraient 150 ici, PHP donne à la closure un instantané pris à sa création.

<img src="images/ch05-closure-snapshot.png" alt="Une closure en cours de création prend une photo de la variable rate qui affiche 0.2 ; ensuite, le rate extérieur passe à 0.5 sur le bureau, mais la closure tient toujours la photo où on lit 0.2" width="560">

Pour capturer la variable plutôt que sa valeur, ajoutez `&` dans la clause, `use (&$rate)`, et la closure partage alors la variable avec la portée extérieure, dans les deux sens. On en a besoin pour un accumulateur, ou pour une closure récursive qui doit se voir elle-même :

```php
$fact = function (int $n) use (&$fact): int {
    return $n <= 1 ? 1 : $n * $fact($n - 1);
};
```

Les fonctions fléchées (PHP 7.4) suppriment la cérémonie. **`fn` capture automatiquement toute la portée englobante, par valeur, et ne contient qu'une seule expression :**

```php
$withTax = fn(float $price): float => $price * (1 + $rate);
```

Il n'y a plus ni `use`, ni `return`, ni accolades, mais la sémantique d'instantané reste la même. La plupart des callbacks que vous écrirez seront des fonctions fléchées, et vous reviendrez à `function () use ()` quand il vous faudra plusieurs instructions ou une capture par référence.

Dans une classe, une closure conserve `$this` automatiquement, comme vous vous y attendez. Marquez-la `static fn` ou `static function` quand elle n'a pas besoin de l'instance, ce qui évite de maintenir l'objet en vie depuis un callback de longue durée. `Closure::bind()` et `$closure->call($object)` rattachent `$this` à un autre objet ; c'est ainsi que les frameworks atteignent un état privé depuis l'extérieur, et vous les écrirez rarement vous-même.

## Générateurs

Une fonction qui contient `yield` renvoie un `Generator` sans exécuter son corps, et chaque tour de `foreach` la fait avancer jusqu'au `yield` suivant. Si vous connaissez les générateurs de Python, vous les retrouvez ici presque ligne pour ligne :

```php
<?php
declare(strict_types=1);

/** @return Generator<int, string> */
function lines(string $path): Generator
{
    $handle = fopen($path, 'r');
    try {
        while (($line = fgets($handle)) !== false) {
            yield rtrim($line, "\n");
        }
    } finally {
        fclose($handle);
    }
}

foreach (lines('/etc/hosts') as $number => $line) {
    echo "$number: $line", PHP_EOL;
}
```

Le fichier est lu une ligne à la fois, quelle que soit sa taille, et fermé quand la boucle se termine ou s'interrompt. **Un générateur est `iterable`, donc toute fonction qui accepte `iterable` le prend sans le savoir.** `yield $key => $value` fixe des clés explicites, `yield from` délègue à un autre générateur ou à un tableau, et un `return` dans un générateur définit une valeur lisible via `getReturn()` une fois l'itération terminée. Un générateur ne s'exécute qu'une fois, et pour itérer à nouveau il faut rappeler la fonction.

## Pipelines

PHP 8.5 ajoute l'opérateur pipe. **`$x |> f(...)` appelle `f($x)`, et les chaînes se lisent de haut en bas au lieu de l'intérieur vers l'extérieur :**

```php
// PHP 8.5
$slug = ' Hello World '
    |> trim(...)
    |> strtolower(...)
    |> (fn(string $s) => str_replace(' ', '-', $s));

echo $slug; // hello-world
```

Chaque étape est n'importe quel callable à un argument, ce qui correspond exactement à ce que produisent la syntaxe de callable de première classe et les fonctions fléchées. Avant 8.5, le même code tenait en trois appels imbriqués ou en trois variables temporaires, deux formes qui fonctionnent toujours et restent courantes.

PHP 8.5 apporte aussi `#[\NoDiscard]`, un attribut pour les fonctions dont la valeur de retour ne doit pas être ignorée. Si vous appelez une telle fonction comme simple instruction, PHP émet un avertissement, et vous transtypez l'appel en `(void)` pour dire que c'est voulu. Les bibliothèques l'utilisent sur les méthodes qui renvoient un nouvel objet immuable, pour éviter le bug classique du `$date->modify()` dont on jette le résultat.

## Les formes anciennes que vous reconnaîtrez

`func_get_args()` et `func_num_args()` lisent les arguments d'une fonction déclarée sans paramètres ; elles précèdent `...$args` et survivent dans le vieux code. `call_user_func()` et `call_user_func_array()` invoquent un callable, ce que `$callable(...$args)` fait aujourd'hui. `create_function()` fabriquait des closures à partir de chaînes et a été supprimée en 8.0. Quand vous croisez ces formes, le remplacement moderne se trouve à une ligne de là, et Rector peut faire la modification pour vous.

> Les closures photographient leurs variables `use`, les fonctions fléchées photographient toute la portée, et une méthode devient une valeur avec `(...)`. Avec ces trois points en tête, les callbacks PHP n'ont plus de surprise en réserve.

Les fonctions portent le comportement, mais les données sur lesquelles elles agissent sont surtout des objets, et le modèle objet de PHP a plus changé ces cinq dernières années que pendant les quinze précédentes. Le chapitre [Les classes](ch06-classes.md) montre à quoi il ressemble aujourd'hui.
