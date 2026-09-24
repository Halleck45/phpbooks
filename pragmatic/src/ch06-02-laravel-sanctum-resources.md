# Laravel: Sanctum, Resources, and API Versioning

Laravel's default approach is more manual than [API Platform's](ch06-01-api-platform-from-one-class.md), and that is often the point. **Routes, controllers, and response shapes stay explicit, at the cost of a little more code per endpoint.**

**Sanctum** handles authentication for SPA and mobile clients (session-based) and for third-party consumers (token-based), from one package.

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

**API Resources** shape a model into a consistent JSON response. Your database columns and your public contract stop being the same thing:

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

**Versioning** is usually a route prefix, and deliberately nothing more:

```php
Route::prefix('v1')->group(base_path('routes/api_v1.php'));
Route::prefix('v2')->group(base_path('routes/api_v2.php'));
```

## When to reach for this

The default for a Laravel project that exposes an API next to a web app, or a small to medium standalone API where control over each response shape matters more than generation.

## When it's the wrong fit

A large, fast-moving data model where a hand-written Resource class per model turns into maintenance. That is the case [API Platform](ch06-01-api-platform-from-one-class.md) is built for.

> **Under the hood:** Sanctum stores API tokens hashed, like passwords, but with PHP's `hash()` function rather than `password_hash()`. Tokens are high-entropy random strings, not user-chosen passwords, so a fast hash is enough of a defense here.
