# Attributs

« Cette méthode est un test. » « Cette propriété correspond à une colonne en base. » « Cette route répond à `GET /users`. » Pendant des années, PHP n'a eu qu'un seul endroit pour ce genre de note : un commentaire au format spécial, un docblock, qu'un framework analysait à l'exécution avec une expression régulière. Ça marchait, et ça restait un peu inconfortable. Le langage ne lisait pas le commentaire, ne le vérifiait pas, et une faute de frappe dedans échouait sans un bruit.

**PHP 8 a fait entrer la note dans le langage : un attribut, écrit `#[QuelqueChoseCommeCeci]` juste au-dessus de ce qu'il décrit.**

## Définir et attacher un attribut

Un attribut est une classe ordinaire. Ce qui en fait un attribut, c'est le marqueur `#[Attribute]` de PHP posé au-dessus :

```php
<?php

#[Attribute]
class Route
{
    public function __construct(
        public readonly string $method,
        public readonly string $path,
    ) {
    }
}
```

Une fois défini, accrochez-le à une méthode avec la syntaxe `#[...]` :

```php
<?php

class UserController
{
    #[Route(method: 'GET', path: '/users')]
    public function index(): string
    {
        return 'List of users';
    }

    #[Route(method: 'POST', path: '/users')]
    public function store(): string
    {
        return 'User created';
    }
}
```

Lancez ce fichier et il ne se passe rien. **`#[Route(...)]` n'appelle rien par lui-même.** C'est une métadonnée inerte, une étiquette pendue à la méthode, qui attend que quelqu'un vienne la lire.

<img src="images/ch20-attribute-tag.png" alt="Une méthode dessinée comme une boîte à laquelle pend une étiquette de bagage marquée Route ; une loupe étiquetée Reflection lit l'étiquette et une flèche mène à une ligne de table de routage, GET /users vers index" width="600">

## Relire les attributs avec la Reflection

Ce quelqu'un, c'est la Reflection, vue plus tôt dans ce chapitre. **`ReflectionMethod`, comme `ReflectionClass` et `ReflectionProperty`, liste les attributs attachés à ce qu'elle reflète, et construit l'objet attribut à la demande.**

```php
<?php

$reflection = new ReflectionClass(UserController::class);

foreach ($reflection->getMethods() as $method) {
    foreach ($method->getAttributes(Route::class) as $attribute) {
        $route = $attribute->newInstance();
        echo "{$route->method} {$route->path} -> {$method->getName()}()\n";
    }
}
```

```console
$ php routes.php
GET /users -> index()
POST /users -> store()
```

`getAttributes(Route::class)` trouve chaque attribut `Route` posé sur une méthode. `newInstance()` le construit, en exécutant le constructeur avec les arguments que vous avez écrits dans `#[Route(...)]`, et rend un vrai objet `Route` avec ses propriétés `method` et `path`. C'est ainsi que se construisent les systèmes de routage simples : parcourir les méthodes d'un contrôleur, relever leurs attributs `Route`, remplir une table de routage avec ce qu'on trouve. Aucun fichier de configuration à part à maintenir en cohérence.

> Un attribut est un objet ordinaire, garé à côté de votre code, que la Reflection peut venir ramasser.

## Où vous l'avez déjà vu

Si vous avez lu le [chapitre 12](ch12-00-testing.md), ce motif vous est familier. Le `#[Test]` de PHPUnit marque une méthode comme cas de test de la même façon que `#[Route]` en marque une ici comme gestionnaire : une classe ordinaire, relue par la Reflection, qui pilote un vrai comportement. Les frameworks s'appuient sur les attributs en permanence. Symfony s'en sert pour les routes et la configuration de l'injection de dépendances, Doctrine pour associer des propriétés à des colonnes en base, PHPUnit pour les métadonnées de test en tout genre.

Vous n'écrirez peut-être pas beaucoup d'attributs à vous. Vous lirez `#[...]` au-dessus de méthodes et de classes tous les jours dans du PHP moderne, et vous savez maintenant exactement ce qui se passe quand vous en voyez un : un objet ordinaire, qui attend d'être relu par la Reflection.
