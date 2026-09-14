# Namespaces, Composer et autoloading

**PHP n'a pas de système de modules, mais trois mécanismes plus modestes, `require`, les espaces de noms et un crochet d'autoloading, que Composer assemble en un gestionnaire de paquets** comparable à npm, pip, Maven ou Cargo. Vous n'écrirez plus jamais de `require` pour l'une de vos propres classes, et il reste utile de savoir ce que Composer fait à votre place.

## Les trois primitives

`require 'file.php';` lit et exécute un fichier, une fois par appel. C'est ainsi que le code se partageait en 2005, et c'est encore ainsi que tout s'amorce aujourd'hui, avec un unique `require` de `vendor/autoload.php` en tête de votre point d'entrée.

Un espace de noms est un préfixe sur un nom de classe. `namespace App\Billing;` en tête d'un fichier fait de chaque classe qui y est déclarée une `App\Billing\Something`, et n'apporte rien d'autre, aucune hiérarchie, aucune visibilité, aucun lien avec un dossier. `App\Billing` n'est pas « dans » `App`, ce sont simplement deux chaînes qui partagent un préfixe.

Le crochet d'autoloading est la pièce qui rend les deux premières utiles. **Quand PHP rencontre une classe qu'il n'a jamais vue, il appelle une fonction que vous avez enregistrée, en lui passant le nom de la classe, et cette fonction est censée faire un `require` du bon fichier**, après quoi PHP réessaie.

```php
<?php
declare(strict_types=1);

spl_autoload_register(function (string $class): void {
    $file = __DIR__ . '/src/' . str_replace('\\', '/', $class) . '.php';
    if (is_file($file)) {
        require $file;
    }
});

$invoice = new App\Billing\Invoice(); // loads src/App/Billing/Invoice.php
```

Le mécanisme se résume à cette closure, et Composer en écrit une meilleure version, avec un cache, qu'il vous remet.

<img src="images/ch09-autoload-lookup.png" alt="Un petit éléphant lit un bout de papier où est écrit App\Billing\Invoice, puis suit une ligne pointillée le long d'un classeur dont les tiroirs sont étiquetés App, Billing, Invoice.php, et ouvre le dernier" width="560">

## PSR-4 : du nom au chemin

La règle que suit la closure ci-dessus porte un nom, PSR-4, et Composer l'applique à partir d'un bloc de `composer.json` :

```json
{
    "name": "acme/shop",
    "type": "project",
    "require": {
        "php": "^8.4",
        "ext-intl": "*"
    },
    "require-dev": {
        "phpunit/phpunit": "^12.0"
    },
    "autoload": {
        "psr-4": { "App\\": "src/" }
    },
    "autoload-dev": {
        "psr-4": { "App\\Tests\\": "tests/" }
    }
}
```

`App\Billing\Invoice` vit dans `src/Billing/Invoice.php` : une classe par fichier, un nom de fichier égal au nom de la classe, et des dossiers qui reprennent les segments de l'espace de noms après le préfixe. L'arborescence qui en résulte est la même sur tous les projets PHP modernes que vous ouvrirez :

```text
shop/
├── composer.json
├── composer.lock
├── public/
│   └── index.php        # require __DIR__ . '/../vendor/autoload.php';
├── src/
│   └── Billing/
│       └── Invoice.php  # namespace App\Billing;
├── tests/
│   └── Billing/
│       └── InvoiceTest.php
└── vendor/              # generated, not committed
```

Ajoutez une classe sous `src/`, et elle est trouvée à la requête suivante, sans commande à lancer, puisque PSR-4 résout par chemin au moment de l'appel. La stratégie plus ancienne `classmap` parcourt les dossiers pour en faire un tableau généré, et réclame un `composer dump-autoload` après chaque nouveau fichier ; vous la rencontrerez dans les projets anciens.

## Composer, dans le vocabulaire que vous connaissez

`composer.json` joue le rôle de votre `package.json`, `composer.lock` celui du fichier de verrouillage, `vendor/` celui de `node_modules`, généré et ignoré par Git, et Packagist celui du registre public.

```bash
composer init                          # interactive composer.json
composer require monolog/monolog       # add and install, updates the lock
composer require --dev phpstan/phpstan # development-only dependency
composer install                       # reproduce exactly what the lock says
composer update                        # resolve anew, rewrite the lock
composer update monolog/monolog        # ... for one package only
composer show                          # what is installed, with versions
composer outdated                      # what has a newer release
composer audit                         # known vulnerabilities in the lock
composer dump-autoload -o              # regenerate the autoloader, optimised
```

**`install` obéit à `composer.lock`, tandis qu'`update` le réécrit.** En CI et en production vous lancez `install`, et vous obtenez exactement les versions que votre collègue a testées. Committez `composer.lock` pour une application ; pour une bibliothèque, la plupart des auteurs ne le font pas, afin qu'elle soit testée avec ce que ses utilisateurs résolvent, et c'est le même débat que dans tous les autres écosystèmes.

Les contraintes de version suivent semver, et `^8.4` signifie « 8.4 ou toute 8.x ultérieure ». L'entrée `php` de `require` est une contrainte elle aussi ; avec `config.platform.php` vous figez la version contre laquelle Composer résout, pour qu'un développeur sous PHP 8.5 ne tire pas un paquet que votre production en 8.4 ne peut pas exécuter.

