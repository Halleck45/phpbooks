# Ajouter une fonctionnalité en développement piloté par les tests

`search()` et `GrepOptions` vivent désormais dans des fichiers qui ne lisent pas `$argv`, ne font pas `echo` et ne font pas `exit`. C'était le but de la section précédente, et ça paie maintenant : pour la première fois dans ce projet, un test PHPUnit peut les appeler directement, comme le [chapitre 12](ch12-00-testing.md) l'a montré. Profitons-en pour ajouter une vraie fonctionnalité, la recherche insensible à la casse, et pour l'ajouter test en premier.

Installez PHPUnit comme vous l'aviez fait là-bas :

```console
$ composer require --dev phpunit/phpunit
```

## Rouge : écrire le test qu'on aimerait déjà voir passer

Retour à `fruits.txt` :

```text
Apple pie recipe
apple sauce for the win
Banana bread is better
cherry clafoutis
```

Chercher `apple` ne trouve que la ligne en minuscules, parce que `str_contains()` ne replie pas la casse. Écrivez, sous forme de test, le comportement que vous voulez à la place : **un `GrepOptions` avec l'insensibilité à la casse activée doit trouver à la fois `"Apple pie recipe"` et `"apple sauce for the win"`.**

```php
<?php
// tests/SearchTest.php
declare(strict_types=1);

use PHPUnit\Framework\TestCase;

require_once __DIR__ . '/../src/GrepOptions.php';
require_once __DIR__ . '/../src/FileNotFoundException.php';
require_once __DIR__ . '/../src/search.php';

final class SearchTest extends TestCase
{
    private string $fixture;

    protected function setUp(): void
    {
        $this->fixture = tempnam(sys_get_temp_dir(), 'phpgrep');
        file_put_contents(
            $this->fixture,
            "Apple pie recipe\napple sauce for the win\nBanana bread is better\ncherry clafoutis\n"
        );
    }

    protected function tearDown(): void
    {
        unlink($this->fixture);
    }

    public function testSearchCanIgnoreCase(): void
    {
        $options = new GrepOptions(
            query: 'apple',
            filename: $this->fixture,
            ignoreCase: true,
        );

        $this->assertSame(
            ['Apple pie recipe', 'apple sauce for the win'],
            search($options)
        );
    }
}
```

`setUp()` et `tearDown()` sont des crochets de PHPUnit exécutés avant et après *chaque* méthode de test de la classe. Ici, ils fabriquent un fichier temporaire neuf par test et le suppriment ensuite, si bien qu'aucun test ne dépend de ce qu'une exécution précédente a laissé derrière elle.

Lancez :

```console
$ vendor/bin/phpunit tests
PHPUnit 10.5.0 by Sebastian Bergmann and contributors.

E                                                                   1 / 1 (100%)

Time: 00:00.014, Memory: 6.00 MB

1) SearchTest::testSearchCanIgnoreCase
Error: Unknown named parameter $ignoreCase
```

Rouge, et pour exactement la bonne raison. `GrepOptions` n'a pas encore de propriété `ignoreCase`, donc PHP ne peut même pas construire l'objet que le test demande. Tout le rythme du développement piloté par les tests tient dans ce pas : **écrire le test du comportement voulu avant que le code existe, le regarder échouer, et laisser l'échec dire ce qu'il faut construire ensuite.**

<img src="images/ch14-red-green.png" alt="La boucle du développement piloté par les tests : écrire un test qui échoue (feu rouge), écrire juste assez de code pour le faire passer (feu vert), ranger le code, et recommencer" width="480">

## Vert : le faire passer

D'abord, donnez à `GrepOptions` la propriété que le test réclame :

```php
<?php
// src/GrepOptions.php
declare(strict_types=1);

final class GrepOptions
{
    public function __construct(
        public readonly string $query,
        public readonly string $filename,
        public readonly bool $ignoreCase,
    ) {
    }

    public static function fromArgv(array $argv): self
    {
        return new self(
            query: $argv[1],
            filename: $argv[2],
            ignoreCase: false,
        );
    }
}
```

`fromArgv()` passe un `false` en dur pour l'instant. Laisser l'utilisateur le piloter, c'est le travail de la section suivante. Apprenez ensuite à `search()` à respecter le drapeau :

```php
<?php
// src/search.php
declare(strict_types=1);

require_once __DIR__ . '/FileNotFoundException.php';

function search(GrepOptions $options): array
{
    if (!is_readable($options->filename)) {
        throw new FileNotFoundException("Cannot read file: {$options->filename}");
    }

    $lines = file($options->filename, FILE_IGNORE_NEW_LINES);
    $query = $options->ignoreCase ? strtolower($options->query) : $options->query;

    $matches = [];
    foreach ($lines as $line) {
        $haystack = $options->ignoreCase ? strtolower($line) : $line;
        if (str_contains($haystack, $query)) {
            $matches[] = $line;
        }
    }

    return $matches;
}
```

Quand `ignoreCase` est actif, la requête et la ligne sont toutes deux passées en minuscules pour la *comparaison*. Regardez pourtant ce qui est poussé dans `$matches` : la `$line` d'origine, intacte. **On veut une recherche insensible à la casse, pas une sortie défigurée.**

```console
$ vendor/bin/phpunit tests
PHPUnit 10.5.0 by Sebastian Bergmann and contributors.

.                                                                   1 / 1 (100%)

Time: 00:00.013, Memory: 6.00 MB

OK (1 test, 1 assertion)
```

Vert. Rouge, puis vert, puis, traditionnellement, refactoring, même s'il n'y a pas grand-chose à remodeler ici pour l'instant. Tant que vous êtes dans le fichier, ajoutez un test de plus, pour figer le comportement que vous ne changez *pas* :

```php
<?php

public function testSearchIsCaseSensitiveByDefault(): void
{
    $options = new GrepOptions(
        query: 'apple',
        filename: $this->fixture,
        ignoreCase: false,
    );

    $this->assertSame(['apple sauce for the win'], search($options));
}
```

Il passe du premier coup. Il ne teste rien de nouveau ; il protège l'ancien comportement contre une régression future. Les deux tests méritent leur place : le premier prouve que la fonctionnalité marche, le second prouve que l'ajouter n'a pas cassé en douce ce qui existait déjà.
