# H - Fonctionnalités PHP couvertes

Chaque chapitre de ce livre introduit un morceau de PHP : un mot-clé, un opérateur, une interface native, un mécanisme du langage. Cette annexe les rassemble en une seule liste, chacun relié à son entrée dans le [PHP Dictionary](https://php-dictionary.readthedocs.io/en/latest/), une référence indépendante et en croissance constante des termes, mots-clés, fonctions et du jargon de PHP. Servez-vous-en comme d'un glossaire : quand un terme d'un chapitre précédent revient et que vous voulez la version courte, sans avoir à retrouver le chapitre qui l'a introduit.

Quelques éléments ci-dessous n'ont pas encore d'entrée dans le dictionnaire. Ils sont listés quand même, tels quels, sans lien.

## Syntaxe et bases

- [Balise d'ouverture `<?php`](https://php-dictionary.readthedocs.io/en/latest/index/php-tag.html) : fait passer l'analyseur du mode HTML au mode PHP.
- [Balise courte d'affichage `<?= ?>`](https://php-dictionary.readthedocs.io/en/latest/index/echo-tag.html) : raccourci qui combine `<?php` et un `echo` immédiat.
- [`echo`](https://php-dictionary.readthedocs.io/en/latest/index/echo.html) et [`print`](https://php-dictionary.readthedocs.io/en/latest/index/print.html) : les constructions d'affichage, traitées au [chapitre 1](ch01-02-hello-world.md).
- [Interpolation de chaînes](https://php-dictionary.readthedocs.io/en/latest/index/interpolation.html) : insérer des variables directement dans une chaîne entre guillemets doubles.
- [Commentaires](https://php-dictionary.readthedocs.io/en/latest/index/comment.html) et [docblocks](https://php-dictionary.readthedocs.io/en/latest/index/docblock.html) : `//`, `#`, `/* */`, et la forme structurée `/** */` que les outils lisent, au [chapitre 3](ch03-04-comments.md).

## Types et comparaison

- [Conversion implicite de type](https://php-dictionary.readthedocs.io/en/latest/index/type-juggling.html) : la conversion automatique entre types que PHP effectue selon le contexte.
- [Transtypage](https://php-dictionary.readthedocs.io/en/latest/index/cast.html) : la conversion explicite avec `(int)`, `(string)` et les autres.
- [Booléen](https://php-dictionary.readthedocs.io/en/latest/index/boolean.html), [`gettype()`](https://php-dictionary.readthedocs.io/en/latest/index/gettype.html), [`var_dump()`](https://php-dictionary.readthedocs.io/en/latest/index/var_dump.html) : le système de types scalaires et comment l'inspecter, au [chapitre 3](ch03-02-data-types.md).
- [`declare(strict_types=1)`](https://php-dictionary.readthedocs.io/en/latest/index/strict_types.html) : désactive la coercition implicite des scalaires pour un fichier.
- [Opérateur d'identité `===`](https://php-dictionary.readthedocs.io/en/latest/index/identical.html), [opérateur d'égalité `==`](https://php-dictionary.readthedocs.io/en/latest/index/equal.html), [comparaison souple](https://php-dictionary.readthedocs.io/en/latest/index/relaxed-comparison.html) : les deux familles de comparaison et là où elles divergent.
- [Opérateur vaisseau spatial `<=>`](https://php-dictionary.readthedocs.io/en/latest/index/spaceship.html) : comparaison à trois issues, renvoie `-1`, `0` ou `1`.
- [Types union](https://php-dictionary.readthedocs.io/en/latest/index/union-type.html) : un type de paramètre ou de retour exprimé comme `int|string`.
- [`TypeError`](https://php-dictionary.readthedocs.io/en/latest/index/typeerror.html) : levée quand une valeur ne respecte pas une déclaration de type.
- [Tableau](https://php-dictionary.readthedocs.io/en/latest/index/array.html) : l'unique type composé de PHP, à la fois liste et dictionnaire, au [chapitre 8](ch08-01-indexed-arrays.md).
- [`array_key_exists()`](https://php-dictionary.readthedocs.io/en/latest/index/array_key_exists.html) et [`isset()`](https://php-dictionary.readthedocs.io/en/latest/index/isset.html) : vérifier la présence d'une clé, ou la présence d'une valeur non nulle.

## Structures de contrôle

- [`if` / `elseif` / `else`](https://php-dictionary.readthedocs.io/en/latest/index/if-then.html) et les [structures conditionnelles](https://php-dictionary.readthedocs.io/en/latest/index/conditional-structure.html) en général.
- [`while`](https://php-dictionary.readthedocs.io/en/latest/index/while.html), [`do`-`while`](https://php-dictionary.readthedocs.io/en/latest/index/do-while.html), [`for`](https://php-dictionary.readthedocs.io/en/latest/index/for.html), [`foreach`](https://php-dictionary.readthedocs.io/en/latest/index/foreach.html) : les boucles, au [chapitre 3](ch03-05-control-flow.md).
- [`break`](https://php-dictionary.readthedocs.io/en/latest/index/break.html) et [`continue`](https://php-dictionary.readthedocs.io/en/latest/index/continue.html) : sortir d'une boucle ou passer au tour suivant, avec leur argument numérique facultatif pour les boucles imbriquées.
- [`switch`](https://php-dictionary.readthedocs.io/en/latest/index/switch.html) et [`match`](https://php-dictionary.readthedocs.io/en/latest/index/match.html) : les deux constructions de branchement par comparaison, l'une instruction, l'autre expression, traitées ensemble au [chapitre 6](ch06-02-match.md) puis comme syntaxe de motifs au [chapitre 19](ch19-03-match-syntax.md).
- [`list()` / déstructuration de tableau](https://php-dictionary.readthedocs.io/en/latest/index/list.html) et la [déstructuration](https://php-dictionary.readthedocs.io/en/latest/index/destructuring.html) en général : décomposer un tableau en variables séparées en une seule étape, au [chapitre 19](ch19-02-destructuring.md).

## Fonctions et closures

- Déclarations de fonctions, [types de retour](https://php-dictionary.readthedocs.io/en/latest/index/return-type.html) et [valeurs par défaut des paramètres](https://php-dictionary.readthedocs.io/en/latest/index/default-value.html).
- [`void`](https://php-dictionary.readthedocs.io/en/latest/index/void.html) : un type de retour qui déclare qu'une fonction ne renvoie rien d'utile.
- [Arguments nommés](https://php-dictionary.readthedocs.io/en/latest/index/named-parameter.html) : appeler une fonction par le nom des paramètres plutôt que par leur position.
- [Passage par référence](https://php-dictionary.readthedocs.io/en/latest/index/by-reference.html) et [passage par valeur](https://php-dictionary.readthedocs.io/en/latest/index/by-value.html) : si une fonction peut ou non modifier la variable de l'appelant.
- [Fonctions anonymes](https://php-dictionary.readthedocs.io/en/latest/index/anonymous-function.html) et [closures](https://php-dictionary.readthedocs.io/en/latest/index/closure.html) : les fonctions comme valeurs, avec capture de variables via `use`, au [chapitre 15](ch15-01-closures.md).
- [Fonctions fléchées (`fn`)](https://php-dictionary.readthedocs.io/en/latest/index/arrow-function.html) : des closures à une seule expression, avec capture implicite de la portée englobante.
- [Syntaxe des callables de première classe `foo(...)`](https://php-dictionary.readthedocs.io/en/latest/index/first-class-callable.html) : transformer la référence à une fonction ou une méthode nommée en véritable `Closure`.
- [Générateurs](https://php-dictionary.readthedocs.io/en/latest/index/generator.html) et [`yield`](https://php-dictionary.readthedocs.io/en/latest/index/yield.html) : des fonctions qui produisent leurs valeurs paresseusement, une à la fois, au [chapitre 15](ch15-02-generators.md).

## Classes et objets

- [Déclarations de classes](https://php-dictionary.readthedocs.io/en/latest/index/class.html), [`new`](https://php-dictionary.readthedocs.io/en/latest/index/new.html), [`instanceof`](https://php-dictionary.readthedocs.io/en/latest/index/instanceof.html), [`clone`](https://php-dictionary.readthedocs.io/en/latest/index/clone.html) : le vocabulaire de base de la création d'objets.
- [Visibilité](https://php-dictionary.readthedocs.io/en/latest/index/visibility.html) (`public`, `protected`, `private`) : contrôler l'accès aux propriétés et aux méthodes.
- [Promotion de propriétés dans le constructeur](https://php-dictionary.readthedocs.io/en/latest/index/promoted-property.html) et [propriétés `readonly`](https://php-dictionary.readthedocs.io/en/latest/index/readonly.html) : construction raccourcie et propriétés à écriture unique, au [chapitre 5](ch05-01-defining-classes.md).
- [Propriétés typées](https://php-dictionary.readthedocs.io/en/latest/index/type-declaration-property.html) : déclarer le type d'une propriété dès le départ.
- [Propriétés et méthodes `static`](https://php-dictionary.readthedocs.io/en/latest/index/static.html), [variables statiques](https://php-dictionary.readthedocs.io/en/latest/index/static-variable.html) et [liaison statique tardive](https://php-dictionary.readthedocs.io/en/latest/index/late-static-binding.html) : les différents travaux, sans rapport entre eux, du mot-clé `static`.
- [Héritage](https://php-dictionary.readthedocs.io/en/latest/index/inheritance.html), [`extends`](https://php-dictionary.readthedocs.io/en/latest/index/extends.html) et [`parent::`](https://php-dictionary.readthedocs.io/en/latest/index/parent.html) : bâtir une classe sur une autre, au [chapitre 17](ch17-01-inheritance-and-polymorphism.md).
- [Classes abstraites](https://php-dictionary.readthedocs.io/en/latest/index/abstract-class.html) et [méthodes abstraites](https://php-dictionary.readthedocs.io/en/latest/index/abstract-method.html) : des classes de base qu'on ne peut pas instancier seules.
- [Interfaces](https://php-dictionary.readthedocs.io/en/latest/index/interface.html) et [traits](https://php-dictionary.readthedocs.io/en/latest/index/trait.html) : contrat partagé contre implémentation partagée, au [chapitre 11](ch11-01-interfaces.md).
- [Constructeur (`__construct`)](https://php-dictionary.readthedocs.io/en/latest/index/constructor.html), [destructeur (`__destruct`)](https://php-dictionary.readthedocs.io/en/latest/index/destructor.html) et les autres méthodes magiques : [`__toString()`](https://php-dictionary.readthedocs.io/en/latest/index/__tostring.html), [`__get()` / `__set()`](https://php-dictionary.readthedocs.io/en/latest/index/__get.html), [`__call()`](https://php-dictionary.readthedocs.io/en/latest/index/__call.html), traitées au [chapitre 17](ch17-03-magic-methods.md).
- [Génériques, via les docblocks](https://php-dictionary.readthedocs.io/en/latest/index/generics.html) : PHP n'a pas de génériques natifs, alors les outils d'analyse statique lisent le type dans un commentaire, comme l'explique le [chapitre 11](ch11-03-generic-style-code.md).

## Enums

- [Enums](https://php-dictionary.readthedocs.io/en/latest/index/enum.html) : cas purs et cas adossés à une valeur, au [chapitre 6](ch06-00-enums.md).

## Espaces de noms et autoloading

- [Espaces de noms](https://php-dictionary.readthedocs.io/en/latest/index/namespace.html) et imports `use` : organiser et importer des noms, au [chapitre 7](ch07-04-use-keyword.md).
- [Autoloading](https://php-dictionary.readthedocs.io/en/latest/index/autoload.html) : charger les fichiers de classes à la demande plutôt qu'avec une pile de `require`.
- **PSR-4** : le standard d'autoloading que Composer implémente, traité au [chapitre 7](ch07-06-psr4.md). Pas encore dans le dictionnaire, seulement mentionné en passant.

## Gestion des erreurs

- [`Exception`](https://php-dictionary.readthedocs.io/en/latest/index/exception.html), [`Error`](https://php-dictionary.readthedocs.io/en/latest/index/error.html), [`Throwable`](https://php-dictionary.readthedocs.io/en/latest/index/throwable.html) : les deux hiérarchies parallèles de ce qui peut être levé en PHP, au [chapitre 9](ch09-00-error-handling.md).
- [`try` / `catch` / `finally`](https://php-dictionary.readthedocs.io/en/latest/index/try-catch.html) et [`DivisionByZeroError`](https://php-dictionary.readthedocs.io/en/latest/index/divisionbyzeroerror.html) : attraper et traiter un échec.
- [`RuntimeException`](https://php-dictionary.readthedocs.io/en/latest/index/predefined-exception.html) : l'une des sous-classes d'exception fournies par PHP, utilisée comme base dans le projet en ligne de commande à partir du [chapitre 14](ch14-03-improving-error-handling-and-modularity.md).
- **Classes d'exception personnalisées** (`extends Exception`) : un idiome courant, mais pas encore d'entrée dédiée dans le dictionnaire.

## Web et bases de données

- [Superglobales](https://php-dictionary.readthedocs.io/en/latest/index/superglobal.html), [`$_GET`](https://php-dictionary.readthedocs.io/en/latest/index/%24_get.html), [`$_POST`](https://php-dictionary.readthedocs.io/en/latest/index/%24_post.html) et [`$_SERVER`](https://php-dictionary.readthedocs.io/en/latest/index/%24_server.html) : lire les données d'une requête web, au [chapitre 10](ch10-01-forms-and-superglobals.md).
- [`htmlspecialchars()`](https://php-dictionary.readthedocs.io/en/latest/index/htmlspecialchars.html) et [XSS](https://php-dictionary.readthedocs.io/en/latest/index/xss.html) : échapper la sortie pour empêcher le balisage d'un attaquant de s'exécuter dans le navigateur de quelqu'un d'autre, au [chapitre 10](ch10-02-validation-and-xss.md).
- [CSRF](https://php-dictionary.readthedocs.io/en/latest/index/csrf.html) : les requêtes intersites forgées, nommées mais pas contrées dans ce livre, au [chapitre 10](ch10-02-validation-and-xss.md).
- [PDO](https://php-dictionary.readthedocs.io/en/latest/index/pdo.html), [`PDOException`](https://php-dictionary.readthedocs.io/en/latest/index/pdoexception.html) et [SQLite3](https://php-dictionary.readthedocs.io/en/latest/index/sqlite3.html) : une façon uniforme, dans un simple fichier, de parler à une base de données, au [chapitre 10](ch10-03-talking-to-a-database.md).
- [Requêtes préparées](https://php-dictionary.readthedocs.io/en/latest/index/prepared-query.html) et [injection SQL](https://php-dictionary.readthedocs.io/en/latest/index/sql-injection.html) : séparer la structure d'une requête de ses valeurs pour empêcher un attaquant de la réécrire.

## Débogage

- [`var_dump()`](https://php-dictionary.readthedocs.io/en/latest/index/var_dump.html), [`print_r()`](https://php-dictionary.readthedocs.io/en/latest/index/print_r.html) et [`var_export()`](https://php-dictionary.readthedocs.io/en/latest/index/var_export.html) : afficher la structure d'une valeur (et, pour `var_dump()`, son type) quand on traque un bug, au [chapitre 13](ch13-01-print-debugging.md).
- [Xdebug](https://php-dictionary.readthedocs.io/en/latest/index/xdebug.html) : un débogueur pas à pas et un profileur, qui suspend l'exécution sur un point d'arrêt au lieu de deviner où afficher, au [chapitre 13](ch13-02-xdebug.md).
- [Profilage](https://php-dictionary.readthedocs.io/en/latest/index/profiling.html) : mesurer où un script passe vraiment son temps, l'un des autres métiers de Xdebug.

## Concurrence

- [`pcntl`](https://php-dictionary.readthedocs.io/en/latest/index/pcntl.html) : l'extension derrière la création et le contrôle de processus séparés au niveau du système.

## Reflection et attributs

- [Reflection](https://php-dictionary.readthedocs.io/en/latest/index/reflection.html) : inspecter classes, méthodes, propriétés et attributs à l'exécution, au [chapitre 20](ch20-01-reflection.md).
- [Constantes magiques](https://php-dictionary.readthedocs.io/en/latest/index/magic-constant.html) (`__CLASS__`, `__FUNCTION__`, `__METHOD__`, `__LINE__`, `__FILE__`) : des constantes résolues à la compilation qui décrivent l'emplacement du code lui-même.
- [Attributs `#[...]`](https://php-dictionary.readthedocs.io/en/latest/index/attribute.html) : des métadonnées structurées attachées au code et relues via Reflection, au [chapitre 20](ch20-04-attributes.md).

## Interfaces natives

- [`Countable`](https://php-dictionary.readthedocs.io/en/latest/index/countable.html) : fait fonctionner `count()` sur un objet à vous.
- [`ArrayAccess`](https://php-dictionary.readthedocs.io/en/latest/index/arrayaccess.html) : autorise l'accès entre crochets sur un objet à vous.
- [`Iterator`](https://php-dictionary.readthedocs.io/en/latest/index/iterator.html) et [`IteratorAggregate`](https://php-dictionary.readthedocs.io/en/latest/index/iteratoraggregate.html) : les deux façons de rendre un objet parcourable par `foreach`, au [chapitre 20](ch20-02-built-in-interfaces.md).

## En vrac

- [`global`](https://php-dictionary.readthedocs.io/en/latest/index/global.html) : ramener une variable depuis la portée globale.
- [Copie à l'écriture](https://php-dictionary.readthedocs.io/en/latest/index/copy-on-write.html) : pourquoi passer un tableau par valeur ne coûte rien tant que personne n'écrit dedans, au [chapitre 4](ch04-01-copy-on-write.md).
- [Ramasse-miettes](https://php-dictionary.readthedocs.io/en/latest/index/garbage-collection.html) : comment PHP récupère la mémoire des objets que plus personne ne référence.
- [`assert()`](https://php-dictionary.readthedocs.io/en/latest/index/assertion.html) : une vérification de bon sens en phase de développement, au [chapitre 12](ch12-00-testing.md).
- [PHPUnit](https://php-dictionary.readthedocs.io/en/latest/index/phpunit.html) : le framework de test utilisé dans toute la seconde moitié du livre.
- [`getenv()`](https://php-dictionary.readthedocs.io/en/latest/index/getenv.html) et [`$_ENV`](https://php-dictionary.readthedocs.io/en/latest/index/$_env.html) : lire les variables d'environnement, au [chapitre 14](ch14-05-working-with-environment-variables.md).
- [`fwrite(STDERR, ...)`](https://php-dictionary.readthedocs.io/en/latest/index/fwrite.html) : écrire sur la sortie d'erreur plutôt que sur la sortie standard.
- [Mise en tampon de la sortie](https://php-dictionary.readthedocs.io/en/latest/index/output-buffering.html) : capturer la sortie générée dans un tampon au lieu de l'envoyer immédiatement.
- [`register_shutdown_function()`](https://php-dictionary.readthedocs.io/en/latest/index/shutdown-function.html) : un callback que PHP garantit d'exécuter à la fin d'un script, au [chapitre 21](ch21-03-shutdown-and-cleanup.md).
- **`$this`** et **`STDIN`** : tous deux utilisés en permanence à partir du [chapitre 2](ch02-00-guessing-game-tutorial.md), aucun n'a encore son entrée dans le dictionnaire.
- **`random_int()`** : la fonction de PHP pour tirer un entier aléatoire de qualité cryptographique, pas encore listée non plus.

Les trous méritent autant d'attention que les liens. Quelques éléments sur lesquels ce livre s'appuie lourdement, `$this`, `STDIN`, PSR-4, les classes d'exception personnalisées, n'ont pas encore d'entrée dans le dictionnaire. Si vous vous surprenez à en expliquer un à quelqu'un, cette explication est déjà l'essentiel d'une entrée de dictionnaire.
