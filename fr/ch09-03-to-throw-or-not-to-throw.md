# Lancer ou ne pas lancer

La syntaxe de `try` et `catch`, c'est la partie facile. La partie difficile, celle qui sépare un code lisible d'un labyrinthe de vérifications défensives, c'est de décider quand une fonction doit lancer une exception, quand elle doit renvoyer `null`, `false` ou un tableau vide, et quand il est acceptable de laisser tout s'écrouler. Aucun compilateur ne tranchera à votre place. C'est du jugement, celui qu'on se forge à s'être brûlé dans les deux sens. Voici comment j'en suis venu à y réfléchir.

## Introuvable n'est pas exceptionnel

L'erreur la plus fréquente que je rencontre, c'est de lancer une exception pour quelque chose qui n'a rien d'exceptionnel, juste une issue normale que l'appelant doit gérer. Chercher un utilisateur par un identifiant qui n'existe pas n'est pas une crise. Cela arrive toute la journée, aussi banalement que n'importe quelle autre branche de votre code :

```php
<?php

declare(strict_types=1);

function findUserById(array $users, int $id): ?array
{
    foreach ($users as $user) {
        if ($user['id'] === $id) {
            return $user;
        }
    }

    return null; // not found, a completely normal outcome, not an error
}

$user = findUserById($users, 42);

if ($user === null) {
    echo "No such user.\n";
} else {
    echo "Found: {$user['name']}\n";
}
```

**Renvoyer `null` dit à l'appelant exactement à quoi s'attendre, et le laisse décider ce que « introuvable » signifie là où il se trouve** : afficher une 404, créer une valeur par défaut, redemander. Le type de retour `?array` inscrit cette possibilité dans la signature, là où tout le monde la voit. Lancer une `UserNotFoundException` à la place forcerait chaque appelant à écrire un `try` pour quelque chose qui se produit sans arrêt et n'a rien de faux.

> Gardez les exceptions pour ce qui est vraiment exceptionnel.

## Lancer quand l'appelant avait une précondition à respecter

L'envers : lancez quand ce que l'appelant était censé garantir avant d'appeler, une précondition, ne tient pas, et qu'aucune valeur par défaut raisonnable n'existe. C'est l'`InvalidAgeException` de la section précédente. Un âge négatif n'est pas une issue normale sur laquelle brancher, c'est une promesse rompue. La fonction ne peut pas deviner ce que vous vouliez dire, alors elle le dit, fort et précisément :

```php
<?php

declare(strict_types=1);

function withdraw(float $balance, float $amount): float
{
    if ($amount > $balance) {
        throw new \RuntimeException(
            "Cannot withdraw {$amount}: balance is only {$balance}."
        );
    }

    return $balance - $amount;
}
```

Ramener silencieusement le retrait au solde disponible, ou renvoyer `0` sans rien dire, cacherait un bug (ou pire, une vraie erreur financière) derrière un nombre plausible, exactement le défaut de l'exemple `catch (\Error $e)` d'il y a deux sections. Lancer force celui qui appelle `withdraw()` à regarder la situation en face au lieu de la laisser filer.

## Laisser planter quand c'est un bug, pas un cas

Parfois, la bonne réponse n'est ni `null` ni un `catch`. C'est de laisser le programme s'arrêter. Si votre propre code appelle une fonction avec le mauvais type, ou atteint une branche de `match` qui devrait être impossible, ce n'est pas une situation à prévoir dans le design. C'est un bug à corriger, et faire comme si de rien n'était ne fait qu'enterrer les preuves :

```php
<?php

declare(strict_types=1);

enum Status
{
    case Draft;
    case Published;
    case Archived;
}

function statusLabel(Status $status): string
{
    return match ($status) {
        Status::Draft => 'Draft',
        Status::Published => 'Published',
        Status::Archived => 'Archived',
    };
}
```

**Un `match` sans branche `default` lance une `UnhandledMatchError` quand rien ne correspond**, et `UnhandledMatchError` est une `Error`, pas une `Exception`. Avec un `enum`, chaque cas est couvert aujourd'hui, donc la seule façon de déclencher cela, c'est que quelqu'un ajoute plus tard un quatrième `Status` et oublie cette fonction. Essayez : ajoutez `case Deleted;` à l'énumération et appelez `statusLabel(Status::Deleted)`. C'est exactement l'échec que vous voulez bruyant et immédiat, à la ligne du bug, pas avalé trois fichiers plus loin. Ne l'enveloppez pas dans un `try` « au cas où ». Laissez échouer, laissez la trace d'appels pointer la branche manquante, et allez corriger `statusLabel()`.

## Un ordre de décision approximatif

Quand vous hésitez entre les trois, posez-vous les questions dans cet ordre.

<img src="images/ch09-three-roads.png" alt="Un poteau à trois panneaux à une bifurcation : une issue normale mène à renvoyer null, une précondition rompue mène à lancer une exception, et un bug mène à laisser planter" width="560">

1. **« Introuvable » ou « vide » est-il ici une issue normale, attendue ?** Renvoyez `null`, `false` ou un tableau vide, et donnez à la fonction un type de retour qui montre cette possibilité (`?array`, pas `array`).
2. **L'appelant a-t-il rompu une précondition, sans valeur par défaut raisonnable ?** Lancez une exception précise : une exception intégrée si elle convient (`InvalidArgumentException`, `RuntimeException`), une petite classe sur mesure si l'appelant a besoin de contexte structuré en retour, comme avec `InvalidAgeException`.
3. **Est-ce impossible, sauf si le code lui-même est faux ?** Ne vous en défendez pas du tout. Laissez la mécanique `Error` de PHP faire son travail, ou utilisez `assert()` pendant le développement. Un échec bruyant à l'endroit du bug coûte bien moins cher qu'un échec silencieux trois couches de `catch` plus loin.

Rien de tout cela ne s'applique mécaniquement. Beaucoup de code réel vit dans la zone grise entre « attendu » et « précondition rompue », et des développeurs raisonnables ne tranchent pas tous pareil. Mais poser la question à voix haute, fonction par fonction, vaut mieux que de retomber sur celui de `throw` ou `return null` que vos doigts ont tapé en premier. Vous prendrez cette décision dans presque chaque fonction que vous écrirez désormais, à commencer par plusieurs dans l'outil en ligne de commande du [chapitre 14](ch14-00-a-cli-project.md).
