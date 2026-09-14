# Un routeur en un seul fichier avec le serveur intégré de PHP

Un navigateur demande `/about`. Quelque part sur le serveur, un bout de code doit répondre. Lequel ? **La partie d'une application web qui transforme une URL en un bout de code s'appelle un routeur**, et chaque framework en a un, si gros soit-il. Avant d'utiliser le leur, construisez le plus petit qui puisse fonctionner, pour voir exactement ce qu'il fait.

## Le serveur de développement intégré à PHP

Il faut un serveur web pour recevoir la requête, et PHP en cache un dans la commande `php` elle-même. Ni Apache, ni nginx, rien à installer. Il n'est pas fait pour la production, mais pour développer, et pour apprendre, c'est exactement ce qu'il faut :

```console
$ php -S localhost:8000 router.php
[Thu Aug 20 10:00:00 2026] PHP 8.3.0 Development Server (http://localhost:8000) started
```

Cette commande lance un serveur sur le port 8000 et fait passer *chaque* requête entrante par `router.php`. Aucune correspondance automatique avec un fichier sur le disque. C'est votre script qui décide, pour chaque requête, quoi renvoyer. On voit tout, et c'est précisément ce qu'on veut.

## Le routeur lui-même

Créez `router.php` :

```php
<?php

$uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

$routes = [
    '/' => function (): string {
        return "Welcome to the home page.\n";
    },
    '/about' => function (): string {
        return "This is a tiny PHP application, built without a framework.\n";
    },
];

header('Content-Type: text/plain');

if (isset($routes[$uri])) {
    echo $routes[$uri]();
} else {
    http_response_code(404);
    echo "404 Not Found: {$uri}\n";
}
```

Lisez-le depuis le haut. **`$_SERVER['REQUEST_URI']` est l'endroit où PHP range le chemin demandé par le navigateur** : `/`, `/about`, ce qui a été tapé ou cliqué. `parse_url(..., PHP_URL_PATH)` en coupe la chaîne de requête éventuelle (`?foo=bar`), si bien que `/about?ref=email` et `/about` tombent sur la même route.

<img src="images/ch21-router-switchboard.png" alt="Une requête pour /about arrive devant une table de correspondance avec une ligne par chemin ; la ligne qui correspond mène au code qui répond, et une corbeille en bas récupère tout le reste en 404" width="560">

Ensuite, `$routes` est un tableau associatif, une simple table de correspondance : un chemin à gauche, et à droite une closure qui produit la réponse. **Le routeur cherche le chemin dans la table ; si c'est une clé connue, il appelle la closure et affiche ce qu'elle renvoie.** Sinon, il répond 404, comme n'importe quel serveur devant une page qui n'existe pas.

Essayez, le serveur toujours lancé dans un autre terminal :

```console
$ curl http://localhost:8000/
Welcome to the home page.

$ curl http://localhost:8000/about
This is a tiny PHP application, built without a framework.

$ curl http://localhost:8000/nonexistent
404 Not Found: /nonexistent
```

Ajoutez maintenant une route à vous : une clé `/contact` avec une closure qui renvoie le texte de votre choix. Enregistrez, et demandez-la à `curl`. Pas besoin de relancer quoi que ce soit, le serveur exécute `router.php` à neuf à chaque requête.

## Ce que ça fait (et ne fait pas)

Ce routeur ignore tout des paramètres de chemin (`/users/{id}`), des méthodes HTTP (`GET` contre `POST` sur le même chemin) et des middlewares. Les vrais routeurs ajoutent tout cela. Mais dans leur structure, ils font ce que font ces quinze lignes : regarder quelque chose dans la requête entrante, et aiguiller vers un bout de code en fonction.

> Un routeur, c'est une table de correspondance avec un 404 en bas.

Quinze lignes suffisent pour voir le mécanisme. Elles ne suffisent pas pour grandir : dès que chaque route devra produire du vrai HTML, les closures de ce tableau deviendront un fouillis. La section suivante donne à chaque route un vrai chez-soi.
