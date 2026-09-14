# Définir un comportement commun avec les interfaces

Supposons que vous deviez afficher le résumé lisible d'un objet : une ligne de facture, un produit, une entrée de journal, ce que la semaine vous apporte. Vous pourriez donner à chaque classe une méthode `describe()` et espérer que tout le monde retienne le nom. Ou vous pourriez en faire une règle que PHP lui-même vérifie. **C'est à ça que sert une interface.**

```php
<?php

interface Formattable
{
    public function format(): string;
}
```

Une interface ressemble à une classe dont on aurait retiré tous les corps de méthode. `format(): string` est une *signature*, pas une implémentation : pas d'accolades, pas de logique, juste une promesse. **Toute classe qui déclare implémenter `Formattable` doit avoir une méthode publique `format()` qui renvoie une chaîne**, et PHP la tient à cette promesse. Oubliez la méthode, ou renvoyez le mauvais type, et le code ne s'exécute pas.

## L'implémenter

Une classe s'engage avec `implements` :

```php
<?php

readonly class Product
{
    public function __construct(
        public string $name,
        public float $price,
    ) {
    }
}

readonly class InvoiceLine implements Formattable
{
    public function __construct(
        private Product $product,
        private int $quantity,
    ) {
    }

    public function format(): string
    {
        $total = $this->product->price * $this->quantity;
        return sprintf('%dx %s, $%.2f', $this->quantity, $this->product->name, $total);
    }
}
```

`InvoiceLine implements Formattable` est une affirmation que PHP vérifie pour vous. Si `format()` manquait, ou était déclarée comme renvoyant un `int`, vous auriez une erreur fatale à l'instant où PHP charge la classe, pas trois appels plus loin, en production. Essayez : renommez `format()` en `describe()` et lancez le fichier.

Une classe peut implémenter plusieurs interfaces, séparées par des virgules. C'est l'une des façons dont PHP compense le fait qu'une classe n'a qu'un seul parent.

## Pourquoi s'embêter : programmer contre l'interface

Voici la partie qui rembourse l'effort. Écrivez une fonction qui type son paramètre avec l'interface, pas avec la classe concrète :

```php
<?php

function printSummary(Formattable $item): void
{
    echo $item->format() . "\n";
}

printSummary(new InvoiceLine(new Product('Keyboard', 49.90), 2));
```

`printSummary()` ne sait pas qu'elle a reçu une `InvoiceLine`, et s'en moque. Elle sait qu'elle a reçu *quelque chose* qui sait se `format()`. Ajoutez demain une classe `Refund`, ou `Discount`, ou `ShippingFee`, implémentez `Formattable` dessus, et `printSummary()` n'a pas besoin de bouger d'une ligne. **Elle fonctionne déjà, parce qu'elle n'a jamais été écrite pour une classe en particulier.**

<img src="images/ch11-interface-socket.png" alt="Une prise murale étiquetée Formattable, et trois appareils de formes différentes, InvoiceLine, Refund et ShippingFee, qui se terminent tous par la même fiche qui s'y branche" width="560">

Une prise murale se moque de savoir si vous y branchez une lampe ou un ordinateur portable ; elle exige seulement que la fiche ait la bonne forme. `Formattable` est la forme, et `printSummary()` est la prise.

Les tests font monter les enjeux. Si `printSummary()` avait exigé une `InvoiceLine`, la tester seule voudrait dire construire une vraie `InvoiceLine` avec un vrai `Product` derrière. Avec `Formattable`, un test peut lui passer n'importe quel objet qui honore le contrat, y compris un faux fabriqué pour l'occasion, sans le moindre `Product` en vue. Le [chapitre 12](ch12-00-testing.md) s'en sert directement.

> Typez sur le contrat, pas sur la classe. La fonction marche alors avec toutes les classes qui le signent, y compris celles que vous n'avez pas encore écrites.

## `instanceof`

De temps en temps, vous devez demander, à l'exécution, si un objet satisfait une interface :

```php
<?php

if ($item instanceof Formattable) {
    echo $item->format() . "\n";
}
```

Servez-vous-en rarement. Une pile de tests `instanceof` avant un appel de méthode signifie presque toujours que la méthode a sa place dans une interface sur laquelle vous devriez typer, et non qu'il vous faut davantage d'`instanceof`.

## Une remarque sur les noms

PHP n'a aucune syntaxe particulière pour distinguer une interface « simple contrat » d'une interface plus structurelle. `Formattable`, `Countable`, `Stringable`, `ArrayAccess` sont toutes des interfaces ordinaires, certaines fournies par le langage, d'autres écrites par vous. La convention préfère un adjectif en *-able* pour un contrat à capacité unique (`Formattable`, `Comparable`, `Sortable`). PHP ne l'impose pas, mais le prochain lecteur vous en saura gré. Plusieurs interfaces natives de PHP font leur apparition au [chapitre 20](ch20-00-advanced-features.md).
