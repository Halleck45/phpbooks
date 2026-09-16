# Symfony: EasyAdmin and Sonata

Symfony has two well-established answers here, sized for different jobs.

**EasyAdmin** generates a clean CRUD interface from a Doctrine entity with minimal configuration, aimed squarely at "I need an admin screen this week."

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

**Sonata Admin** is the heavier, older, and more extensible option: more configuration up front, but built to handle complex permission rules, nested admin relationships, and highly customized workflows that EasyAdmin isn't designed to stretch to.

## When to reach for each

EasyAdmin for most internal tools: fast to set up, easy to read, sufficient for the majority of CRUD-shaped admin needs. Sonata when the admin panel itself is a serious piece of the product, with complex permissions or deeply nested relationships that need more structure than EasyAdmin's simpler model provides.

## When it's the wrong fit

A public customer-facing dashboard, same caveat as [Filament](ch05-01-laravel-filament.md): both tools are built for internal, trusted-user administration, not consumer product surfaces.

> **Under the hood:** Both bundles read Doctrine's entity metadata (the same annotations or attributes that define your database schema) to infer field types automatically. A `price` column typed as `decimal` in your entity becomes a numeric field in the admin with no extra declaration, because the framework already knows the type.
