# Validating Input: Respect/Validation

Every form, every API payload, every CSV upload eventually needs the same question answered: is this data actually usable? Respect/Validation gives you readable, chainable rules for answering that question, without needing a framework's request lifecycle wrapped around it.

```bash
composer require respect/validation
```

```php
<?php
require 'vendor/autoload.php';

use Respect\Validation\Validator as v;

$validator = v::key('email', v::email())
    ->key('age', v::intVal()->between(18, 120))
    ->key('username', v::alnum()->length(3, 20));

try {
    $validator->assert([
        'email' => 'ada@example.com',
        'age' => 34,
        'username' => 'ada_l',
    ]);
    echo "Valid.\n";
} catch (\Respect\Validation\Exceptions\NestedValidationException $e) {
    foreach ($e->getMessages() as $message) {
        echo "- {$message}\n";
    }
}
```

Rules read close to plain English and compose freely: `v::stringType()->notEmpty()->length(1, 255)` or `v::arrayType()->each(v::stringType())` cover most of what a typical form or API payload needs without writing a single custom rule.

## When to reach for this

A script or small service accepting outside input (a CSV import, a webhook receiver, a lightweight API) where pulling in a full framework just for its validation layer would be overkill.

## When it's the wrong fit

Laravel's built-in `$request->validate()` and Symfony's Validator component are both more tightly integrated with their framework's forms and error display, and are the better default once you're already building inside one of them.

> **Under the hood:** Validation libraries like this one lean on PHP's type system more than they used to. Underneath the fluent `v::intVal()` calls, modern versions increasingly use PHP's own union types and enums to describe what "valid" means, rather than reinventing type-checking from scratch.
