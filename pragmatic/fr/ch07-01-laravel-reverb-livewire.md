# Laravel : Reverb et Livewire, sans écrire de JavaScript

Reverb est le serveur WebSocket de Laravel, auto-hébergé et gratuit. **Il se branche sur le système de diffusion d'événements déjà présent dans Laravel, et le service tiers devient facultatif.**

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

Associé à **Livewire**, le front n'a souvent besoin d'aucun JavaScript. Un composant Livewire écoute l'événement diffusé et se réaffiche de lui-même :

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

Le template Blade affiche `$order->status`, rien d'autre. Quand l'événement arrive, Livewire réaffiche ce fragment par la connexion WebSocket, sans le moindre état client écrit à la main.

## Quand le choisir

Un projet Laravel qui veut des notifications, des statuts en direct ou un chat simple sans adopter un framework front séparé ni payer un service de WebSockets.

## Quand ce n'est pas le bon outil

Un front chargé en JavaScript (un éditeur sur canvas, une application monopage complexe), où l'aller-retour serveur de Livewire ajoute une latence qu'un framework côté client n'aurait pas. Reverb reste utilisable comme transport. C'est Livewire qu'il faut reconsidérer.

> **Sous le capot :** Reverb repose sur les Fibers de PHP, arrivées avec PHP 8.1. Un seul processus PHP peut tenir de nombreuses connexions ouvertes et passer de l'une à l'autre de façon coopérative au lieu de bloquer. C'est ce qui rend un serveur WebSocket persistant praticable en PHP, un travail pour lequel le modèle d'un processus par requête n'a jamais été fait.
