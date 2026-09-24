# Symfony : EasyAdmin et Sonata

Symfony a deux réponses éprouvées, taillées pour des tâches différentes. **EasyAdmin vous donne un écran d'administration cette semaine ; Sonata est pour l'administration qui est elle-même un produit.**

**EasyAdmin** génère une interface CRUD propre à partir d'une entité Doctrine, avec un minimum de configuration.

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

**Sonata Admin** est plus lourd, plus ancien et plus extensible. Il demande davantage de configuration au départ et, en échange, il encaisse des règles de permissions complexes, des administrations imbriquées et des workflows pour lesquels EasyAdmin n'a jamais été conçu.

## Lequel choisir

EasyAdmin pour la plupart des outils internes : rapide à installer, facile à lire, suffisant pour tout ce qui a la forme d'un CRUD. Sonata quand l'administration porte des permissions complexes ou des relations profondément imbriquées, et qu'il lui faut plus de structure que le modèle simple d'EasyAdmin.

## Quand ce n'est pas le bon outil

Un tableau de bord public, destiné aux clients : même réserve que pour [Filament](ch05-01-laravel-filament.md). Les deux outils sont faits pour des utilisateurs internes de confiance.

> **Sous le capot :** les deux bundles lisent les métadonnées des entités Doctrine (les mêmes attributs qui définissent votre schéma de base de données) pour déduire le type des champs. Une colonne `price` typée `decimal` dans votre entité devient un champ numérique dans l'administration sans déclaration supplémentaire, parce que le framework connaît déjà le type.
