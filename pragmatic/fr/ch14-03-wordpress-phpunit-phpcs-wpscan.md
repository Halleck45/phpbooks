# WordPress : PHPUnit, PHPCS/WPCS et WPScan

**Tester une extension ou un thème WordPress, c'est tester contre WordPress lui-même**, pas contre une imitation allégée. L'échafaudage officiel met en place précisément cela.

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

**PHP_CodeSniffer avec le jeu de règles WordPress Coding Standards (WPCS)** relève les écarts de style, et avec eux une bonne part des erreurs de sécurité pour lesquelles les extensions WordPress sont connues : sortie non échappée, entrée non assainie.

```bash
composer require --dev squizlabs/php_codesniffer wp-coding-standards/wpcs
vendor/bin/phpcs --standard=WordPress my-plugin.php
```

**WPScan** compare les extensions et les thèmes d'un site en ligne à une base de vulnérabilités WordPress connues. Quand une brique dont vous dépendez reçoit une CVE publique, vous l'apprenez par le scan plutôt que par vos logs.

```bash
wpscan --url https://example.com --api-token YOUR_TOKEN
```

## Quand le choisir

Toute extension ou tout thème sur mesure qui contient de la logique, et pas seulement du balisage. Le code qui manipule des saisies utilisateur ou des paiements est celui qui profite le plus de WPCS et de ses contrôles sur les sorties non échappées.

## Quand ce n'est pas le bon outil

Un thème enfant purement visuel, sans logique PHP, n'a pas grand-chose à tester. Mettez l'effort là où il y a du code, pas du balisage.

> **Sous le capot :** WP_UnitTestCase exécute chaque test dans une transaction de base de données, annulée ensuite. Les tests peuvent créer des articles, des utilisateurs et des options à volonté sans salir la base pour le suivant, la même stratégie d'isolation que la plupart des frameworks de test PHP.
