# Symfony: PHPUnit, PHPStan/Psalm, and Rector

Symfony's testing story starts with plain PHPUnit. A bridge package smooths over the framework-specific parts: booting the kernel, making requests against it, querying Doctrine from a test.

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

**PHPStan**, or its close cousin Psalm, analyzes code without running it. It catches type errors, unreachable code and calls to methods that do not exist, before they become runtime bugs. Both work outside Symfony too, on the [standalone components](ch02-00-standalone-components.md) from earlier in this book.

```bash
composer require phpstan/phpstan --dev
vendor/bin/phpstan analyse src --level=8
```

**Rector** automates upgrades and refactors. Point it at a target PHP or Symfony version and it rewrites your syntax to match, mechanically, across thousands of files at once.

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

Any Symfony project, at any size. **Rector earns its place the day a major Symfony or PHP upgrade looms** and editing every affected file by hand stops being realistic.

## When it's the wrong fit

Rector on a codebase with no tests at all. Its changes are mechanical, but something has to check they did not change behavior. Pair it with at least the tests above.

> **Under the hood:** Rector parses your code into an AST (Abstract Syntax Tree), the same structure PHP's engine builds before execution, applies a rule to it, and prints modified PHP back out. It is mechanical code transformation, not a language model guessing at intent.
