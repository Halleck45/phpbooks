# Classes, héritage et polymorphisme

Une boutique accepte les cartes bancaires. Puis PayPal. Le trimestre prochain, elle acceptera les virements. Chacun débite l'argent à sa manière, et pourtant, vu de la caisse, tous sont la même chose : une façon de payer. **L'héritage est le moyen de dire à PHP que plusieurs classes sont des variations d'une même idée**, qui partagent ce qu'elles ont en commun et ne diffèrent que là où il le faut. Depuis le chapitre 5, chaque classe que vous avez écrite vivait seule. Il est temps d'en apparenter quelques-unes.

## `extends` et la redéfinition de méthode

Une classe se construit sur une autre avec `extends` : elle hérite de ses propriétés et de ses méthodes, et remplace celles qui doivent se comporter autrement :

```php
<?php
declare(strict_types=1);

class PaymentMethod
{
    public function charge(float $amount): string
    {
        return sprintf('Charged $%.2f.', $amount);
    }
}

class CreditCard extends PaymentMethod
{
    public function __construct(private string $last4)
    {
    }

    public function charge(float $amount): string
    {
        $base = parent::charge($amount);
        return $base . " (card ending {$this->last4})";
    }
}
```

Lisez `class CreditCard extends PaymentMethod` comme « une carte bancaire est un moyen de paiement ». **Tout ce que `PaymentMethod` sait faire, `CreditCard` le sait aussi, sans une ligne de plus.** La seule méthode que `CreditCard` définit pour elle-même est `charge()`, et comme le parent en a déjà une, la version de l'enfant prend sa place. C'est ce qu'on appelle redéfinir une méthode.

<img src="images/ch17-family-tree.png" alt="Un arbre généalogique de classes : PaymentMethod en haut avec sa méthode charge(), CreditCard et PayPal en dessous, chacune avec son propre charge(), et une flèche courbe qui remonte du charge() de CreditCard vers celui du parent, étiquetée parent::" width="560">

Regardez maintenant la première ligne de la redéfinition. `parent::charge($amount)` appelle le `charge()` d'origine du parent, celui-là même qui vient d'être remplacé, et s'appuie sur son résultat au lieu de le jeter. **`parent::`, c'est la façon dont une redéfinition dit « fais ce que tu allais faire, puis laisse-moi ajouter quelque chose ».** La classe de base met toujours le montant en forme ; `CreditCard` ne fait qu'y accoler les quatre derniers chiffres. Sans `parent::`, cette ligne de `sprintf()` serait recopiée dans chaque sous-classe, exactement la duplication que l'héritage est censé éliminer.

> `extends` dit « est un ». `parent::` dit « et aussi ».

## Une deuxième sous-classe

Ajoutez un autre moyen de paiement de la même façon, avec un `charge()` qui fait tout autre chose :

```php
<?php
declare(strict_types=1);

class PayPal extends PaymentMethod
{
    public function __construct(private string $email)
    {
    }

    public function charge(float $amount): string
    {
        return sprintf('Charged $%.2f via PayPal account %s.', $amount, $this->email);
    }
}
```

`PayPal` n'appelle jamais `parent::charge()`. Rien n'oblige une redéfinition à réutiliser la version du parent ; elle doit seulement exister. **Une sous-classe peut garder le comportement du parent, le compléter, ou le remplacer entièrement**, et ces trois usages de l'héritage sont aussi ordinaires les uns que les autres. `CreditCard` et `PayPal` partagent la promesse que tout `PaymentMethod` sait faire `charge()`, et une seule des deux partage du code.

## Le polymorphisme : la vraie récompense

Voici pourquoi tout cela valait la peine. Écrivez une fonction contre le type de base et confiez-lui n'importe quelle sous-classe :

```php
<?php
declare(strict_types=1);

function processPayment(PaymentMethod $method, float $amount): void
{
    echo $method->charge($amount) . "\n";
}

$methods = [
    new CreditCard('4242'),
    new PayPal('damien@example.com'),
];

foreach ($methods as $method) {
    processPayment($method, 42.00);
}
```

```console
$ php payments.php
Charged $42.00. (card ending 4242)
Charged $42.00 via PayPal account damien@example.com.
```

`processPayment()` demande un `PaymentMethod`. Elle ne mentionne jamais `CreditCard` ni `PayPal`. Donnez-lui pourtant l'un ou l'autre, et c'est le bon `charge()` qui s'exécute. **Le même appel, `$method->charge($amount)`, fait ce qu'il faut quel que soit l'objet réellement caché derrière `$method`.** C'est cela, le polymorphisme.

<img src="images/ch17-one-slot.png" alt="Une boîte aux lettres étiquetée processPayment() avec une seule fente à la taille d'un PaymentMethod, et trois enveloppes qui font la queue : une carte bancaire, un compte PayPal, et une troisième encore inconnue" width="560">

Pensez à une boîte aux lettres. Peu lui importe qui a écrit l'enveloppe, seulement qu'elle passe par la fente. `PaymentMethod`, c'est la fente, et chaque sous-classe est une enveloppe taillée à cette mesure, y compris celles que personne n'a encore écrites. Ajoutez `BankTransfer` le mois prochain : tant qu'elle étend `PaymentMethod` et implémente `charge()`, ni `processPayment()` ni la boucle ne changent. Elles n'ont jamais été écrites contre une classe précise, seulement contre la forme que tout `PaymentMethod` garantit.

Essayez : écrivez `BankTransfer`, ajoutez `new BankTransfer()` au tableau `$methods`, relancez. Comptez les lignes que vous avez modifiées dans `processPayment()`.

Cela devrait vous rappeler quelque chose. C'est le même geste que programmer contre une interface au [chapitre 11](ch11-01-interfaces.md) : interfaces et héritage sont deux routes vers la même destination, un code qui n'a pas besoin de savoir quelle classe concrète il tient. La section suivante met les deux routes côte à côte et demande quand prendre laquelle.
