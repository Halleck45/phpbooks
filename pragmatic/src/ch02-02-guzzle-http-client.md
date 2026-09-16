# Talking to Other APIs: Guzzle

Almost every feature that "talks to another service" boils down to making HTTP requests and handling the response. Guzzle has been the default way to do that in PHP for over a decade, and it works identically whether you're inside a framework or writing a forty-line script.

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

Guzzle also handles the parts that get tedious to write by hand: retries, timeouts, streaming large responses, and sending concurrent requests without blocking on each one in turn.

```php
use GuzzleHttp\Promise\Utils;

$promises = [
    'users' => $client->getAsync('/users'),
    'orders' => $client->getAsync('/orders'),
];

$results = Utils::unwrap($promises);
```

## When to reach for this

Any script or service that needs to call a third-party API and isn't already inside a framework that ships its own HTTP client (Laravel's `Http` facade and Symfony's `HttpClient` component both wrap similar ideas, and either is a fine choice if you're already there). Guzzle is the safe default when you're not sure yet what the rest of the project will look like.

## When it's the wrong fit

If you're deep inside Laravel, its `Http::get(...)` facade is Guzzle under a friendlier syntax, so there's rarely a reason to bypass it and reach for raw Guzzle directly.

> **Under the hood:** Guzzle and most modern PHP HTTP clients speak PSR-7 and PSR-18, standard interfaces for HTTP messages and clients. That's why Laravel's `Http` facade, Symfony's `HttpClient`, and Guzzle can all hand requests and responses to each other without any of them needing to know the others exist.
