# Pusher ($): Managed WebSockets Without Running Your Own Server

Pusher does one thing: it runs the WebSocket infrastructure for you. **A feature that would need [Reverb](ch07-01-laravel-reverb-livewire.md) or [Mercure](ch07-02-symfony-ux-turbo-mercure.md) running as a service you operate becomes an API call and an npm package.**

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

Laravel's broadcasting system was built with Pusher as its original target, and it still swaps in for Reverb with the same event classes and the same `broadcast()` call. Only a config value changes:

```ini
# .env
BROADCAST_CONNECTION=pusher
```

## Pricing

Pusher bills by concurrent connections and messages per day. The free tier covers development and small production apps; past that, the monthly cost grows with traffic.

## When to reach for this

A team that does not want to operate WebSocket infrastructure at all, or a project with traffic unpredictable enough that a managed, auto-scaling connection layer beats self-hosting Reverb or a Mercure hub.

## When it's the wrong fit

Predictable, modest real-time traffic. Reverb and Mercure are free and self-hosted, and cost nothing beyond the server you are probably already running.

> **Under the hood:** Because Laravel's broadcasting abstraction was designed against Pusher's API shape, swapping Pusher for Reverb is a configuration change, not a code change. The lesson generalizes: a good abstraction is what makes "self-host it" versus "pay someone to run it" a decision you can defer, or reverse, without a rewrite.
