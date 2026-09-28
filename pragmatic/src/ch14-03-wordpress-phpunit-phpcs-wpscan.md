# WordPress: PHPUnit, PHPCS/WPCS, and WPScan

**Testing a WordPress plugin or theme means testing against WordPress itself**, not a lightweight mock of it. The official scaffold sets up precisely that.

```bash
wp scaffold plugin-tests my-plugin
cd wp-content/plugins/my-plugin
composer install
./bin/install-wp-tests.sh wordpress_test root '' localhost latest
```

```php
class DiscountCalculationTest extends WP_UnitTestCase
{
    public function test_bulk_discount_applies_over_ten_items(): void
    {
        $product = $this->factory->post->create(['post_type' => 'product']);

        $price = apply_filters('calculate_bulk_price', 100, 12);

        $this->assertEquals(90, $price);
    }
}
```

**PHP_CodeSniffer with the WordPress Coding Standards (WPCS)** ruleset catches style violations, and with them a good share of the security mistakes WordPress plugins are known for: unescaped output, unsanitized input.

```bash
composer require --dev squizlabs/php_codesniffer wp-coding-standards/wpcs
vendor/bin/phpcs --standard=WordPress my-plugin.php
```

**WPScan** checks a running site's plugins and themes against a database of known WordPress vulnerabilities. When something you depend on gets a disclosed CVE, you hear about it from the scan rather than from your logs.

```bash
wpscan --url https://example.com --api-token YOUR_TOKEN
```

## When to reach for this

Any custom plugin or theme with logic in it, not only template markup. Code that handles user input or payments benefits most from WPCS and its checks for unescaped output.

## When it's the wrong fit

A purely visual child theme with no PHP logic has little to test. Spend the effort where there is code, not markup.

> **Under the hood:** WP_UnitTestCase runs each test inside a database transaction and rolls it back afterward. Tests can create posts, users and options freely without leaving the database dirty for the next one, the same isolation strategy most PHP testing frameworks use.
