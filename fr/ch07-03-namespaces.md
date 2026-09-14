# Portée et visibilité avec les espaces de noms

**Un espace de noms est un préfixe.** C'est tout le concept, et il vaut mieux le dire avant que la syntaxe ne le fasse paraître plus gros qu'il n'est. `App\Models\Product`, c'est le nom `Product`, qui vit dans `App\Models`, exactement comme `/home/damien/notes.txt` est le fichier `notes.txt`, qui vit dans `/home/damien`. La classe elle-même ne change pas. Ce qui change, c'est la façon dont vous, et PHP, la désignez sans ambiguïté.

## Déclarer un espace de noms

La ligne `namespace` est la première instruction du fichier. Seuls un commentaire ou un `declare(strict_types=1)` peuvent la précéder :

```php
<?php

declare(strict_types=1);

namespace App\Models;

class Product
{
    public function __construct(
        public readonly string $name,
        public readonly float $price,
    ) {
    }
}
```

Tout ce que déclare ce fichier vit désormais sous `App\Models` : la classe `Product`, et toute classe, interface ou fonction que vous ajouterez dessous. Son nom complet est `App\Models\Product`. Dans ce fichier, et dans tout autre fichier qui s'ouvre lui aussi par `namespace App\Models;`, le simple `Product` continue de fonctionner, parce que **PHP résout d'abord un nom nu par rapport à l'espace de noms courant.**

## Pourquoi s'embêter

Voici la situation pour laquelle les espaces de noms ont été conçus. Votre projet utilise une bibliothèque qui livre une classe `Collection` ; beaucoup le font, c'est le nom naturel pour « un ensemble de choses avec quelques méthodes utilitaires ». Vous voulez aussi votre propre `Collection`, pour une application de philatélie, disons. Sans espaces de noms, PHP tomberait sur deux classes qui se disputent le même nom et refuserait de charger la seconde. Une erreur fatale, et pas des plus discrètes.

Avec les espaces de noms, il n'y a pas de dispute :

```php
<?php

namespace App\Models;

class Collection
{
    // your Collection, entirely unrelated to anyone else's
}
```

```php
<?php

// Illuminate\Support\Collection, from a package you installed
namespace Illuminate\Support;

class Collection
{
    // their Collection
}
```

<img src="images/ch07-same-first-name.png" alt="Deux personnages qui portent le même prénom, Collection, mais des badges différents, App\Models pour l'un et Illuminate\Support pour l'autre, si bien que personne ne les confond" width="560">

Même nom court, deux classes différentes, aucune collision : `App\Models\Collection` et `Illuminate\Support\Collection` sont simplement deux identifiants. **Les espaces de noms existent parce que votre projet contiendra du code écrit par des gens que vous n'avez jamais rencontrés, et que personne ne s'est mis d'accord sur les noms à l'avance.** Le rangement du code est un effet secondaire agréable. Éviter la collision, c'est la raison.

## Noms pleinement qualifiés

Vous pouvez toujours désigner une classe par son chemin complet, quel que soit l'espace de noms où vous vous trouvez. Écrivez-le en entier, avec une barre oblique inverse en tête, et vous obtenez un *nom pleinement qualifié* :

```php
<?php

namespace App\Services;

function makeProduct(): \App\Models\Product
{
    return new \App\Models\Product('Keyboard', 49.00);
}
```

Toute l'affaire tient dans ce `\`. Dans `App\Services`, un `Product` nu se résout par rapport à l'espace de noms courant : PHP cherche `App\Services\Product`, qui n'existe pas. **Un `\` en tête signifie « pars tout en haut », depuis l'espace de noms global.**

<img src="images/ch07-leading-backslash.png" alt="Un arbre d'espaces de noms avec l'espace global à la racine : depuis App\Services, le nom nu Product ne cherche que dans la branche courante et ne trouve rien, tandis que \App\Models\Product remonte à la racine et suit le chemin complet" width="560">

Vous avez besoin de la même astuce pour les classes intégrées à PHP, dès que votre fichier a un espace de noms :

```php
<?php

namespace App\Services;

function now(): \DateTimeImmutable
{
    return new \DateTimeImmutable();
}
```

`DateTimeImmutable` n'a pas d'espace de noms. Elle vit tout en haut, à côté d'`Exception`, d'`ArrayObject` et de toutes les autres classes intégrées, et depuis `App\Services` le seul moyen de l'atteindre est la barre oblique inverse en tête. Ou le mot-clé `use`, qui importe le nom une fois pour toutes et vous épargne le `\` partout ailleurs. C'est la suite.

## Un mot sur les fonctions et les constantes

Les espaces de noms couvrent aussi les fonctions et les constantes. `namespace App\Helpers;` suivi de `function slugify(string $s): string { ... }` vous donne `App\Helpers\slugify()`. Vous le croiserez moins souvent que prévu, pour une raison précise : **pour un nom nu de fonction ou de constante, PHP se rabat sur l'espace de noms global quand aucune version dans l'espace courant n'existe.** C'est pour cela que `strlen()` et `array_map()` continuent de fonctionner dans un fichier avec espace de noms, sans y penser. Les classes n'ont pas ce filet. Trompez-vous d'espace de noms pour une classe, et PHP ne la trouvera tout simplement pas.
