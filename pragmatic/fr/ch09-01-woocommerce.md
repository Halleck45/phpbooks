# WooCommerce : le e-commerce par-dessus WordPress

Quand un site WordPress (voir [Livrer un site de contenu](ch03-01-wordpress-block-themes.md)) doit vendre quelque chose, WooCommerce est la réponse par défaut. **Il ajoute une boutique complète sous forme d'extension, dans l'administration que votre client connaît déjà :** produits, déclinaisons, panier, passage en caisse, commandes, codes promo.

```bash
wp plugin install woocommerce --activate
wp wc --version
```

Les produits sont un type de contenu personnalisé, et tout ce que vous savez de la gestion de contenu WordPress reste valable :

```php
$product = new WC_Product_Simple();
$product->set_name('Wireless Mouse');
$product->set_regular_price('29.99');
$product->set_stock_quantity(50);
$product->save();
```

Les paiements se branchent par des extensions de passerelle, pas par du code d'intégration maison :

```bash
wp plugin install woocommerce-gateway-stripe --activate
```

La logique sur mesure (une règle de prix, un programme de fidélité, un système de stock externe) s'accroche aux actions et aux filtres de WooCommerce, le même mécanisme d'extension que le cœur de WordPress :

```php
add_filter('woocommerce_product_get_price', function ($price, $product) {
    if (is_user_logged_in() && current_user_can('wholesale_customer')) {
        return $price * 0.85;
    }
    return $price;
}, 10, 2);
```

## Quand le choisir

Une boutique sur un site déjà sous WordPress, ou un client dont le besoin ressemble davantage à « un site de contenu qui vend aussi un catalogue modeste » qu'à une plateforme de commerce à fort volume.

## Quand ce n'est pas le bon outil

Un fort volume de transactions avec une logique de paiement sur mesure, là où l'architecture de WordPress se met à résister à la fois sur les performances et sur la personnalisation. C'est le territoire de [Sylius](ch09-02-sylius.md).

> **Sous le capot :** les produits WooCommerce vivent dans la même table `wp_posts` que tout autre contenu, avec leurs données propres (prix, stock) dans `wp_postmeta`. C'est l'architecture « tout est un post » des [types de contenu personnalisés](ch05-04-wordpress-cpt-as-crud.md), étirée jusqu'à modéliser un catalogue entier.
