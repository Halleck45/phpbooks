# Tests, analyse statique et outillage

**Un projet PHP maintenu lance quatre outils à chaque commit : un lanceur de tests, un analyseur statique, un correcteur de style de code, et l'audit intégré à Composer.** Aucun de ces outils n'est livré avec le langage, mais tous s'installent avec un seul `composer require --dev` et se lancent depuis `vendor/bin/`. Si vous avez déjà utilisé pytest avec mypy, ou Jest avec tsc et Prettier, vous connaissez la forme de cette chaîne et il ne vous reste que les noms à apprendre.

Ce chapitre nomme deux outils pour chaque tâche, non par indécision, mais parce que les deux sont largement utilisés et bons, et que le projet que vous venez de rejoindre a de toute façon déjà choisi le sien.

## Les tests

Deux lanceurs de tests dominent l'écosystème. **PHPUnit est le lanceur de style xUnit sur lequel tous les autres outils de test PHP s'appuient, et Pest est une couche describe-et-it posée sur le moteur de PHPUnit.** Ils partagent les assertions, les mocks, la configuration et la machinerie de couverture, et ne diffèrent que par la façon dont un test se lit.

La fonction à tester :

```php
<?php
declare(strict_types=1);

namespace App;

function slugify(string $title): string
{
    $slug = strtolower(trim($title));
    $slug = preg_replace('/[^a-z0-9]+/', '-', $slug);

    return trim($slug, '-');
}
```

Une fonction dans un espace de noms n'est pas une classe, donc PSR-4 ne peut pas la trouver : le fichier va dans une entrée `files` du bloc `autoload` de `composer.json`, et Composer le charge avec `require` à chaque exécution.

Le même test, PHPUnit d'abord :

```php
<?php
declare(strict_types=1);

namespace App\Tests;

use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\Attributes\Test;
use PHPUnit\Framework\TestCase;
use function App\slugify;

final class SlugifyTest extends TestCase
{
    #[Test]
    public function itLowercasesAndJoinsWithDashes(): void
    {
        self::assertSame('hello-world', slugify('Hello World'));
    }

    #[Test]
    #[DataProvider('edgeCases')]
    public function itHandlesEdgeCases(string $input, string $expected): void
    {
        self::assertSame($expected, slugify($input));
    }

    public static function edgeCases(): iterable
    {
        yield 'leading punctuation' => ['!!Hi', 'hi'];
        yield 'empty' => ['', ''];
        yield 'unicode is stripped' => ['café', 'caf'];
    }
}
```

Puis Pest :

```php
<?php
declare(strict_types=1);

use function App\slugify;

it('lowercases and joins with dashes', function () {
    expect(slugify('Hello World'))->toBe('hello-world');
});

it('handles edge cases', function (string $input, string $expected) {
    expect(slugify($input))->toBe($expected);
})->with([
    'leading punctuation' => ['!!Hi', 'hi'],
    'empty' => ['', ''],
    'unicode is stripped' => ['café', 'caf'],
]);
```

Lancez-les avec `vendor/bin/phpunit` ou `vendor/bin/pest`. La configuration vit dans `phpunit.xml` à la racine du projet, et Pest lit le même fichier : on y déclare quels dossiers contiennent les tests, s'il faut échouer sur un warning, et quelles variables d'environnement définir.

Les conventions PHPUnit à connaître dès le premier jour : une classe de test se termine par `Test` et étend `TestCase`, une méthode de test porte l'attribut `#[Test]` ou commence par `test`, `setUp()` s'exécute avant chaque test, `self::assertSame()` est l'assertion stricte (il existe un `assertEquals()`, qui jongle avec les types comme `==`, donc préférez `assertSame()`), et `$this->createMock(SomeInterface::class)` renvoie un double de test que vous configurez avec `->method('name')->willReturn($value)`.

La couverture n'est pas intégrée au langage et demande une extension qui observe quelles lignes s'exécutent, soit Xdebug (avec `xdebug.mode=coverage`), soit PCOV, qui ne fait que de la couverture et le fait plus vite. Dans les deux cas, `vendor/bin/phpunit --coverage-text` affiche le rapport.

> Le test unicode ci-dessus documente un bug : `slugify('café')` supprime le `é` au lieu de le translittérer. Un test qui fige le comportement actuel reste un test utile, et vous corrigerez la fonction plus tard avec le `Transliterator` d'`intl`.

