# The `match` Expression

<img src="images/ch06-icon.svg" alt="The match Expression illustration" width="72">

Back in [Control Flow](ch03-05-control-flow.md), you saw `match(true)` used to test a series of conditions against an HTTP status code, a neat trick, but not actually `match` doing what it's best at. `match`'s real strength shows up when you're comparing one value directly against a small, known set of possibilities, which is precisely what an enum gives you.

## Matching directly on an enum case

```php
<?php
declare(strict_types=1);

enum Status: string
{
    case Pending = 'pending';
    case Shipped = 'shipped';
    case Cancelled = 'cancelled';
}

function nextAction(Status $status): string
{
    return match ($status) {
        Status::Pending => 'Pack the order',
        Status::Shipped => 'Notify the customer',
        Status::Cancelled => 'Issue a refund',
    };
}

echo nextAction(Status::Pending); // Pack the order
```

No `true`, no comparison operators, no range checks: `match ($status)` compares `$status` directly against each arm using strict (`===`) comparison, and returns the value beside whichever arm matched. This is `match` at its cleanest: read top to bottom, it's a direct, literal table mapping each possible case to what should happen for it, and there's no ambiguity about what's being compared against what.

## Multiple conditions per arm

You're not limited to one value per arm: separate several with commas, and any one of them matching is enough:

```php
<?php
declare(strict_types=1);

function isFinal(Status $status): bool
{
    return match ($status) {
        Status::Shipped, Status::Cancelled => true,
        Status::Pending => false,
    };
}

var_dump(isFinal(Status::Shipped));   // true
var_dump(isFinal(Status::Cancelled)); // true
var_dump(isFinal(Status::Pending));   // false
```

`Status::Shipped, Status::Cancelled => true` reads naturally as "either of these, same outcome": considerably clearer than writing the same arm twice, or reaching for an `||` inside a `match(true)` construction.

## Exhaustiveness is enforced

Here's the detail that makes `match` more than a tidier `switch`: every possible case has to be accounted for, either by name or with a `default` arm. Leave one out, and PHP doesn't silently skip it: it throws:

```php
<?php
declare(strict_types=1);

enum Status: string
{
    case Pending = 'pending';
    case Shipped = 'shipped';
    case Cancelled = 'cancelled';
    case Returned = 'returned'; // added later
}

function nextAction(Status $status): string
{
    return match ($status) {
        Status::Pending => 'Pack the order',
        Status::Shipped => 'Notify the customer',
        Status::Cancelled => 'Issue a refund',
        // forgot to add a Returned arm
    };
}

nextAction(Status::Returned); // UnhandledMatchError: Unhandled match case Status::Returned
```

This is a real safety feature, not just strictness for its own sake. Add a new case to an enum months from now, forget to update one of the several `match` expressions scattered around your codebase that switch on it, and PHP tells you immediately, loudly, at the exact call site that needed updating, instead of a `switch` statement silently falling through to nothing, or an `if` chain quietly doing the wrong thing for a value nobody anticipated. If a `match` genuinely doesn't need to handle every case explicitly, because most of them share the same fallback behavior, add a `default` arm, exactly like `switch` has always had, and it soaks up anything not named above it.
