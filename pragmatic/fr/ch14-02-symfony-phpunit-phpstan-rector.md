# Symfony : PHPUnit, PHPStan/Psalm et Rector

Chez Symfony, les tests commencent avec PHPUnit tout court. Un paquet de liaison lisse ce qui tient au framework : démarrer le noyau, lui envoyer des requêtes, interroger Doctrine depuis un test.

```bash
composer require symfony/test-pack --dev
```

```php
class OrderControllerTest extends WebTestCase
{
    public function testSubmittingAnEmptyOrderFails(): void
    {
        $client = static::createClient();
        $client->request('POST', '/orders/1/submit');

        $this->assertResponseStatusCodeSame(422);
    }
}
```

```bash
php bin/phpunit
```

**PHPStan**, ou son proche cousin Psalm, analyse le code sans le lancer. Il attrape les erreurs de type, le code inatteignable et les appels à des méthodes qui n'existent pas, avant qu'ils ne deviennent des bugs à l'exécution. Les deux fonctionnent aussi hors de Symfony, sur les [composants autonomes](ch02-00-standalone-components.md) vus plus haut dans ce livre.

```bash
composer require phpstan/phpstan --dev
vendor/bin/phpstan analyse src --level=8
```

**Rector** automatise les montées de version et les refactorisations. Donnez-lui une version cible de PHP ou de Symfony et il réécrit votre syntaxe pour s'y conformer, mécaniquement, sur des milliers de fichiers d'un coup.

```bash
composer require rector/rector --dev
```

```php
// rector.php
return RectorConfig::configure()
    ->withPaths([__DIR__ . '/src'])
    ->withSets([SymfonySetList::SYMFONY_64]);
```

```bash
vendor/bin/rector process
```

## Quand le choisir

Tout projet Symfony, quelle que soit sa taille. **Rector gagne sa place le jour où une montée de version majeure de Symfony ou de PHP se profile** et où retoucher chaque fichier concerné à la main cesse d'être réaliste.

## Quand ce n'est pas le bon outil

Rector sur une base de code sans aucun test. Ses modifications sont mécaniques, mais quelque chose doit vérifier qu'elles n'ont pas changé le comportement. Associez-le au moins aux tests ci-dessus.

> **Sous le capot :** Rector transforme votre code en AST (arbre de syntaxe abstraite), la structure que le moteur de PHP construit lui-même avant l'exécution, lui applique une règle, puis réimprime du PHP modifié. C'est une transformation mécanique du code, pas un modèle de langage qui devine une intention.
