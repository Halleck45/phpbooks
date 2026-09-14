# Variables, constantes et mutabilité

Dans le jeu de devinette, `$guess` contenait un nombre différent à chaque tour de boucle, tandis que `$secretNumber` gardait le même du début à la fin. Même syntaxe, deux rôles différents. PHP vous donne un moyen de dire lequel des deux vous voulez.

## Les variables

**Une variable PHP commence par un signe dollar, et c'est à peu près toute la syntaxe à connaître :**

```php
<?php

$greeting = "Hello";
echo $greeting;

$greeting = "Goodbye";
echo $greeting;
```

Pas de `let`, pas d'étape de déclaration à oublier. (Il existe bien un mot-clé `var`, un fossile de PHP 4 qui n'a de sens qu'à l'intérieur d'une classe. Vous ne l'utiliserez pas.) Vous affectez, et à partir de cette ligne la variable existe, exactement comme `$guess` dans le jeu : aucune annonce, juste une boîte et une valeur dedans.

La seconde affectation change ce que contient la boîte, sans permission particulière. **Toute variable PHP est mutable par défaut.** Réaffecter, c'est affecter, une fois de plus. Si vous venez d'un langage où la mutabilité se demande explicitement, c'est le défaut inverse : pour PHP, changer une valeur est le cas normal, et l'immutabilité est quelque chose que l'on construit exprès, en général avec des objets.

Essayez : dans le jeu, ajoutez `$secretNumber = 42;` juste sous la ligne du `random_int()`. Rien ne proteste, et vous voilà propriétaire d'un jeu que vous gagnez du premier coup.

## Le nommage

Les noms de variables distinguent les majuscules des minuscules : `$guess` et `$Guess` sont deux boîtes différentes. Un nom commence par une lettre ou un tiret bas, et par convention il s'écrit en `camelCase` :

```php
<?php

$userName = "damien";
$total_price = 42.50; // valid, but not idiomatic PHP
```

Les deux lignes fonctionnent. Seule la première ressemble à ce que vous verrez dans le PHP moderne et dans la norme de codage que suivent la plupart des projets, PSR-12. **L'écosystème PHP tient plus à la cohérence à l'intérieur d'une base de code qu'à la supériorité d'un style sur un autre**, mais le `camelCase` pour les variables est ce qui se rapproche le plus d'une convention universelle en PHP.

## Les constantes

`$secretNumber` n'a jamais changé pendant une partie, mais rien ne l'en empêchait : une affectation égarée dans la boucle, et le jeu se cassait sans un mot. Pour une valeur qui ne doit pas changer pendant l'exécution (un réglage de configuration, une constante mathématique, l'URL de base d'une API), PHP a mieux qu'une variable que vous promettez de ne pas toucher :

```php
<?php

define('MAX_RETRIES', 3);
echo MAX_RETRIES;

const APP_NAME = 'GuessingGame';
echo APP_NAME;
```

<img src="images/ch03-variable-vs-constant.png" alt="Une boîte en carton avec une étiquette en papier qu'on peut décoller et remplacer, à côté d'une pierre où un nom est gravé : la variable peut changer, la constante non" width="520">

**Une constante n'a pas de `$`, et c'est voulu.** N'importe où dans un fichier, vous voyez d'un coup d'œil que `MAX_RETRIES` ne changera pas dans votre dos, alors que `$maxRetries` est à la merci de quiconque passe après vous.

Deux façons d'en écrire une, toutes deux courantes. `define()` est un appel de fonction, évalué pendant l'exécution, et fonctionne partout. `const` est une construction du langage, résolue avant l'exécution, et (c'est là que les gens trébuchent) elle n'est autorisée qu'au niveau supérieur d'un fichier ou dans une classe, jamais dans un bloc `if` ni dans le corps d'une fonction. Hors d'une classe, préférez `const` : c'est légèrement plus rapide et ça se lit comme ce que c'est.

> Une variable est une boîte dont on peut décoller l'étiquette. Une constante est un nom gravé dans la pierre.

## La mutabilité, et ce que PHP en fait vraiment

Si vous avez lu des choses sur des langages qui font grand cas de la propriété ou de l'emprunt des données, vous vous attendez peut-être à une histoire plus compliquée que « affectez, c'est tout ». À ce niveau, ce n'est pas le cas. PHP a bien sa propre idée, beaucoup plus douce, de qui possède une donnée, et elle apparaît dès que vous passez des tableaux et des objets à des fonctions au lieu d'afficher des chaînes. C'est le sujet du [chapitre 4](ch04-00-variables-and-references.md).
