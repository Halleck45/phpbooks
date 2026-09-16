# Laravel: Cashier and Stripe ($) for Custom Checkouts

Not every "we need to take payments" request is a storefront. Often it's a single subscription plan, a one-time checkout, or a usage-based billing model bolted onto an app that isn't a store at all. Cashier is Laravel's official wrapper around Stripe (and, in a separate package, Paddle), designed for exactly that.

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

Webhooks (payment succeeded, subscription canceled, card expired) are handled by a route Cashier registers automatically, keeping your database in sync with Stripe's state without polling.

## Pricing

Stripe itself is a paid, transaction-fee-based service (a percentage plus a fixed amount per successful charge), which is what earns it the `$` here. Cashier, the Laravel integration package, is free and open source; the cost is entirely on the payment processing side.

## When to reach for this

A Laravel app that needs subscriptions, one-time payments, or usage billing, but isn't a multi-product catalog store. Think SaaS pricing tiers, not a shopping cart.

## When it's the wrong fit

An actual product catalog with inventory, variations, and shipping. That's [WooCommerce](ch09-01-woocommerce.md) or [Sylius](ch09-02-sylius.md) territory; Cashier has no concept of a "product" beyond a Stripe price ID.

> **Under the hood:** Cashier verifies incoming Stripe webhooks using a cryptographic signature check against a shared secret, confirming the request genuinely came from Stripe and wasn't spoofed, before ever trusting its payload to update a subscription's status in your database.
