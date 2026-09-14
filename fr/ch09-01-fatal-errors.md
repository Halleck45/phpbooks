# Erreurs irrécupérables : erreurs fatales et `Error`

Certains problèmes n'ont rien à voir avec la malchance. Aucun fichier n'a disparu, aucun utilisateur n'a tapé n'importe quoi : c'est votre code qui est faux. Vous avez appelé une méthode qui n'existe pas. Vous avez passé une chaîne de caractères à une fonction qui exigeait un entier, avec les types stricts activés. Vous avez divisé par zéro. **Face à un bug, un programme n'a rien de sensé à faire, sinon s'arrêter et vous laisser corriger.**

PHP représente cette famille avec la classe `Error` et ses sous-classes. En voici trois que vous croiserez sans arrêt :

```php
<?php

declare(strict_types=1);

function half(int $n): int
{
    return $n / 0; // DivisionByZeroError
}

function double(int $n): int
{
    return $n * 2;
}

double("four"); // TypeError: strict_types is on, no silent conversion

$user = null;
$user->getName(); // Error: Call to a member function getName() on null
```

`DivisionByZeroError`, `TypeError` et la simple `Error` obtenue en appelant une méthode sur `null` font toutes le même travail : vous dire, aussi précisément que possible, que le programme a atteint un état où il n'avait rien à faire. Lancez le fichier. Il s'arrête à `double("four")`, la première chose fausse qu'il exécute vraiment. Mettez cette ligne en commentaire, relancez, et c'est l'appel sur `null` qui prend le relais ; appelez `half(3)` et ce sera la division. C'est exactement à cela que sert `declare(strict_types=1)`, rencontré dans [Les types de données](ch03-02-data-types.md) : faire échouer un appel incorrect bruyamment, sur place, au lieu de le laisser passer.

## Pourquoi c'était pire avant

Le code écrit avant PHP 7 est truffé de vérifications de `null` et de gardes `is_int()` semées dans les corps de fonctions, et il y avait une raison. À l'époque, la plupart de ces situations ne lançaient rien que l'on puisse attraper. Appeler une méthode sur `null` était une erreur fatale qui arrêtait le script, point final ; aucun `try` au monde ne pouvait s'interposer. Un type qui ne correspondait pas était converti sans bruit, ou provoquait un avertissement dans un journal que personne ne surveillait, et le programme continuait avec des données absurdes.

PHP 7 a introduit `Error` pour corriger cela, et PHP 8 a affûté le mécanisme. **Presque tout, dans cette famille, est désormais un véritable objet qui implémente `Throwable`, la même interface que `Exception`.** Vous *pouvez* donc écrire `catch (Error $e)` et laisser le programme continuer. Très souvent, vous ne devriez pas.

## Attrapable ne veut pas dire « à attraper »

La question n'est pas de savoir si PHP peut vous tendre le problème sous forme d'objet. Depuis PHP 8, il le peut presque toujours. La question est de savoir si l'attraper répare quoi que ce soit. Comparez :

```php
<?php

declare(strict_types=1);

// Reasonable: the input is genuinely unpredictable, and there's a sensible fallback.
try {
    $config = json_decode($configJson, associative: true, flags: JSON_THROW_ON_ERROR);
} catch (\JsonException $e) {
    $config = [];
}

// Unreasonable: papering over a bug instead of fixing it.
try {
    $total = $order->getTotal(); // $order might be null due to a bug upstream
} catch (\Error $e) {
    $total = 0; // now every bug in this code path just... returns zero, silently
}
```

Le premier `try` gère une situation qui peut vraiment se produire : du JSON venu de l'extérieur est parfois mal formé, et se rabattre sur une configuration vide est un choix défendable. Le second `try` attrape le symptôme d'un bug et le cache derrière un nombre plausible. Six mois plus tard, quelqu'un se demande pourquoi les totaux tombent parfois à zéro, sans exception, sans ligne de journal, sans le moindre indice, parce que le bloc `catch` a avalé la seule preuve.

<img src="images/ch09-catch-eats-evidence.png" alt="Un bloc catch dessiné comme une créature qui avale un message d'erreur tout entier, pendant qu'un développeur, plus tard, fouille le sol vide à la loupe et ne trouve rien" width="560">

> [!WARNING]
> Un large `catch (\Error $e)` n'est pas un filet de sécurité. C'est une déchiqueteuse pour la trace d'appels dont vous aurez besoin plus tard.

**N'attrapez `Error` et ses sous-classes qu'avec une bonne raison et un type étroit, précis.** Si votre propre code produit une `TypeError`, la correction consiste à réparer l'appel, pas à l'envelopper dans un `try`. [Lancer ou ne pas lancer](ch09-03-to-throw-or-not-to-throw.md) trace cette frontière plus finement. Pour l'instant, lisez `Error` comme PHP vous disant que quelque chose est cassé, et les exceptions, juste après, comme PHP vous disant que quelque chose demande une décision.
