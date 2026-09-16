# WooCommerce: E-Commerce on Top of WordPress

If a WordPress site (see [Shipping a Content Site](ch03-01-wordpress-block-themes.md)) needs to sell things, WooCommerce is the default answer, and for good reason: it's a full store (products, variations, cart, checkout, orders, coupons) added as a plugin, using the same admin your client already knows.

```bash
wp plugin install woocommerce --activate
wp wc --version
```

Products are stored as a custom post type, so anything already familiar about managing WordPress content carries over directly:

```php
$product = new WC_Product_Simple();
$product->set_name('Wireless Mouse');
$product->set_regular_price('29.99');
$product->set_stock_quantity(50);
$product->save();
```

Payment processing plugs in through gateway extensions rather than custom integration code:

```bash
wp plugin install woocommerce-gateway-stripe --activate
```

Custom logic (special pricing rules, a loyalty program, an integration with an external inventory system) hooks into WooCommerce's own action and filter system, the same extension pattern as WordPress core:

```php
add_filter('woocommerce_product_get_price', function ($price, $product) {
    if (is_user_logged_in() && current_user_can('wholesale_customer')) {
        return $price * 0.85;
    }
    return $price;
}, 10, 2);
```

## When to reach for this

Any storefront where the site is already WordPress, or where the client's actual need is closer to "a content site that also sells a modest catalog of products" than a high-volume, highly custom commerce platform.

## When it's the wrong fit

High-transaction-volume commerce with complex custom checkout logic, where WordPress's underlying architecture starts fighting the performance and customization needs. That's [Sylius](ch09-02-sylius.md) territory.

> **Under the hood:** WooCommerce products are stored using the same `wp_posts` table as any other content type, with product-specific data (price, stock) kept in `wp_postmeta`. It's the same "everything is a post" architecture from [Custom Post Types](ch05-04-wordpress-cpt-as-crud.md), stretched to model an entire commerce catalog.
