# Laravel: Reverb and Livewire Without Writing JavaScript

Reverb is Laravel's own WebSocket server, self-hosted and free. **It slots into Laravel's existing broadcasting system, so a third-party service becomes optional.**

```bash
composer require laravel/reverb
php artisan reverb:install
php artisan reverb:start
```

```php
// broadcasting an event from anywhere in the app
broadcast(new OrderShipped($order))->toOthers();

// the event class
class OrderShipped implements ShouldBroadcast
{
    public function __construct(public Order $order) {}

    public function broadcastOn(): Channel
    {
        return new PrivateChannel('orders.' . $this->order->user_id);
    }
}
```

Paired with **Livewire**, the front end often needs no JavaScript at all. A Livewire component listens for the broadcast and re-renders itself:

```php
class OrderStatus extends Component
{
    public Order $order;

    #[On('echo-private:orders.{order.user_id},OrderShipped')]
    public function refreshStatus(): void
    {
        $this->order->refresh();
    }

    public function render()
    {
        return view('livewire.order-status');
    }
}
```

The Blade template renders `$order->status` and nothing else. When the event fires, Livewire re-renders that fragment over the WebSocket connection, with no client-side state written by hand.

## When to reach for this

A Laravel project that wants notifications, live status updates, or simple chat without adopting a separate front-end framework or paying for a WebSocket service.

## When it's the wrong fit

A JavaScript-heavy front end (a canvas editor, a complex single-page app), where Livewire's round trip to the server adds latency a client-side framework would not. Reverb still works there as the transport. Livewire is the piece to reconsider.

> **Under the hood:** Reverb is built on PHP Fibers, introduced in PHP 8.1. A single PHP process can hold many open connections and switch between them cooperatively instead of blocking. That is what makes a persistent WebSocket server practical in PHP, a job the one-request-per-process model was never suited for.
