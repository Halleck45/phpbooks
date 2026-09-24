# Symfony : UX Turbo et Mercure

Le temps réel de Symfony repose sur Mercure, un protocole ouvert et non une invention maison. **Les mises à jour arrivent au navigateur en HTTP ordinaire, sous forme de Server-Sent Events, et n'importe quel client peut s'y abonner, pas seulement un front Symfony.**

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

**Turbo**, par le paquet `symfony/ux-turbo`, abonne la page à cette mise à jour et remplace le fragment HTML concerné. Un attribut de données tient lieu de JavaScript écrit à la main :

```twig
<turbo-stream-source src="{{ mercure('orders/' ~ order.id) }}"></turbo-stream-source>

<div id="order-{{ order.id }}-status">
    {{ order.status }}
</div>
```

Quand le serveur diffuse une mise à jour Turbo Stream correspondante, Turbo remplace ce `<div>` sur place. Pas de rechargement, pas de code client à écrire.

## Quand le choisir

Un projet Symfony qui veut des mises à jour en direct sans framework JavaScript séparé, et en particulier un projet où un protocole ouvert, fondé sur HTTP, compte pour des raisons d'infrastructure ou de conformité.

## Quand ce n'est pas le bon outil

Un trafic bidirectionnel à haute fréquence : une interaction multijoueur en direct, un tableau de bord de trading rafraîchi plusieurs fois par seconde. Les Server-Sent Events ne vont que dans un sens, par conception, et une connexion WebSocket convient mieux à ce travail.

> **Sous le capot :** les Server-Sent Events sont une fonctionnalité HTTP ordinaire : une réponse longue qui continue d'envoyer des morceaux au fil du temps. Mercure bâtit un hub complet de publication et d'abonnement sur cette seule primitive, et c'est pourquoi il traverse l'infrastructure HTTP habituelle (proxies, répartiteurs de charge) là où un WebSocket brut réclame parfois une configuration à part.
