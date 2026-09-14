# Programmer un jeu de devinette

Construisons un jeu.

Les règles tiennent en une phrase. **L'ordinateur choisit en secret un nombre entre 1 et 100. Vous proposez un nombre. Il répond « trop petit » ou « trop grand », et vous recommencez jusqu'à tomber juste.**

<img src="images/ch02-game-rules.png" alt="Les règles du jeu en trois cases : l'ordinateur pense à un nombre, le joueur propose, l'ordinateur répond trop petit ou trop grand" width="600">

Si petit soit-il, ce jeu contient presque tout ce dont les vrais programmes sont faits : une entrée, une sortie, une décision, une boucle, et un peu de nettoyage de ce que l'utilisateur a tapé. C'est pour cela qu'il passe avant la théorie.

**Vous allez croiser des mots que vous ne comprendrez pas encore tout à fait. C'est normal, c'est même le but.** Vous voyez d'abord PHP en action, et le [chapitre 3](ch03-00-common-programming-concepts.md) reviendra expliquer chaque pièce posément.

## Le jeu en un dessin

Avant de taper quoi que ce soit, voici le programme entier en un dessin. Chaque boîte deviendra quelques lignes de PHP.

<img src="images/ch02-flowchart.png" alt="Organigramme du jeu : choisir un nombre secret, demander une proposition, la lire, vérifier que c'est un nombre, la comparer au secret, répondre trop petit, trop grand ou gagné, et recommencer jusqu'à la victoire" width="520">

Lisez-le une fois, de haut en bas. Choisir un secret. Demander. Lire la réponse. Est-ce bien un nombre ? Sinon, redemander. Comparer au secret. Trop petit, trop grand, ou trouvé. Trouvé ? On s'arrête.

> Choisir un secret. Demander. Lire. Vérifier. Comparer. Répondre. Recommencer. C'est tout le plan.

Construisons-le maintenant, une boîte à la fois.

## Étape 1 : demander au joueur

Créez un fichier `guessing_game.php` :

```php
<?php

echo "Guess the number!\n";
echo "Please input your guess.\n";

$guess = trim(fgets(STDIN));

echo "You guessed: {$guess}\n";
```

Lancez-le, tapez un nombre, Entrée :

```console
$ php guessing_game.php
Guess the number!
Please input your guess.
42
You guessed: 42
```

Les deux premières lignes, vous les connaissez : `echo` affiche du texte. La ligne intéressante est celle du milieu, qui fait trois choses d'un coup. Lisons-la de l'intérieur vers l'extérieur.

**`fgets(STDIN)` attend que le joueur tape une ligne et appuie sur Entrée, puis remet cette ligne au programme.** `STDIN` est le nom du canal par lequel arrive ce que vous tapez au clavier, le même que lisent tous les outils en ligne de commande.

<img src="images/ch02-stdin-trim.png" alt="La saisie au clavier voyage par le canal STDIN jusqu'au programme sous la forme du texte 42 suivi d'un caractère de saut de ligne, que trim() coupe" width="600">

Il y a un piège : la ligne reçue contient aussi la touche Entrée, sous la forme d'un caractère de saut de ligne invisible, tout au bout. On n'en veut presque jamais, alors **`trim()` le coupe**. `trim()` retire les espaces et les sauts de ligne aux deux bouts d'un texte, et l'enrouler autour de `fgets(STDIN)` est un duo si courant que vos doigts le taperont bientôt tout seuls.

Enfin, `$guess = ...` range le résultat. **`$guess` est une variable : une boîte étiquetée dans laquelle le programme garde une valeur pour plus tard.** En PHP, tous les noms de variables commencent par `$`. Rien à déclarer, aucun type à annoncer : vous mettez quelque chose dans la boîte, et la boîte existe.

<img src="images/ch02-variable-box.png" alt="Une boîte étiquetée $guess avec le texte 42 à l'intérieur" width="300">

> Une variable, c'est une boîte avec une étiquette. Mettez-y quelque chose, et la boîte existe.

La dernière ligne montre au joueur ce que contient la boîte. Entre guillemets doubles, `{$guess}` est remplacé par la valeur de la variable. Les accolades sont facultatives pour un nom simple comme celui-là, mais elles montrent sans ambiguïté où le nom s'arrête, et cette clarté rendra service plus tard, avec des expressions plus longues.

## Étape 2 : choisir le nombre secret

L'ordinateur a besoin d'un nombre à cacher. PHP a une fonction faite pour ça :

```php
<?php

$secretNumber = random_int(1, 100);

echo "Guess the number!\n";
echo "The secret number is between 1 and 100.\n";
echo "Please input your guess.\n";

$guess = trim(fgets(STDIN));

echo "You guessed: {$guess}\n";
```

**`random_int(1, 100)` renvoie un nombre entier tiré au hasard entre 1 et 100**, bornes comprises, et nous le rangeons dans une deuxième boîte, `$secretNumber`.

> [!TIP]
> `random_int()` est un générateur aléatoire de haute qualité, bien plus qu'il n'en faut pour un jeu. Mais c'est aussi celui qu'il faut choisir chaque fois que vous avez besoin de hasard en PHP, autant prendre la bonne habitude tout de suite.

Lancez le programme plusieurs fois. Le secret change à chaque fois, mais rien ne vous permet encore de le voir : personne ne le compare à votre proposition. Réglons ça.

## Étape 3 : comparer

