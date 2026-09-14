# Portée des variables et ramasse-miettes

## Chaque fonction a sa propre portée

Une variable créée dans une fonction vit dans cette fonction, et nulle part ailleurs :

```php
<?php
declare(strict_types=1);

function greet(): void
{
    $message = "Hello from inside greet()";
    echo $message . "\n";
}

greet();
echo $message ?? "no such variable out here\n";
```

Lancez-le. La seconde ligne affiche « no such variable out here » : le `$message` de `greet()` et n'importe quel `$message` qui traînerait dehors n'ont aucun lien, même s'ils portent le même nom. **Chaque fonction a son propre jeu de variables, invisible de l'extérieur.** C'est ce qu'on appelle la portée locale, et c'est le bon réglage par défaut. Sans elle, tous les noms de variables de toutes les fonctions se disputeraient un seul espace commun, et appeler une fonction que vous n'avez pas écrite serait un petit acte de foi : pourvu qu'elle n'ait pas écrasé l'une des vôtres en passant.

Imaginez chaque fonction comme une pièce avec ses propres étagères. Une boîte posée dans une pièce n'existe pas dans la pièce d'à côté.

<img src="images/ch04-scope-rooms.png" alt="Le script est une grande salle avec ses propres boîtes, et une fonction est une pièce fermée avec son étagère : la boîte $message dans la pièce est invisible depuis la salle, et seule une petite trappe marquée global permet à la pièce d'atteindre une boîte du dehors" width="600">

## `global`, et pourquoi vous y toucherez rarement

PHP a bien un moyen de laisser une fonction lire et écrire une variable du script principal : le mot-clé `global`.

```php
<?php
declare(strict_types=1);

$counter = 0;

function increment(): void
{
    global $counter;
    $counter++;
}

increment();
increment();
echo $counter; // 2
```

Ça marche. **Ce n'est presque jamais le bon outil.** Une fonction qui passe par `global` pour modifier un état qui vit hors de ses paramètres et de sa valeur de retour est une fonction que sa signature ne suffit pas à comprendre : il faut retrouver chaque `global $counter` du code pour savoir qui le modifie, et dans quel ordre. Invisible dans un exemple de cinq lignes, douloureux dans une application de cinq mille.

Préférez recevoir les valeurs en paramètres et rendre les résultats en valeur de retour, ou bien, à partir du [chapitre 5](ch05-00-classes.md), garder l'état partagé dans une propriété d'un objet que vous faites circuler volontairement. Si vous sentez l'attrait de `global`, c'est en général que la fonction réclame un paramètre.

## Les variables `static` dans les fonctions

Il existe une façon plus sage, pour une fonction, de se souvenir de quelque chose d'un appel à l'autre. Une variable locale ordinaire naît et disparaît à chaque exécution de la fonction. **Une variable locale `static` garde sa valeur d'un appel au suivant, et seule cette fonction peut la voir.**

```php
<?php
declare(strict_types=1);

function nextId(): int
{
    static $id = 0;
    $id++;
    return $id;
}

echo nextId(); // 1
echo nextId(); // 2
echo nextId(); // 3
```

`$id = 0` ne s'exécute qu'au tout premier appel de `nextId()` ; chaque appel suivant reprend là où le précédent s'est arrêté. Rien en dehors de `nextId()` ne peut lire ni remettre `$id` à zéro. Aucune fuite à la `global` ici, juste une fonction dotée d'une mémoire privée. C'est un motif pratique pour un petit compteur, un cache simple ou un drapeau « ai-je déjà fait cette initialisation », quand un objet entier serait disproportionné pour un seul nombre.

## Un mot bref et honnête sur le ramasse-miettes

Vous entendrez parler du « garbage collector » de PHP, en général à côté des mots « fuite mémoire » ou « script de longue durée ». Il est utile de savoir en gros de quoi il s'agit, même si vous y penserez rarement.

Chaque valeur que PHP crée, chaque tableau et chaque objet, porte un petit compteur : le nombre de variables qui pointent dessus en ce moment. **Quand ce compteur tombe à zéro, PHP libère la mémoire immédiatement.** La dernière variable est sortie de sa portée ou a été réaffectée, plus personne n'a besoin de la valeur, elle disparaît. Ce compteur est aussi ce qui fait fonctionner la copie à l'écriture, dans la [première section de ce chapitre](ch04-01-copy-on-write.md) : PHP sait toujours combien d'endroits partagent un tableau donné.

<img src="images/ch04-refcount-cycle.png" alt="À gauche, une boîte perd sa dernière étiquette, son compteur tombe à zéro et elle part à la poubelle. À droite, deux boîtes pointent l'une vers l'autre sans aucune étiquette : leurs compteurs n'atteignent jamais zéro, et un collecteur à part doit venir les ramasser" width="600">

Le comptage a un angle mort. Deux objets qui pointent l'un vers l'autre forment un cycle, et un cycle peut être oublié par le reste du programme alors que ses deux membres se tiennent encore. Leurs compteurs n'atteignent jamais zéro. PHP lance de temps en temps un collecteur de cycles séparé, qui repère ces cycles orphelins et les nettoie quand même.

**Vous ne gérez pas la mémoire en PHP.** Pas de `malloc`, pas de `free`, aucune comptabilité de qui possède quoi. Les valeurs disparaissent quand plus rien n'en a besoin, et PHP détermine ce « plus rien » pour vous, cycles compris. Ce n'est pas un manque par rapport aux langages qui vous font penser à la mémoire ; c'est tout l'intérêt. Gardez le vocabulaire sous le coude pour le jour rare où vous traquerez une mémoire qui enfle dans un script de longue durée, et le reste du temps, laissez-le faire son travail.
