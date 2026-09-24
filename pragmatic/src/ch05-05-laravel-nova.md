# Laravel Nova ($): The Official, Supported Alternative to Filament

Nova is the admin panel built and maintained by the Laravel team itself. Feature for feature it overlaps heavily with [Filament](ch05-01-laravel-filament.md): resources generated from Eloquent models, searchable and filterable tables, custom fields and actions. **The difference is who answers when something breaks or a new Laravel version ships.**

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

## Licensing

Nova is sold per developer or per site, with no free tier for commercial use. In exchange you get official support channels, compatibility with new Laravel releases on the same schedule, and a roadmap set by the team that builds the framework.

## When to reach for this

Teams or agencies that want a support contract behind their admin panel, or that already pay for other Laravel products (Forge, Vapor, see [Shipping to Production](ch16-01-laravel-forge-vapor.md)) and want one vendor accountable for the whole stack.

## When it's the wrong fit

A tight budget, or a team happy to rely on Filament's open-source community. From the outside, most projects cannot tell the two panels apart.

> **Under the hood:** Being a paid product changes nothing about how Nova integrates with Laravel. It installs through Composer like anything else, with the same service provider and package discovery mechanism as a free package. The license is a business decision layered on top of ordinary PHP package architecture.
