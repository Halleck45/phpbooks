# Reusing Code with PHP Traits

An interface promises nothing about implementation: it is pure shape. **A trait is a chunk of real method bodies that PHP pastes into a class for you, as if you had typed them there yourself.** No contract, no polymorphism, no "these classes can be used interchangeably". Copy-paste, made official and made safe by the language.

Say two classes with nothing in common, a `PaymentProcessor` and a `ReportGenerator`, both want to write timestamped messages somewhere. They share no parent class, and they should not: they are not the same kind of thing. But they want the same few lines of logging code.

```php
<?php

trait LoggableTrait
{
    private array $log = [];

    public function log(string $message): void
    {
        $this->log[] = sprintf('[%s] %s', date('H:i:s'), $message);
    }

    public function getLog(): array
    {
        return $this->log;
    }
}
```

`trait` looks like a class, but you can never write `new LoggableTrait()`. A trait is not a type. It appears in no `instanceof` check and no type hint. It exists only to be pulled into other classes with `use`:

```php
<?php

class PaymentProcessor
{
    use LoggableTrait;

    public function charge(float $amount): void
    {
        $this->log("Charging \${$amount}");
    }
}

class ReportGenerator
{
    use LoggableTrait;

    public function generate(): void
    {
        $this->log('Generating monthly report');
    }
}

$processor = new PaymentProcessor();
$processor->charge(42.00);

var_dump($processor->getLog());
// array(1) { [0]=> string(...) "[14:32:01] Charging $42" }
```

`PaymentProcessor` and `ReportGenerator` now both have a working `log()` method, a `getLog()` method, and a private `$log` property, and neither class wrote a line of it. Once `use LoggableTrait;` is there, it is exactly as if you had typed those three members into the class body.

<img src="images/ch11-trait-paste.png" alt="A small elephant pastes the same sheet of code, headed log(), into two unrelated class boxes, PaymentProcessor and ReportGenerator, with a glue stick" width="560">

What they do not gain is a family tie. Asking `$processor instanceof LoggableTrait` gets you nowhere: a trait grants behavior, not identity. `PaymentProcessor` and `ReportGenerator` remain two unrelated classes that happen to share some code, not siblings in a type hierarchy.

> A trait gives a class code, not an identity.

## Why not just use inheritance?

Because these classes have nothing else in common. Forcing `PaymentProcessor` and `ReportGenerator` to extend a shared `LoggableBase` class purely to get a `log()` method would model a relationship that does not exist. PHP also gives each class exactly one parent, and you would be spending that one shot on logging. **A trait sidesteps the whole question: not "is a", but "has this behavior, borrowed from here".**

## Conflicts between traits

A class can `use` several traits at once. If two of them define a method with the same name, PHP will not guess which one you meant. It raises a fatal error until you settle the matter yourself:

```php
<?php

class Report
{
    use LoggableTrait, TimestampableTrait {
        LoggableTrait::log insteadof TimestampableTrait;
        TimestampableTrait::log as logTimestampOnly;
    }
}
```

`insteadof` picks the winner. `as` gives the loser's version a new name instead of throwing it away. You will not need this often, since most traits are narrow enough that collisions are rare, but knowing the syntax means a codebase that uses it will not read as a mystery the first time you meet it.

## Naming convention

You will see traits named both `Loggable` and `LoggableTrait` in the wild. This book adds the `Trait` suffix to keep them visually apart from the interfaces they often travel with. Pairing a `Loggable` interface (the contract: "this class can log") with a `LoggableTrait` (the shared implementation that fulfills it) is arguably the best use of traits in real code. PHP enforces neither convention. Pick one for a codebase and stay consistent.

Interfaces and traits both work at the level of the class. The next gap in PHP's type system sits one level down, inside the array, and the language leaves that one to you.
