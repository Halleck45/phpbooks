# API Platform : une administration générée depuis votre API

Si vous construisez avec API Platform (voir [Livrer une API que d'autres équipes peuvent utiliser](ch06-01-api-platform-from-one-class.md)), vos données sont déjà décrites assez précisément pour une administration. **Le panneau lit le schéma de l'API elle-même, il n'y a donc aucun code d'administration à écrire.**

Prenez une ressource déjà exposée par l'API :

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

Le paquet d'administration d'API Platform lit le schéma OpenAPI et affiche par-dessus une interface React (liste, création, édition, suppression) :

```bash
npm install @api-platform/admin
```

```javascript
// src/App.js
import { HydraAdmin } from '@api-platform/admin';

export default () => <HydraAdmin entrypoint="https://api.example.com" />;
```

Aucune configuration champ par champ n'est nécessaire pour obtenir un panneau qui fonctionne. Vous n'en ajoutez que là où un défaut doit être remplacé, par exemple un composant personnalisé pour un champ.

## Quand le choisir

Tout projet déjà bâti sur un backend API Platform. À ce stade, le panneau est presque gratuit : il lit des métadonnées que vous avez produites pour la documentation de l'API, au lieu de vous demander de décrire le modèle de données une deuxième fois.

## Quand ce n'est pas le bon outil

Un projet sans couche API. Monter une API rien que pour ce générateur est un détour, alors que [Filament](ch05-01-laravel-filament.md) ou [EasyAdmin](ch05-02-symfony-easyadmin.md) produiraient le même panneau directement depuis la base de données.

> **Sous le capot :** API Platform génère une description lisible par machine de votre API, en OpenAPI et en Hydra/JSON-LD, à partir des attributs PHP posés sur vos classes. Le panneau d'administration est un client générique qui sait afficher une interface pour *n'importe quelle* API décrite ainsi, pas un programme écrit pour votre projet.
