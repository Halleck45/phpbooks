# Laravel Nova ($): The Official, Supported Alternative to Filament

Nova is Laravel's own first-party admin panel, built and maintained by the Laravel team itself rather than the open-source community. Functionally it overlaps heavily with [Filament](ch05-01-laravel-filament.md): resources generated from Eloquent models, searchable and filterable tables, custom fields and actions. The difference is who's on the other end when something breaks or a new Laravel version ships.

```bash
composer require laravel/nova
php artisan nova:install
php artisan make:nova-resource Product
```

```php
public function fields(NovaRequest $request): array
{
    return [
        ID::make()->sortable(),
        Text::make('Name')->sortable()->rules('required', 'max:255'),
        Currency::make('Price'),
        BelongsTo::make('Category'),
    ];
}
```

## Licensing

Nova is sold under a paid, per-developer or per-site license, with no free tier for commercial use, which is what earns it the `$`. In exchange, you get official support channels, guaranteed compatibility with new Laravel releases on the same schedule, and a roadmap set by the same team that builds the framework.

## When to reach for this

Teams or agencies that want an admin panel with an official support contract behind it, or that are already paying for other Laravel ecosystem products (Forge, Vapor, see [Shipping to Production](ch16-01-laravel-forge-vapor.md)) and want one vendor accountable for the whole stack.

## When it's the wrong fit

A budget-conscious project, or a team happy to rely on Filament's large open-source community for support instead of a paid vendor relationship. Feature-for-feature, most projects can't tell the difference from the outside.

> **Under the hood:** Being a paid product changes nothing about how Nova integrates with Laravel: it's installed via Composer like anything else, using the same service provider and package discovery mechanism as free packages. The license model is a business decision layered on top of ordinary PHP package architecture, not a technical one.
