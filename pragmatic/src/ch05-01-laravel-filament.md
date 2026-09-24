# Laravel: Filament in an Afternoon

Point Filament at an Eloquent model and it builds the admin resource around it: a list with search and filters, a create form, an edit form, delete actions. **You configure a single PHP class; you do not write the screens.**

```bash
composer require filament/filament
php artisan filament:install --panels
php artisan make:filament-resource Product --generate
```

The last command inspects the `products` table and pre-fills a resource class. What is left is usually a short list of fields:

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

That is a searchable, sortable, paginated screen with validated create and edit forms. No HTML, no controller.

## When to reach for this

Any Laravel project that needs an internal admin screen and can live with what a schema-driven form and table express. That covers most back-office requests.

## When it's the wrong fit

A customer-facing dashboard with a custom design. A generated panel fights that kind of design instead of speeding it up. Filament is built for internal tools, not product surfaces.

> **Under the hood:** Filament's form and table builders are fluent, chainable PHP objects (`TextInput::make(...)->required()->numeric()`). Named arguments and first-class enums make that style pleasant to write: one method call configures behavior that used to need several array keys or config options.
