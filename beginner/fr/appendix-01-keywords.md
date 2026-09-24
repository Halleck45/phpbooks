# A - Mots réservés

Les mots qui suivent sont réservés par PHP. Vous ne pouvez utiliser aucun d'eux comme nom de variable, de fonction, de classe, de constante ou d'espace de noms : l'analyseur syntaxique se les est déjà appropriés pour autre chose.

## Structures de contrôle

`if` · `else` · `elseif` · `endif` · `while` · `endwhile` · `do` · `for` · `endfor` · `foreach` · `endforeach` · `as` · `switch` · `endswitch` · `case` · `default` · `match` · `break` · `continue` · `goto` · `return` · `yield`

## Classes

`class` · `interface` · `trait` · `enum` · `extends` · `implements` · `new` · `clone` · `instanceof` · `abstract` · `final` · `public` · `protected` · `private` · `readonly` · `static` · `const` · `var` · `function` · `fn` · `use`

## Gestion des erreurs

`try` · `catch` · `finally` · `throw`

## Espaces de noms et inclusions

`namespace` · `use` · `require` · `require_once` · `include` · `include_once`

## Autres

`echo` · `print` · `declare` · `enddeclare` · `global` · `list` · `array` · `isset` · `unset` · `empty` · `exit` · `die` · `and` · `or` · `xor` · `not` · `int` · `float` · `bool` · `string` · `null` · `true` · `false` · `void` · `mixed` · `never` · `self` · `parent`

Le dernier groupe, celui des noms de types (`int`, `string`, `null`, `true`, `false` et les autres), mérite une remarque : ces mots ne sont devenus réservés que progressivement, au fur et à mesure que PHP en a fait de vraies déclarations de type. Du code ancien utilise parfois `String` ou `Int` comme nom de classe, du temps où c'était encore permis. Ça ne l'est plus.

`use` apparaît dans deux groupes parce qu'il fait deux travaux sans rapport : importer des noms depuis un espace de noms ([chapitre 7](ch07-04-use-keyword.md)) et capturer des variables dans une closure ([chapitre 15](ch15-01-closures.md)). Même mot, même réservation, contexte différent.

Aucun de ces mots ne peut être détourné, même si le nom irait parfaitement à votre code. Essayez de nommer une variable `$class` : celle-là passe, en fait, car les mots réservés ne bloquent que les identifiants *nus*, pas les noms de variables derrière le `$`. Essayez de nommer une fonction `list()` ou une classe `Match`, et PHP vous arrêtera à l'analyse du fichier, pas à l'exécution. Mieux vaut là qu'en production.
