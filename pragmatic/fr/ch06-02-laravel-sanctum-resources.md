# Laravel : Sanctum, Resources et versions d'API

L'approche par défaut de Laravel est plus manuelle que celle d'[API Platform](ch06-01-api-platform-from-one-class.md), et c'est souvent voulu. **Routes, contrôleurs et formes de réponse restent explicites, au prix d'un peu plus de code par endpoint.**

**Sanctum** gère l'authentification des clients SPA et mobiles (par session) et celle des consommateurs tiers (par jeton), depuis un seul paquet.

```bash
composer require laravel/sanctum
php artisan vendor:publish --provider="Laravel\Sanctum\SanctumServiceProvider"
php artisan migrate
```

```php
// issuing a token
$token = $user->createToken('mobile-app')->plainTextToken;

// protecting a route
Route::middleware('auth:sanctum')->get('/api/user', fn (Request $r) => $r->user());
```

**Les API Resources** donnent à un modèle une forme JSON stable. Vos colonnes de base de données et votre contrat public cessent d'être la même chose :

```php
class ProductResource extends JsonResource
{
    public function toArray(Request $request): array
    {
        return [
            'id' => $this->id,
            'name' => $this->name,
            'price_usd' => number_format($this->price, 2),
        ];
    }
}

// in a controller
return ProductResource::collection(Product::paginate());
```

**Le versionnement** est le plus souvent un préfixe de route, et délibérément rien de plus :

```php
Route::prefix('v1')->group(base_path('routes/api_v1.php'));
Route::prefix('v2')->group(base_path('routes/api_v2.php'));
```

## Quand le choisir

Le choix par défaut pour un projet Laravel qui expose une API à côté d'une application web, ou pour une API autonome de taille petite à moyenne où le contrôle de chaque forme de réponse compte plus que la génération.

## Quand ce n'est pas le bon outil

Un gros modèle de données qui évolue vite, où une classe Resource écrite à la main par modèle devient de la maintenance. C'est le cas pour lequel [API Platform](ch06-01-api-platform-from-one-class.md) est fait.

> **Sous le capot :** Sanctum stocke les jetons d'API hachés, comme des mots de passe, mais avec la fonction `hash()` de PHP plutôt qu'avec `password_hash()`. Un jeton est une chaîne aléatoire à forte entropie, pas un mot de passe choisi par un humain, et un hachage rapide suffit donc à le protéger.
