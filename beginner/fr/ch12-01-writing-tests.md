# Écrire des tests avec PHPUnit

Créez un projet vierge, comme au [chapitre 7](ch07-01-hello-composer.md) :

```console
$ composer init --no-interaction
$ composer require --dev phpunit/phpunit
```

L'option `--dev` compte. **PHPUnit est un outil que vous utilisez pendant que vous construisez le projet, pas quelque chose dont le projet a besoin pour tourner.** Composer garde les dépendances de développement à part pour cette raison : elles ne partent jamais en production.

## Le code à tester

Voici une petite classe qui mérite un test, du genre de celles que vous écrivez depuis le [chapitre 5](ch05-00-classes.md) :

```php
<?php
// src/Rectangle.php

declare(strict_types=1);

final class Rectangle
{
    public function __construct(
        private readonly float $width,
        private readonly float $height,
    ) {
    }

    public function area(): float
    {
        return $this->width * $this->height;
    }

    public function isSquare(): bool
    {
        return $this->width === $this->height;
    }
}
```

Rien de nouveau : une classe readonly, deux propriétés, deux méthodes. La question à laquelle un test répond est simple. Fait-elle vraiment ce qu'elle prétend ?

## Votre premier test

**Un test est une classe qui étend le `TestCase` de PHPUnit, avec des méthodes dont le nom commence par `test`.** Chaque méthode met en place une situation, puis affirme quelque chose sur le résultat :

```php
<?php
// tests/RectangleTest.php

declare(strict_types=1);

use PHPUnit\Framework\TestCase;

final class RectangleTest extends TestCase
{
    public function testAreaOfARectangle(): void
    {
        $rectangle = new Rectangle(8.0, 7.0);

        $this->assertEquals(56.0, $rectangle->area());
    }
}
```

Lisez la méthode comme une phrase : construire un rectangle de 8 sur 7, puis affirmer que son aire vaut 56. **`assertEquals(expected, actual)` est l'affirmation.** Si les deux valeurs diffèrent, le test échoue et PHPUnit vous montre les deux côtés. Lancez-le :

```console
$ vendor/bin/phpunit tests
PHPUnit 10.5.0 by Sebastian Bergmann and contributors.

.                                                                   1 / 1 (100%)

Time: 00:00.012, Memory: 6.00 MB

OK (1 test, 1 assertion)
```

Un point par test réussi. C'est toute la boucle de travail jusqu'à la fin du chapitre : modifier le code, lancer les tests, compter les points.

Essayez : remplacez `56.0` par `57.0` et relancez. Le point devient un `F`, et PHPUnit vous dit quelle affirmation a cassé, avec la valeur attendue et la valeur obtenue.

<img src="images/ch12-test-scale.png" alt="Une balance avec la valeur attendue 56 sur un plateau et l'aire calculée du rectangle sur l'autre, à l'équilibre, avec l'éléphant PHP qui lève le pouce" width="520">

> Un test est une affirmation sur votre code. PHPUnit vérifie qu'elle tient toujours.

## `#[Test]`, l'alternative au préfixe `test`

Les attributs de PHP 8 (le [chapitre 20](ch20-00-advanced-features.md) les traite pour de bon) donnent à PHPUnit une deuxième façon de marquer une méthode comme test, sans contrainte sur le nom :

```php
<?php

use PHPUnit\Framework\Attributes\Test;
use PHPUnit\Framework\TestCase;

final class RectangleTest extends TestCase
{
    #[Test]
    public function itCalculatesArea(): void
    {
        $rectangle = new Rectangle(8.0, 7.0);

        $this->assertEquals(56.0, $rectangle->area());
    }
}
```

Les deux styles se valent ; choisissez-en un par projet et tenez-vous-y. Ce livre garde le préfixe `test` : pas de `use` à ajouter, et le nom dit tout seul ce qu'il est.

## D'autres assertions : `assertTrue`, et `assertEquals` contre `assertSame`

```php
<?php

final class RectangleTest extends TestCase
{
    public function testASquareIsDetected(): void
    {
        $square = new Rectangle(5.0, 5.0);

        $this->assertTrue($square->isSquare());
    }

    public function testEqualsVsSame(): void
    {
        $this->assertEquals(1, "1");   // passes, loose comparison, like ==
        $this->assertSame(1, "1");     // fails, strict comparison, like ===
    }
}
```

`assertTrue()` fait ce que son nom dit. La deuxième méthode est la plus intéressante, parce qu'une de ses deux lignes échoue.

**`assertEquals()` compare comme `==`, et `assertSame()` compare comme `===`.** C'est exactement la distinction du [chapitre 3](ch03-02-data-types.md), déguisée en assertion. Pour `assertEquals()`, `1` et `"1"` sont assez égaux. `assertSame()` refuse : il vérifie le type et la valeur ensemble.

<img src="images/ch12-equals-vs-same.png" alt="Deux portillons côte à côte : celui d'assertEquals laisse passer le nombre 1 et le texte 1, celui d'assertSame laisse passer le nombre et arrête le texte" width="600">

Prenez `assertSame()` par défaut. Il attrape toute une famille de bugs, une fonction qui renvoie une chaîne là où vous attendiez un entier, que `assertEquals()` laisse passer sans un mot. Ne revenez à `assertEquals()` que lorsque la comparaison souple est vraiment ce que vous voulez tester.

Une assertion qui échoue vous dit exactement ce qui a cloché :

```console
$ vendor/bin/phpunit tests
1) RectangleTest::testEqualsVsSame
Failed asserting that 1 is identical to '1'.
```

Ce message travaille pour vous : « pas identique » plutôt que « différent » pointe droit sur le type. Lisez les messages d'échec de près ; PHPUnit est plus précis qu'il n'en a l'air.
