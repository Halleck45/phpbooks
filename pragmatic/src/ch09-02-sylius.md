# Sylius: A Symfony-Based E-Commerce Framework

Sylius takes the opposite approach from WooCommerce: instead of a plugin bolted onto a content platform, it's an e-commerce framework built from Symfony components from the ground up, aimed at stores with real custom business logic that a generic plugin architecture would fight rather than support.

```bash
composer create-project sylius/sylius-standard my-shop
cd my-shop
symfony console sylius:install
symfony server:start
```

Because it's built on Symfony, extending it means writing ordinary Symfony code (events, services, Doctrine entities) rather than learning a commerce-specific plugin API:

```php
class OrderPlacedListener
{
    public function __construct(private LoyaltyPointsCalculator $calculator) {}

    public function onOrderPlaced(ResourceControllerEvent $event): void
    {
        $order = $event->getSubject();
        $this->calculator->awardPoints($order->getCustomer(), $order->getTotal());
    }
}
```

```yaml
services:
    App\EventListener\OrderPlacedListener:
        tags:
            - { name: kernel.event_listener, event: sylius.order.post_create, method: onOrderPlaced }
```

That's the same event-listener pattern used throughout Symfony (see [Shipping Background Work](ch11-02-symfony-messenger.md)), applied to commerce events instead of custom application events.

## When to reach for this

A storefront with genuinely custom pricing rules, order workflows, or B2B logic (tiered pricing, approval workflows, multi-warehouse fulfillment) that would mean fighting a generic plugin system elsewhere.

## When it's the wrong fit

A straightforward catalog of products with standard checkout needs. That's a great deal more setup and Symfony familiarity than [WooCommerce](ch09-01-woocommerce.md) requires for the same practical result.

> **Under the hood:** Sylius is built almost entirely from reusable Symfony components (the Form component, the Workflow component for order state machines, Doctrine for persistence), the same building blocks covered in [Chapter 2](ch02-00-standalone-components.md), assembled specifically for commerce rather than invented from scratch.
