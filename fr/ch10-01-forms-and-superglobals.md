# Recevoir des données avec les formulaires HTML et les superglobales

PHP n'a aucune syntaxe particulière pour dire « ce script est une page web ». Un script web est un script ordinaire. Ce qui change, c'est d'où viennent ses données : **avant même votre première ligne, PHP a déjà déballé la requête dans une poignée de tableaux**, et votre code les lit comme n'importe quel autre tableau. On les appelle superglobales parce qu'elles sont accessibles partout, y compris à l'intérieur des fonctions, sans mot-clé `global` et sans paramètre. Elles sont là, c'est tout.

## Un formulaire HTML tout simple

Commencez par le formulaire lui-même. Créez `guestbook.php` :

```html
<!DOCTYPE html>
<html>
<head>
    <title>Guestbook</title>
    <style>
        body { font-family: sans-serif; max-width: 40em; margin: 2em auto; }
        textarea { width: 100%; }
    </style>
</head>
<body>
    <h1>Guestbook</h1>

    <form method="post">
        <p><label>Name: <input type="text" name="name"></label></p>
        <p><label>Message: <textarea name="message"></textarea></label></p>
        <p><button type="submit">Sign the guestbook</button></p>
    </form>
</body>
</html>
```

Il n'y a pas encore une ligne de PHP. C'est un `<form>` avec `method="post"` et sans attribut `action`, donc l'envoyer déclenche une requête `POST` vers cette même URL. L'autre choix courant est `method="get"`, et la différence compte. **Une requête `GET` écrit ses données dans l'URL** (`?name=Alice`), visibles dans la barre d'adresse et dans les journaux du serveur : très bien pour un champ de recherche, mauvais pour tout ce qui est privé, et mauvais pour tout ce qui modifie des données. Une requête `POST` transporte ses données dans le corps de la requête, à l'abri des regards. Une entrée de livre d'or a sa place là.

<img src="images/ch10-get-vs-post.png" alt="Deux enveloppes côte à côte : sur l'enveloppe GET, les données sont écrites à l'extérieur, dans l'adresse, tandis que sur l'enveloppe POST, elles sont pliées à l'intérieur et seule l'adresse est visible" width="520">

Servez-le avec le serveur de développement intégré de PHP :

```console
$ php -S localhost:8000
```

Ouvrez `http://localhost:8000` : le formulaire s'affiche. Remplissez-le, envoyez-le, et il ne se passe rien. La même page se recharge, et ce que vous avez tapé a disparu. Lire ce qui a été envoyé, c'est le travail de PHP, et personne ne le lui a encore demandé.

## Les superglobales : `$_GET`, `$_POST`, `$_SERVER`

Trois d'entre elles comptent pour un script comme celui-ci. **`$_POST` contient les champs du formulaire envoyés dans le corps d'une requête `POST`**, sous forme de tableau associatif, une clé par nom de champ. `$_GET` contient les paramètres de la chaîne de requête, la partie de l'URL après le `?` ; il est rempli pour toute requête, mais par convention on le lit sur les requêtes `GET`. `$_SERVER` décrit la requête et le serveur lui-même, et une seule de ses entrées fait presque tout le travail ici : `$_SERVER['REQUEST_METHOD']`, qui vaut `'GET'` ou `'POST'`, permet à un seul script d'afficher un formulaire vide et de traiter un formulaire envoyé.

<img src="images/ch10-form-submission.png" alt="Un formulaire envoyé voyage sous forme de requête POST dont le corps contient name=Alice et message=Hello, et PHP le déballe dans le tableau $_POST avec une clé name et une clé message avant que le script démarre" width="600">

Il existe aussi `$_REQUEST`, qui fusionne `$_GET`, `$_POST` et les cookies en un seul tableau. C'est pratique, et il vaut mieux s'en passer : avec lui, votre script ne sait plus si une valeur est arrivée par l'URL ou par le corps de la requête, et cette distinction pèse plus qu'il n'y paraît dès que la sécurité entre en jeu, à la section suivante.

## Lire ce qui a été envoyé

Ajoutez du PHP en tête de `guestbook.php`, avant la ligne `<!DOCTYPE html>` :

```php
<?php

$name = '';
$message = '';
$submitted = false;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = $_POST['name'] ?? '';
    $message = $_POST['message'] ?? '';
    $submitted = true;
}
?>
```

Le `if`, c'est le script qui demande « un formulaire a-t-il été envoyé, ou quelqu'un regarde-t-il seulement ? ». L'opérateur de fusion null `??` (vu au [chapitre 3](ch03-02-data-types.md)) couvre le cas d'un champ absent : une requête forgée à la main ne doit pas provoquer un avertissement « undefined array key ». Plus bas dans le fichier, affichez le message quand il y en a un :

```php
<body>
    <h1>Guestbook</h1>

    <?php if ($submitted) { ?>
        <p>Thanks, <?= $name ?>. You wrote: <?= $message ?></p>
    <?php } ?>

    <form method="post">
```

`<?= $name ?>` est un raccourci pour `<?php echo $name ?>`, fait exactement pour ça : glisser une valeur au milieu du HTML. Rechargez, remplissez le formulaire, envoyez. La page vous salue avec exactement ce que vous avez tapé. Pour voir la requête elle-même, sans navigateur, essayez `curl` :

```console
$ curl -X POST -d "name=Alice&message=Hello there" http://localhost:8000/
```

La réponse contient `Thanks, Alice. You wrote: Hello there`. Même salutation, construite entièrement à partir de `$_POST`, et le navigateur s'est révélé facultatif. **Tout ce qui sait envoyer une requête HTTP peut remplir votre formulaire.**

> Un formulaire, c'est une requête avec des données dedans. PHP les déballe dans `$_POST` avant que votre code démarre.

## Le problème qu'on voit déjà venir

Ce `<?= ?>` imprime `$name` et `$message` tels quels dans la page, sans aucun filtre. Essayez : envoyez `<b>bold</b>` comme nom. La page affiche votre nom en gras, pas avec des chevrons. **Le livre d'or exécute pour l'instant n'importe quel HTML tapé par un visiteur, pas seulement le vôtre.** La section suivante referme cette brèche, avant que quoi que ce soit ne soit rangé quelque part pour de bon.
