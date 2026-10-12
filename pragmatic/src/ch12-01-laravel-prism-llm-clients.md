# Laravel: Prism and the OpenAI/Anthropic PHP Clients

Prism is a Laravel-native package for talking to large language models (OpenAI, Anthropic and others) behind one API. **A feature built against one provider is not locked to it.**

```bash
composer require prism-php/prism
```

```php
use Prism\Prism\Prism;
use Prism\Prism\Enums\Provider;

$response = Prism::text()
    ->using(Provider::Anthropic, 'claude-sonnet')
    ->withPrompt("Summarize this support ticket in two sentences:\n\n{$ticket->body}")
    ->generate();

echo $response->text;
```

Comparing cost or quality between providers for the same feature is a one-line change:

```php
Prism::text()->using(Provider::OpenAI, 'gpt-4o')->withPrompt($prompt)->generate();
```

When the result has to go back into your database rather than onto a screen, ask for structured output. You give a schema instead of parsing text by hand:

```php
$response = Prism::structured()
    ->using(Provider::Anthropic, 'claude-sonnet')
    ->withSchema($ticketClassificationSchema)
    ->withPrompt("Classify this ticket: {$ticket->body}")
    ->generate();

$category = $response->structured['category'];
```

For a thinner layer, the official `openai-php/client` and `anthropic-php` packages call each provider's API directly. They fit a feature that only ever needs one provider.

## When to reach for this

A specific, bounded feature (summarisation, classification, a support chatbot, content suggestions) added to an app that is otherwise a normal Laravel product.

## When it's the wrong fit

A feature where the model must act on live, private data at request time, which an API call alone cannot provide. That usually points to a retrieval step first (search your own data, then put it in the prompt), not to a reason to avoid the approach.

> **Under the hood:** Prism's provider abstraction is a PHP interface, the same pattern behind [Flysystem's storage adapters](ch02-06-league-flysystem-standalone.md): one contract, several interchangeable implementations, so your application code depends on the contract rather than a specific vendor's SDK.
