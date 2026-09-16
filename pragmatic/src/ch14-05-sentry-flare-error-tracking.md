# Catching It in Production: Sentry and Flare ($)

Tests catch what you thought to test for. Static analysis catches what the type system can prove. Neither catches the thing a real user does at 11 p.m. that nobody anticipated. That's what error tracking is for: confidence doesn't stop at the deploy button, it extends into knowing, immediately, when something breaks for a real person, with a full stack trace instead of a support email that just says "it's broken."

**Sentry** works across every framework covered in this book, with SDKs for Laravel, Symfony, and plain PHP alike.

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

Uncaught exceptions are captured automatically once installed; the manual call above is for cases where you want to log something that's handled gracefully but still worth knowing about.

**Flare ($)**, from the Laravel ecosystem's Spatie, is more tightly scoped to Laravel specifically, with deeper framework-aware context in every report: which route, which query, which job, alongside the stack trace.

```bash
composer require facade/ignition
```

## Pricing

Sentry has a genuinely usable free tier for small projects, scaling to a paid plan as event volume grows. Flare is a paid product with a free trial, no meaningful free tier for ongoing use, which is why both carry the `$` here even though Sentry's is more conditional.

## When to reach for this

Any application in real production use, full stop. The alternative, waiting for a user to report a bug they can't fully describe, costs far more debugging time than the subscription.

## When it's the wrong fit

A prototype or an internal tool with a handful of users who'll simply ping you directly when something breaks; the overhead of setting this up isn't justified yet.

> **Under the hood:** These tools hook into PHP's own exception handler and error reporting mechanism (`set_exception_handler()`, `set_error_handler()`), which is why installing them is typically a few lines of bootstrap code rather than wrapping every function call in your application by hand.