```php
<?php

$secretNumber = random_int(1, 100);

echo "Guess the number!\n";
echo "Please input your guess.\n";

$guess = (int) trim(fgets(STDIN));

if ($guess < $secretNumber) {
    echo "Too small!\n";
} elseif ($guess > $secretNumber) {
    echo "Too big!\n";
} else {
    echo "You win!\n";
}
```

**Le bloc `if`, c'est la décision du dessin.** PHP teste la première condition : la proposition est-elle plus petite que le secret ? Si oui, il affiche « Too small! » et ignore le reste. Sinon, il teste la deuxième. Si aucune des deux n'est vraie, la proposition n'est ni plus petite ni plus grande, donc elle est égale, et c'est la branche `else` qui s'exécute. Un seul des trois messages s'affiche, jamais deux.

Il y a un second changement, petit et facile à rater : `(int)` devant `trim(fgets(STDIN))`.

<img src="images/ch02-string-vs-int.png" alt="Le texte 42, dessiné comme deux caractères séparés entre guillemets, à côté du nombre 42, avec (int) comme flèche qui convertit l'un en l'autre" width="480">

**Tout ce qui vient du clavier arrive sous forme de texte.** Quand le joueur tape 42, le programme reçoit les deux caractères « 4 » et « 2 », pas le nombre quarante-deux. PHP accepte souvent de comparer du texte à des nombres, et il devine généralement juste, mais « généralement » n'est pas un mot qu'on veut voir dans une comparaison. **`(int)` convertit le texte en vrai entier**, explicitement, de sorte que les deux côtés du `<` sont des nombres et qu'il ne reste rien à deviner.

> « 42 », c'est du texte. 42, c'est un nombre. `(int)` transforme le premier en second, et le dit clairement.

Le [chapitre 3](ch03-00-common-programming-concepts.md) reviendra sur cette idée, qu'on appelle le jonglage de types, et sur les bonnes raisons d'être explicite.

## Étape 4 : recommencer

Pour l'instant, la partie s'arrête après une seule proposition, gagnée ou perdue. Sur le dessin, une flèche remonte. En PHP, cette flèche s'appelle une boucle :

```php
<?php

$secretNumber = random_int(1, 100);

echo "Guess the number!\n";

while (true) {
    echo "Please input your guess.\n";
    $guess = (int) trim(fgets(STDIN));

    if ($guess < $secretNumber) {
        echo "Too small!\n";
    } elseif ($guess > $secretNumber) {
        echo "Too big!\n";
    } else {
        echo "You win!\n";
        break;
    }
}
```

**`while (true)` signifie « répète ce bloc indéfiniment ».** Ça paraît dangereux, et ça le serait sans porte de sortie. **La sortie, c'est `break`** : dès que PHP l'exécute, il quitte la boucle et reprend après l'accolade fermante. Nous plaçons `break` uniquement dans la branche gagnante, donc la boucle redemande jusqu'à ce que le joueur trouve, puis s'arrête.

<img src="images/ch02-loop-track.png" alt="Une piste de course dessinée en boucle, avec une porte marquée break qui mène dehors et un raccourci marqué continue qui ramène à la ligne de départ" width="520">

## Étape 5 : encaisser n'importe quoi

Il reste une aspérité. Tapez `banana` à la place d'un nombre, et `(int) "banana"` devient `0` sans un mot. Pas d'erreur, pas d'avertissement, juste une mauvaise proposition qui compte comme les autres. Vérifions l'entrée avant de lui faire confiance :

```php
<?php

$secretNumber = random_int(1, 100);

echo "Guess the number!\n";

while (true) {
    echo "Please input your guess.\n";
    $input = trim(fgets(STDIN));

    if (!is_numeric($input)) {
        echo "That doesn't look like a number, try again.\n";
        continue;
    }

    $guess = (int) $input;

    if ($guess < $secretNumber) {
        echo "Too small!\n";
    } elseif ($guess > $secretNumber) {
        echo "Too big!\n";
    } else {
        echo "You win!\n";
        break;
    }
}
```

**`is_numeric()` répond par oui ou par non à une question : ce texte ressemble-t-il à un nombre ?** Le `!` devant inverse la réponse, si bien que le `if` se lit « si l'entrée n'est pas un nombre ». Dans ce cas, on affiche un message aimable et on passe par `continue`.

**`continue`, c'est l'autre porte du dessin.** Là où `break` sort de la boucle, `continue` saute directement au début pour un nouveau tour, en ignorant tout ce qui se trouve en dessous. Une faute de frappe ne coûte rien au joueur : le jeu redemande, c'est tout.

> `break` sort de la boucle. `continue` lance le tour suivant.

## À vous de jouer

Lancez le jeu et gagnez-le. Puis revenez au dessin : chaque boîte est maintenant dans votre fichier. Choisir le secret, demander, lire, vérifier, comparer, répondre, recommencer.

Trente lignes, et le programme sait déjà :

- **lire ce qu'on tape** au clavier, avec `fgets()` et `trim()`,
- **prendre des décisions**, avec `if`, `elseif` et `else`,
- **se répéter**, avec `while`, `break` et `continue`,
- **transformer du texte en nombre**, avec `(int)`,
- **refuser poliment n'importe quoi**, avec `is_numeric()`.

Gardez ce fichier. Vous retrouverez sa silhouette dans tous les programmes que vous écrirez, et au [chapitre 14](ch14-00-a-cli-project.md), vous construirez des outils en ligne de commande nettement plus sérieux qu'un jeu de devinette.
