# B - Les versions de PHP, 2015 à 2026

Chaque version a sa section ci-dessous, avec sa date de sortie, sa fenêtre de support et ses changements marquants. Les dates viennent de php.net (pages des versions supportées, des fins de vie et des changelogs, vérifiées le 17 septembre 2026). Le support actif couvre les corrections de bugs et les correctifs de sécurité, le support de sécurité les correctifs de sécurité seulement. Depuis la mise à jour du cycle de publication votée en 2024, les deux fenêtres se terminent le 31 décembre de leur dernière année.

| Version | Sortie | Support actif jusqu'au | Support de sécurité jusqu'au |
|---|---|---|---|
| PHP 5.6 | 28 août 2014 | 19 janv. 2017 | 31 déc. 2018 |
| PHP 7.0 | 3 déc. 2015 | 3 déc. 2017 | 10 janv. 2019 |
| PHP 7.1 | 1er déc. 2016 | 1er déc. 2018 | 1er déc. 2019 |
| PHP 7.2 | 30 nov. 2017 | 30 nov. 2019 | 30 nov. 2020 |
| PHP 7.3 | 6 déc. 2018 | 6 déc. 2020 | 6 déc. 2021 |
| PHP 7.4 | 28 nov. 2019 | 28 nov. 2021 | 28 nov. 2022 |
| PHP 8.0 | 26 nov. 2020 | 26 nov. 2022 | 26 nov. 2023 |
| PHP 8.1 | 25 nov. 2021 | 25 nov. 2023 | 31 déc. 2025 |
| PHP 8.2 | 8 déc. 2022 | 31 déc. 2024 | 31 déc. 2026 |
| PHP 8.3 | 23 nov. 2023 | 31 déc. 2025 | 31 déc. 2027 |
| PHP 8.4 | 21 nov. 2024 | 31 déc. 2026 | 31 déc. 2028 |
| PHP 8.5 | 20 nov. 2025 | 31 déc. 2027 | 31 déc. 2029 |

Ce qu'il faut retenir du tableau, ce sont onze versions annuelles consécutives, chacune sortie entre le 20 novembre et le 8 décembre. Le calendrier de la suivante paraît sur wiki.php.net des mois à l'avance, avec ses dates de gel des fonctionnalités et de release candidate.

## PHP 7.0, décembre 2015

- Nouveau moteur, avec une forte réduction de l'usage mémoire et, sur le travail propre de l'interpréteur, à peu près deux fois la vitesse de PHP 5.6 ; voir [Débit et latence](ch03-throughput-and-latency.md) pour l'affirmation de l'éditeur et la mesure synthétique indépendante, avec leurs réserves.
- Déclarations de types scalaires (`int`, `float`, `string`, `bool`) pour les paramètres, et déclarations de types de retour.
- `declare(strict_types=1)`.
- Opérateur de fusion null `??`, opérateur spaceship `<=>`.
- Classes anonymes.
- Les erreurs du moteur deviennent des exceptions (hiérarchie `Error`), si bien qu'une erreur fatale peut être attrapée.
- Suppression des fonctions `mysql_*`, des fonctions `ereg_*` et des constructeurs à la PHP 4.

## PHP 7.1 à 7.4, 2016 à 2019

- 7.1 : types nullables (`?int`), type de retour `void`, `iterable`, visibilité des constantes de classe.
- 7.2 : type `object`, hachage de mots de passe Argon2, Libsodium dans le cœur.
- 7.3 : syntaxe heredoc assouplie, `is_countable()`, erreurs JSON sous forme d'exceptions.
- 7.4 : propriétés typées, fonctions fléchées (`fn`), préchargement OPcache, interface de fonctions étrangères (FFI), opérateur `??=`, retours covariants et paramètres contravariants.

## PHP 8.0, novembre 2020

- Arguments nommés : `str_pad(string: 'a', length: 3)`.
- Attributs : `#[Route('/home')]`, des métadonnées structurées lues par réflexion.
- Promotion de propriétés dans le constructeur : `public function __construct(private int $x) {}`.
- Types union : `int|string $id`.
- Expression `match` : comparaison stricte, pas de fallthrough, exhaustive.
- Opérateur nullsafe : `$user?->address?->city`.
- `mixed` et `static` comme types.
- `throw` comme expression.
- `str_contains()`, `str_starts_with()`, `str_ends_with()`.
- Interface `Stringable`, `WeakMap`.
- Compilateur JIT, à l'intérieur d'OPcache.
- Comparaisons chaîne-nombre assainies : `0 == 'foo'` vaut `false`.
- Les fonctions internes lèvent `TypeError` et `ValueError` au lieu d'émettre un avertissement et de renvoyer `null` ou `false`.

## PHP 8.1, novembre 2021

- Énumérations, pures et adossées.
- Propriétés `readonly`.
- Syntaxe de callable de première classe : `strlen(...)`.
- Fibers : des coroutines à pile, la brique de base des bibliothèques asynchrones.
- `new` dans les initialiseurs.
- Types intersection purs : `Countable&Traversable`.
- Type de retour `never`, constantes de classe `final`, `array_is_list()`, notation octale explicite.

## PHP 8.2, décembre 2022

- Classes `readonly`.
- Types en forme normale disjonctive : `(A&B)|null`.
- Types `true`, `false` et `null` autonomes.
- Propriétés dynamiques dépréciées ; `#[\AllowDynamicProperties]` réautorise une classe.
- `#[\SensitiveParameter]` pour masquer un argument dans les traces d'appel.
- Constantes dans les traits, `Random\Randomizer`.

## PHP 8.3, novembre 2023

- Constantes de classe typées.
- Attribut `#[\Override]` : le moteur vérifie qu'une méthode parente existe.
- `json_validate()`.
- Accès dynamique aux constantes de classe : `Foo::{$name}`.
- Les propriétés `readonly` peuvent être réinitialisées dans `__clone()`.

## PHP 8.4, novembre 2024

- Hooks de propriété : la logique `get` et `set` déclarée sur la propriété elle-même.
- Visibilité asymétrique : `public private(set) int $x`.
- `new Foo()->bar()` sans parenthèses englobantes.
- Objets paresseux via la réflexion (`newLazyGhost()`, `newLazyProxy()`).
- Attribut `#[\Deprecated]`.
- `array_find()`, `array_find_key()`, `array_any()`, `array_all()`.
- `mb_trim()` et consorts, `mb_ucfirst()`, `mb_lcfirst()`.
- Nouvelle extension DOM avec un analyseur HTML5 (`Dom\HTMLDocument`).
- API objet pour BCMath (`BcMath\Number`), sous-classes PDO par pilote (`Pdo\Sqlite`, `Pdo\Mysql`, `Pdo\Pgsql`).
- Types de paramètres implicitement nullables dépréciés.

## PHP 8.5, novembre 2025

- Opérateur pipe : `$value |> trim(...) |> strtoupper(...)`.
- `clone` avec mise à jour de propriétés : `clone($obj, ['prop' => $value])`.
- Attribut `#[\NoDiscard]`, avec le cast `(void)` pour le faire taire volontairement.
- `array_first()`, `array_last()`.
- Closures et callables de première classe dans les expressions constantes (arguments d'attributs, valeurs par défaut, constantes).
- Attributs sur les constantes.
- Nouvelle extension `uri` (`Uri\Rfc3986\Uri`, `Uri\WhatWg\Url`).
- Les erreurs fatales incluent une trace d'appel.
- `get_error_handler()`, `get_exception_handler()`.
- L'opérateur d'exécution shell entre accents graves est déprécié.
