# Performances : boucles, générateurs et fonctions de tableau

Élevez deux millions d'entiers au carré et additionnez-les. Vous pouvez l'écrire avec une boucle simple, avec `array_map()`, ou avec un générateur, et les trois programmes affichent le même nombre. **Ils ne coûtent pas la même chose, et le coût veut dire deux choses ici, le temps et la mémoire, qui ne bougent pas toujours ensemble.** Plutôt que deviner, mesurons.

## Un petit banc d'essai

La même tâche, de trois façons :

```php
<?php
declare(strict_types=1);

const N = 2_000_000;

// 1. plain loop
$sum = 0;
for ($i = 1; $i <= N; $i++) {
    $sum += $i * $i;
}

// 2. array functions
$numbers = range(1, N);
$squares = array_map(fn(int $n): int => $n * $n, $numbers);
$sum = array_sum($squares);

// 3. generator
function squares(int $max): Generator {
    for ($i = 1; $i <= $max; $i++) {
        yield $i * $i;
    }
}
$sum = 0;
foreach (squares(N) as $square) {
    $sum += $square;
}
```

Lancez chaque version dans son propre processus, pour que l'une ne gonfle pas le pic de mémoire de l'autre, et mesurez avec `hrtime()` et `memory_get_peak_usage()`. Sur la machine qui a servi à écrire ce livre :

```console
loop              ~100 ms   peak memory:   2 MB
array functions   ~140 ms   peak memory:  66 MB
generator         ~170 ms   peak memory:   2 MB
```

<img src="images/ch15-three-ways.png" alt="Trois coureurs sur une piste : la boucle file en tête avec un petit gobelet, les fonctions de tableau traînent sous deux sacs énormes, et le générateur porte un petit gobelet mais s'arrête à chaque pas pour tendre une valeur" width="600">

Prenez les chiffres exacts avec des pincettes : ils varient avec votre version de PHP, votre machine et ce qui tourne à côté. La *forme* du résultat, elle, est fiable. **La boucle simple est la plus rapide et la plus sobre, point.** La version à fonctions de tableau est la plus lente et de loin la plus gourmande : `range()` construit un tableau de deux millions d'éléments, puis `array_map()` en construit un second pour recevoir les carrés, et les deux existent en même temps avant même que `array_sum()` démarre. Le générateur se place entre les deux en temps, parce que suspendre et reprendre une fonction deux millions de fois a un coût réel, mais il égale la mémoire plate de la boucle, puisqu'il ne tient jamais plus d'une valeur.

## Lire ça honnêtement

Rien de tout cela ne signifie « écrivez toujours des boucles ». Les trois outils sont bons à des choses différentes, et en choisir un, c'est savoir laquelle vous cherchez.

**Une boucle `for` ou `foreach` est l'option la plus rapide, et souvent la plus claire.** Il n'y a rien à apprendre, juste une variable qui change à chaque tour. Prenez-la quand la vitesse compte, quand la logique dépasse la transformation d'une ligne, ou chaque fois que vous hésitez. Elle est rarement le mauvais choix par défaut.

**Un générateur échange un peu de vitesse contre une mémoire qui ne grossit pas avec l'entrée.** Un fichier énorme, une API que vous parcourez page par page, une suite sans fin : c'est son territoire. Vous l'avez vu payer dans `phpgrep`, qui affiche sa première ligne avant d'avoir fini le fichier. Si toute la série tenait confortablement en mémoire de toute façon, le surcoût de la pause-reprise ne vous apporte rien.

**`array_map()` et `array_filter()` sont souvent l'option la plus lisible pour des données petites ou moyennes déjà en mémoire.** Un `array_map(fn($x) => ..., $items)` d'une ligne se lit mieux que la boucle de cinq lignes qu'il remplace, et c'est un vrai gain. Ce qu'ils ne sont pas, c'est une économie de mémoire : chacun construit un tableau tout neuf en plus de celui que vous lui donnez. Pour cent éléments, sans importance. Pour des millions, ce sont les 66 Mo que vous venez de voir.

## Une règle de décision, pas un tableau

Si les données sont assez petites pour que vous n'hésitiez jamais à les garder toutes en mémoire, prenez ce qui se lit le mieux à l'endroit de l'appel : en général une fonction de tableau pour une transformation simple, une boucle pour tout ce qui contient de la vraie logique. Si les données sont grosses, sans limite connue ou coûteuses à produire (un gros fichier, un curseur de base de données, tout ce que vous parcourez page par page), prenez un générateur et acceptez le léger surcoût en échange d'une mémoire qui ne bouge pas. Et si vous courez après la vitesse brute sur un chemin critique, et que vous avez mesuré que ça compte, la boucle simple reste, discrètement, la chose la plus rapide que PHP vous offre.

> Petites données : ce qui se lit le mieux. Grosses données : un générateur. Chemin critique : une boucle, une fois que vous avez mesuré.

Ne devinez pas quel cas est le vôtre. Le banc d'essai ci-dessus tient en une douzaine de lignes. Mesurez le vôtre, si la question mérite d'être posée.
