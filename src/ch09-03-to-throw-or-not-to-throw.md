# To Throw or Not to Throw

<img src="images/ch09-icon.svg" alt="To Throw or Not to Throw illustration" width="72">

Knowing the syntax of `try`/`catch` is the easy part. The harder question, and the one that actually separates readable PHP code from a maze of defensive checks, is deciding *when* a function should throw, when it should just return `null` or `false` or an empty array, and when it's fine to let the whole thing come crashing down. There's no compiler rule for this: it's judgment, the kind you build from having been burned both ways. Here's how I've come to think about it.

## Not found is not exceptional

The most common mistake I see is throwing for something that isn't actually exceptional: it's just a normal outcome the caller needs to handle. Looking up a user by an ID that doesn't exist isn't a crisis. It's a completely ordinary thing to happen, as routine as any other branch in your code:

```php
<?php

declare(strict_types=1);

function findUserById(array $users, int $id): ?array
{
    foreach ($users as $user) {
        if ($user['id'] === $id) {
            return $user;
        }
    }

    return null; // not found, a completely normal outcome, not an error
}

$user = findUserById($users, 42);

if ($user === null) {
    echo "No such user.\n";
} else {
    echo "Found: {$user['name']}\n";
}
```

Returning `null` here (and giving the function a `?array` return type so the possibility is visible right in the signature, not just implied) tells the caller exactly what to expect and lets them decide what "not found" means in their context: show a 404, create a default, ask again. Throwing `UserNotFoundException` instead would force every caller into a `try`/`catch` for something that's going to happen constantly and isn't wrong in any sense. Save exceptions for things that are actually exceptions.

## Throw when the caller has a precondition to meet

The flip side: throw when something the caller was supposed to guarantee didn't hold, and there's genuinely no reasonable default to fall back to. This is the `InvalidAgeException` from the previous section: a negative age isn't "a normal outcome to branch on," it's a violated contract. The function can't sensibly guess what you meant, so it says so, loudly and specifically:

```php
<?php

declare(strict_types=1);

function withdraw(float $balance, float $amount): float
{
    if ($amount > $balance) {
        throw new \RuntimeException(
            "Cannot withdraw {$amount}: balance is only {$balance}."
        );
    }

    return $balance - $amount;
}
```

Silently clamping the withdrawal to the available balance, or quietly returning `0`, would hide a bug (or worse, a real financial error) behind a plausible-looking number, exactly the failure mode from the previous section's `catch (\Error $e)` example. Throwing here forces whoever's calling `withdraw()` to actually confront the situation instead of it slipping past unnoticed.

## Let it crash when it's a bug, not a case

Sometimes the right answer isn't `null` and isn't a caught exception: it's letting the program stop. If your own code calls a function with the wrong argument type, or reaches a `match` arm that should be logically impossible, that's not a runtime condition to design around; it's a bug to fix, and pretending otherwise just buries the evidence:

```php
<?php

declare(strict_types=1);

enum Status
{
    case Draft;
    case Published;
    case Archived;
}

function statusLabel(Status $status): string
{
    return match ($status) {
        Status::Draft => 'Draft',
        Status::Published => 'Published',
        Status::Archived => 'Archived',
    };
}
```

`match` without a `default` arm throws `UnhandledMatchError` (a subclass of `Error`, not `Exception`) if none of the cases fit. For an `enum`, every case is already covered, so this can only happen if someone adds a new `Status` case later and forgets to update this function. That's exactly the kind of failure you want loud and immediate at the point of the bug, not silently swallowed three files away. Don't wrap this in a `try`/`catch` "just in case": let it fail, let the stack trace point straight at the missing arm, and go fix `statusLabel()`.

## A rough decision order

When you're not sure which of the three to reach for, this order has served me well:

1. **Is "not found" or "empty" a normal, expected outcome here?** Return `null`, `false`, or an empty array, and give the function a return type that makes the possibility explicit (`?array`, not `array`).
2. **Did the caller violate a precondition, with no sensible default to fall back to?** Throw a specific exception: built-in if one fits (`InvalidArgumentException`, `RuntimeException`), a small custom class if the caller needs structured context back, as with `InvalidAgeException`.
3. **Is this actually impossible unless the code itself is wrong?** Don't defend against it at all. Let PHP's own `Error` machinery do its job, or use `assert()` during development. A loud, immediate failure at the site of the bug is far cheaper to fix than a quiet one three layers of `catch` away.

None of this is a rule you can apply mechanically: plenty of real code sits in a gray area between "expected" and "precondition violated," and reasonable developers land in different places. But asking the question explicitly, function by function, beats defaulting to whichever of `throw` or `return null` you happened to type first. It's a habit worth building deliberately, because you'll be making this exact call in nearly every function you write from here on, including several in the CLI project starting at [Chapter 14](ch14-00-a-cli-project.md).
