# Implémenter un design pattern classique

Un design pattern (un patron de conception, si vous préférez) est un nom donné à une forme de code qui revient si souvent, dans tant de problèmes différents, qu'elle mérite d'être reconnue au premier coup d'œil. **Vous en construisez un depuis trois sections sans l'avoir nommé.** La famille `PaymentMethod` est presque tout le pattern Strategy, l'un des plus courants de toute la programmation orientée objet. Cette section le termine.

## L'idée

Prenez un comportement qui peut varier : *comment* un paiement est débité, *comment* une liste est triée, *comment* un prix est remisé. Cachez-le derrière une interface. Confiez-le à une classe qui utilise ce comportement sans savoir quelle version elle a reçue. Cette dernière étape, c'est le polymorphisme vu [plus tôt dans ce chapitre](ch17-01-inheritance-and-polymorphism.md). **Strategy ajoute une pièce, le contexte : une classe dont tout le travail est de tenir une stratégie, de lui déléguer, et de la laisser remplacer, même une fois le contexte créé.**

<img src="images/ch17-strategy-socket.png" alt="Un appareil Checkout avec une seule prise à la forme d'un PaymentMethod, et deux fiches de cette forme, CreditCard et PayPal, qu'on branche et débranche à tour de rôle" width="560">

## La construction

Une interface cette fois, pas une classe abstraite. Il n'y a aucun code partagé qui vaille la peine d'être imposé à chaque moyen de paiement, seulement un contrat, et c'est exactement le cas où [la section précédente](ch17-02-abstract-classes.md) disait qu'une interface convient le mieux :

```php
<?php
declare(strict_types=1);

interface PaymentMethod
{
    public function charge(float $amount): string;
}

final class CreditCard implements PaymentMethod
{
    public function __construct(private string $last4)
    {
    }

    public function charge(float $amount): string
    {
        return sprintf('Charged $%.2f to card ending %s.', $amount, $this->last4);
    }
}

final class PayPal implements PaymentMethod
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

Rien de nouveau : les deux mêmes classes que plus tôt dans le chapitre, qui implémentent une interface au lieu d'étendre une classe de base. Maintenant, le contexte :

```php
<?php
declare(strict_types=1);

final class Checkout
{
    public function __construct(private PaymentMethod $paymentMethod)
    {
    }

    public function setPaymentMethod(PaymentMethod $paymentMethod): void
    {
        $this->paymentMethod = $paymentMethod;
    }

    public function complete(float $amount): void
    {
        echo $this->paymentMethod->charge($amount) . "\n";
    }
}
```

`Checkout` tient un `PaymentMethod`, n'importe lequel, et `complete()` confie le travail à celui qu'elle tient à ce moment-là. Regardez ce qui manque. **Il n'y a aucun `if` qui demande « es-tu une carte ou un compte PayPal ? »** Cette absence est la signature d'un Strategy bien fait : le contexte appelle `charge()` et fait confiance à l'interface.

## L'utiliser et changer de stratégie en cours de route

```php
<?php
$checkout = new Checkout(new CreditCard('4242'));
$checkout->complete(42.00);

$checkout->setPaymentMethod(new PayPal('damien@example.com'));
$checkout->complete(19.99);
```

```console
$ php checkout.php
Charged $42.00 to card ending 4242.
Charged $19.99 via PayPal account damien@example.com.
```

Même objet `$checkout`, même appel à `complete()`, deux résultats différents, parce que `setPaymentMethod()` a changé la stratégie entre les deux. Imaginez l'alternative : un `if ($type === 'credit_card')` à l'intérieur de `Checkout`, qui gagne une branche à chaque moyen de paiement que le produit ajoute. Avec Strategy, le virement du trimestre prochain est une nouvelle classe qui implémente `PaymentMethod`, et `Checkout` ne bouge pas. Elle fonctionne déjà, pour la même raison que `processPayment()` fonctionnait plus tôt dans le chapitre : elle a été écrite contre l'interface, jamais contre une classe précise.

Essayez : écrivez `BankTransfer`, passez-la à `setPaymentMethod()`, terminez un troisième paiement. Comptez les lignes que vous avez modifiées dans `Checkout`.

C'est tout le pattern. Une interface qui décrit un comportement interchangeable, des classes qui l'implémentent, et un contexte qui délègue à celle qu'il tient. Pas de syntaxe nouvelle, pas de bibliothèque, rien de propre à PHP : les interfaces et le polymorphisme que vous aviez déjà, agencés à dessein pour résoudre un problème reconnaissable. Une fois que vous en aurez construit un ainsi, vous verrez la même forme partout, sous d'autres noms, dans du code que vous n'avez pas écrit.

> Une stratégie est un comportement qu'on débranche et qu'on remplace. Le contexte, c'est la prise.
