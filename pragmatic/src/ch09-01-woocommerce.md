# WooCommerce: E-Commerce on Top of WordPress

When a WordPress site (see [Shipping a Content Site](ch03-01-wordpress-block-themes.md)) needs to sell things, WooCommerce is the default answer. **It adds a full store as a plugin, inside the admin your client already knows:** products, variations, cart, checkout, orders, coupons.

```bash
wp plugin install woocommerce --activate
wp wc --version
```

Products are a custom post type, so everything you know about managing WordPress content carries over:

```php
$product = new WC_Product_Simple();
$product->set_name('Wireless Mouse');
$product->set_regular_price('29.99');
$product->set_stock_quantity(50);
$product->save();
```

Payments plug in through gateway extensions rather than custom integration code:

```bash
wp plugin install woocommerce-gateway-stripe --activate
```

Custom logic (a pricing rule, a loyalty program, an external inventory system) hooks into WooCommerce's own actions and filters, the same extension pattern as WordPress core:

```php
add_filter('woocommerce_product_get_price', function ($price, $product) {
    if (is_user_logged_in() && current_user_can('wholesale_customer')) {
        return $price * 0.85;
    }
    return $price;
}, 10, 2);
```

## When to reach for this

A storefront on a site that is already WordPress, or a client whose need is closer to "a content site that also sells a modest catalog" than to a high-volume commerce platform.

## When it's the wrong fit

High transaction volume with custom checkout logic, where the WordPress architecture starts fighting both performance and customization. That is [Sylius](ch09-02-sylius.md) territory.

> **Under the hood:** WooCommerce products live in the same `wp_posts` table as any other content, with product data (price, stock) in `wp_postmeta`. It is the "everything is a post" architecture from [Custom Post Types](ch05-04-wordpress-cpt-as-crud.md), stretched to model a whole catalog.
