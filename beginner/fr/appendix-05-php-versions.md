# E - Versions de PHP et rétrocompatibilité

## Rythme des sorties

PHP publie une nouvelle version mineure à peu près une fois par an. Chaque version reçoit environ deux ans de maintenance active (nouvelles fonctionnalités, corrections de bugs, correctifs de sécurité), puis à peu près un an de maintenance limitée à la sécurité avant d'atteindre sa fin de vie. Passé ce point, la faire tourner en production revient à faire tourner un logiciel sans correctifs, ni plus ni moins.

Vérifiez ce que vous utilisez :

```console
$ php -v
PHP 8.3.0 (cli) (built: ...)
```

Ou depuis l'intérieur d'un script :

```php
<?php

echo phpversion(); // "8.3.0"
```

## Une brève histoire

Le passage de PHP 5 à PHP 7 a été un bond énorme : un moteur réécrit, des performances à peu près doublées, et l'arrivée des déclarations de types scalaires. Le passage de PHP 7 à PHP 8 a été plus modeste en performances brutes mais plus dense en fonctionnalités : le compilateur JIT, les types union, les enums, les attributs, les arguments nommés, l'opérateur nullsafe, la promotion de propriétés dans le constructeur, `match`. L'essentiel de ce sur quoi ce livre s'appuie (les enums au [chapitre 6](ch06-00-enums.md), les attributs au [chapitre 20](ch20-04-attributes.md), la promotion de propriétés au [chapitre 5](ch05-03-methods.md)) n'existait pas avant PHP 8. C'est précisément pour cela que ce livre vise PHP 8.1 et suivants.

## Fixer une version minimale

Dites à Composer, et à quiconque installe votre paquet, ce dont il a vraiment besoin :

```json
{
    "require": {
        "php": ">=8.1"
    }
}
```

Ce n'est pas une formalité. Sans cette ligne, Composer laissera volontiers votre paquet s'installer sur une version de PHP qui n'a pas les fonctionnalités que vous utilisez, et l'échec surviendra à l'exécution plutôt qu'à l'installation, ce qui est un bien pire endroit pour le découvrir.

## N'ayez pas peur de mettre à jour

PHP prend la rétrocompatibilité au sérieux à l'intérieur d'une version majeure. Du code écrit pour PHP 8.0 tourne, à peu de choses près, sur PHP 8.3. Les avertissements de dépréciation apparaissent en général une ou deux versions avant qu'une chose soit réellement retirée, ce qui vous laisse un vrai préavis plutôt qu'une surprise. Mettre à jour est rarement l'épreuve que la vieille réputation de PHP laisse craindre. Le plus grand risque, en pratique, c'est de rester sur une version qui n'est plus maintenue et de perdre en silence les correctifs de sécurité.
