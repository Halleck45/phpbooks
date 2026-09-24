# API Platform: A Full API From One PHP Class

API Platform's entire pitch is in this example. One class, decorated with a single attribute, becomes a complete, documented API:

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

That's it. Running this gives you, with no further code:

- `GET /api/products` and `GET /api/products/{id}`
- `POST /api/products`, `PUT`, and `DELETE`, with request validation
- An interactive OpenAPI/Swagger documentation page at `/api/docs`
- A GraphQL endpoint at `/api/graphql`, if the GraphQL package is installed

Restricting which operations are exposed, or filtering, is configuration on the same attribute rather than new controller code:

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

Any project where the API *is* the product, or where you need to move fast on a data model that's still evolving and don't want to hand-maintain matching controllers, serializers, and docs for every change.

## When it's the wrong fit

An API with only one or two endpoints and no plan to grow, where the convention and setup cost of API Platform outweighs just writing two controller methods directly.

> **Under the hood:** This is possible because PHP attributes are readable at runtime via reflection, letting API Platform inspect your class, its properties, and their types, then generate routing, validation, and an OpenAPI schema from that single source of truth instead of three separate ones.
