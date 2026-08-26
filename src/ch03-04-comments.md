# Comments

PHP gives you three ways to write a comment, which is one more than most languages bother with, for reasons rooted in its templating-language ancestry.

```php
<?php

// A single-line comment.

# Also a single-line comment, same effect, different heritage
// (this style is borrowed from shell scripts; you'll see it far less often).

/*
 * A multi-line comment,
 * for when one line isn't enough.
 */
```

In practice, `//` dominates for everyday comments, and `/* ... */` shows up for the longer, more structured kind: most commonly as a *docblock* sitting right above a function or class:

```php
<?php

/**
 * Calculates compound interest.
 *
 * @param float $principal Starting amount
 * @param float $rate Annual interest rate, as a decimal (e.g. 0.05 for 5%)
 * @param int $years Number of years to compound
 * @return float The final amount after compounding
 */
function compoundInterest(float $principal, float $rate, int $years): float {
    return $principal * (1 + $rate) ** $years;
}
```

That `/**` opener (two asterisks, not one) marks it as a docblock (a convention, not a language feature) and tools like your editor, PHPStan, and documentation generators all know to read `@param` and `@return` tags out of it. We'll lean on docblocks properly once we hit generics-adjacent territory in [Chapter 10](ch10-00-interfaces-and-traits.md), where PHP's type system needs a little help from comments to say things the language itself can't express yet.

## What's worth commenting

The honest answer is: less than you'd think. A well-named function and well-typed parameters explain themselves; a comment repeating what the code already says just gives you two places to keep in sync, and only one of them the compiler checks.

```php
<?php

// Bad: says what, which the code already says
// Increment the counter by one
$counter++;

// Good: says why, which the code can't say on its own
// Retry once more here: the upstream API is flaky on cold start
$retries++;
```

Comment the *why*, not the *what*. A comment explaining a workaround, a non-obvious constraint, or a decision that would look wrong without context is worth its weight. A comment translating code into English, line by line, usually isn't, and it's one more thing to go stale the next time someone edits the code without updating the comment above it.
