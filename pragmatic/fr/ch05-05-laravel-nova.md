# Laravel Nova ($) : l'alternative officielle à Filament

Nova est le panneau d'administration construit et maintenu par l'équipe de Laravel elle-même. Fonctionnalité pour fonctionnalité, il recouvre largement [Filament](ch05-01-laravel-filament.md) : ressources générées depuis les modèles Eloquent, tableaux avec recherche et filtres, champs et actions personnalisés. **La différence, c'est qui répond quand quelque chose casse ou quand une nouvelle version de Laravel sort.**

```bash
composer require laravel/nova
php artisan nova:install
php artisan make:nova-resource Product
```

```php
class Product extends Resource
{
    public function fields(NovaRequest $request): array
    {
        return [
            ID::make()->sortable(),
            Text::make('Name')->sortable()->rules('required', 'max:255'),
            Currency::make('Price'),
            BelongsTo::make('Category'),
        ];
    }
}
```

## Licence

Nova se vend par développeur ou par site, sans offre gratuite pour un usage commercial. En échange, vous avez des canaux de support officiels, la compatibilité avec chaque nouvelle version de Laravel le jour de sa sortie, et une feuille de route décidée par l'équipe qui écrit le framework.

## Quand le choisir

Les équipes ou les agences qui veulent un contrat de support derrière leur administration, ou qui paient déjà d'autres produits Laravel (Forge, Vapor, voir [Livrer en production](ch16-01-laravel-forge-vapor.md)) et veulent un seul fournisseur responsable de toute la stack.

## Quand ce n'est pas le bon outil

Un budget serré, ou une équipe qui se satisfait de la communauté open source de Filament. Vu de l'extérieur, la plupart des projets ne distinguent pas les deux panneaux.

> **Sous le capot :** être un produit payant ne change rien à la façon dont Nova s'intègre à Laravel. Il s'installe par Composer comme n'importe quel paquet, avec le même service provider et le même mécanisme de découverte que les paquets gratuits. La licence est une décision commerciale posée sur une architecture de paquet PHP tout à fait ordinaire.
