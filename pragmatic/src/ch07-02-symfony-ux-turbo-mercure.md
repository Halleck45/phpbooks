# Symfony: UX Turbo and Mercure

Symfony's real-time story is built on Mercure, an open protocol rather than a Symfony invention. **Updates reach the browser over plain HTTP, as Server-Sent Events, so any client can subscribe, not only a Symfony front end.**

```bash
composer require symfony/mercure-bundle
# Mercure hub runs as a small standalone binary, or via Docker
```

```php
use Symfony\Component\Mercure\HubInterface;
use Symfony\Component\Mercure\Update;

class OrderController
{
    public function ship(Order $order, HubInterface $hub): Response
    {
        $order->markShipped();

        $hub->publish(new Update(
            "orders/{$order->getId()}",
            json_encode(['status' => 'shipped']),
        ));

        return new Response('OK');
    }
}
```

**Turbo**, through the `symfony/ux-turbo` package, subscribes the page to that update and swaps the matching HTML fragment. One data attribute replaces the hand-written JavaScript:

```twig
<turbo-stream-source src="{{ mercure('orders/' ~ order.id) }}"></turbo-stream-source>

<div id="order-{{ order.id }}-status">
    {{ order.status }}
</div>
```

When the server broadcasts a matching Turbo Stream update, Turbo replaces that `<div>` in place. No reload, no custom client code.

## When to reach for this

A Symfony project that wants live updates without a separate JavaScript framework, and in particular one where an open, HTTP-based protocol matters for infrastructure or compliance reasons.

## When it's the wrong fit

High-frequency, two-way traffic: live multiplayer interaction, a trading dashboard with sub-second updates. Server-Sent Events are one-way by design, and a WebSocket connection fits that job better.

> **Under the hood:** Server-Sent Events are a plain HTTP feature: a long-lived response that keeps sending chunks over time. Mercure builds a full publish/subscribe hub on that one primitive, which is why it passes through ordinary HTTP infrastructure (proxies, load balancers) that a raw WebSocket sometimes needs special configuration for.
