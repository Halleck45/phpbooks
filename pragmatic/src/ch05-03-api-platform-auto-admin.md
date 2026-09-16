# API Platform: An Admin Generated From Your API

If you're already building an API with API Platform (see [Shipping an API Other Teams Can Use](ch06-01-api-platform-from-one-class.md)), you've already described your data well enough to generate an admin panel from it too, with no separate admin-specific code.

Given a resource already exposed through the API:

```php
#[ApiResource]
class Product
{
    public ?int $id = null;

    #[ApiProperty(description: 'The product name')]
    public string $name;

    public float $price;

    #[ApiProperty]
    public ?Category $category = null;
}
```

API Platform's admin package reads the API's own OpenAPI schema and renders a working React-based admin interface, list, create, edit, delete, against it directly:

```bash
composer create-project api-platform/admin my-admin
```

```javascript
// src/App.js
import { HydraAdmin } from '@api-platform/admin';

export default () => <HydraAdmin entrypoint="https://api.example.com" />;
```

No field-by-field configuration is required to get a working panel; you only add configuration where the defaults need overriding, like a custom widget for a specific field.

## When to reach for this

Any project already built around an API Platform backend. The admin panel is nearly free at that point: it's reading metadata you already produced for API documentation, not asking you to describe your data model a second time.

## When it's the wrong fit

A project with no existing API layer. Standing up an API purely to unlock this admin generator, when [Filament](ch05-01-laravel-filament.md) or [EasyAdmin](ch05-02-symfony-easyadmin.md) would generate the same panel directly from the database, is unnecessary indirection.

> **Under the hood:** This works because API Platform generates a machine-readable OpenAPI (and Hydra/JSON-LD) description of your API automatically, from PHP attributes on your classes. The admin panel is a generic client that can render a UI from *any* API described that way, not something written specifically for your project.
