# Talking to Other APIs: Guzzle

Almost every feature that "talks to another service" comes down to sending HTTP requests and handling the responses. **Guzzle has been the default way to do that in PHP for over a decade**, and it behaves the same inside a framework and in a forty-line script.

```bash
composer require guzzlehttp/guzzle
```

```php
<?php
require 'vendor/autoload.php';

use GuzzleHttp\Client;

$client = new Client(['base_uri' => 'https://api.example.com']);

$response = $client->get('/users/42', [
    'headers' => ['Authorization' => 'Bearer ' . getenv('API_TOKEN')],
]);

$user = json_decode($response->getBody()->getContents(), true);
echo $user['name'];
```

Guzzle also handles the parts that get tedious by hand: retries, timeouts, streaming large responses, and concurrent requests that don't block on each other in turn.

```php
use GuzzleHttp\Promise\Utils;

$promises = [
    'users' => $client->getAsync('/users'),
    'orders' => $client->getAsync('/orders'),
];

$results = Utils::unwrap($promises);
```

## When to reach for this

Any script or service that calls a third-party API and isn't already inside a framework with its own HTTP client. Laravel's `Http` facade and Symfony's `HttpClient` component wrap the same ideas, and either is a fine choice if you are already there. Guzzle is the safe default when you don't know yet what the rest of the project will look like.

## When it's the wrong fit

Deep inside Laravel, `Http::get(...)` is Guzzle under a friendlier syntax. There is rarely a reason to bypass it and reach for raw Guzzle.

> **Under the hood:** Guzzle and most PHP HTTP clients speak PSR-7 and PSR-18, standard interfaces for HTTP messages and clients. That is why Laravel's `Http` facade, Symfony's `HttpClient`, and Guzzle can hand requests and responses to each other without any of them knowing the others exist.
