# Parler à d'autres API : Guzzle

Presque toute fonctionnalité qui « parle à un autre service » revient à envoyer des requêtes HTTP et à traiter les réponses. **Guzzle est la façon par défaut de le faire en PHP depuis plus de dix ans**, et il se comporte de la même manière dans un framework et dans un script de quarante lignes.

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

Guzzle prend aussi en charge ce qui devient fastidieux à écrire soi-même : les nouvelles tentatives, les délais d'expiration, le streaming des grosses réponses, et les requêtes concurrentes qui ne s'attendent pas les unes les autres.

```php
use GuzzleHttp\Promise\Utils;

$promises = [
    'users' => $client->getAsync('/users'),
    'orders' => $client->getAsync('/orders'),
];

$results = Utils::unwrap($promises);
```

## Quand le choisir

Tout script ou service qui appelle une API tierce sans être déjà dans un framework doté de son propre client HTTP. La façade `Http` de Laravel et le composant `HttpClient` de Symfony emballent les mêmes idées, et l'un comme l'autre est un bon choix si vous y êtes déjà. Guzzle est la valeur sûre quand vous ne savez pas encore à quoi ressemblera le reste du projet.

## Quand ce n'est pas le bon outil

Au fond d'un projet Laravel, `Http::get(...)` est Guzzle sous une syntaxe plus aimable. Il y a rarement une raison de le contourner pour appeler Guzzle directement.

> **Sous le capot :** Guzzle et la plupart des clients HTTP en PHP parlent PSR-7 et PSR-18, des interfaces standard pour les messages et les clients HTTP. C'est pour cela que la façade `Http` de Laravel, le `HttpClient` de Symfony et Guzzle peuvent se passer des requêtes et des réponses sans qu'aucun ne sache que les autres existent.
