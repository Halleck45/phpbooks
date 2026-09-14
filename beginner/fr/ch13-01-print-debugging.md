# Déboguer par affichage avec `var_dump()` et `print_r()`

`echo $count` affiche `5`. Est-ce que `$count` contient le nombre cinq, ou le texte `"5"` ? `echo` ne vous le dira jamais, et cette différence est souvent tout le bug.

Vous avez croisé `var_dump()` brièvement au [chapitre 3](ch03-02-data-types.md) : la fonction montre le type d'une valeur en même temps que la valeur elle-même. `var_dump($count)` affiche `int(5)` ou `string(1) "5"`, et vous voilà fixé. **C'est ce qui en fait un outil de débogage et pas seulement d'inspection : un bug, c'est très souvent une valeur du mauvais *type*, pas du mauvais contenu.**

<img src="images/ch13-echo-vs-var-dump.png" alt="Les deux mêmes valeurs, l'entier 5 et le texte 5, paraissent identiques une fois affichées par echo, tandis que var_dump montre int(5) et string(1) 5 et rend la différence visible" width="560">

## `var_dump()` sur des données structurées

`var_dump()` ne se limite pas à une valeur simple. Donnez-lui un tableau ou un objet, et il le parcourt en entier pour vous en montrer la forme :

```php
<?php

$user = [
    'name' => 'Alice',
    'age' => '32',
    'active' => true,
    'roles' => ['admin', 'editor'],
];

var_dump($user);
```

```console
array(4) {
  ["name"]=>
  string(5) "Alice"
  ["age"]=>
  string(2) "32"
  ["active"]=>
  bool(true)
  ["roles"]=>
  array(2) {
    [0]=>
    string(5) "admin"
    [1]=>
    string(6) "editor"
  }
}
```

Regardez `"age"` : il ressort en `string(2) "32"`, pas en `int(32)`. Si ce tableau vient d'un formulaire (le genre de données que le [chapitre 10](ch10-01-forms-and-superglobals.md) lit dans `$_POST`), c'est attendu, parce que tout ce qui arrive dans `$_POST` est du texte. Le code plus bas qui suppose que `$user['age']` est déjà un entier est un bug en attente. **`var_dump()` attrape en quelques secondes ce qu'une mauvaise réponse silencieuse, trois fonctions plus loin, vous coûterait une heure à remonter.**

Essayez : remplacez `'32'` par `32` dans le tableau et relancez le script. La ligne `"age"` devient `int(32)`.

`var_dump($name, $age, $roles)` affiche les trois valeurs l'une après l'autre, en plus court que trois appels séparés.

## `print_r()` : plus lisible, moins précis

`print_r()` montre la même structure sans les types, dans un format nettement plus facile à parcourir quand le tableau est grand :

```php
<?php

print_r($user);
```

```console
Array
(
    [name] => Alice
    [age] => 32
    [active] => 1
    [roles] => Array
        (
            [0] => admin
            [1] => editor
        )

)
```

Notez ce qui a disparu. `true` est devenu `1`, et rien ne dit si `32` est un nombre ou du texte. C'est le compromis : **prenez `print_r()` pour voir vite la forme de quelque chose, et `var_dump()` dès que le type exact d'une valeur est en question**, ce qui est presque toujours le cas quand on traque un bug.

`print_r()` a un tour de plus dans son sac. Passez-lui `true` en second argument et il *renvoie* le texte formaté au lieu de l'afficher, ce qui permet d'envoyer un instantané vers un journal plutôt qu'à l'écran :

```php
<?php

$snapshot = print_r($user, true);
error_log("user state: {$snapshot}");
```

Une troisième fonction, `var_export()`, se place entre les deux. Elle montre à peu près ce que montre `print_r()`, mais sous la forme de code PHP valide : `var_export($user)` affiche quelque chose que vous pourriez recoller tel quel dans un script comme littéral de tableau. Pratique pour capturer une vraie valeur et en faire une fixture de test.

## Les limites de l'affichage

Les trois fonctions partagent la même faiblesse. **Il faut déjà soupçonner *où* est le problème pour savoir où poser l'appel**, et chaque fois que vous voulez regarder ailleurs, vous modifiez le fichier et relancez le programme. Pointer la lampe, regarder, la déplacer, regarder encore.

Pour un script de la taille de ceux du livre jusqu'ici, ça marche. Ça cesse de marcher quand un bug dépend de l'enchaînement exact de plusieurs appels de fonctions, ou n'apparaît qu'au cinquième tour d'une boucle, ou se cache dans une bibliothèque que vous préféreriez ne pas modifier. À ce stade, l'affichage n'a plus rien de chirurgical et devient du tâtonnement. Xdebug est l'outil de ce moment-là : il vous laisse mettre un script en pause et regarder autour de vous, au lieu de deviner à l'avance où pointer la lampe.