Les scripts vivent sous une clé `scripts` et se lancent avec `composer run nom` ou comme crochets de cycle de vie (`post-install-cmd`), à la manière des scripts npm. Les extensions ne sont pas des paquets : `ext-intl` dans `require` vérifie seulement que l'extension est présente, et l'installer est le travail de votre gestionnaire de paquets système, de PECL ou de PIE. Les outils que vous installeriez globalement ailleurs (linters, analyseurs) vont dans `require-dev`, pour que chaque développeur et la CI utilisent la même version ; `composer global require` existe et il vaut mieux le laisser de côté. Un monorepo déclare ses paquets internes comme dépôts `path`, et Composer crée des liens symboliques.

<img src="images/ch09-install-vs-update.png" alt="Deux panneaux. À gauche, étiqueté install : un éléphant lit un registre cadenassé et empile des boîtes exactement comme listé. À droite, étiqueté update : le même éléphant consulte un tableau d'affichage couvert d'annonces de versions, choisit de nouvelles boîtes, puis réécrit le registre" width="560">

## Vivre avec les espaces de noms

Dans un fichier, une instruction `use` importe un nom pour que vous puissiez l'écrire court. Les alias résolvent les collisions, et les fonctions comme les constantes peuvent aussi être importées :

```php
<?php
declare(strict_types=1);

namespace App\Billing;

use App\Customer\Customer;
use DateTimeImmutable as Date;
use function App\Support\money;
use const App\Support\CURRENCY;

final class Invoice
{
    public function __construct(
        public readonly Customer $customer,
        public readonly Date $issuedOn,
    ) {
    }

    public function total(): string
    {
        return money(1999, CURRENCY);
    }
}

echo Invoice::class, PHP_EOL; // App\Billing\Invoice
```

`Invoice::class` donne le nom pleinement qualifié sous forme de chaîne, ce qui est ce que vous passez à un conteneur, à un mock ou aux vérifications `instanceof` qui prennent une chaîne. Un antislash initial, comme dans `\DateTimeImmutable`, nomme une classe de l'espace de noms global sans passer par `use`.

**Les fonctions se rabattent sur l'espace de noms global, alors que les classes ne le font pas.** Appeler `strlen()` dans `App\Billing` cherche d'abord `App\Billing\strlen`, puis `strlen`, tandis qu'appeler `new DateTimeImmutable()` sans `use` ni antislash initial échoue. Vous verrez `\strlen()` dans certaines bibliothèques, parce que l'antislash saute la recherche et laisse OPcache inliner quelques fonctions intégrées ; c'est une micro-optimisation, pas une convention que vous ayez à adopter.

## Les standards à connaître

Le PHP-FIG est le groupe où les auteurs de frameworks et de bibliothèques s'accordent sur des interfaces, publiées sous forme de PSR. **Une PSR est un contrat plutôt qu'une bibliothèque** : les implémentations viennent de nombreux éditeurs, et vous pouvez en remplacer une par une autre parce que votre code ne voit que l'interface. Voici celles que vous croiserez dès la première semaine :

- **PSR-4**, l'autoloading, ci-dessus.
- **PER Coding Style**, successeur de PSR-12 : placement des accolades, indentation, nommage. PHP-CS-Fixer ou PHP_CodeSniffer le font respecter.
- **PSR-3**, `LoggerInterface`. Toutes les bibliothèques journalisent à travers elle ; vous branchez le logger de votre choix.
- **PSR-7**, **PSR-15** et **PSR-17** : objets requête et réponse HTTP, middlewares, et leurs fabriques. Les `$_GET` et `header()` du langage sont traités dans [Une requête web, sans framework](ch11-web-request.md) ; PSR-7 est le modèle objet que les bibliothèques partagent par-dessus.
- **PSR-11**, `ContainerInterface`, pour qu'une bibliothèque puisse demander un service à n'importe quel conteneur.
- **PSR-14**, la distribution d'événements, **PSR-6** et **PSR-16**, le cache.

Une bibliothèque qui type son constructeur contre `Psr\Log\LoggerInterface` fonctionne dans tous les frameworks cités dans ce livre. Cette interopérabilité explique pourquoi l'écosystème compte moins de forks et de réécritures que sa taille ne le laisserait penser.

## Le piège

Ne modifiez jamais un fichier de `vendor/`. Le prochain `composer install` sur n'importe quelle machine efface la modification, et personne ne saura pourquoi la production diffère de votre portable. Forkez le paquet, ou surchargez la classe par votre propre entrée d'autoloading, ou envoyez le correctif en amont.

Le second piège est plus discret : vous ajoutez une classe, PHP dit qu'elle n'existe pas, et vous passez vingt minutes à chercher une faute de frappe qui n'existe pas. Comparez l'espace de noms au dossier : `App\Billing\Invoice` doit être `src/Billing/Invoice.php`, lettre pour lettre, casse comprise sous Linux. Si le projet utilise `classmap` plutôt que `psr-4`, lancez `composer dump-autoload` et passez à autre chose.

> Composer n'est pas une étape de build, puisqu'il n'y a rien à compiler, à empaqueter ni à transpiler : après `composer install`, le code s'exécute tel quel.

Une fois les classes trouvées et les paquets installés, il reste la bibliothèque standard sur laquelle vous vous appuierez chaque jour, et [Chaînes, nombres, dates et JSON](ch10-standard-library.md) en fait le tour.
