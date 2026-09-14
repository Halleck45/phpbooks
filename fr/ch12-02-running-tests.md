# Contrôler l'exécution des tests

`vendor/bin/phpunit tests` lance tout, à chaque fois. Avec cinq tests, très bien. Avec cinq cents, attendre la suite entière à chaque fichier enregistré devient pénible, et l'essentiel de la sortie parle de code auquel vous n'avez pas touché. **PHPUnit sait ne lancer qu'une tranche de la suite, et un fichier de configuration rend le tout reproductible.**

## Filtrer par nom

**`--filter` ne lance que les tests dont le nom correspond à un motif :**

```console
$ vendor/bin/phpunit --filter testAreaOfARectangle tests
```

Le motif est une expression régulière comparée au nom de la méthode, donc `--filter Area` attrape `testAreaOfARectangle` et tout ce qui contient « Area ». C'est le mode qu'il vous faut quand vous êtes plongé dans une fonctionnalité : lancer les deux ou trois tests qui comptent, et garder le reste pour plus tard.

<img src="images/ch12-filter-funnel.png" alt="Un tas de fichiers de test versé dans un entonnoir marqué filter et group, dont seuls deux tests ressortent en bas, sur un terminal" width="520">

## Grouper les tests

Pour découper plus large qu'un test à la fois, étiquetez les tests avec un groupe, soit par l'ancienne annotation en docblock, soit par l'attribut moderne :

```php
<?php

use PHPUnit\Framework\Attributes\Group;
use PHPUnit\Framework\TestCase;

final class RectangleTest extends TestCase
{
    #[Group('geometry')]
    public function testAreaOfARectangle(): void
    {
        $rectangle = new Rectangle(8.0, 7.0);

        $this->assertSame(56.0, $rectangle->area());
    }
}
```

Puis lancez seulement ce groupe :

```console
$ vendor/bin/phpunit --group geometry tests
```

L'usage quotidien, c'est la vitesse. **Marquez les tests lents (base de données, système de fichiers, réseau) avec `#[Group('slow')]` et tenez-les hors de votre boucle de travail avec `--exclude-group slow`.** Le passage complet attend l'intégration continue, où quelques secondes de plus ne coûtent rien à personne.

## `phpunit.xml`

Taper `tests` et se souvenir de ses options préférées à chaque lancement finit aussi par lasser. Un fichier `phpunit.xml` à la racine du projet règle ça, et PHPUnit le lit sans qu'on le lui demande :

```xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit bootstrap="vendor/autoload.php"
         colors="true">
    <testsuites>
        <testsuite name="default">
            <directory>tests</directory>
        </testsuite>
    </testsuites>
</phpunit>
```

Deux choses y vivent. **`bootstrap` nomme le fichier que PHPUnit charge avant tout le reste**, presque toujours l'autoloader de Composer, pour que vos tests puissent citer `Rectangle` sans `require` manuel. **`testsuites` définit ce que « la suite » veut dire** : ici, tout ce qui se trouve sous `tests/`. Une fois le fichier en place, la commande se réduit à sa forme la plus courte :

```console
$ vendor/bin/phpunit
```

`--filter` et `--group` se posent toujours par-dessus quand vous voulez un passage plus étroit. Si vous préférez répondre à quelques questions plutôt qu'écrire du XML à la main, `vendor/bin/phpunit --generate-configuration` produit une première version. Dans les deux cas, committez le fichier. C'est de la configuration de projet, pas une préférence personnelle : toute l'équipe, et le pipeline d'intégration continue, doivent lancer la même suite de la même façon.

> La suite est définie une fois, dans `phpunit.xml`. Les options la rétrécissent pour l'instant présent.
