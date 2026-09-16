# Laravel: Filament in an Afternoon

Filament reads an Eloquent model and generates a full admin resource around it: list view with search and filters, a create form, an edit form, and delete actions, from a single PHP class you mostly just configure rather than write from scratch.

```bash
composer require filament/filament
php artisan filament:install --panels
php artisan make:filament-resource Product --generate
```

That last command inspects the `products` table and pre-fills a resource class. What's left is usually a short list of field definitions:

```php
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Select;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Columns\BooleanColumn;

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
        BooleanColumn::make('is_active'),
    ]);
}
```

That's a searchable, sortable, paginated admin screen with validated create and edit forms, no hand-written HTML or controller logic.

## When to reach for this

Any Laravel project that needs an internal admin screen and doesn't need to customize its behavior beyond what a schema-driven form and table can express, which covers the large majority of real "back office" requests.

## When it's the wrong fit

A public-facing customer dashboard with heavily custom UX, where "generated admin panel" would fight the design rather than speed it up. Filament is built for internal tools, not customer-facing product surfaces.

> **Under the hood:** Filament's form and table builders are fluent, chainable PHP objects (`TextInput::make(...)->required()->numeric()`), a pattern made pleasant to write by PHP's named arguments and first-class enum support, which let a single method call configure behavior that used to need several array keys or config options to express.
