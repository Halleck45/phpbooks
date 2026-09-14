# Erreurs et exceptions

**PHP a des exceptions, et elles fonctionnent comme celles de Python ou de Java. Il a aussi un mécanisme plus ancien, les erreurs moteur, antérieur aux exceptions et toujours présent.** La pratique moderne consiste à tout faire passer par les exceptions, et ce chapitre montre d'abord ce modèle, puis la poignée de lignes de configuration qui ramènent l'ancien mécanisme dans le même circuit.

## Deux hiérarchies, une racine

Tout ce qui peut être levé avec `throw` et rattrapé avec `catch` implémente `Throwable`, et cette interface se divise en deux familles.

`Error` est ce que le moteur lève quand votre code est faux : `TypeError` pour un mauvais argument, `ValueError` pour un bon type avec une valeur impossible, `ArgumentCountError`, `DivisionByZeroError`, `UnhandledMatchError` quand un `match` ne trouve aucune branche. Vous ne les levez pas vous-même, et vous les rattrapez rarement, parce qu'elles signalent un bug plutôt qu'une situation.

`Exception` est la famille de vos propres erreurs. PHP en livre un petit jeu dans la SPL, dont les noms tiennent lieu de documentation : `InvalidArgumentException`, `RuntimeException`, `LogicException`, `DomainException`, `OutOfRangeException`, `UnexpectedValueException`. Étendez l'une d'elles plutôt qu'`Exception` directement, et vos appelants disposent d'une famille parlante à rattraper.

<img src="images/ch08-throwable-tree.png" alt="Un arbre avec Throwable à la racine qui se sépare en deux branches : Error, dont les feuilles sont TypeError, ValueError et UnhandledMatchError avec une petite icône d'engrenage, et Exception, dont les feuilles sont RuntimeException, InvalidArgumentException et une feuille étiquetée « les vôtres »" width="560">

La syntaxe ne réserve aucune surprise :

```php
<?php
declare(strict_types=1);

function parsePort(string $raw): int
{
    if (!ctype_digit($raw)) {
        throw new InvalidArgumentException("Not a port: $raw");
    }

    return (int) $raw;
}

try {
    $port = parsePort('80a');
} catch (InvalidArgumentException|ValueError $e) {
    echo 'Bad input: ', $e->getMessage(), PHP_EOL;
} finally {
    echo 'Done.', PHP_EOL;
}
```

`|` rattrape plusieurs types dans un même bloc (PHP 7.1). `finally` s'exécute qu'une exception ait été levée ou non. Rattrapez `Throwable` quand vous voulez vraiment tout, par exemple en tête de la boucle d'un worker.

## Exceptions vérifiées et valeurs d'erreur

**Une fonction PHP signale un échec en levant une exception ou en renvoyant `null`.** Rien n'oblige l'appelant à gérer l'un ou l'autre, et rien dans la signature ne liste ce qui peut être levé. Si vous venez de Java, il n'y a pas de clause `throws` ni de vérification à la compilation ; un docblock `@throws` est une courtoisie lue par votre IDE et par PHPStan ou Psalm, pas par le moteur. Si vous venez de Go ou de Rust, il n'y a ni valeur de retour d'erreur ni type `Result` dans le langage. Quelques bibliothèques en proposent un, mais le PHP idiomatique ne s'en sert pas.

Le type de retour nullable plus `??` est l'idiome du « peut-être » :

```php
<?php
declare(strict_types=1);

function findUser(int $id): ?array
{
    return $id === 1 ? ['name' => 'Ada'] : null;
}

$name = findUser(2)['name'] ?? 'anonymous';
echo $name, PHP_EOL; // anonymous
```

La règle courante est de renvoyer `null` quand l'absence est normale et de lever une exception quand elle ne l'est pas. Comme `throw` est une expression (PHP 8.0), les deux se combinent sur une ligne :

```php
$user = findUser($id) ?? throw new RuntimeException("No user $id");
```

## Les exceptions personnalisées transportent des données

Une exception personnalisée est une classe, donc elle peut porter un contexte typé et offrir un constructeur nommé qui compose le message pour vous :

```php
<?php
declare(strict_types=1);

final class InsufficientFunds extends DomainException
{
    public function __construct(
        public readonly int $requested,
        public readonly int $available,
        ?Throwable $previous = null,
    ) {
        parent::__construct(
            "Requested $requested, only $available available",
            previous: $previous,
        );
    }

    public static function forWithdrawal(int $requested, int $available): self
    {
        return new self($requested, $available);
    }
}

try {
    throw InsufficientFunds::forWithdrawal(100, 40);
} catch (InsufficientFunds $e) {
    echo $e->available, PHP_EOL; // 40
}
```

L'argument `previous` sert à chaîner. **Rattrapez une exception de bas niveau, enveloppez-la dans une exception qui a un sens pour votre appelant, et passez l'originale en `previous`.** `getPrevious()` remonte la chaîne, et tous les loggers l'affichent, donc rien ne se perd.

```php
try {
    $pdo->query($sql);
} catch (PDOException $e) {
    throw new RuntimeException('Order lookup failed', previous: $e);
}
```

