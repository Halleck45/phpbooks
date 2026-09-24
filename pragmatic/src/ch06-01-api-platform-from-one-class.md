# API Platform: A Full API From One PHP Class

API Platform's whole pitch fits in one example. **One class with one attribute becomes a complete, documented API.**

```php
<?php

namespace App\Entity;

use ApiPlatform\Metadata\ApiResource;
use Doctrine\ORM\Mapping as ORM;

#[ORM\Entity]
#[ApiResource]
class Product
{
    #[ORM\Id, ORM\GeneratedValue, ORM\Column]
    public ?int $id = null;

    #[ORM\Column(length: 255)]
    public string $name;

    #[ORM\Column]
    public float $price;
}
```

That is all. With no further code you get:

- `GET /api/products` and `GET /api/products/{id}`
- `POST /api/products`, `PUT`, and `DELETE`, with request validation
- An interactive OpenAPI/Swagger documentation page at `/api/docs`
- A GraphQL endpoint at `/api/graphql`, if the GraphQL package is installed

Restricting the operations, or adding filters, is configuration on the same attribute rather than new controller code:

```php
#[ApiResource(
    operations: [new GetCollection(), new Get(), new Post(security: 'is_granted("ROLE_ADMIN")')],
)]
#[ApiFilter(SearchFilter::class, properties: ['name' => 'partial'])]
class Product
{
    // ...
}
```

## When to reach for this

A project where the API *is* the product, or a data model still evolving fast enough that hand-maintaining matching controllers, serializers, and docs for every change would slow you down.

## When it's the wrong fit

An API with one or two endpoints and no plan to grow. There, the conventions and setup of API Platform cost more than writing two controller methods.

> **Under the hood:** PHP attributes are readable at runtime through reflection. API Platform inspects your class, its properties, and their types, then generates routing, validation, and an OpenAPI schema from that single source of truth instead of three separate ones.
