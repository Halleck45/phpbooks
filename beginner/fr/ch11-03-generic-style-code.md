# Du code générique avec les docblocks et l'analyse statique

PHP n'a pas de génériques. Beaucoup de documentations tournent autour de cette phrase, alors la voici, sans détour. Dans un langage qui en a (le `List<String>` de Java, le `Array<Product>` de TypeScript), le compilateur refuse de laisser entrer le mauvais type dans un conteneur typé. **Le système de types de PHP s'arrête à la frontière du tableau.** Vous pouvez typer un paramètre `array`, mais « un tableau de quoi » est une question à laquelle le langage ne répondra jamais à l'exécution.

```php
<?php

function totalPrice(array $products): float
{
    $total = 0.0;
    foreach ($products as $product) {
        $total += $product->price;
    }
    return $total;
}
```

Rien ne vous empêche d'appeler `totalPrice([1, 2, 3])` ou `totalPrice(['not', 'products'])`. PHP déroule la boucle sans broncher et explose sur `$product->price` dès qu'il tombe sur quelque chose qui n'a pas de propriété `price`. À l'exécution, en production si vous n'avez pas de chance, au lieu du moment où vous avez écrit le bug. Essayez : ajoutez `totalPrice([1, 2, 3]);` en bas du fichier et lisez ce que PHP vous répond.

## Le contournement : des docblocks que les outils d'analyse statique comprennent

La réponse de l'écosystème PHP n'est pas une fonctionnalité du langage. C'est une convention. **Vous écrivez ce que contient le tableau dans un commentaire docblock, et un outil à part, lancé avant de livrer, confronte cette promesse à l'usage réel du code.**

```php
<?php

/**
 * @param Product[] $products
 */
function totalPrice(array $products): float
{
    $total = 0.0;
    foreach ($products as $product) {
        $total += $product->price;
    }
    return $total;
}
```

`@param Product[] $products` ne veut rien dire pour l'interpréteur PHP. C'est un commentaire, et `php totalPrice.php` s'exécute à l'identique avec ou sans. En revanche, cela veut dire beaucoup pour [PHPStan](https://phpstan.org/) ou [Psalm](https://psalm.dev/), les deux outils d'analyse statique qui dominent le monde PHP. Lancez l'un des deux sur ce fichier et il remonte chaque site d'appel. Si une autre fonction passe un tableau contenant un `int`, ou un `Refund` là où un `Product` était promis, l'analyseur le signale. La même famille d'erreurs qu'un compilateur à génériques attraperait, attrapée par un programme à part plutôt que par le langage.

<img src="images/ch11-two-checkpoints.png" alt="Un tapis roulant emmène des cartons vers la production en passant deux contrôles : un inspecteur étiqueté PHPStan lit un panneau @param Product[] et arrête une banane, puis un petit éléphant étiqueté php laisse tout passer" width="620">

Deux postes de contrôle jalonnent la route de la production. L'analyseur lit votre docblock et arrête tout ce qui ne correspond pas ; `php` lui-même laisse tout passer sans regarder. Seul le premier poste refuse une banane, et il n'existe que si vous l'avez installé.

> Un docblock est une promesse. PHP l'ignore. L'analyseur vous y tient.

## `@template` : au plus près des vrais génériques

Pour les structures vraiment génériques, disons une classe de collection capable de contenir n'importe quel type, mais un seul à la fois, les deux outils comprennent une annotation plus riche, calquée sur la façon dont les génériques s'écrivent dans d'autres langages :

```php
<?php

/**
 * @template T
 */
final class TypedCollection
{
    /** @var T[] */
    private array $items = [];

    /**
     * @param T $item
     */
    public function add(mixed $item): void
    {
        $this->items[] = $item;
    }

    /**
     * @return T[]
     */
    public function all(): array
    {
        return $this->items;
    }
}
```

Avec l'annotation `@var` correspondante au point d'utilisation :

```php
<?php

/** @var TypedCollection<Product> $products */
$products = new TypedCollection();
$products->add(new Product('Keyboard', 49.90));
```

PHPStan suit `T` comme étant `Product` pendant toute la vie de cette variable, et proteste dès que vous lui `add()` autre chose. Regardez la vraie signature : `mixed`. C'est ce que PHP voit et autorise à l'exécution, absolument n'importe quoi. **L'annotation `@template T` est la couche du dessus, comprise seulement par l'analyseur, qui réduit `mixed` à un type précis tant que l'analyse statique regarde.**

## Ce que ça change pour vous

Rien dont il faille s'excuser. C'est ainsi que fonctionne le système de types de PHP aujourd'hui, et l'écosystème s'en est très bien accommodé. Les vrais projets lancent PHPStan ou Psalm comme étape obligatoire de leur intégration continue, souvent à un niveau strict, et traitent un docblock non respecté comme une erreur de compilation : la construction échoue. L'exécution reste permissive, par choix, une habitude aussi vieille que le langage, mais rien ne vous oblige à *livrer* du code que seule l'exécution a vérifié. Annotez chaque paramètre `array` dont le contenu compte, installez l'un des deux outils, et vous obtenez l'essentiel de ce qu'offre un langage à génériques, une étape plus tôt plutôt qu'à l'intérieur de `php` lui-même.
