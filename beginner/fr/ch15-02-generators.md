# Traiter une série d'éléments avec les générateurs

Toutes les fonctions que vous avez écrites jusqu'ici pour rendre une série de valeurs l'ont fait de la même manière : construire un tableau, le remplir, le `return`. Ça marche jusqu'au jour où la série devient si grosse qu'il n'est plus raisonnable de tout construire avant que quiconque ait vu le premier élément. **Un générateur est une fonction qui produit ses valeurs une par une, à la demande, au lieu de toutes d'un coup.**

## La méthode du tableau, et sa limite

Voici une fonction ordinaire qui renvoie les `$max` premiers carrés :

```php
<?php
declare(strict_types=1);

function squaresUpTo(int $max): array
{
    $result = [];
    for ($i = 1; $i <= $max; $i++) {
        $result[] = $i * $i;
    }
    return $result;
}

foreach (squaresUpTo(5) as $square) {
    echo $square . "\n";
}
```

Pour cinq carrés, personne ne s'inquiète que `squaresUpTo()` construise le tableau entier avant que le `foreach` voie une seule valeur. Pour cinq millions, ce sont cinq millions d'entiers en mémoire avant le moindre affichage. Et si vous ne voulez regarder que les trois premiers, vous payez les cinq millions quand même.

## La même fonction, réécrite avec `yield`

Remplacez `return` par `yield`, et changez le type de retour en `Generator` :

```php
<?php
declare(strict_types=1);

function squaresUpTo(int $max): Generator
{
    for ($i = 1; $i <= $max; $i++) {
        yield $i * $i;
    }
}

foreach (squaresUpTo(5) as $square) {
    echo $square . "\n";
}
```

Le code appelant n'a pas bougé d'un caractère : `foreach` ne sait pas, et ne cherche pas à savoir, s'il parcourt un tableau ou un générateur. Ce qui a changé, c'est *le moment* où le travail se fait. **Une fonction qui contient `yield` n'exécute pas son corps quand vous l'appelez.** `squaresUpTo(5)` renvoie immédiatement un objet `Generator`, sans rien de calculé dedans. La boucle avance ensuite d'un tour à la fois, quand `foreach` demande la valeur suivante, et il n'existe jamais qu'un seul carré à la fois.

<img src="images/ch15-array-vs-generator.png" alt="Un boulanger qui tend un plateau entier de pains d'un coup, comparé au même boulanger qui tend un pain à la fois pendant que le client demande le suivant" width="600">

Imaginez une boulangerie. La fonction à tableau cuit tous les pains, les empile sur un plateau et vous tend le plateau. Le générateur vous tend un pain, attend que vous reveniez en chercher un autre, puis cuit le suivant.

## Regarder la paresse à l'œuvre

« S'exécute paresseusement », on hoche la tête en le lisant, et on y croit bien mieux quand on le voit :

```php
<?php
function countUp(): Generator
{
    echo "starting\n";
    for ($i = 1; $i <= 3; $i++) {
        echo "about to yield {$i}\n";
        yield $i;
        echo "resumed after {$i}\n";
    }
}

$gen = countUp();
echo "generator created, nothing has run yet\n";

foreach ($gen as $value) {
    echo "got {$value}\n";
}
```

```console
$ php lazy.php
generator created, nothing has run yet
starting
about to yield 1
got 1
resumed after 1
about to yield 2
got 2
resumed after 2
about to yield 3
got 3
resumed after 3
```

Regardez l'ordre. Appeler `countUp()` n'affiche rien, pas même `"starting"`, parce que le corps n'a pas tourné. L'exécution démarre quand `foreach` réclame la première valeur, et elle s'arrête net sur `yield`, en tendant `1` à la boucle. `"resumed after 1"` ne s'affiche que lorsque `foreach` revient chercher la valeur suivante, et `countUp()` reprend exactement là où elle s'était arrêtée, au milieu de sa boucle, avec `$i` et toutes ses variables locales intactes.

<img src="images/ch15-yield-bookmark.png" alt="Une fonction dessinée comme un livre ouvert avec un marque-page à la ligne du yield : une valeur sort vers la boucle foreach, et la demande suivante rouvre le livre au marque-page" width="560">

**Un générateur est une fonction qu'on peut mettre en pause et reprendre, et `yield` est l'endroit de la pause.** C'est tout le mécanisme.

> `yield` tend une valeur et laisse un marque-page dans la fonction. La demande suivante rouvre la fonction au marque-page.

## Générateurs associatifs

`yield` sait aussi produire des paires clé-valeur, avec la même syntaxe `clé => valeur` que pour construire un tableau associatif :

```php
<?php
function statusCodes(): Generator
{
    yield 200 => 'OK';
    yield 404 => 'Not Found';
    yield 500 => 'Internal Server Error';
}

foreach (statusCodes() as $code => $message) {
    echo "{$code}: {$message}\n";
}
```

Tout le reste fonctionne pareil : les paires sortent paresseusement, une à la fois, quand `foreach` les demande. Un petit détail, mais bien pratique dès que ce que vous produisez a une clé évidente, comme c'est souvent le cas d'un tableau associatif.

Les générateurs ne remplacent pas les tableaux. Beaucoup de code a besoin d'un vrai tableau, qu'on peut indexer, compter, ou passer à `array_map()`. **Les générateurs sont faits pour une série de valeurs dont personne n'a besoin en mémoire toutes en même temps.** Plus loin dans ce chapitre, cette idée se met au travail sur un fichier nettement plus gros que cinq carrés.
