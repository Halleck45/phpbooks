# Laravel : Cashier et Stripe ($) pour un paiement sur mesure

Toutes les demandes « il faut qu'on encaisse des paiements » ne sont pas des boutiques. Souvent, c'est un seul abonnement, un paiement unique ou une facturation à l'usage greffée sur une application qui n'a rien d'un magasin. **Cashier est l'enveloppe officielle de Laravel autour de Stripe (et, dans un paquet séparé, de Paddle), conçue pour ce cas précis.**

```bash
composer require laravel/cashier
php artisan vendor:publish --tag="cashier-migrations"
php artisan migrate
```

```php
class User extends Authenticatable
{
    use Billable;
}

// starting a subscription
$user->newSubscription('default', 'price_monthly_pro')
    ->create($paymentMethodId);

// checking access
if ($user->subscribed('default')) {
    // grant access
}

// a one-time checkout, no subscription
return $user->checkout(['price_one_time_item']);
```

Les webhooks (paiement réussi, abonnement annulé, carte expirée) arrivent sur une route que Cashier enregistre pour vous. Votre base reste alignée sur l'état de Stripe sans interrogation répétée.

## Tarif

Stripe prélève un pourcentage plus un montant fixe par paiement réussi ; c'est le `$` du titre. Cashier lui-même, le paquet Laravel, est gratuit et open source.

## Quand le choisir

Une application Laravel qui a besoin d'abonnements, de paiements uniques ou de facturation à l'usage, sans catalogue de produits. Des paliers tarifaires de SaaS, pas un panier.

## Quand ce n'est pas le bon outil

Un catalogue avec des stocks, des déclinaisons et de la livraison. C'est le territoire de [WooCommerce](ch09-01-woocommerce.md) ou de [Sylius](ch09-02-sylius.md). Cashier n'a aucune notion de produit au-delà d'un identifiant de prix Stripe.

> **Sous le capot :** Cashier vérifie chaque webhook entrant de Stripe par une signature cryptographique contrôlée avec un secret partagé, si bien que la requête est reconnue comme venant de Stripe et non d'un usurpateur avant que son contenu ne serve à mettre à jour un abonnement dans votre base.
