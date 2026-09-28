# Laravel : Pest, Larastan et `composer audit`

**Pest** est un framework de test construit sur PHPUnit, conçu pour qu'un test se lise presque comme une phrase. Un test facile à lire est un test qu'on écrit.

```bash
composer require pestphp/pest --dev --with-all-dependencies
php artisan pest:install
```

```php
it('rejects an order with no items', function () {
    $order = Order::factory()->create();

    expect(fn () => $order->submit())
        ->toThrow(EmptyOrderException::class);
});

it('applies a discount code correctly', function () {
    $order = Order::factory()->create(['total' => 100]);

    $order->applyDiscount('SAVE10');

    expect($order->total)->toBe(90.0);
});
```

```bash
php artisan test
```

**Larastan** enveloppe PHPStan (voir [PHPStan/Psalm côté Symfony](ch14-02-symfony-phpunit-phpstan-rector.md) pour la version indépendante du framework) avec la connaissance des types propre à Laravel. Il repère l'appel d'une méthode qui n'existe pas sur un modèle, ou le mauvais type passé à un job, sans exécuter le code.

```bash
composer require larastan/larastan --dev
```

```neon
# phpstan.neon
includes:
    - vendor/larastan/larastan/extension.neon
parameters:
    level: 6
    paths: [app]
```

```bash
vendor/bin/phpstan analyse
```

**`composer audit`** compare vos dépendances installées à une base de vulnérabilités connues. Le jour où un paquet dont vous dépendez reçoit une CVE, cette commande vous le dit, avant qu'un attaquant ne s'en charge.

```bash
composer audit
```

## Quand le choisir

Tout projet Laravel qui a dépassé le stade du prototype. **Tests et analyse statique coûtent le moins cher le premier jour, et le plus cher à rattraper** sur une base de code qui a déjà grossi sans eux.

## Quand ce n'est pas le bon outil

Il n'y a pas de mauvais cas ici. Le seul échec possible, c'est de sauter cette page sous la pression d'une échéance.

> **Sous le capot :** PHPStan, et Larastan avec lui, lit vos déclarations de types, y compris les types union, les propriétés `readonly` et les enums, et raisonne sur ce qui est possible sans rien exécuter. Plus vos types sont stricts, plus il attrape de bugs avant même le premier test.
