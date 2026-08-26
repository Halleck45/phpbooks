# Abstract Classes and Interfaces Revisited

The `PaymentMethod` base class from the previous section had a working `charge()` implementation of its own: generic, but real. That's a design smell worth noticing: nothing stops anyone from writing `new PaymentMethod()` directly and calling `charge()` on a payment method that isn't actually connected to a card, an account, or anything else capable of processing money. The base class was only ever meant as a foundation for subclasses, never as something to instantiate on its own, but PHP had no way of knowing that. `abstract` is how you tell it.

## Making the contract explicit

```php
<?php
declare(strict_types=1);

abstract class PaymentMethod
{
    abstract public function charge(float $amount): string;

    protected function receipt(float $amount): string
    {
        return sprintf('$%.2f processed on %s', $amount, date('Y-m-d'));
    }
}

class CreditCard extends PaymentMethod
{
    public function __construct(private string $last4)
    {
    }

    public function charge(float $amount): string
    {
        return $this->receipt($amount) . " (card ending {$this->last4})";
    }
}
```

Two things changed. `PaymentMethod` is now `abstract class PaymentMethod`, which means PHP refuses to let you instantiate it directly: `new PaymentMethod()` is a fatal error, full stop, enforced by the language rather than left as a convention you hope people follow. And `charge()` is declared `abstract public function charge(float $amount): string;` (a signature with no body, exactly like an interface method) which means every non-abstract subclass *must* implement it, or PHP refuses to load that subclass too. What `PaymentMethod` still has is `receipt()`, a real, shared, working method that every subclass inherits for free. That's the combination an abstract class gives you that a plain interface can't: an enforced contract (`charge()` must exist) bundled with genuine shared implementation (`receipt()`, written once, used everywhere).

## Compare this to `Formattable`

Go back to the `Formattable` interface from [Chapter 10](ch10-01-interfaces.md):

```php
<?php
interface Formattable
{
    public function format(): string;
}
```

An interface is *only* a contract: no method bodies are allowed at all, not even ones a class could optionally inherit. Every class implementing `Formattable` writes its own `format()` from scratch; there's no shared code to lean on, because an interface has none to offer. That's not a limitation so much as the point: interfaces exist to describe a capability that classes with nothing else in common can all claim, without dragging in any shared ancestry. A `Product`, a `LogEntry`, and an `HttpResponse` could all reasonably implement `Formattable` despite having nothing else to do with one another, and a class can implement as many interfaces as it needs, which is exactly how PHP works around not supporting multiple inheritance for classes. An abstract class, by contrast, is a real ancestor: a class can only `extends` one, and everything that abstract class carries (properties, working methods, constructor logic) comes along with it.

## When to reach for which

The honest rule: reach for an **abstract class** when you have real implementation code you want every subclass to share, *and* you want to force each subclass to fill in the specific parts that must differ: `receipt()` shared, `charge()` mandatory but unique per subclass, in the example above. Reach for an **interface** when all you want is a guarantee that a method exists, with no assumption that the implementing classes are related to each other at all, or when a class already needs to `extends` something else and still needs to promise a second, unrelated capability: a class can only have one parent, but as many interfaces as it likes.

They're not actually rivals, and PHP doesn't make you pick exactly one. A class can extend an abstract parent and implement an interface at the same time:

```php
<?php
declare(strict_types=1);

interface Formattable
{
    public function format(): string;
}

abstract class PaymentMethod implements Formattable
{
    abstract public function charge(float $amount): string;

    public function format(): string
    {
        return static::class;
    }
}
```

`PaymentMethod` gets both: the shared, enforced structure of an abstract class for its own family of subclasses, and a separate, unrelated `Formattable` contract that lets it interoperate with any other code in the system that only cares whether something can `format()`, no relationship to `PaymentMethod` required.
