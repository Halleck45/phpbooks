# Pusher ($) : des WebSockets gérés, sans serveur à faire tourner

Pusher fait une seule chose : il fait tourner l'infrastructure WebSocket à votre place. **Une fonctionnalité qui exigerait [Reverb](ch07-01-laravel-reverb-livewire.md) ou [Mercure](ch07-02-symfony-ux-turbo-mercure.md) comme service à exploiter devient un appel d'API et un paquet npm.**

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

Le système de diffusion de Laravel a été conçu avec Pusher pour cible d'origine, et il se substitue toujours à Reverb avec les mêmes classes d'événements et le même appel `broadcast()`. Seule une valeur de configuration change :

```ini
# .env
BROADCAST_CONNECTION=pusher
```

## Tarif

Pusher facture au nombre de connexions simultanées et de messages par jour. L'offre gratuite couvre le développement et les petites applications en production ; au-delà, la facture mensuelle suit le trafic.

## Quand le choisir

Une équipe qui ne veut pas du tout exploiter d'infrastructure WebSocket, ou un projet dont le trafic est assez imprévisible pour qu'une couche de connexions gérée et auto-dimensionnée batte l'auto-hébergement de Reverb ou d'un hub Mercure.

## Quand ce n'est pas le bon outil

Un trafic temps réel modeste et prévisible. Reverb et Mercure sont gratuits, auto-hébergés, et ne coûtent rien de plus que le serveur que vous faites probablement déjà tourner.

> **Sous le capot :** l'abstraction de diffusion de Laravel ayant été dessinée sur la forme de l'API de Pusher, remplacer Pusher par Reverb est un changement de configuration, pas de code. La leçon se généralise : une bonne abstraction est ce qui fait de « l'héberger soi-même » contre « payer quelqu'un pour le faire » une décision qu'on peut repousser, ou inverser, sans réécriture.
