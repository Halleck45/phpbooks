# Laravel: Cashier and Stripe ($) for Custom Checkouts

Not every "we need to take payments" request is a storefront. Often it is one subscription plan, a one-time checkout, or usage-based billing bolted onto an app that is not a store at all. **Cashier is Laravel's official wrapper around Stripe (and, in a separate package, Paddle), built for that case.**

```bash
composer require laravel/cashier
php artisan vendor:publish --tag="cashier-migrations"
php artisan migrate
```

```php
class User extends Authenticatable
{
    use Billable;
}

// starting a subscription
$user->newSubscription('default', 'price_monthly_pro')
    ->create($paymentMethodId);

// checking access
if ($user->subscribed('default')) {
    // grant access
}

// a one-time checkout, no subscription
return $user->checkout(['price_one_time_item']);
```

Webhooks (payment succeeded, subscription canceled, card expired) land on a route Cashier registers for you. Your database stays in sync with Stripe without polling.

## Pricing

Stripe charges a percentage plus a fixed amount per successful charge; that is the `$` in the title. Cashier itself, the Laravel package, is free and open source.

## When to reach for this

A Laravel app that needs subscriptions, one-time payments, or usage billing, without a product catalog. SaaS pricing tiers, not a shopping cart.

## When it's the wrong fit

A catalog with inventory, variations, and shipping. That is [WooCommerce](ch09-01-woocommerce.md) or [Sylius](ch09-02-sylius.md) territory. Cashier has no notion of a product beyond a Stripe price ID.

> **Under the hood:** Cashier verifies each incoming Stripe webhook with a cryptographic signature check against a shared secret, so the request is known to come from Stripe and not from a spoofer before its payload is trusted to update a subscription in your database.
