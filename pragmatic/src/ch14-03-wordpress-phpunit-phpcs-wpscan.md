# WordPress: PHPUnit, PHPCS/WPCS, and WPScan

Testing a WordPress plugin or theme means testing against WordPress itself, not a lightweight mock of it, which is exactly what the official test suite scaffold sets up.

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

**PHP_CodeSniffer with the WordPress Coding Standards (WPCS)** ruleset catches both style violations and a meaningful number of common security mistakes (unescaped output, unsanitized input) specific to how WordPress plugins tend to go wrong.

```bash
composer require --dev squizlabs/php_codesniffer wp-coding-standards/wpcs
vendor/bin/phpcs --standard=WordPress my-plugin.php
```

**WPScan** checks a running site's installed plugins and themes against a database of known WordPress-specific vulnerabilities, catching the moment something you depend on gets a disclosed CVE.

```bash
wpscan --url https://example.com --api-token YOUR_TOKEN
```

## When to reach for this

Any custom plugin or theme with real logic in it, not just template markup. Security-sensitive code (anything handling user input or payments) especially benefits from WPCS's built-in checks for unescaped output.

## When it's the wrong fit

A purely visual child theme with no custom PHP logic has little to test; the effort is better spent where actual code, not just markup, exists.

> **Under the hood:** WP_UnitTestCase runs each test inside a database transaction that's rolled back afterward, so tests can freely create posts, users, and options without leaving the test database dirty for the next test, the same isolation strategy most PHP testing frameworks use.
