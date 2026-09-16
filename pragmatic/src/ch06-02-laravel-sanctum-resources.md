# Laravel: Sanctum, Resources, and API Versioning

Laravel's default approach is more manual than [API Platform's](ch06-01-api-platform-from-one-class.md), and that's often the point: routes, controllers, and response shapes stay explicit and easy to reason about, at the cost of writing a bit more per endpoint.

**Sanctum** handles authentication for both SPA/mobile clients (session-based) and third-party API consumers (token-based), from one package.

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

**API Resources** shape a model into a consistent JSON response, decoupling your database columns from your API's public contract:

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

**Versioning** is typically just route prefixing, kept deliberately simple:

```php
Route::prefix('v1')->group(base_path('routes/api_v1.php'));
Route::prefix('v2')->group(base_path('routes/api_v2.php'));
```

## When to reach for this

The default choice for a Laravel project exposing an API alongside a web app, or a small-to-medium standalone API where explicit control over each response shape matters more than automatic generation.

## When it's the wrong fit

A large, rapidly evolving data model where writing a Resource class by hand for every model becomes real maintenance overhead. That's the case [API Platform](ch06-01-api-platform-from-one-class.md) is built for.

> **Under the hood:** Sanctum's API tokens are stored hashed, the same way passwords are, using PHP's `hash()` function rather than `password_hash()` since tokens are high-entropy random strings rather than user-chosen passwords, so a fast hash is an appropriate and sufficient defense here.