## L'analyse statique

PHP vérifie les types à l'exécution, un appel à la fois, et il ne vous dira donc jamais qu'une fonction située trois fichiers plus loin peut renvoyer `null` sans que vous le gériez. **PHPStan et Psalm jouent le rôle du compilateur que PHP n'a pas** : ils lisent toute la base de code, suivent chaque type à travers chaque appel, et signalent ce qui échouerait avant que quoi que ce soit ne s'exécute, comme mypy le fait pour Python ou le vérificateur de types de `tsc` pour TypeScript.

```php
<?php
declare(strict_types=1);

function findUser(int $id): ?User
{
    return $id === 1 ? new User('Ada') : null;
}

echo findUser(2)->name;
```

PHP exécute ce code et plante sur la seconde ligne avec « Attempt to read property on null », alors que les deux analyseurs le refusent avant même de l'exécuter :

```text
Cannot access property $name on User|null.
```

Les deux outils fonctionnent par niveaux : PHPStan va de 0 (erreurs évidentes seulement) à 10 (chaque `mixed` doit être précisé), et Psalm compte dans l'autre sens, de 8 (permissif) à 1 (strict). Un nouveau projet démarre au niveau le plus strict qu'il peut tenir et n'en redescend jamais, tandis qu'un projet ancien génère une baseline, un fichier qui liste toutes les erreurs actuelles pour que seules les nouvelles fassent échouer le build, puis la réduit au fil du temps.

Un `phpstan.neon` minimal :

```yaml
parameters:
    level: 8
    paths:
        - src
        - tests
```

Les deux outils lisent les docblocks pour ce que le langage ne sait pas exprimer : `@param list<int> $ids`, `@return array<string, User>`, et les génériques `@template` présentés dans [Le système de types](ch03-types.md). C'est dans ces docblocks que vivent les génériques en PHP : le moteur les ignore et l'analyseur les fait respecter.

<img src="images/ch12-analyser-xray.png" alt="Un petit éléphant tient un écran à rayons X au-dessus d'une pile de fichiers PHP ; à travers l'écran, une ligne pointillée suit une valeur d'un fichier à l'autre et se termine sur une marque rouge, là où un null atteint un appel de méthode" width="560">

## Le style de code

**PER Coding Style, publié par le PHP-FIG, est le guide de style de référence.** Il a succédé à PSR-12, qui avait succédé à PSR-2, et tous les frameworks et la plupart des bibliothèques le suivent : quatre espaces, accolades sur leur propre ligne pour les classes et les fonctions, sur la même ligne pour les structures de contrôle, une classe par fichier. Vous n'avez pas à l'apprendre par cœur, puisqu'un outil l'applique pour vous.

PHP-CS-Fixer réécrit les fichiers pour respecter un jeu de règles. PHP_CodeSniffer signale les violations avec `phpcs` et corrige ce qu'il peut avec `phpcbf`. Les deux acceptent PER en une ligne de configuration. Pour PHP-CS-Fixer, `.php-cs-fixer.dist.php` :

```php
<?php
declare(strict_types=1);

$finder = PhpCsFixer\Finder::create()->in([__DIR__ . '/src', __DIR__ . '/tests']);

return (new PhpCsFixer\Config())
    ->setRules(['@PER-CS' => true])
    ->setFinder($finder);
```

Pour PHP_CodeSniffer, `phpcs.xml` :

```xml
<?xml version="1.0"?>
<ruleset name="project">
    <rule ref="PSR12"/>
    <file>src</file>
    <file>tests</file>
</ruleset>
```

Choisissez-en un et lancez-le en CI, ce qui met fin aux discussions sur le placement des accolades en revue de code.

## Les migrations

**Rector réécrit votre code vers une version plus récente de PHP, ou d'un framework, automatiquement.** Il sait que `Foo $x = null` doit devenir `?Foo $x = null`, qu'un `switch` qui renvoie une valeur est un `match`, qu'un constructeur qui affecte des propriétés peut les promouvoir. Donnez-lui une version cible et il fait la partie mécanique d'une migration :

