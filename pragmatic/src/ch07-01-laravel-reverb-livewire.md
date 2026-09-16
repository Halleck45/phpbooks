# Laravel: Reverb and Livewire Without Writing JavaScript

Reverb is Laravel's own WebSocket server, self-hosted and free, built to slot directly into Laravel's existing broadcasting system with no third-party service required.

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

Paired with **Livewire**, the frontend side often needs no JavaScript at all. A Livewire component can listen for a broadcast event and re-render automatically:

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

The Blade template just renders `$order->status`; Livewire handles re-rendering that fragment over the WebSocket connection when the event fires, no client-side state management written by hand.

## When to reach for this

Laravel projects wanting real-time features (notifications, live status updates, simple chat) without adopting a separate frontend framework or paying for a third-party WebSocket service.

## When it's the wrong fit

A highly interactive, JavaScript-heavy frontend (a canvas-based editor, a complex single-page app) where Livewire's server-round-trip model adds latency a client-side framework wouldn't have. Reverb still works there as the transport; Livewire specifically is the piece worth reconsidering.

> **Under the hood:** Reverb is built on PHP Fibers, introduced in PHP 8.1, which let a single PHP process hold many open connections and switch between them cooperatively instead of blocking. That's what makes a persistent WebSocket server practical to write in PHP at all, a job PHP's traditional one-request-per-process model was never suited for.
