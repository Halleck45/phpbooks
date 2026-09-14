# Paquets et chargement automatique

`composer require` dépose un paquet dans `vendor/`, et `require 'vendor/autoload.php'` rend disponible chaque classe qu'il contient. Vous l'avez vu fonctionner. Ce que vous n'avez pas encore vu, c'est *comment* cette seconde moitié fonctionne, et la réponse explique pourquoi le reste de ce chapitre existe.

## Le problème que résout l'autoloading

Imaginez PHP sans lui. Une classe `Cart` dans un fichier, une classe `Product` dans un autre, et un script qui a besoin des deux :

```php
<?php

require 'Product.php';
require 'Cart.php';

$product = new Product('Keyboard', 49.00);
$cart = new Cart();
$cart->add($product);
```

Deux classes, deux lignes `require`, synchronisées à la main. Gérable. Imaginez maintenant quarante classes réparties dans une douzaine de paquets que vous n'avez pas écrits, chacune dépendant des autres dans un ordre qu'il vous faudrait reconstituer vous-même. **Charger les fichiers à la main ne tient pas au-delà d'une poignée de classes**, et tout casse le jour où vous en renommez une. Plus personne ne fait ça.

<img src="images/ch07-require-pile.png" alt="Avant et après : un script dont le haut disparaît sous une pile de lignes require, à côté du même script avec un seul require de vendor/autoload.php" width="600">

## `spl_autoload_register()`

PHP a un crochet intégré pour exactement ce cas. **`spl_autoload_register()` confie à PHP une fonction à appeler la première fois qu'il rencontre un nom de classe qu'il ne connaît pas.** Au lieu d'échouer sur-le-champ, PHP laisse à votre fonction une chance d'aller chercher le fichier et de le charger :

```php
<?php

spl_autoload_register(function (string $className): void {
    $file = __DIR__ . '/' . $className . '.php';

    if (file_exists($file)) {
        require $file;
    }
});

$cart = new Cart(); // Cart.php is loaded automatically, on first use
```

`new Cart()` s'exécute, PHP n'a jamais entendu parler de `Cart`, il appelle donc votre fonction avec la chaîne `'Cart'`. La fonction construit un chemin, trouve `Cart.php` et l'inclut. La classe existe désormais, et `new` se poursuit comme si de rien n'était. Essayez : placez une classe `Cart` dans un fichier `Cart.php` à côté de ce script, lancez-le, puis renommez le fichier et relancez.

<img src="images/ch07-autoloader-librarian.png" alt="L'autoloading vu comme un comptoir de bibliothèque : le programme demande Cart, l'autoloader va jusqu'au rayon, trouve le fichier Cart.php et le rapporte" width="600">

Beaucoup de projets ont écrit leur propre version de ce mécanisme avant que Composer n'existe. Ça marche, jusqu'au jour où un paquet dont vous dépendez livre son propre autoloader maison avec des règles légèrement différentes, et vous revoilà à tout coordonner à la main.

## Ce que Composer génère réellement

Chaque `composer install` ou `composer require` régénère les fichiers de `vendor/composer/`. L'un d'eux, `autoload_psr4.php`, est un simple tableau PHP qui associe des préfixes d'espaces de noms à des répertoires. `vendor/autoload.php` construit un seul autoloader à partir de cette table et l'enregistre avec `spl_autoload_register()`. Dès lors, chaque classe de chaque paquet installé se résout toute seule.

Ça fonctionne parce que les paquets ne déversent pas leurs fichiers dans un tas commun. **Chaque paquet déclare, dans son propre `composer.json`, quel préfixe d'espace de noms vit dans quel répertoire.** Voici à quoi ressemble cette déclaration (vous écrirez la vôtre dans la section [PSR-4](ch07-06-psr4.md)) :

```json
{
    "autoload": {
        "psr-4": {
            "App\\": "src/"
        }
    }
}
```

> Un espace de noms est une promesse sur l'emplacement du fichier. PSR-4 est la règle qui transforme la promesse en chemin. L'autoloader de Composer ne fait qu'appliquer la règle, vite.

## Pourquoi il faut des espaces de noms

Tout le système repose sur une condition : **les noms de classes doivent rester uniques dans l'ensemble des paquets installés dans votre projet.** Un `Product` venu de votre code et un `Product` venu d'un paquet de commerce en ligne seraient indiscernables. PHP ne saurait pas quel `Product.php` charger, et vous non plus, en relisant le code dans six mois.

Les espaces de noms suppriment la collision en faisant de `Product` le raccourci de quelque chose de plus précis : `App\Models\Product` d'un côté, `Vendor\Ecommerce\Product` de l'autre. Deux noms, deux fichiers, rien à deviner. C'est la section suivante.
