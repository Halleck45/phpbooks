# Sylius: A Symfony-Based E-Commerce Framework

Sylius takes the opposite approach from WooCommerce. Instead of a plugin on a content platform, it is an e-commerce framework built from Symfony components. **It is aimed at stores whose business logic a generic plugin architecture would fight rather than support.**

```bash
composer create-project sylius/sylius-standard my-shop
cd my-shop
symfony console sylius:install
symfony server:start
```

Because it is Symfony, extending it means writing ordinary Symfony code (events, services, Doctrine entities) rather than learning a commerce-specific plugin API:

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

That is the event-listener pattern used throughout Symfony (see [Shipping Background Work](ch11-02-symfony-messenger.md)), applied to commerce events.

## When to reach for this

A storefront with custom pricing rules, order workflows, or B2B logic: tiered pricing, approval workflows, multi-warehouse fulfillment.

## When it's the wrong fit

A plain catalog with standard checkout needs. That is far more setup, and more Symfony to know, than [WooCommerce](ch09-01-woocommerce.md) asks for the same result.

> **Under the hood:** Sylius is assembled almost entirely from reusable Symfony components (the Form component, the Workflow component for order state machines, Doctrine for persistence), the same building blocks as [Chapter 2](ch02-00-standalone-components.md), put together for commerce rather than invented from scratch.
