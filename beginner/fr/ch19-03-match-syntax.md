# La syntaxe des motifs de `match`

Le chapitre 6 a présenté `match` dans les règles, aux côtés des énumérations, là où il brille le plus. Trois détails n'y tenaient pas, et vous voudrez les trois la première fois que vous écrirez un `match` de plus de deux ou trois bras.

## Plusieurs conditions par bras

Un bras n'est pas obligé de tester une seule valeur. Séparez-en plusieurs par des virgules, et le bras correspond dès que l'une d'elles est égale au sujet :

```php
<?php

$dayNumber = 6;

$dayType = match ($dayNumber) {
    1, 2, 3, 4, 5 => 'Weekday',
    6, 7 => 'Weekend',
    default => 'Invalid',
};

echo $dayType; // Weekend
```

**Lisez la virgule comme un « ou ».** `1, 2, 3, 4, 5 =>` signifie « si le sujet vaut 1, ou 2, ou 3, ou 4, ou 5 ». Sans elle, vous écririez cinq bras qui renvoient tous `'Weekday'`, exactement la répétition que `match` existe pour supprimer.

## L'ordre compte : le premier qui correspond gagne

`match` examine ses bras de haut en bas et s'arrête au premier qui convient. La plupart du temps, vous n'y pensez jamais, parce que des conditions bien conçues ne se recouvrent pas. Associez `match (true)` (qui teste des conditions booléennes au lieu d'une seule valeur, comme au [chapitre 3](ch03-05-control-flow.md)) à des conditions qui peuvent se recouvrir, et l'ordre cesse d'être une formalité :

```php
<?php

$score = 85;

$grade = match (true) {
    $score >= 90 => 'A',
    $score >= 80 => 'B',
    $score >= 70 => 'C',
    default => 'F',
};

echo $grade; // B
```

<img src="images/ch19-first-match-wins.png" alt="Trois tamis empilés du plus fin au plus grossier, étiquetés 90 ou plus, 80 ou plus, 70 ou plus ; une bille marquée 85 traverse le premier et est retenue par le deuxième, marqué B" width="520">

Remontez `$score >= 70` en tête, et 85 le satisfait avant même que le bras `B` ait son tour. 95 aussi. Les bras `A` et `B` deviennent du code mort, et PHP n'en dira pas un mot. Essayez : réordonnez les bras et relancez le fichier.

> [!TIP]
> **Quand des bras peuvent se recouvrir, placez la condition la plus restrictive en premier**, comme des tamis empilés du plus fin au plus grossier.

## Les bras sont des expressions, pas seulement des valeurs

Un bras n'a pas à être un simple littéral. **Chaque bras d'un `match` est une expression complète, évaluée et renvoyée seulement quand ce bras est choisi.** Appelez une fonction, construisez un objet, exécutez tout ce que PHP accepte comme expression :

```php
<?php

enum LogLevel
{
    case Info;
    case Warning;
    case Error;
}

function formatMessage(string $level, string $text): string
{
    return "[" . strtoupper($level) . "] {$text}";
}

$level = LogLevel::Warning;

$output = match ($level) {
    LogLevel::Info => formatMessage('info', 'Request completed'),
    LogLevel::Warning => formatMessage('warning', 'Disk usage above 80%'),
    LogLevel::Error => (new RuntimeException('Disk full'))->getMessage(),
};

echo $output; // [WARNING] Disk usage above 80%
```

Le dernier bras construit une exception et appelle une méthode dessus, d'un seul mouvement ; les parenthèses autour de `new RuntimeException(...)` sont nécessaires pour que PHP comprenne qu'il doit appeler `getMessage()` sur l'objet terminé, plutôt que d'analyser la ligne autrement. Les bras n'ont aucune obligation d'être courts ou triviaux. Ils doivent être des expressions, et en PHP cela couvre presque tout, ce qui fait de `match` un vrai remplaçant pour quantité de petites fonctions utilitaires, pas seulement un `switch` mieux rangé.
