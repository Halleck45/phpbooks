# Structurer une petite application façon MVC

Deux routes, deux closures, un fichier : le routeur de la section précédente fonctionne. Ajoutez dix routes et il cesse d'être lisible, parce que ce que chaque route *fait* se mélange à la façon dont elle a été *trouvée*. Les vraies applications séparent les deux. Le découpage classique s'appelle **Modèle, Vue, Contrôleur**, MVC pour faire court, et même à notre échelle sa forme vaut la peine : **un contrôleur décide de ce qui doit se passer pour une requête, et une vue décide de la façon dont le résultat devient du HTML.** Pas de modèle pour l'instant, faute de données à conserver. Deux ou trois routes suffisent pour voir le motif.

## Les contrôleurs

Un contrôleur, à cette taille, est une classe dont chaque méthode prend en charge une route et renvoie le corps de la réponse sous forme de chaîne de caractères :

```php
<?php

class HomeController
{
    public function index(): string
    {
        return render('home', ['title' => 'Welcome']);
    }
}

class AboutController
{
    public function show(): string
    {
        return render('about', [
            'title' => 'About',
            'description' => 'A tiny PHP application, built without a framework.',
        ]);
    }
}
```

Regardez ce qui manque. Rien ici ne lit `$_SERVER`, rien ne sait par quelle URI on est arrivé. C'est l'affaire du routeur. **Une méthode de contrôleur n'a qu'un travail : produire une réponse.** Elle reste facile à lire, et facile à tester : appelez `(new HomeController())->index()` et regardez la chaîne qui revient.

## Les vues : le premier talent de PHP

`render()` est l'endroit où vit la couche des vues, et elle s'appuie sur quelque chose que PHP sait faire depuis le premier jour. **Sous le langage de programmation, PHP est un langage de templates.** C'était sa raison d'être à l'origine, avant qu'il ne grandisse dans toutes les directions. Une vue est un fichier ordinaire avec du HTML dedans et de petits îlots de PHP pour les parties mobiles, le même style `<?php ... ?>`-dans-du-HTML que les toutes premières pages de ce livre.

Créez `views/home.php`. À la différence des autres exemples du livre, celui-ci est un fichier HTML avec des îlots de PHP, pas un fichier PHP à part entière, donc il ne commence pas par `<?php` :

```html
<!DOCTYPE html>
<html>
<head><title><?= htmlspecialchars($title) ?></title></head>
<body>
    <h1><?= htmlspecialchars($title) ?></h1>
    <p>This page was rendered from views/home.php.</p>
</body>
</html>
```

Et une petite fonction qui inclut un fichier de vue en lui rendant des données accessibles :

```php
<?php

function render(string $view, array $data = []): string
{
    extract($data);
    ob_start();
    include __DIR__ . "/views/{$view}.php";
    return ob_get_clean();
}
```

Quatre lignes, chacune avec son rôle. **`extract()` transforme chaque clé de `$data` en variable locale** : `'title' => 'Welcome'` devient `$title`, visible dans le fichier inclus. **`ob_start()` et `ob_get_clean()`, c'est la mise en tampon de la sortie.** Sans elles, le HTML du fichier inclus partirait directement vers le navigateur. Avec elles, il est capturé dans un tampon et rendu sous forme de chaîne, que le contrôleur peut retourner comme n'importe quelle autre valeur.

<img src="images/ch21-output-buffer.png" alt="Sans mise en tampon, le HTML d'une vue coule directement vers le navigateur ; avec ob_start(), un seau le recueille et le rend au contrôleur sous forme de chaîne" width="600">

De retour dans la vue, `<?= ... ?>` est le raccourci de `<?php echo ... ?>`, et `$title` passe par `htmlspecialchars()` avant d'être affiché. C'est cet appel, et lui seul, qui empêche un texte venu d'un utilisateur d'être interprété comme du HTML. Faites-en un réflexe.

## Relier le routeur aux contrôleurs

Modifiez `router.php` pour qu'il aiguille vers des méthodes de contrôleurs au lieu de closures :

```php
<?php

require __DIR__ . '/render.php';
require __DIR__ . '/controllers.php';

$uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

$routes = [
    '/' => [HomeController::class, 'index'],
    '/about' => [AboutController::class, 'show'],
];

if (isset($routes[$uri])) {
    [$class, $method] = $routes[$uri];
    echo (new $class())->{$method}();
} else {
    http_response_code(404);
    echo "404 Not Found: {$uri}";
}
```

`$routes` associe maintenant chaque chemin à une paire `[classe, méthode]` plutôt qu'à une closure. La paire est déstructurée sur place avec `[$class, $method] = $routes[$uri]`, la syntaxe du [chapitre 19](ch19-02-destructuring.md) ; `new $class()` construit le contrôleur, et `->{$method}()` appelle la méthode dessus.

Suivez une requête d'un bout à l'autre.

<img src="images/ch21-request-path.png" alt="L'aller-retour d'une requête : le navigateur demande un chemin, le routeur trouve le contrôleur et la méthode dans sa table, le contrôleur appelle render(), qui remplit la vue et capture son HTML, et le HTML repart vers le navigateur" width="620">

Le navigateur demande `/`. Le routeur trouve `HomeController` et `index` dans sa table, construit le contrôleur, appelle la méthode. La méthode appelle `render('home', ...)`, qui inclut `views/home.php` en capturant sa sortie et renvoie le HTML sous forme de chaîne. La chaîne repart vers le routeur, qui l'affiche. Réponse envoyée.

**Cet aller-retour, c'est ce sur quoi repose le routeur de tous les frameworks** : regarder la requête, trouver la classe et la méthode qui en ont la charge, les appeler, renvoyer ce qu'elles donnent. La mécanique est petite, et c'est toute l'idée.

Essayez : `/about` a un contrôleur mais pas de vue. Écrivez `views/about.php` sur le modèle de `home.php`, avec `$description` dedans, et demandez `/about` à `curl`.