## L'autre mécanisme

Avant l'existence des exceptions, PHP signalait les problèmes en émettant une erreur d'un niveau donné (notice, warning, fatal) et, pour tout ce qui n'était pas fatal, continuait. L'essentiel de cette machinerie a été replié dans des exceptions `Error` au fil des ans : une division par zéro lève, un argument du mauvais type lève, un appel de méthode sur `null` lève. **Quelques situations émettent encore un warning et continuent** : lire une variable non définie, une clé de tableau absente, une propriété non définie, et toute notice de dépréciation.

```php
<?php
declare(strict_types=1);

$config = [];
echo $config['debug']; // Warning: Undefined array key "debug"
echo 'still running', PHP_EOL;
```

Ce « still running » est précisément ce qu'un développeur venu d'un autre langage n'attend pas. Le remède est un gestionnaire d'erreurs, installé à l'amorçage, qui transforme chaque erreur moteur en exception, et c'est ce que font tous les frameworks :

```php
<?php
declare(strict_types=1);

error_reporting(E_ALL);

set_error_handler(function (int $severity, string $message, string $file, int $line): bool {
    throw new ErrorException($message, 0, $severity, $file, $line);
});

$config = [];
echo $config['debug']; // ErrorException: Undefined array key "debug"
```

<img src="images/ch08-error-handler-funnel.png" alt="De petits papiers étiquetés warning, notice et deprecated tombent d'en haut dans un entonnoir. De son bec sort une seule enveloppe propre, tamponnée du mot exception, qui atterrit dans un bloc try dessiné comme une boîte" width="420">

`ErrorException` est une exception intégrée qui se souvient de la sévérité. À partir de là, il n'y a plus qu'un chemin d'échec, et `try` le rattrape en entier.

Quelques réglages accompagnent ce gestionnaire. `error_reporting(E_ALL)` garantit que rien n'est filtré. `display_errors` vaut `On` en développement et `Off` en production, où les erreurs partent dans le journal : une exception non rattrapée sur une page publique ne doit jamais afficher une trace. `set_exception_handler()` reçoit tout ce qui atteint le sommet sans avoir été rattrapé, et c'est là que vous journalisez et affichez une page d'erreur générique. PHP 8.5 ajoute `get_error_handler()` et `get_exception_handler()` pour qu'une bibliothèque puisse inspecter ce qui est installé avant de l'envelopper.

## Ce qui ne se rattrape pas

Les erreurs fatales terminent la requête sans qu'aucun `catch` ne les voie : mémoire épuisée, `max_execution_time` dépassé, même classe déclarée deux fois. Une erreur de syntaxe dans un fichier inclus, en revanche, est une `ParseError` que vous pouvez rattraper depuis PHP 7. S'il faut réagir, `register_shutdown_function()` s'exécute après l'arrêt du script, et `error_get_last()` vous dit si l'arrêt était propre. Depuis PHP 8.5, une erreur fatale affiche une trace d'appels, et une mémoire épuisée en production pointe enfin vers une ligne.

## L'opérateur `@` et `assert()`

Vous croiserez `@` dans du code ancien : `@file_get_contents($url)`. **Il réduit au silence tout warning émis par l'expression.** Votre gestionnaire d'erreurs est toujours appelé, mais `error_reporting()` y renvoie un masque réduit, ce qui permet au gestionnaire de savoir que `@` a été utilisé. Considérez cet opérateur comme un signal d'alerte quand vous le croisez. Le seul usage défendable entoure une fonction qui émet un warning et renvoie `false` en cas d'échec, immédiatement suivi d'un test sur cette valeur de retour. Même là, un `try` autour d'une alternative qui lève une exception se lit mieux.

`assert()` mérite aussi d'être reconnu. C'est une vérification de développement, retirée en production quand `zend.assertions` vaut `-1` dans `php.ini`, la valeur recommandée pour la production. Servez-vous-en pour des invariants qui documentent une intention, jamais pour valider une entrée.

## Le piège

Les deux erreurs classiques sont silencieuses. La première consiste à rattraper `Exception` dans un gestionnaire de haut niveau et à croire que l'on a tout rattrapé, alors qu'une `TypeError` est une `Error` et non une `Exception`, et qu'elle passe donc tout droit devant ce bloc. À la frontière de l'application, c'est `Throwable` qu'il faut rattraper.

La seconde est le catch vide :

```php
try {
    $cache->delete($key);
} catch (Throwable) {
}
```

La variable peut être omise (PHP 8.0), ce qui rend le bloc honnête sur le fait qu'il ignore l'exception, et il y a des cas où ignorer est le bon choix. Mais un catch vide autour de quoi que ce soit d'important est la façon la plus sûre de cacher un bug pendant un an, alors journalisez au minimum ce que vous ignorez.

> Tout ce qui tourne mal doit vous parvenir sous la forme d'une exception, en un seul endroit. PHP le fait, à condition de le lui demander.

Ce gestionnaire, et chaque classe que vous levez, vivent dans des fichiers que PHP doit trouver. [Namespaces, Composer et autoloading](ch09-composer-and-namespaces.md) explique comment il les trouve.
