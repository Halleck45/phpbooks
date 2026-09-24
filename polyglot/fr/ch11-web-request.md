# Une requête web, sans framework

**PHP peut servir une page web sans bibliothèque, sans code serveur et sans configuration, parce que traiter une requête HTTP est ce pour quoi le langage a été conçu.** La requête est déjà analysée quand votre script démarre, et la réponse est ce que vous affichez. Un framework ajoute de la structure par-dessus, mais il n'ajoute pas la capacité.

Avoir vu une fois cette couche brute rend ensuite chaque framework lisible, parce qu'ils reposent tous sur exactement ces primitives.

## Le contrôleur frontal

Pointez le serveur de développement de PHP sur un seul fichier, et chaque URL passe par lui :

```bash
php -S localhost:8000 public/index.php
```

Ce fichier est le contrôleur frontal. En production, le serveur web fait la même chose avec une règle de réécriture (ou FrankenPHP et RoadRunner le font pour vous, comme le décrit [Comment PHP s'exécute](ch01-how-php-runs.md)). Avec le serveur de développement, un détail compte : **si le script renvoie `false`, le serveur sert le fichier demandé depuis le disque**, et c'est ainsi que passent les ressources statiques.

```php
<?php
declare(strict_types=1);

$path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

if ($path !== '/' && is_file(__DIR__ . $path)) {
    return false; // let the built-in server send the CSS or image
}

echo 'Every other URL lands here: ', htmlspecialchars($path, ENT_QUOTES);
```

## Lire la requête

La requête vit dans les superglobales, des tableaux que PHP remplit avant la première ligne de votre code. `$_GET` contient la chaîne de requête, `$_POST` les champs d'un formulaire soumis, `$_COOKIE` les cookies, `$_FILES` les fichiers envoyés, et `$_SERVER` tout le reste : `REQUEST_METHOD`, `REQUEST_URI`, et chaque en-tête HTTP sous la forme `HTTP_` suivi de son nom en majuscules, de sorte que `Accept-Language` devient `$_SERVER['HTTP_ACCEPT_LANGUAGE']`.

```php
<?php
declare(strict_types=1);

$method = $_SERVER['REQUEST_METHOD'];
$page = filter_input(INPUT_GET, 'page', FILTER_VALIDATE_INT) ?: 1;
$name = trim($_POST['name'] ?? '');
$lang = $_SERVER['HTTP_ACCEPT_LANGUAGE'] ?? 'en';

$body = json_decode(file_get_contents('php://input'), true, flags: JSON_THROW_ON_ERROR);
```

`$_POST` n'est rempli que pour les corps `application/x-www-form-urlencoded` et `multipart/form-data` envoyés en POST. Un corps JSON, quelle que soit la méthode, se lit brut depuis `php://input`. Un formulaire envoyé en PUT ou PATCH n'est pas analysé du tout, sauf si vous le demandez : `request_parse_body()` (PHP 8.4) renvoie les champs et les fichiers pour ces méthodes aussi.

**Rien dans ces tableaux n'est digne de confiance.** `HTTP_HOST` est ce que le client a envoyé, `REQUEST_URI` peut contenir n'importe quoi, et un champ attendu comme chaîne arrive sous forme de tableau si le client écrit `name[]=x`. Traitez chaque valeur comme une entrée utilisateur non typée, validez-la avec `filter_var` ou vos propres vérifications, et seulement ensuite laissez-la approcher votre logique.

<img src="images/ch11-request-response.png" alt="Une enveloppe étiquetée request s'ouvre sur quatre bacs étiquetés GET, POST, COOKIE et SERVER, qui alimentent un script dessiné comme une page ; la sortie imprimée du script coule dans une seconde enveloppe étiquetée response, avec un petit autocollant d'en-tête collé avant le corps" width="560">

## Écrire la réponse

**Tout ce que votre script affiche est le corps de la réponse**, qu'il s'agisse d'un `echo`, d'un `print` ou de texte placé hors des balises `<?php ?>`. Le statut et les en-têtes se règlent avec deux fonctions, à appeler avant le premier octet de sortie, parce que les en-têtes voyagent en premier :

```php
<?php
declare(strict_types=1);

http_response_code(201);
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
setcookie('theme', 'dark', [
    'expires' => time() + 86400 * 30,
    'path' => '/',
    'secure' => true,
    'httponly' => true,
    'samesite' => 'Lax',
]);

echo json_encode(['created' => true], JSON_THROW_ON_ERROR);
```

Affichez quoi que ce soit avant, même un saut de ligne égaré devant `<?php`, et `header()` échoue avec « headers already sent ». La mise en tampon de la sortie (`ob_start()` au début, `ob_end_flush()` à la fin) retient le corps en mémoire jusqu'à la fin du script et rend l'ordre indifférent ; c'est ce que font les frameworks.

## Les gabarits sont du PHP

PHP a commencé comme langage de gabarits, et il l'est toujours : un fichier HTML avec des `<?= $expr ?>` dedans est un gabarit, et un `include` suffit à l'afficher. La seule règle porte sur la sortie : **échappez chaque valeur avec `htmlspecialchars` avant qu'elle n'atterrisse dans le HTML**, sinon le premier utilisateur nommé `<script>` est propriétaire de votre page.

```php
<?php
declare(strict_types=1);

function e(string $value): string
{
    return htmlspecialchars($value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

$todos = ['Write the chapter', 'Escape <everything>'];
?>
<ul>
<?php foreach ($todos as $todo): ?>
    <li><?= e($todo) ?></li>
<?php endforeach; ?>
</ul>
```

La forme `foreach (...): ... endforeach;` existe précisément pour cet entrelacement. Un utilitaire `e()` de deux lignes est toute l'histoire de l'échappement pour le HTML ; les attributs, les URL et les contextes JavaScript demandent chacun leur propre encodage, et c'est la partie que les moteurs de gabarits automatisent.

## Une application complète

L'application ci-dessous fonctionne telle quelle, en un seul fichier : une liste de notes stockées dans SQLite, avec un formulaire pour en ajouter une. Elle tourne avec `php -S localhost:8000 index.php` et rien d'autre.

```php
<?php
declare(strict_types=1);

$db = new PDO('sqlite:' . __DIR__ . '/notes.db', options: [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
]);
$db->exec('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, body TEXT NOT NULL)');

function e(string $value): string
{
    return htmlspecialchars($value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

$route = $_SERVER['REQUEST_METHOD'] . ' ' . parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

match ($route) {
    'GET /' => (function () use ($db): void {
        $notes = $db->query('SELECT id, body FROM notes ORDER BY id DESC')->fetchAll();
        echo '<h1>Notes</h1><form method="post" action="/notes">',
            '<input name="body" required> <button>Add</button></form><ul>';
        foreach ($notes as $note) {
            echo '<li>', e($note['body']), '</li>';
        }
        echo '</ul>';
    })(),
    'POST /notes' => (function () use ($db): void {
        $body = trim($_POST['body'] ?? '');
        if ($body === '') {
            http_response_code(422);
            echo 'A note needs a body.';
            return;
        }
        $stmt = $db->prepare('INSERT INTO notes (body) VALUES (:body)');
        $stmt->execute(['body' => $body]);
        http_response_code(303);
        header('Location: /');
    })(),
    default => (function (): void {
        http_response_code(404);
        echo 'Not found';
    })(),
};
```

Ce fichier illustre l'essentiel de ce qu'il y a à savoir. **Le routeur est un `match` sur la méthode et le chemin**, ce qui tient jusqu'à une dizaine de routes avant que vous n'en vouliez un vrai. **PDO est l'API de base de données**, une seule interface pour SQLite, MySQL, PostgreSQL et d'autres, et `ERRMODE_EXCEPTION` transforme chaque échec en `PDOException` levée plutôt qu'en `false` que vous oubliez de vérifier. **La requête utilise un marqueur nommé et `execute()` lie la valeur** ; le texte SQL et les données ne se rencontrent jamais sous forme de chaîne, donc aucune injection SQL à craindre. PHP 8.4 ajoute des sous-classes par pilote (`Pdo\Sqlite`, `Pdo\Mysql`, `Pdo\Pgsql`) via `Pdo::connect()`, qui exposent les spécificités de chaque pilote avec des types corrects.

Construire le SQL par interpolation, `"WHERE id = $id"`, est la seule habitude des vieux tutoriels PHP que le langage vous laisse encore garder, et c'est précisément celle qu'il faut abandonner.

## Sessions et mots de passe

Une session est un stockage côté serveur indexé par un cookie. Appelez `session_start()` avant toute sortie, et `$_SESSION` devient un tableau qui survit d'une requête à l'autre pour ce visiteur. Par défaut, les données vivent dans des fichiers sur le serveur ; les frameworks y substituent une base de données ou un cache via `session_set_save_handler()`. Le cookie ne transporte que l'identifiant de session.

```php
<?php
declare(strict_types=1);

session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $ok = password_verify($_POST['password'] ?? '', $storedHash ?? '');
    if ($ok) {
        session_regenerate_id(true);
        $_SESSION['user_id'] = 42;
    }
}

$csrf = $_SESSION['csrf'] ??= bin2hex(random_bytes(32));
```

`password_hash` et `password_verify`, vus dans [Chaînes, nombres, dates et JSON](ch10-standard-library.md), suffisent pour les mots de passe, à condition de régénérer l'identifiant de session à la connexion. Pour la protection CSRF, mettez un jeton aléatoire dans la session, imprimez-le en champ caché dans chaque formulaire, et comparez-le à la soumission avec `hash_equals()` ; cela tient en quatre lignes, et chaque framework fait la même chose sous un nom plus flatteur.

## La couche des standards

Les superglobales et `header()` fonctionnent, mais c'est de l'état global, ce qui rend le code difficile à tester et impossible à composer. Le PHP-FIG a répondu par des interfaces :

- **PSR-7** définit des objets immuables `RequestInterface` et `ResponseInterface`, de sorte qu'une requête est une valeur que vous passez et une réponse une valeur que vous renvoyez.
- **PSR-15** définit l'intergiciel (middleware) : un gestionnaire prend une requête et renvoie une réponse, et un middleware enveloppe des gestionnaires. Authentification, CORS, journalisation, limitation de débit sont chacun une classe.
- **PSR-17** définit les fabriques qui créent ces objets, pour qu'une bibliothèque ne dépende jamais d'une implémentation précise.
- **PSR-18** définit un client HTTP, le côté sortant des mêmes objets.

**Une bibliothèque écrite contre PSR-7 et PSR-15 tourne dans tout framework qui les parle**, c'est-à-dire aujourd'hui la plupart. CakePHP, Laminas, Laravel, Symfony et Yii, et les micro-frameworks Mezzio et Slim, ajoutent chacun routage, injection de dépendances, gabarits et couche de base de données par-dessus ces primitives ; les primitives en dessous sont celles que vous venez de voir.

<img src="images/ch11-middleware-onion.png" alt="Des anneaux concentriques dessinés comme un oignon coupé en deux, étiquetés de l'extérieur vers l'intérieur : logging, auth, CORS, et au centre une petite boîte étiquetée handler ; une flèche étiquetée request entre par la gauche à travers chaque anneau et une flèche étiquetée response ressort à droite à travers les mêmes anneaux" width="480">

En production, le contrôleur frontal reste le même, et seul change ce qui l'appelle : PHP-FPM derrière nginx, Apache ou Caddy, ou un runtime persistant comme FrankenPHP ou RoadRunner. Rien dans ce chapitre n'a besoin d'être adapté à l'un ou à l'autre.

L'application ci-dessus n'a ni tests ni analyse statique, et [Tests, analyse statique et outillage](ch12-tooling.md) y remédie.
