# API Platform : une API complète à partir d'une classe PHP

Tout l'argumentaire d'API Platform tient dans un exemple. **Une classe et un attribut donnent une API complète et documentée.**

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

C'est tout. Sans une ligne de plus, vous obtenez :

- `GET /api/products` et `GET /api/products/{id}`
- `POST /api/products`, `PUT` et `DELETE`, avec validation des requêtes
- une page de documentation interactive OpenAPI/Swagger sur `/api/docs`
- un endpoint GraphQL sur `/api/graphql`, si le paquet GraphQL est installé

Restreindre les opérations ou ajouter des filtres se fait par configuration sur le même attribut, pas par un nouveau contrôleur :

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

## Quand le choisir

Un projet où l'API *est* le produit, ou un modèle de données qui bouge encore assez vite pour que maintenir à la main les contrôleurs, les sérialiseurs et la documentation à chaque changement vous ralentisse.

## Quand ce n'est pas le bon outil

Une API à un ou deux endpoints, sans perspective de croissance. Là, les conventions et la mise en place d'API Platform coûtent plus cher que deux méthodes de contrôleur.

> **Sous le capot :** les attributs PHP se lisent à l'exécution par réflexion. API Platform inspecte votre classe, ses propriétés et leurs types, puis génère le routage, la validation et le schéma OpenAPI depuis cette source unique de vérité, au lieu de trois sources séparées.
