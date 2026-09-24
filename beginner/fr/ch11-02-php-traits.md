# Réutiliser du code avec les traits

Une interface ne promet rien sur l'implémentation : c'est une forme pure. **Un trait, ce sont de vrais corps de méthode que PHP colle dans une classe pour vous, comme si vous les y aviez tapés vous-même.** Pas de contrat, pas de polymorphisme, pas de « ces classes sont interchangeables ». Du copier-coller, rendu officiel et rendu sûr par le langage.

Prenez deux classes qui n'ont rien en commun, un `PaymentProcessor` et un `ReportGenerator`, qui veulent toutes deux écrire quelque part des messages horodatés. Elles ne partagent aucune classe parente, et elles ne devraient pas : ce ne sont pas des choses de même nature. Mais elles veulent les mêmes quelques lignes de journalisation.

```php
<?php

trait LoggableTrait
{
    private array $log = [];

    public function log(string $message): void
    {
        $this->log[] = sprintf('[%s] %s', date('H:i:s'), $message);
    }

    public function getLog(): array
    {
        return $this->log;
    }
}
```

`trait` ressemble à une classe, mais vous ne pourrez jamais écrire `new LoggableTrait()`. Un trait n'est pas un type. Il n'apparaît dans aucun test `instanceof` ni dans aucune déclaration de type. Il n'existe que pour être aspiré dans d'autres classes avec `use` :

```php
<?php

class PaymentProcessor
{
    use LoggableTrait;

    public function charge(float $amount): void
    {
        $this->log("Charging \${$amount}");
    }
}

class ReportGenerator
{
    use LoggableTrait;

    public function generate(): void
    {
        $this->log('Generating monthly report');
    }
}

$processor = new PaymentProcessor();
$processor->charge(42.00);

var_dump($processor->getLog());
// array(1) { [0]=> string(...) "[14:32:01] Charging $42" }
```

`PaymentProcessor` et `ReportGenerator` ont maintenant tous deux une méthode `log()` qui fonctionne, une méthode `getLog()` et une propriété privée `$log`, et aucune des deux classes n'en a écrit une ligne. Une fois `use LoggableTrait;` en place, tout se passe exactement comme si vous aviez tapé ces trois membres dans le corps de la classe.

<img src="images/ch11-trait-paste.png" alt="Un petit éléphant colle la même feuille de code, intitulée log(), dans deux boîtes de classes sans rapport, PaymentProcessor et ReportGenerator, avec un bâton de colle" width="560">

Ce qu'elles ne gagnent pas, c'est un lien de parenté. Demander `$processor instanceof LoggableTrait` ne vous mène nulle part : un trait donne un comportement, pas une identité. `PaymentProcessor` et `ReportGenerator` restent deux classes sans rapport qui partagent un peu de code, pas deux sœurs dans une hiérarchie de types.

> Un trait donne du code à une classe, pas une identité.

## Pourquoi pas simplement l'héritage ?

Parce que ces classes n'ont rien d'autre en commun. Forcer `PaymentProcessor` et `ReportGenerator` à étendre une classe `LoggableBase` partagée, dans le seul but d'obtenir une méthode `log()`, reviendrait à modéliser une relation qui n'existe pas. PHP ne donne d'ailleurs qu'un seul parent à chaque classe, et vous dépenseriez cette unique cartouche pour de la journalisation. **Un trait esquive toute la question : pas « est un », mais « a ce comportement, emprunté ici ».**

## Conflits entre traits

Une classe peut `use` plusieurs traits à la fois. Si deux d'entre eux définissent une méthode du même nom, PHP ne devinera pas laquelle vous vouliez. Il lève une erreur fatale tant que vous n'avez pas tranché vous-même :

```php
<?php

class Report
{
    use LoggableTrait, TimestampableTrait {
        LoggableTrait::log insteadof TimestampableTrait;
        TimestampableTrait::log as logTimestampOnly;
    }
}
```

`insteadof` désigne le gagnant. `as` donne un nouveau nom à la version du perdant au lieu de la jeter. Vous n'en aurez pas souvent besoin, la plupart des traits sont assez étroits pour que les collisions restent rares, mais connaître la syntaxe évite qu'une base de code qui l'utilise vous paraisse mystérieuse la première fois que vous la croisez.

## Convention de nommage

Vous croiserez des traits nommés aussi bien `Loggable` que `LoggableTrait`. Ce livre ajoute le suffixe `Trait` pour les distinguer d'un coup d'œil des interfaces qui les accompagnent souvent. Associer une interface `Loggable` (le contrat : « cette classe sait journaliser ») à un `LoggableTrait` (l'implémentation partagée qui le remplit) est sans doute le meilleur usage des traits dans du vrai code. PHP n'impose ni l'une ni l'autre convention. Choisissez-en une par base de code et tenez-vous-y.

Interfaces et traits travaillent tous deux à l'échelle de la classe. Le prochain trou dans le système de types de PHP se trouve un étage plus bas, à l'intérieur du tableau, et celui-là, le langage vous le laisse.
