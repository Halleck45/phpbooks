# Associer des clés à des valeurs avec les tableaux associatifs

Reprenez la rangée de boîtes de la section précédente et remplacez les étiquettes numérotées par des mots. C'est un tableau associatif, et c'est toute la différence.

**Un tableau associatif est un tableau dont vous avez choisi les clés vous-même**, des chaînes le plus souvent, au lieu de laisser PHP distribuer 0, 1, 2. Même structure, la table ordonnée de PHP, autres étiquettes :

```php
<?php

declare(strict_types=1);

$prices = [
    'apple' => 0.50,
    'banana' => 0.30,
    'cherry' => 3.20,
];

echo $prices['banana'] . "\n"; // 0.3
$prices['date'] = 4.10; // add a new key
```

<img src="images/ch08-array-shelf.png" alt="Deux étagères identiques de trois boîtes : sur celle du haut les étiquettes disent 0, 1, 2, sur celle du bas apple, banana, cherry, avec les prix à l'intérieur. Même structure, autres clés" width="520">

Les clés peuvent être des chaînes ou des entiers, et PHP mélange les deux dans un même tableau sans broncher. Elles doivent être uniques, en revanche : affectez une clé qui existe déjà et vous écrasez sa valeur, au lieu d'ajouter une seconde entrée.

## `isset()` contre `array_key_exists()`, et le piège entre les deux

Les deux fonctions répondent à une version de « cette clé est-elle là ? », et elles ne sont pas interchangeables. La différence a causé de vrais bugs, alors autant la comprendre une fois plutôt que de s'en souvenir à moitié.

```php
<?php

declare(strict_types=1);

$user = [
    'name' => 'Alice',
    'nickname' => null,
];

var_dump(isset($user['name']));               // true
var_dump(isset($user['nickname']));           // false, surprising!
var_dump(array_key_exists('nickname', $user)); // true
```

Imaginez le tableau comme une rangée de tiroirs étiquetés. **`isset()` ouvre le tiroir et demande s'il y a quelque chose dedans.** Le tiroir `nickname` existe, mais il contient `null`, et pour `isset()` c'est comme s'il n'y avait pas de tiroir du tout. **`array_key_exists()` ne lit que les étiquettes.** Peu lui importe le contenu, seule compte l'existence du tiroir.

<img src="images/ch08-isset-drawers.png" alt="Deux tiroirs étiquetés, name qui contient Alice et nickname qui ne contient rien : isset regarde dedans et dit non pour nickname, array_key_exists lit l'étiquette et dit oui" width="560">

Cela compte chaque fois que `null` est une valeur à part entière plutôt qu'une absence : une fiche utilisateur où « pas de surnom » est volontairement rangé comme `null`, par exemple. Prenez `isset()` dans le cas courant (est-ce que ça existe et contient quelque chose d'utilisable), et `array_key_exists()` quand vous devez distinguer « jamais défini » de « défini à `null` ». Les confondre coûte une heure la première fois, et plus jamais ensuite. Croyez-moi sur parole.

## Parcourir avec `foreach`

Vous avez vu `foreach` dans [Structures de contrôle](ch03-05-control-flow.md), surtout sur des tableaux indexés. Sur un tableau associatif, c'est la forme clé-valeur qui prend tout son sens :

```php
<?php

declare(strict_types=1);

$prices = [
    'apple' => 0.50,
    'banana' => 0.30,
    'cherry' => 3.20,
];

foreach ($prices as $fruit => $price) {
    echo "{$fruit}: \${$price}\n";
}
// apple: $0.5
// banana: $0.3
// cherry: $3.2
```

**L'ordre de parcours est l'ordre d'insertion, toujours.** Encore une conséquence directe du fait que les tableaux sont des tables ordonnées et non de vraies tables de hachage sans ordre. Vous n'avez jamais à trier un tableau associatif pour obtenir un ordre prévisible ; il en a déjà un.

## Imbriquer : des tableaux de tableaux associatifs

La forme que vous rencontrerez sans cesse dans du vrai code est la liste de fiches : un tableau indexé dont chaque élément est lui-même un tableau associatif, qui tient lieu de ligne de données :

```php
<?php

declare(strict_types=1);

$books = [
    ['title' => 'The Pragmatic Programmer', 'author' => 'Hunt & Thomas', 'year' => 1999],
    ['title' => 'Refactoring', 'author' => 'Martin Fowler', 'year' => 2018],
    ['title' => 'Clean Code', 'author' => 'Robert C. Martin', 'year' => 2008],
];

foreach ($books as $book) {
    echo "{$book['title']} ({$book['year']}): {$book['author']}\n";
}

$recent = array_filter($books, fn (array $book) => $book['year'] >= 2008);
$titles = array_map(fn (array $book) => $book['title'], $books);

echo implode(', ', $titles) . "\n";
```

<img src="images/ch08-list-of-records.png" alt="Une boîte de fiches numérotées 0, 1, 2, chaque fiche portant les trois mêmes champs, title, author et year : un tableau indexé de tableaux associatifs" width="520">

Imaginez une boîte de fiches cartonnées. Chaque fiche porte les trois mêmes lignes (titre, auteur, année), et la boîte les garde dans l'ordre. **Tableau indexé dehors, tableau associatif dedans** : c'est exactement ce que renvoie une requête de base de données, une réponse JSON décodée avec `json_decode($json, true)`, ou un fichier CSV lu ligne par ligne.

Ça paraît presque trop simple pour mériter un nom, et ça en mérite un quand même. Le temps d'arriver au [chapitre 14](ch14-00-a-cli-project.md) et au-delà, c'est sous cette forme que vous tiendrez la plupart des données réelles avant qu'elles ne deviennent quelque chose de plus structuré, comme les objets du [chapitre 5](ch05-00-classes.md).
