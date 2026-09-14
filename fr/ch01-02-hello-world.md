# Hello, World!

Faisons parler PHP.

Ouvrez votre éditeur, créez un fichier `hello.php` où vous voulez, et tapez-y ces lignes :

```php
<?php

echo "Hello, world!\n";
```

Enregistrez. Puis, dans le terminal, placez-vous dans le dossier du fichier et lancez :

```console
$ php hello.php
Hello, world!
```

Voilà un programme PHP complet. Il est court, mais **chaque caractère y a un rôle**. Démontons-le.

<img src="images/ch01-hello-anatomy.png" alt="Le programme hello.php avec chaque partie étiquetée : la balise d'ouverture, echo, la chaîne, le retour à la ligne et le point-virgule" width="560">

## `<?php`, la balise d'ouverture

PHP est né pour glisser de petits morceaux de logique dans des pages web. Cette origine a laissé une trace définitive : par défaut, un fichier PHP est du texte ordinaire, et **seul ce qui se trouve entre `<?php` et `?>` est considéré comme du code**. Tout le reste est recopié tel quel en sortie.

<img src="images/ch01-php-island.png" alt="Une page de texte brut avec une île de code PHP entre balises d'ouverture et de fermeture" width="480">

Dans un fichier qui ne contient que du code, comme le nôtre, on écrit la balise d'ouverture une fois, tout en haut, et rien d'autre. Deux habitudes en découlent.

- **Rien avant `<?php`.** Pas même une ligne vide : elle partirait en sortie avant que le programme ait commencé.
- **Pas de balise fermante en fin de fichier.** Omettre `?>` a l'air d'un oubli, mais c'est volontaire. Un espace ou un saut de ligne égaré après la balise fermante part lui aussi en sortie, et ce genre de caractère invisible produit des bugs exaspérants. Une balise jamais fermée ne laisse rien fuir.

## `echo`, la voix du programme

**`echo` affiche ce qui le suit.** C'est ainsi qu'un programme PHP parle. Vous vous en servirez tout le temps, et vous croiserez deux cousins en route : `print`, qui fait presque la même chose, et `printf`, pour quand le texte a besoin d'être mis en forme.

`echo` n'est pas une fonction, il n'a donc pas besoin de parenthèses. `echo("Hello")` marche aussi, PHP n'est pas regardant, mais la forme nue est celle que vous verrez partout.

## `"Hello, world!\n"`, le texte

Un texte entre guillemets s'appelle une **chaîne de caractères**. Celle-ci se termine par `\n`, et ce ne sont pas deux caractères affichés à l'écran : c'est l'ordre « passe à la ligne », comme si on appuyait sur Entrée. Sans lui, la prochaine chose affichée viendrait se coller juste après le point d'exclamation.

PHP connaît deux sortes de guillemets, et la différence compte. **Les guillemets doubles** demandent à PHP de regarder dans le texte et d'interpréter les séquences spéciales comme `\n`. **Les guillemets simples** lui demandent de ne toucher à rien : `'Hello, world!\n'` affiche une barre oblique inverse suivie d'un `n`.

> Les guillemets doubles regardent dans le texte. Les guillemets simples n'y touchent pas. Aucun n'est meilleur, vous choisirez entre les deux en permanence.

## `;`, le point final

**Chaque instruction PHP se termine par un point-virgule**, comme une phrase se termine par un point. Oubliez-en un, et PHP protestera, mais pas là où vous l'attendez. Essayez : retirez le point-virgule et ajoutez une deuxième ligne.

```php
<?php

echo "Hello, world!\n"
echo "Nice to meet you.\n";
```

```console
$ php hello.php
PHP Parse error:  syntax error, unexpected token "echo", expecting "," or ";" in hello.php on line 4
```

PHP accuse la ligne 4, qui n'a rien fait. Le point-virgule manque à la ligne 3 : PHP ne s'en est aperçu qu'en arrivant au mot suivant, quand plus rien n'avait de sens.

<img src="images/ch01-semicolon-detective.png" alt="Un détective pointe une ligne de code innocente tandis que le vrai coupable, un point-virgule manquant à la ligne du dessus, se cache juste derrière" width="420">

> [!TIP]
> Quand une erreur incompréhensible désigne une ligne qui a l'air correcte, **le vrai coupable est presque toujours juste au-dessus**.

## Lancer, relancer

`php hello.php` confie votre fichier à PHP, qui le lit de haut en bas et fait ce qu'il dit. Pas de compilation, pas de build, rien qui reste derrière.

<img src="images/ch01-edit-run-look.png" alt="La boucle en trois temps de la programmation PHP : modifier le fichier, le lancer, regarder le résultat, et on recommence" width="420">

> Modifier le fichier. Le lancer. Regarder le résultat. Modifier, lancer, regarder.

Cette boucle serrée est la plus grande différence de sensation entre PHP et un langage compilé, et ce livre en profite sans arrêt. **Quand vous vous demandez ce que fait un bout de code, le plus rapide est de le lancer.**

Pour un essai d'une ligne, PHP a aussi un mode interactif. Tapez `php -a` : vous obtenez une invite où chaque ligne s'exécute dès que vous appuyez sur Entrée.

```console
$ php -a
Interactive shell

php > echo "Hello, world!\n";
Hello, world!
php > exit
```

Pratique pour vérifier un détail. Ce n'est pas là qu'on construit de vrais programmes, mais ça ne l'est dans aucun langage.

Vous venez d'écrire, de lancer, de casser et de réparer un programme PHP. Tout le rythme du métier tient là, en miniature. Le [chapitre 2](ch02-00-guessing-game-tutorial.md) s'en sert pour construire un jeu.
