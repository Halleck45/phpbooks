# Symfony: EasyAdmin and Sonata

Symfony has two established answers, sized for different jobs. **EasyAdmin gets you an admin screen this week; Sonata is for the admin panel that is itself a product.**

**EasyAdmin** generates a clean CRUD interface from a Doctrine entity with minimal configuration.

```bash
composer require easycorp/easyadmin-bundle
php bin/console make:admin:dashboard
php bin/console make:admin:crud
```

```php
use EasyCorp\Bundle\EasyAdminBundle\Config\Crud;
use EasyCorp\Bundle\EasyAdminBundle\Field\TextField;
use EasyCorp\Bundle\EasyAdminBundle\Field\MoneyField;

class ProductCrudController extends AbstractCrudController
{
    public static function getEntityFqcn(): string
    {
        return Product::class;
    }

    public function configureFields(string $pageName): iterable
    {
        yield TextField::new('name');
        yield MoneyField::new('price')->setCurrency('USD');
        yield AssociationField::new('category');
    }
}
```

**Sonata Admin** is heavier, older, and more extensible. It asks for more configuration up front, and in exchange it handles complex permission rules, nested admin relationships, and workflows that EasyAdmin was never designed to stretch to.

## When to reach for each

EasyAdmin for most internal tools: quick to set up, easy to read, enough for CRUD-shaped needs. Sonata when the admin panel carries complex permissions or deeply nested relationships, and needs more structure than EasyAdmin's simpler model gives you.

## When it's the wrong fit

A public, customer-facing dashboard, the same caveat as [Filament](ch05-01-laravel-filament.md). Both tools are built for trusted internal users.

> **Under the hood:** Both bundles read Doctrine's entity metadata (the same attributes that define your database schema) to infer field types. A `price` column typed as `decimal` in your entity becomes a numeric field in the admin with no extra declaration, because the framework already knows the type.
