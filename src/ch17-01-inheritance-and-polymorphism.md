# Classes, Inheritance, and Polymorphism

You've defined classes since Chapter 5 and implemented interfaces since Chapter 11, but so far every class you've written has stood alone. Real designs usually involve classes that are variations on a theme: several kinds of the same basic idea, sharing some behavior and differing in the rest. That's what inheritance is for.

## `extends` and method overriding

A class can build on another with `extends`, inheriting its properties and methods and overriding whichever ones need to behave differently:

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

`CreditCard extends PaymentMethod` means every `CreditCard` *is* a `PaymentMethod`, with all of its behavior, unless `CreditCard` explicitly overrides a method, which is exactly what its `charge()` does here, replacing the parent's version with one that adds the card's last four digits. `parent::charge($amount)` calls the *original* implementation from inside the override, rather than throwing it away entirely: the base class still does the generic formatting work; `CreditCard` just adds to it. Without `parent::`, you'd need to duplicate that `sprintf()` line in every subclass that wants it, which is exactly the kind of duplication inheritance exists to avoid.

## A second subclass

Add another payment method the same way, overriding `charge()` with entirely different logic:

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

`PayPal` doesn't call `parent::charge()` at all: nothing requires an override to reuse the parent's implementation, only that it exist. Both `CreditCard` and `PayPal` fully replace the base behavior with their own, which is a perfectly normal use of inheritance: sharing the *contract* ("every `PaymentMethod` can `charge()`") without necessarily sharing any code.

## Polymorphism: the actual payoff

Here's why any of this was worth setting up. Write code against the base type, `PaymentMethod`, and hand it any subclass: it works, without the calling code knowing or caring which one it actually got:

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

`processPayment()` is typed against `PaymentMethod`, never against `CreditCard` or `PayPal` specifically, and the `foreach` loop above treats every element identically even though each one runs completely different code when `charge()` is called. That's polymorphism: the same call, `$method->charge($amount)`, does the right thing for whatever concrete object is actually behind `$method` at runtime. Add a third payment method next month (`BankTransfer`, `Cryptocurrency`, whatever the product needs), and as long as it extends `PaymentMethod` and implements `charge()`, `processPayment()` and the `foreach` loop above need no changes at all. They were never written against a specific class in the first place, only against the shape every `PaymentMethod` is guaranteed to have.

This should feel familiar: it's the same idea as programming against an interface, from [Chapter 11](ch11-01-interfaces.md), and for good reason: interfaces and inheritance are two different roads to the same destination, polymorphic code that doesn't need to know which concrete class it's holding. The next section puts them side by side and asks, directly, when to reach for which one.
