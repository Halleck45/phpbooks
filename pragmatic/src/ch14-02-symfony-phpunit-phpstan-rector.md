# Symfony: PHPUnit, PHPStan/Psalm, and Rector

Symfony's testing story starts with plain PHPUnit, with a bridge package smoothing over the framework-specific parts: booting the kernel, making requests against it, and querying Doctrine in tests.

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

**PHPStan** (or its close cousin Psalm) analyzes code without running it, catching type errors, unreachable code, and incorrect method calls before they become runtime bugs. Both work equally well outside Symfony too, on the [standalone components](ch02-00-standalone-components.md) covered earlier in this book.

```bash
composer require phpstan/phpstan --dev
vendor/bin/phpstan analyse src --level=8
```

**Rector** automates upgrades and refactors: point it at a target PHP or Symfony version, and it rewrites your codebase's syntax to match, mechanically, across thousands of files at once.

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

## When to reach for this

Any Symfony project, at any size. Rector specifically earns its place the moment a major Symfony or PHP upgrade looms and hand-editing every affected file isn't realistic.

## When it's the wrong fit

Running Rector against a codebase with no test suite at all is riskier than it should be; pair it with at least the tests described here so its automated changes have something checking they didn't break behavior.

> **Under the hood:** Rector works by parsing your code into an AST (Abstract Syntax Tree), the same structure PHP's own engine builds internally before execution, applying a rule to it, and printing modified PHP back out. It's mechanical code transformation, not a language model guessing at intent.
