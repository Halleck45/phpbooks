# Catching It in Production: Sentry and Flare ($)

Tests catch what you thought to test for. Static analysis catches what the type system can prove. Neither catches what a user does at 11 p.m. that nobody anticipated. **Error tracking is confidence past the deploy button:** you learn that something broke for a real person the moment it happens, with a stack trace, instead of a support email that says "it's broken."

**Sentry** works across every framework in this book, with SDKs for Laravel, Symfony and plain PHP.

```bash
composer require sentry/sentry-laravel
php artisan sentry:publish --dsn=your-dsn-here
```

```php
try {
    $order->submit();
} catch (\Throwable $e) {
    \Sentry\captureException($e);
    throw $e;
}
```

Uncaught exceptions are captured automatically once the SDK is installed. The manual call above is for an error you handle gracefully but still want to know about.

**Flare ($)**, from Spatie in the Laravel ecosystem, is scoped to Laravel and adds framework-aware context to every report: which route, which query, which job, next to the stack trace.

```bash
composer require spatie/laravel-flare
```

## Pricing

Sentry has a usable free tier for small projects and a paid plan as event volume grows. Flare is a paid product with a free trial and no free tier for ongoing use. Both carry the `$` here, Sentry's more conditional than Flare's.

## When to reach for this

Any application in production. Waiting for a user to report a bug they cannot describe costs more debugging time than the subscription.

## When it's the wrong fit

A prototype, or an internal tool with a handful of users who will ping you directly when something breaks. The setup is not justified yet.

> **Under the hood:** These tools hook into PHP's own exception and error handlers (`set_exception_handler()`, `set_error_handler()`). That is why installing them is a few lines of bootstrap code rather than a wrapper around every function call in your application.
