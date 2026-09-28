# API Platform: An Admin Generated From Your API

If you build with API Platform (see [Shipping an API Other Teams Can Use](ch06-01-api-platform-from-one-class.md)), your data is already described well enough for an admin panel. **The panel reads the API's own schema, so there is no admin-specific code to write.**

Take a resource already exposed through the API:

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

API Platform's admin package reads the OpenAPI schema and renders a React-based interface (list, create, edit, delete) against it:

```bash
npm install @api-platform/admin
```

```javascript
// src/App.js
import { HydraAdmin } from '@api-platform/admin';

export default () => <HydraAdmin entrypoint="https://api.example.com" />;
```

No field-by-field configuration is needed for a working panel. You add configuration only where a default needs overriding, such as a custom widget for one field.

## When to reach for this

Any project already built on an API Platform backend. The panel is close to free at that point: it reads metadata you produced for the API documentation, instead of asking you to describe the data model a second time.

## When it's the wrong fit

A project with no API layer. Standing up an API just to get this generator is a detour, when [Filament](ch05-01-laravel-filament.md) or [EasyAdmin](ch05-02-symfony-easyadmin.md) would generate the same panel straight from the database.

> **Under the hood:** API Platform generates a machine-readable OpenAPI (and Hydra/JSON-LD) description of your API from the PHP attributes on your classes. The admin panel is a generic client that renders a UI from *any* API described that way, not something written for your project.