```php
<?php
declare(strict_types=1);

use Rector\Config\RectorConfig;
use Rector\ValueObject\PhpVersion;

return RectorConfig::configure()
    ->withPaths([__DIR__ . '/src', __DIR__ . '/tests'])
    ->withPhpVersion(PhpVersion::PHP_84)
    ->withPreparedSets(deadCode: true, codeQuality: true);
```

`vendor/bin/rector --dry-run` montre le diff. Sans l'option, il l'applique. Le chapitre [Revenir à PHP après des années](ch14-returning-developer.md) est, en pratique, la liste de ce que Rector fera au code que vous avez laissé derrière vous.

## Le débogage

`var_dump($value)` affiche une valeur avec son type sans interrompre l'exécution, et `var_dump($value); exit;` reste le débogueur le plus rapide qui soit. Les frameworks ajoutent un `dump()` et un `dd()` (dump and die) plus agréables à lire, mais celui du langage a l'avantage de marcher partout.

**Xdebug est le seul débogueur pas à pas de l'écosystème.** Une fois l'extension installée et `xdebug.mode=debug` placé dans `php.ini`, votre éditeur s'arrête sur les points d'arrêt, montre la pile et vous laisse inspecter les variables, dans les requêtes web comme dans les scripts CLI. C'est une extension réservée au développement, parce qu'elle ralentit tout : les builds de production s'en passent, et quand il vous faut de la vitesse en local, `php -d xdebug.mode=off script.php` la désactive le temps d'une exécution.

Côté éditeurs, PhpStorm intègre le langage et VS Code a besoin d'une extension PHP. Les deux lisent les mêmes docblocks que les analyseurs, donc les génériques que vous écrivez pour PHPStan ou Psalm alimentent aussi l'autocomplétion.

## Relier le tout

Les scripts Composer donnent au projet un vocabulaire unique, quels que soient les outils choisis. Dans `composer.json` :

```json
{
    "scripts": {
        "test": "phpunit",
        "lint": "php-cs-fixer fix --dry-run --diff",
        "lint:fix": "php-cs-fixer fix",
        "analyse": "phpstan analyse",
        "check": ["@lint", "@analyse", "@test"]
    }
}
```

`composer check` lance les trois. Composer place `vendor/bin` dans le chemin des scripts, donc les noms d'outils n'ont pas besoin de préfixe. Un nouveau membre de l'équipe lit `composer.json` et sait comment le projet est vérifié sans ouvrir de README.

La CI lance les mêmes commandes, sur chaque version de PHP que le projet prend en charge (la contrainte `php` de `composer.json` dit lesquelles), plus `composer audit`, qui confronte `composer.lock` à la base des vulnérabilités connues et échoue à la première trouvée. `composer outdated` liste ce qui a une version plus récente ; un robot de mise à jour des dépendances peut ouvrir les pull requests pour vous.

Pour un runtime local, `php -S localhost:8000 -t public` sert le projet comme l'a montré [Une requête web, sans framework](ch11-web-request.md), et l'image Docker officielle `php:8.5-cli` donne à tout le monde le même interpréteur. N'importe quel réglage de `php.ini` peut être surchargé pour une commande avec `php -d memory_limit=1G`. Sachez enfin que les fichiers `.env` sont une convention de bibliothèques, que plusieurs paquets chargent dans l'environnement, et non quelque chose que PHP lit de lui-même.

## Le piège

Les deux erreurs classiques tiennent au moment où l'on fait les choses.

La première consiste à écrire des tests qui touchent la base de données par défaut : ils passent sur la machine de l'auteur, prennent des minutes en CI, et finissent par ne plus être lancés. Testez la fonction, passez la dépendance par le constructeur, et gardez les tests d'intégration dans leur propre dossier avec leur propre suite dans `phpunit.xml`, pour qu'ils s'exécutent quand on le décide.

La seconde consiste à lancer l'analyse statique à la fin du projet. Une base de code qui atteint le niveau 8 dès le premier jour y reste sans y penser, alors qu'une base de code qui rencontre PHPStan après deux ans l'accueille avec quatre mille erreurs et une baseline que personne ne réduit. Ajoutez l'analyseur au premier commit, au niveau le plus élevé qui passe, et montez-le dès que c'est possible.

Une fois les outils en place, il reste la question que tout développeur polyglotte pose la première semaine, celle de l'asynchrone, et [Concurrence et performance](ch13-concurrency-and-performance.md) y répond.
