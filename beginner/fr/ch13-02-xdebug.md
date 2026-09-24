# Déboguer pas à pas avec Xdebug

Imaginez appuyer sur pause dans votre programme, exactement sur la ligne qui vous intrigue, puis lire chaque variable telle qu'elle était à cet instant. C'est ce que Xdebug vous donne.

Xdebug n'est pas un programme à part, ni une fonction que vous appelez comme `var_dump()`. **C'est une extension PHP : une fois installée, elle change le comportement de PHP lui-même.** Cela demande un peu plus d'installation que la section précédente, en échange de la seule chose que l'affichage ne sait pas faire : regarder tout ce qui est à portée sans avoir deviné à l'avance quoi afficher.

## L'installer

Xdebug n'est pas livré avec PHP, il faut donc l'installer séparément. La méthode générique passe par PECL :

```console
$ pecl install xdebug
```

La plupart des gestionnaires de paquets le proposent aussi (`apt install php-xdebug` sur Debian et Ubuntu, `brew install php` puis `pecl install xdebug` sur macOS avec le PHP de Homebrew). Quelle que soit la voie choisie, il faut ensuite l'activer dans `php.ini` par une ligne qui ressemble à :

```ini
zend_extension=xdebug
```

Vérifiez qu'il est chargé :

```console
$ php -v
PHP 8.3.0 (cli) (built: ...)
    with Xdebug v3.3.0, Copyright (c) 2002-2024, by Derick Rethans
```

Si le nom de Xdebug apparaît là, il est actif.

## `xdebug.mode` : n'allumer que ce qu'il faut

Xdebug fait plusieurs choses sans rapport entre elles, et un seul réglage, `xdebug.mode`, dit lesquelles sont allumées. Il prend une liste séparée par des virgules dans `php.ini` :

```ini
xdebug.mode=develop,debug
```

`develop` mérite de rester allumé en permanence. Il ne demande aucun autre outil et améliore discrètement des sorties que vous produisez déjà : `var_dump()` affiche en couleur et indique le fichier et la ligne d'où il a été appelé, et une exception non rattrapée vient avec une trace complète, arguments compris, au lieu du format plus sec de PHP. **`debug` est le mode dont parle cette section : il permet à un outil extérieur de mettre l'exécution en pause et de l'inspecter.**

## Brancher un éditeur

Le débogage pas à pas fait dialoguer deux bouts. D'un côté, PHP exécute votre script. De l'autre, un éditeur attend que PHP lui dise « je suis en pause, viens voir ». PhpStorm et VS Code (avec l'extension « PHP Debug ») savent le faire d'office, par un protocole nommé DBGp, sur le port 9003 par défaut.

La mise en place a la même forme dans les deux éditeurs. Vous lui demandez d'écouter les connexions Xdebug. Vous cliquez dans la marge à côté d'une ligne de code, et un point rouge apparaît : un **point d'arrêt**, qui veut dire « pause ici ». Puis vous lancez le script, depuis le terminal avec `php your_script.php` ou en rechargeant une page servie par `php -S`, avec `xdebug.mode` contenant `debug`. **L'exécution s'arrête à l'instant où elle atteint cette ligne, avant de l'exécuter, et l'éditeur montre chaque variable à portée à ce point précis.**

<img src="images/ch13-breakpoint.png" alt="Un script figé sur un point d'arrêt : les lignes du dessus ont été exécutées, la ligne marquée pas encore, et un panneau à côté montre la valeur actuelle de chaque variable" width="560">

De là, vous avez trois façons d'avancer. Le pas **par-dessus** (step over) exécute la ligne et s'arrête à la suivante. Le pas **dedans** (step into) suit l'exécution à l'intérieur de la fonction appelée au lieu de l'exécuter d'un bloc. Le pas **dehors** (step out) termine la fonction en cours et s'arrête de retour chez l'appelant. Les variables se mettent à jour dans le panneau au fur et à mesure.

<img src="images/ch13-step-over-into-out.png" alt="Les trois mouvements d'un débogueur pas à pas : step over saute à la ligne suivante, step into descend dans l'appel de fonction, step out remonte chez l'appelant" width="560">

## Essai sur le livre d'or

Le code de validation du [chapitre 10](ch10-02-validation-and-xss.md) est un bon terrain d'entraînement : assez petit pour tenir dans la tête, avec une vraie branche qui vaut le coup d'œil.

```php
if ($name === '') {
    $errors[] = 'Name cannot be empty.';
} elseif (mb_strlen($name) > 60) {
    $errors[] = 'Name is too long.';
}
```

Posez un point d'arrêt sur la ligne `if ($name === '')`. Lancez le serveur intégré avec `xdebug.mode=debug`, mettez votre éditeur en écoute, et envoyez le formulaire du livre d'or en laissant le champ du nom vide. L'exécution s'arrête pile là. Le panneau des variables montre `$name` comme chaîne vide et `$errors` comme tableau vide, exactement tels qu'ils étaient à cet instant, avant qu'une seule ligne du bloc `if` ait tourné. Passez par-dessus, et regardez `$errors` recevoir sa première entrée.

> Aucun `var_dump()` n'a eu besoin d'être écrit, déplacé ou retiré pour voir tout ça. C'est toute la valeur du débogage pas à pas.

## Le profilage, en bref

`xdebug.mode=profile` allume une troisième capacité. Au lieu de mettre l'exécution en pause, Xdebug mesure la durée de chaque appel de fonction et écrit le résultat dans un fichier « cachegrind » (`xdebug.output_dir` dit où). Des outils comme QCachegrind, ou le profileur intégré à PhpStorm, lisent ce fichier et vous montrent exactement où une requête lente a passé son temps : quelle fonction, appelée combien de fois, pour quelle part du total. Traquer la lenteur est un autre métier que traquer une mauvaise réponse, plus proche de ce que le [chapitre 15](ch15-04-performance.md) raconte sur les boucles et les générateurs, mais c'est la même extension, et elle mérite d'être connue.

## Choisir entre les deux outils

Franchement, commencez par `var_dump()` et `print_r()`. Ils ne demandent aucune installation, et pour la plupart des bugs, surtout au début, afficher la valeur et la regarder trouve le problème en quelques secondes.

**Passez à Xdebug quand l'affichage cesse de resserrer l'étau** : quand un bug dépend d'une suite d'appels plutôt que d'une seule valeur, ou quand vous vous surprenez à ajouter et retirer un `var_dump()` pour la troisième fois sur le même problème. À ce stade, mettre le programme en pause et regarder autour coûte moins cher que deviner encore une fois.
