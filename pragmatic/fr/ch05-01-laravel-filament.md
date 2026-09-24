# Laravel : Filament en un après-midi

Pointez Filament sur un modèle Eloquent et il bâtit la ressource d'administration autour : une liste avec recherche et filtres, un formulaire de création, un formulaire d'édition, des actions de suppression. **Vous configurez une seule classe PHP, vous n'écrivez pas les écrans.**

```bash
composer require filament/filament
php artisan filament:install --panels
php artisan make:filament-resource Product --generate
```

La dernière commande inspecte la table `products` et pré-remplit une classe de ressource. Ce qui reste à écrire tient le plus souvent en une courte liste de champs :

```php
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Select;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Columns\IconColumn;

class ProductResource extends Resource
{
    public static function form(Form $form): Form
    {
        return $form->schema([
            TextInput::make('name')->required(),
            TextInput::make('price')->numeric()->prefix('$'),
            Select::make('category_id')->relationship('category', 'name'),
        ]);
    }

    public static function table(Table $table): Table
    {
        return $table->columns([
            TextColumn::make('name')->searchable(),
            TextColumn::make('price')->money('usd'),
            IconColumn::make('is_active')->boolean(),
        ]);
    }
}
```

Vous obtenez un écran paginé, triable, avec recherche, et des formulaires de création et d'édition validés. Pas une ligne de HTML, pas de contrôleur.

## Quand le choisir

Tout projet Laravel qui a besoin d'un écran d'administration interne et se satisfait de ce qu'un formulaire et un tableau dérivés du schéma savent exprimer. C'est le cas de la plupart des demandes de back-office.

## Quand ce n'est pas le bon outil

Un tableau de bord destiné aux clients, avec un design sur mesure. Un panneau généré se bat contre ce genre de design au lieu de l'accélérer. Filament est fait pour les outils internes, pas pour les écrans d'un produit.

> **Sous le capot :** les constructeurs de formulaires et de tableaux de Filament sont des objets PHP fluides, chaînables (`TextInput::make(...)->required()->numeric()`). Les arguments nommés et les énumérations natives rendent ce style agréable à écrire : un appel de méthode configure ce qui demandait autrefois plusieurs clés de tableau ou options de configuration.
