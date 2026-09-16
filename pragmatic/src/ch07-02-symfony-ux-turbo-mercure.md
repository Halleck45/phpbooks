# Symfony: UX Turbo and Mercure

Symfony's real-time story is built on Mercure, an open protocol (not a Symfony-specific invention) for pushing updates to browsers over standard HTTP, using Server-Sent Events rather than a custom WebSocket implementation. That means any client, not just a Symfony frontend, can subscribe to it.

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

**Turbo**, via the `symfony/ux-turbo` package, subscribes the frontend to that same update and swaps the relevant HTML fragment automatically, with a data attribute instead of hand-written JavaScript:

```twig
<turbo-stream-source src="{{ mercure('orders/' ~ order.id) }}"></turbo-stream-source>

<div id="order-{{ order.id }}-status">
    {{ order.status }}
</div>
```

When the server broadcasts a matching Turbo Stream update, Turbo replaces that `<div>` in place, no page reload, no custom client-side code.

## When to reach for this

Symfony projects that want real-time updates without introducing a separate JavaScript framework, especially where using an open, HTTP-based protocol (rather than a proprietary WebSocket server) matters for infrastructure or compliance reasons.

## When it's the wrong fit

Very high-frequency, bidirectional real-time needs (live multiplayer interaction, a trading dashboard with sub-second updates), where Server-Sent Events' one-way-by-design model is a worse fit than a true WebSocket connection.

> **Under the hood:** Server-Sent Events are a plain HTTP feature: a long-lived response that keeps sending chunks over time. Mercure builds a full publish/subscribe hub on top of that single primitive, which is part of why it works through ordinary HTTP infrastructure (proxies, load balancers) that a raw WebSocket connection sometimes needs special configuration to pass through.
