# Reusing Code with PHP Traits

<img src="images/ch11-icon.svg" alt="Reusing Code with PHP Traits illustration" width="72">

An interface, as you just saw, promises nothing about implementation: it's pure shape. A trait is the opposite kind of tool, and it's worth being blunt about the difference because the two get confused constantly: a trait is a chunk of actual method bodies that PHP pastes into a class for you, as if you'd typed the code directly inside it. There's no contract, no polymorphism, no "any of these classes can be used interchangeably." It's copy-paste, formalized and made safe by the language.

Say two completely unrelated classes (a `PaymentProcessor` and a `ReportGenerator`) both want to write timestamped messages somewhere. They share no parent class, and shouldn't; they're not the same kind of thing. But they want the same three lines of logging code.

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

`trait` looks like a class, but you can never write `new LoggableTrait()`: a trait isn't a type, and it doesn't appear anywhere in `instanceof` checks or type hints. It exists purely to be pulled into other classes with `use`:

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

`PaymentProcessor` and `ReportGenerator` now both have a working `log()` method, a `getLog()` method, and a private `$log` property, none of which either class wrote. As far as PHP is concerned, once `use LoggableTrait;` runs, it's exactly as if you'd typed those three members directly into the class body. Crucially, `$processor instanceof LoggableTrait` isn't even valid: a trait grants behavior, not identity. `PaymentProcessor` and `ReportGenerator` remain two unrelated classes that happen to share some code, not siblings in a type hierarchy.

## Why not just use inheritance?

Because these classes have nothing else in common. Forcing `PaymentProcessor` and `ReportGenerator` to extend some shared `LoggableBase` class purely to get a `log()` method would be modeling a relationship that doesn't exist: a payment processor is not a kind of report generator's parent, and PHP only gives you one parent class per class anyway, so you'd be spending your one shot on logging. A trait sidesteps the whole question: it's not "is-a," it's "has this behavior, borrowed from here."

## Conflicts between traits

A class can `use` more than one trait at a time, and if two traits happen to define a method with the same name, PHP won't guess which one you meant; it raises a fatal error unless you resolve it explicitly:

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

`insteadof` picks a winner when two traits collide; `as` gives the loser's version a new name instead of discarding it. You won't need this often: most traits are narrow and purpose-built enough that collisions are rare, but it's worth knowing the syntax exists so a codebase that uses it doesn't read as mysterious the first time you meet it.

## Naming convention

You'll see traits named both `Loggable` and `LoggableTrait` in the wild; this book suffixes with `Trait` to keep them visually distinct from the interfaces they often accompany: it's common to pair a `Loggable` interface (the contract: "this class can log") with a `LoggableTrait` (the shared implementation that satisfies it), which is arguably traits' best use case in real code. Neither convention is enforced by PHP itself; pick one for a codebase and stay consistent.
