# Pusher ($): Managed WebSockets Without Running Your Own Server

Pusher does one thing: it runs the WebSocket infrastructure for you, so a feature that would otherwise need [Reverb](ch07-01-laravel-reverb-livewire.md) or [Mercure](ch07-02-symfony-ux-turbo-mercure.md) running as a service you operate becomes an API call and an npm package instead.

```bash
composer require pusher/pusher-php-server
```

```php
$pusher = new Pusher\Pusher(
    getenv('PUSHER_KEY'),
    getenv('PUSHER_SECRET'),
    getenv('PUSHER_APP_ID'),
    ['cluster' => 'us2', 'useTLS' => true],
);

$pusher->trigger('orders-channel', 'order.shipped', [
    'order_id' => $order->id,
    'status' => 'shipped',
]);
```

Laravel's broadcasting system, notably, was built with Pusher as its original target and still supports it as a drop-in swap for Reverb, same event classes, same `broadcast()` call, different config value:

```php
// .env
BROADCAST_DRIVER=pusher
```

## Pricing

Pusher bills by concurrent connections and messages per day, with a free tier generous enough for development and small production apps, scaling to a real monthly cost once traffic grows, which is what earns it the `$`.

## When to reach for this

A team that doesn't want to operate WebSocket infrastructure at all, or a project where traffic is unpredictable enough that a managed, auto-scaling connection layer is worth paying for over self-hosting Reverb or a Mercure hub.

## When it's the wrong fit

A project with predictable, modest real-time traffic where Reverb or Mercure, both free and self-hosted, cost nothing beyond the server you're likely already running.

> **Under the hood:** Because Laravel's broadcasting abstraction was designed against Pusher's API shape from the start, swapping between Pusher and Reverb is a configuration change, not a code change. The lesson generalizes: a good abstraction layer is what makes "self-host it" versus "pay someone else to run it" a decision you can defer, or reverse, without a rewrite.
