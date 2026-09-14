# Valider les entrées et prévenir le cross-site scripting

Envoyez `<script>alert('hello from your own guestbook')</script>` comme message. Le navigateur l'exécute. Un livre d'or qui imprime les valeurs de `$_POST` directement dans le HTML laisse n'importe quel visiteur poser n'importe quel balisage sur la page, et le balisage inclut les scripts. **C'est le cross-site scripting, XSS pour faire court : un attaquant fait tourner son propre JavaScript dans votre page, dans le navigateur de vos visiteurs, avec la confiance de votre site derrière lui.** Un livre d'or qui enregistre des messages et les montre à tout le monde est le cas d'école, ce qui en fait le bon endroit pour apprendre à s'en protéger.

## Échapper la sortie

Le remède n'est pas d'interdire les chevrons. C'est de s'assurer que tout texte venu d'un utilisateur est *échappé* avant d'atterrir dans le HTML, pour que le navigateur l'affiche comme du texte au lieu de le lire comme du balisage. L'outil de PHP pour ça s'appelle `htmlspecialchars()`. Il convertit les quelques caractères qui intéressent un analyseur HTML (`<`, `>`, `&` et les guillemets) en leurs entités (`&lt;`, `&gt;`, `&amp;` et ainsi de suite), que le navigateur affiche comme les caractères d'origine sans agir dessus :

```php
<?php if ($submitted) { ?>
    <p>Thanks, <?= htmlspecialchars($name) ?>. You wrote: <?= htmlspecialchars($message) ?></p>
<?php } ?>
```

<img src="images/ch10-escaping.png" alt="Avant et après échappement : le texte <b>hi</b> imprimé brut est rendu en gras par le navigateur, tandis que le même texte passé par htmlspecialchars() devient &lt;b&gt;hi&lt;/b&gt; et s'affiche comme les caractères eux-mêmes" width="600">

Renvoyez le message `<script>`. La page affiche maintenant le texte littéral `<script>alert('hello from your own guestbook')</script>`, et rien ne s'exécute. Depuis PHP 8.1, `htmlspecialchars()` échappe par défaut les guillemets en plus des chevrons, ce qu'on veut presque à chaque fois.

La règle tient en une phrase. **Toute valeur venue de l'extérieur de votre script, imprimée n'importe où dans du HTML, passe d'abord par `htmlspecialchars()`.** Pas d'exception pour les valeurs « probablement » inoffensives : un champ nom a l'air anodin jusqu'au jour où quelqu'un y glisse une balise `<script>`.

> Échappez à la sortie. Chaque valeur, à chaque fois.

## Valider avant de faire confiance aux données

L'échappement protège la sortie. La validation est une autre question : cette entrée est-elle seulement acceptable ? Un nom de deux mille caractères, ou un message fait uniquement d'espaces, n'est pas dangereux, juste faux, et le script doit le dire avant d'en faire quoi que ce soit. Étendez le traitement du formulaire pour repérer les problèmes et les collecter :

```php
<?php

$name = '';
$message = '';
$submitted = false;
$errors = [];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name'] ?? '');
    $message = trim($_POST['message'] ?? '');
    $submitted = true;

    if ($name === '') {
        $errors[] = 'Name cannot be empty.';
    } elseif (mb_strlen($name) > 60) {
        $errors[] = 'Name is too long.';
    }

    if ($message === '') {
        $errors[] = 'Message cannot be empty.';
    } elseif (mb_strlen($message) > 500) {
        $errors[] = 'Message is too long.';
    }
}
?>
```

`trim()` retire les espaces aux deux bouts, si bien qu'un message fait uniquement d'espaces ne passe pas le test du vide. `mb_strlen()` plutôt que `strlen()` compte des caractères et non des octets, ce qui compte dès qu'un nom contient autre chose que de l'ASCII pur, la même question d'UTF-8 que le [chapitre 8](ch08-02-strings.md) a traitée pour les chaînes en général. Et les erreurs s'accumulent dans un tableau au lieu d'arrêter tout à la première, pour que le visiteur voie tous les problèmes d'un coup plutôt que de les découvrir un envoi après l'autre.

<img src="images/ch10-validate-escape.png" alt="Un script PHP dessiné comme une maison à deux portes : à l'entrée, la validation contrôle les données qui arrivent et refoule les mauvaises ; à la sortie, l'échappement emballe chaque valeur avant qu'elle ne parte vers le navigateur" width="600">

Affichez les erreurs, et remettez les valeurs envoyées dans le formulaire (échappées, comme toujours), pour que personne n'ait à retaper un long message parce que son nom était trop court :

```php
<?php if ($errors) { ?>
    <ul>
        <?php foreach ($errors as $error) { ?>
            <li><?= htmlspecialchars($error) ?></li>
        <?php } ?>
    </ul>
<?php } elseif ($submitted) { ?>
    <p>Thanks, <?= htmlspecialchars($name) ?>. You wrote: <?= htmlspecialchars($message) ?></p>
<?php } ?>

<form method="post">
    <p><label>Name: <input type="text" name="name" value="<?= htmlspecialchars($name) ?>"></label></p>
    <p><label>Message: <textarea name="message"><?= htmlspecialchars($message) ?></textarea></label></p>
    <p><button type="submit">Sign the guestbook</button></p>
</form>
```

Regardez `value="<?= htmlspecialchars($name) ?>"` dans la balise `<input>`. **L'échappement compte autant à l'intérieur d'un attribut HTML que dans le corps de la page** : un `"` non échappé dans la valeur permettrait à un visiteur de fermer l'attribut avant l'heure et d'écrire le sien.

## Un risque voisin qu'il faut nommer

Le XSS, c'est le navigateur d'un visiteur qui exécute le script d'un attaquant dans votre page. Son cousin s'appelle **CSRF**, cross-site request forgery : un autre site pousse le navigateur d'un visiteur à envoyer un formulaire à *votre* site en son nom, avec la session dans laquelle il est déjà connecté. La parade habituelle, un jeton caché généré par formulaire et vérifié à l'envoi, dépasse ce dont ce petit livre d'or a besoin. Gardez le nom en mémoire pour le jour où vous construirez quelque chose où un envoi forgé coûterait vraiment.

Le livre d'or se tient bien, le temps d'une requête : il valide ce qui entre et échappe ce qui sort. Ce qu'il ne sait toujours pas faire, c'est se souvenir. Rechargez la page et chaque message disparaît, parce que rien n'a jamais été rangé nulle part. C'est la suite.
