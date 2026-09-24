# B - PHP 8.0 à 8.5 en un coup d'œil

Cette annexe consacre une section à chaque version, avec les nouveautés principales seulement. Trouvez la version de votre projet, puis lisez vers le bas à partir de là pour voir ce que vous pouvez utiliser.

## PHP 8.0, novembre 2020

- Arguments nommés : `str_pad(string: 'a', length: 3)`.
- Attributs : `#[Route('/home')]`, des métadonnées structurées lues par réflexion.
- Promotion de propriétés dans le constructeur : `public function __construct(private int $x) {}`.
- Types union : `int|string $id`.
- Expression `match` : comparaison stricte, pas de fallthrough, exhaustive.
- Opérateur nullsafe : `$user?->address?->city`.
- `mixed` et `static` comme types.
- `throw` comme expression : `$x = $y ?? throw new Exception();`.
- `str_contains()`, `str_starts_with()`, `str_ends_with()`.
- Interface `Stringable`, implémentée automatiquement par toute classe qui définit `__toString()`.
- `WeakMap`.
- Compilateur JIT, à l'intérieur d'OPcache.
- Comparaisons chaîne-nombre assainies : `0 == 'foo'` vaut `false`.
- Virgule finale autorisée dans les listes de paramètres.
- Les fonctions internes lèvent `TypeError` et `ValueError` au lieu d'émettre un avertissement et de renvoyer `null` ou `false`.

## PHP 8.1, novembre 2021

- Énumérations, pures et adossées : `enum Suit: string { case Hearts = 'H'; }`.
- Propriétés `readonly` : `public readonly int $x`.
- Syntaxe de callable de première classe : `strlen(...)`.
- Fibers : des coroutines à pile, la brique de base des bibliothèques asynchrones.
- `new` dans les initialiseurs : `public function __construct(private Logger $l = new NullLogger()) {}`.
- Types intersection purs : `Countable&Traversable`.
- Type de retour `never`.
- Constantes de classe `final`.
- Dépliage de tableaux avec clés textuelles : `[...$defaults, ...$options]`.
- `array_is_list()`.
- Notation octale explicite : `0o16`.

## PHP 8.2, décembre 2022

- Classes `readonly` : `final readonly class Point {}`.
- Types en forme normale disjonctive : `(A&B)|null`.
- Types `true`, `false` et `null` autonomes.
- Propriétés dynamiques dépréciées ; `#[\AllowDynamicProperties]` réautorise une classe.
- `#[\SensitiveParameter]` pour masquer un argument dans les traces d'appel.
- Constantes dans les traits.
- `Random\Randomizer` et l'extension `random`.
- Cas d'énumération utilisables dans les expressions constantes.

## PHP 8.3, novembre 2023

- Constantes de classe typées : `const string NAME = 'x';`.
- Attribut `#[\Override]` : le moteur vérifie qu'une méthode parente existe.
- `json_validate()`.
- Accès dynamique aux constantes de classe : `Foo::{$name}`.
- Les propriétés `readonly` peuvent être réinitialisées dans `__clone()`.
- `Randomizer::getBytesFromString()`, `Randomizer::getFloat()`.
- Les indices négatifs de tableau se comportent de façon cohérente.
- `mb_str_pad()`.

## PHP 8.4, novembre 2024

- Hooks de propriété : `public string $name { get => ...; set => ...; }`.
- Visibilité asymétrique : `public private(set) int $x`.
- `new` sans parenthèses dans un chaînage : `new Foo()->bar()`.
- Objets paresseux : `ReflectionClass::newLazyGhost()`, `newLazyProxy()`.
- Attribut `#[\Deprecated]` pour votre propre code.
- `array_find()`, `array_find_key()`, `array_any()`, `array_all()`.
- `mb_trim()`, `mb_ltrim()`, `mb_rtrim()`, `mb_ucfirst()`, `mb_lcfirst()`.
- Nouvelle extension DOM avec un analyseur HTML5 : `Dom\HTMLDocument`.
- API objet pour BCMath : `BcMath\Number`.
- Sous-classes PDO par pilote : `Pdo\Sqlite`, `Pdo\Mysql`, `Pdo\Pgsql`, via `Pdo::connect()`.
- `request_parse_body()` pour les corps de formulaire quelle que soit la méthode HTTP.
- Paramètres implicitement nullables (`Foo $x = null` sans `?`) dépréciés.
- `exit` et `die` sont désormais des fonctions.

## PHP 8.5, novembre 2025

- Opérateur pipe : `$slug = $title |> trim(...) |> strtolower(...);`.
- `clone` avec mise à jour de propriétés : `clone($point, ['x' => 3])`.
- Attribut `#[\NoDiscard]`, qui avertit quand une valeur de retour est ignorée ; cast `(void)` pour le faire taire volontairement.
- `array_first()`, `array_last()`.
- Closures et callables de première classe dans les expressions constantes (arguments d'attributs, valeurs par défaut, constantes).
- Attributs sur les constantes.
- Nouvelle extension `uri` : `Uri\Rfc3986\Uri`, `Uri\WhatWg\Url`.
- Les erreurs fatales incluent désormais une trace d'appel.
- `get_error_handler()`, `get_exception_handler()`.
- `#[\DelayedTargetValidation]`.
- Constante `PHP_BUILD_DATE`.
- L'opérateur d'exécution shell entre accents graves est déprécié.

## Politique de support

Chaque version reçoit deux ans de support actif (corrections de bugs) suivis de deux ans de correctifs de sécurité seulement. Une version publiée en novembre 2025 est donc en support actif jusqu'à fin 2027 et corrigée jusqu'à fin 2029. Les dates bougent à chaque version, et [php.net/supported-versions](https://www.php.net/supported-versions) tient la table à jour. Faire tourner une version au-delà de sa fenêtre de sécurité est un risque, et mieux vaut le prendre en connaissance de cause que le découvrir après coup.

## Trouver la version de votre projet

`php -v` affiche l'interpréteur que vous exécutez en local. `composer.json` déclare ce que le projet prend en charge sous `require.php` (`"php": "^8.3"`), et `config.platform.php` fige la version contre laquelle Composer résout, celle à croire quand les deux diffèrent. La production peut encore tourner sur autre chose, et seul un `phpinfo()` ou un `php -v` sur le serveur permet de trancher.
