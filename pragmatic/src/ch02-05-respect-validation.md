# Validating Input: Respect/Validation

Every form, every API payload, every CSV upload asks the same question: is this data usable? **Respect/Validation answers it with readable, chainable rules**, and needs no framework request lifecycle wrapped around it.

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

Rules read close to plain English and compose freely. `v::stringType()->notEmpty()->length(1, 255)` or `v::arrayType()->each(v::stringType())` cover most of what a form or an API payload needs, without a single custom rule.

## When to reach for this

A script or a small service that accepts outside input: a CSV import, a webhook receiver, a lightweight API. Pulling in a whole framework for its validation layer alone would be overkill.

## When it's the wrong fit

Once you are inside Laravel or Symfony. `$request->validate()` and the Symfony Validator component are wired into their framework's forms and error display, and are the better default there.

> **Under the hood:** Validation libraries lean on PHP's type system more than they used to. Underneath the fluent `v::intVal()` calls, recent versions describe what "valid" means with PHP's own union types and enums rather than reinventing type checks from scratch.
