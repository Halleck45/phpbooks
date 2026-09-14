# B - Opérateurs et symboles

Une table de référence, groupée par ce que les opérateurs font plutôt que par ordre alphabétique. L'ordre alphabétique est parfait pour un dictionnaire et désastreux pour retenir quoi que ce soit.

## Arithmétique

| Opérateur | Signification |
|---|---|
| `+` | Addition |
| `-` | Soustraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulo (reste de la division) |
| `**` | Puissance |

## Affectation

| Opérateur | Signification |
|---|---|
| `=` | Affectation |
| `+=` `-=` `*=` `/=` | Opération arithmétique, puis affectation |
| `.=` | Concaténation, puis affectation |
| `%=` `**=` | Modulo ou puissance, puis affectation |

Chaque opérateur d'affectation combinée est un raccourci : `$x += 1` est exactement `$x = $x + 1`, en plus court et, une fois l'habitude prise, plus lisible d'un coup d'œil.

## Comparaison

| Opérateur | Signification |
|---|---|
| `==` | Égal, après conversion de type |
| `===` | Identique : même type et même valeur, sans conversion |
| `!=` `<>` | Différent |
| `!==` | Non identique |
| `<` `>` `<=` `>=` | Inférieur, supérieur, et leurs variantes « ou égal » |
| `<=>` | Vaisseau spatial |

L'opérateur vaisseau spatial (`<=>`) compare deux valeurs et renvoie `-1`, `0` ou `1`, pour inférieur, égal ou supérieur. C'est exactement la réponse à trois issues qu'attendent les fonctions de tri :

```php
<?php

$numbers = [5, 3, 8, 1];
usort($numbers, fn($a, $b) => $a <=> $b);
```

Avant son arrivée, cette comparaison prenait trois lignes de `if`. Maintenant, un seul opérateur fait ce qu'il annonce.

Préférez `===` à `==` par défaut, pour les raisons données au [chapitre 3](ch03-02-data-types.md).

## Logique

| Opérateur | Signification |
|---|---|
| `&&` | Et |
| `\|\|` | Ou |
| `!` | Non |
| `and` `or` `xor` | Formes en toutes lettres du et, du ou et du ou exclusif |

`and` et `or` font le même travail que `&&` et `||`, mais avec une priorité bien plus basse, assez basse pour perdre face à `=`. Ceci compile, et ne fait pas ce qu'on croit :

```php
<?php

$result = false or true;
var_dump($result); // bool(false)
```

`=` est prioritaire sur `or`, donc cette ligne se lit en réalité `($result = false) or true` : `$result` reçoit `false`, et le `or true` est jeté comme une expression sans effet. Remplacez par `||` et tout rentre dans l'ordre. Tenez-vous-en à `&&` et `||`. Laissez `and`, `or` et `xor` de côté, sauf si vous avez appris par cœur leur table de priorité, ce qui ne vaut pas la peine.

## Chaînes de caractères

| Opérateur | Signification |
|---|---|
| `.` | Concaténation |
| `.=` | Concaténation et affectation |

## Tableaux

| Opérateur | Signification |
|---|---|
| `+` | Union : en cas de conflit, les clés du tableau de gauche gagnent |
| `...` | Décomposition : déverse les éléments d'un tableau dans un autre, ou dans un appel de fonction |

Le `+` des tableaux n'est pas une fusion. Le [chapitre 8](ch08-00-common-collections.md) explique la différence entre `+` et `array_merge()`, qui traitent les clés en double de façon opposée.

## Autour de null

| Opérateur | Signification |
|---|---|
| `??` | Coalescence : la partie droite, seulement si la partie gauche est `null` ou non définie |
| `??=` | Affectation par coalescence |
| `?->` | Accès nullsafe à une méthode ou une propriété |

```php
<?php

$name = $user->name ?? 'Anonymous';   // fall back if null
$config['retries'] ??= 3;             // set only if not already set

$city = $user?->address?->city;       // null, not a fatal error, if either is null
```

Les trois sont traités en détail au [chapitre 6](ch06-00-enums.md).

## Autres symboles

| Symbole | Signification |
|---|---|
| `$` | Marque un nom de variable |
| `->` | Accède à une propriété ou une méthode d'une instance |
| `::` | Accède à une propriété statique, une méthode statique, une constante de classe, ou au parent depuis l'intérieur d'une classe |
| `#[...]` | Attribut : métadonnée structurée attachée à une classe, une méthode ou une propriété |

Les attributs sont le plus récent des quatre, et le [chapitre 20](ch20-04-attributes.md) leur est consacré.
