# Organiser ses tests

L'endroit où vivent les tests ne change rien pour PHPUnit et tout pour la personne qui les cherche, vous compris dans six mois. **La convention PHP tient en une phrase : un dossier `tests/` qui reflète `src/`, une classe de test par classe, nommée comme la classe suivie de `Test`.**

```text
src/
    Rectangle.php
    GrepOptions.php
tests/
    RectangleTest.php
    GrepOptionsTest.php
```

<img src="images/ch12-mirror-tree.png" alt="Deux arborescences face à face comme dans un miroir : chaque fichier de src a son jumeau dans tests, même nom avec le suffixe Test" width="560">

`src/Rectangle.php` a droit à `tests/RectangleTest.php`. `src/Http/Client.php` aurait `tests/Http/ClientTest.php`, les dossiers alignés des deux côtés. Rien n'impose cela : PHPUnit lance ce que `phpunit.xml` lui désigne, nommé comme bon vous semble. Mais presque tous les projets PHP suivent cette convention, et s'en écarter sans bonne raison ne fait que compliquer la vie de la prochaine personne qui ouvrira votre code. L'autoloading PSR-4 de Composer, vu au [chapitre 7](ch07-00-namespaces-and-composer.md), associe en général un espace de noms `Tests\` à `tests/`, de la même manière qu'il associe l'espace de noms de votre application à `src/`.

## Tests unitaires et tests d'intégration

**Un test unitaire exerce une classe ou une fonction seule, sans rien d'extérieur** : pas de base de données, pas de système de fichiers, pas de réseau. `RectangleTest` en est un. Il construit un `Rectangle` et vérifie ses méthodes, rien de plus. Les tests unitaires sont rapides. Des milliers d'entre eux tournent en quelques secondes, et c'est précisément ce qui vous permet de lancer la suite entière sans arrêt sans qu'elle vous ralentisse.

**Un test d'intégration vérifie que plusieurs pièces fonctionnent ensemble** : votre code qui parle à une vraie base de données, à un vrai fichier sur le disque, à un autre service par un vrai appel HTTP. Il attrape une famille de bugs qu'un test unitaire ne peut structurellement pas voir, quand deux pièces sont chacune correcte de leur côté et se trompent l'une sur l'autre. Le prix, c'est la vitesse, souvent de plusieurs ordres de grandeur, et une tendance à échouer pour des raisons sans rapport avec votre code : un disque lent, un réseau qui hoquette.

<img src="images/ch12-unit-vs-integration.png" alt="À gauche, un engrenage seul testé sur un établi avec un chronomètre rapide ; à droite, plusieurs engrenages engrenés avec une base de données et un fichier, avec un chronomètre plus lent" width="600">

```php
<?php

use PHPUnit\Framework\TestCase;

final class FindMatchingLinesIntegrationTest extends TestCase
{
    public function testFindsLinesInARealFile(): void
    {
        $path = tempnam(sys_get_temp_dir(), 'lines');
        file_put_contents($path, "apple\nbanana\ncherry\n");

        $lines = findMatchingLines($path, 'banana');

        $this->assertSame(['banana'], $lines);

        unlink($path);
    }
}
```

Rien d'exotique ici. C'est toujours un `TestCase`, toujours plein d'assertions. Ce qui en fait un test d'intégration, c'est qu'il touche le vrai système de fichiers, en créant un vrai fichier temporaire puis en le supprimant, au lieu d'en simuler un. La différence est dans ce que le test touche, pas dans sa syntaxe.

## Un partage pratique

La plupart des projets gardent les deux sortes dans le même dossier `tests/` et les séparent par répertoire (`tests/Unit/` et `tests/Integration/`) ou par groupe (l'attribut `#[Group('integration')]` de la section précédente). La suite unitaire, rapide, tourne alors sans arrêt pendant que vous travaillez, et la suite d'intégration, plus lente, attend un commit ou l'intégration continue. Aucune ne remplace l'autre. Les tests unitaires vous disent qu'une pièce marche seule ; les tests d'intégration vous disent que les pièces marchent encore une fois qu'elles se parlent, et c'est la seule façon dont votre programme tourne jamais.
