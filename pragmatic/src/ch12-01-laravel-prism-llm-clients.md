# Laravel: Prism and the OpenAI/Anthropic PHP Clients

Prism is a Laravel-native package for talking to large language models (OpenAI, Anthropic, and others) behind one consistent API, so a feature you build against one provider isn't locked to it.

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

Swapping providers, comparing cost or quality between Anthropic and OpenAI for the same feature, is a one-line change:

```php
Prism::text()->using(Provider::OpenAI, 'gpt-4o')->withPrompt($prompt)->generate();
```

Structured output, useful for anything that needs to feed the result back into your database rather than just display it, is a schema instead of hand-parsed text:

```php
$response = Prism::structured()
    ->using(Provider::Anthropic, 'claude-sonnet')
    ->withSchema($ticketClassificationSchema)
    ->withPrompt("Classify this ticket: {$ticket->body}")
    ->generate();

$category = $response->structured['category'];
```

For projects that want a thinner layer with less abstraction, the official `openai-php/client` and `anthropic-php` packages call each provider's API directly, useful when a feature genuinely only needs to work with one provider.

## When to reach for this

A specific, bounded feature: summarization, classification, a support chatbot, content suggestions, added to an app that's otherwise a normal Laravel product.

## When it's the wrong fit

A feature that needs the model to act on live, private data at request time in a way an API call alone can't provide, which usually points toward a retrieval step (searching your own data first, then including it in the prompt) rather than a reason to avoid this approach entirely.

> **Under the hood:** Prism's provider abstraction is a PHP interface, the same pattern behind [Flysystem's storage adapters](ch02-06-league-flysystem-standalone.md): one contract, several interchangeable implementations, so your application code depends on the contract rather than a specific vendor's SDK.
