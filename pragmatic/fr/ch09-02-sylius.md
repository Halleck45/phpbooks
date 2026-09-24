# Sylius : un framework e-commerce bâti sur Symfony

Sylius prend le contre-pied de WooCommerce. Au lieu d'une extension posée sur une plateforme de contenu, c'est un framework e-commerce assemblé à partir de composants Symfony. **Il vise les boutiques dont la logique métier se heurterait à une architecture d'extensions générique au lieu d'y trouver un appui.**

```bash
composer create-project sylius/sylius-standard my-shop
cd my-shop
symfony console sylius:install
symfony server:start
```

Parce que c'est du Symfony, l'étendre revient à écrire du code Symfony ordinaire (événements, services, entités Doctrine) plutôt qu'à apprendre une API d'extensions propre au commerce :

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

C'est le motif écouteur d'événements employé partout dans Symfony (voir [Livrer du travail en arrière-plan](ch11-02-symfony-messenger.md)), appliqué aux événements du commerce.

## Quand le choisir

Une boutique avec des règles de prix, des workflows de commande ou une logique B2B qui lui sont propres : tarifs par paliers, circuits de validation, préparation depuis plusieurs entrepôts.

## Quand ce n'est pas le bon outil

Un simple catalogue avec un passage en caisse standard. C'est beaucoup plus de mise en place, et beaucoup plus de Symfony à connaître, que ce que [WooCommerce](ch09-01-woocommerce.md) demande pour le même résultat.

> **Sous le capot :** Sylius est assemblé presque entièrement à partir de composants Symfony réutilisables (le composant Form, le composant Workflow pour les machines à états des commandes, Doctrine pour la persistance), les mêmes briques qu'au [chapitre 2](ch02-00-standalone-components.md), agencées pour le commerce plutôt qu'inventées de zéro.
