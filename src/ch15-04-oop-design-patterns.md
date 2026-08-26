# Implementing a Classic OOP Design Pattern

A design pattern is just a name for a shape of code that shows up often enough, across enough different problems, that it's worth recognizing on sight. You've actually been building most of one already, across the last three sections: the `PaymentMethod` family. This section finishes the job and names what you've built: the **Strategy pattern**, one of the most common in all of object-oriented programming, and one you'll recognize instantly in other people's code once you've written it yourself.

## The idea

Strategy's whole premise: take a piece of behavior that can vary (*how* a payment gets charged, *how* a list gets sorted, *how* a price gets discounted), pull it out behind a shared interface, and hand it to a class that uses that behavior without needing to know which specific version it received. That last part should sound familiar; it's exactly the polymorphism from [ch15-01](ch15-01-inheritance-and-polymorphism.md). Strategy just adds one more piece: a dedicated class, usually called the *context*, whose entire job is holding onto a strategy and delegating to it, and letting that strategy be swapped out, even after the context already exists.

## Building it

Back to an interface, not an abstract class this time: there's no shared implementation code worth forcing on every payment method, only a contract, which is exactly the case [ch15-02](ch15-02-abstract-classes.md) said an interface fits best:

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

Nothing new here: this is the same pair of classes from earlier in the chapter, just implementing an interface instead of extending an abstract base. Now the context:

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

`Checkout` is the context. It holds a `PaymentMethod` (any `PaymentMethod`), and its `complete()` method delegates entirely to whatever strategy it's currently holding, without a single `if` statement checking which one it is. That absence of branching is the tell that you're looking at Strategy done properly: `Checkout` never asks "are you a `CreditCard` or a `PayPal`?" It just calls `charge()` and trusts the interface.

## Using it and swapping strategies at runtime

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

Same `$checkout` object, same `complete()` call, two completely different outcomes, because `setPaymentMethod()` swapped out the strategy in between. That's the part a plain `if ($type === 'credit_card')` branch scattered through `Checkout` could never give you as cleanly: adding a third payment method next quarter means writing one new class that implements `PaymentMethod`, and changing nothing whatsoever in `Checkout` itself. It already works, for the same reason `processPayment()` already worked back in ch15-01: it was never written against a specific strategy in the first place, only against the interface every strategy is guaranteed to satisfy.

That's the entire pattern: an interface describing a swappable behavior, one or more classes implementing it, and a context class that delegates to whichever one it's holding. No new syntax, no library, nothing PHP-specific about it at all: just the interfaces and polymorphism you already had, arranged on purpose to solve a recognizable problem. Once you've built one pattern this way, you'll start noticing the same shape everywhere, under other names, in code you didn't write.
