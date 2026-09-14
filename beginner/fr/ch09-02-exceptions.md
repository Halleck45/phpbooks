# Erreurs récupérables avec les exceptions

La section précédente parlait de bugs. Celle-ci parle des ennuis que votre code doit s'attendre à rencontrer : un fichier qui peut ne pas exister, un âge qui peut être négatif, une API qui peut refuser la requête. Rien de tout cela ne signifie que le programme est cassé. Il y a une décision à prendre, et la fonction qui repère le problème est rarement celle qui est en position de trancher. **Une exception, c'est la manière pour une fonction de dire « voilà un problème, et voilà ce que j'en sais » à qui, plus haut dans la pile d'appels, saura quoi en faire.**

## `try`, `catch`, `finally`

La forme est la même que dans la plupart des langages qui ont des exceptions :

```php
<?php

declare(strict_types=1);

function readConfig(string $path): array
{
    if (!file_exists($path)) {
        throw new \RuntimeException("Config file not found: {$path}");
    }

    return json_decode(file_get_contents($path), associative: true);
}

try {
    $config = readConfig('config.json');
    echo "Loaded " . count($config) . " settings.\n";
} catch (\RuntimeException $e) {
    echo "Couldn't load config: {$e->getMessage()}\n";
    $config = [];
} finally {
    echo "Config load attempt finished.\n";
}
```

Lancez-le sans `config.json` à côté du fichier. `readConfig()` atteint le `throw`, et l'exécution normale s'arrête là : rien après le `throw` ne s'exécute, et le `echo "Loaded..."` de l'appelant non plus. **Le contrôle saute au `catch` englobant le plus proche dont le type correspond, en ignorant tout ce qui se trouve entre les deux, quel que soit le nombre d'appels de fonctions à traverser.**

<img src="images/ch09-exception-climbs.png" alt="Une exception qui monte à travers les trois étages d'un immeuble, depuis la fonction qui l'a lancée, en passant par une fonction qui ne la voit jamais, jusqu'à un bloc catch au dernier étage qui l'arrête" width="500">

Pensez à une fuite au rez-de-chaussée d'un immeuble. Personne là ne peut la réparer, alors l'alarme monte, étage par étage, et chaque étage traversé lâche ce qu'il faisait, jusqu'à ce que quelqu'un l'attrape au filet. Si personne ne le fait, l'alarme atteint le toit, et PHP arrête le programme en affichant le message et le chemin que l'exception a parcouru.

`finally` s'exécute quoi qu'il soit arrivé : exception attrapée, exception non attrapée, ou pas d'exception du tout. C'est donc l'endroit pour le nettoyage qui doit avoir lieu dans tous les cas, comme fermer un fichier ou libérer un verrou.

> [!TIP]
> Essayez : créez un `config.json` contenant `{"debug": true}` et relancez. Cette fois, le bloc `catch` est ignoré, et `finally` affiche quand même sa ligne.

## `Exception` contre `Error`, et `Throwable`

La hiérarchie des exceptions de PHP a deux branches parallèles, qui poussent depuis la même interface, `Throwable`.

<img src="images/ch09-throwable-tree.png" alt="Un arbre avec Throwable à la racine et deux branches : Exception, avec RuntimeException, InvalidArgumentException et JsonException pour feuilles, et Error, avec TypeError et DivisionByZeroError pour feuilles" width="520">

`Exception` et ses sous-classes (`InvalidArgumentException`, `RuntimeException`, `JsonException`) servent aux situations qu'un programme bien écrit peut anticiper et surmonter. `Error` et ses sous-classes (`TypeError`, `DivisionByZeroError`) sont les bugs de la section précédente.

Cette séparation est ce qui permet à un `catch` d'être précis. **`catch (\Exception $e)` attrape les exceptions et laisse passer une `Error` ; `catch (\Throwable $e)` attrape les deux.** Ne sortez `\Throwable` qu'à la lisière d'une application, dans un gestionnaire de dernier recours qui journalise ce que personne d'autre n'a traité avant que le processus ne se termine. Jamais comme type de `catch` ordinaire dans du code courant : l'attraper par réflexe, c'est ainsi que des bugs deviennent des cas « gérés » que personne ne corrige jamais.

## Attraper plusieurs types à la fois

Un seul `catch` peut lister plusieurs types séparés par `|`, quand vous voulez les traiter de la même façon :

```php
<?php

declare(strict_types=1);

try {
    $result = $client->send($request);
} catch (ConnectionException|TimeoutException $e) {
    echo "Network problem, retrying: {$e->getMessage()}\n";
    $result = retry($request);
}
```

Si le traitement diffère entre les deux, écrivez deux blocs `catch`. Le `|` sert quand la réponse est vraiment identique, pas à s'épargner un second bloc.

## Écrire sa propre exception

`RuntimeException` et `InvalidArgumentException` couvrent beaucoup de terrain, mais nommer vos propres exceptions est l'une des choses les plus courantes que vous ferez en PHP. **Un type d'exception précis dit à l'appelant exactement ce qui a échoué, et lui permet d'attraper cela et rien d'autre**, au lieu de deviner à partir d'un message :

```php
<?php

declare(strict_types=1);

class InvalidAgeException extends \Exception
{
    public function __construct(
        public readonly int $age,
    ) {
        parent::__construct("Invalid age: {$age}. Must be between 0 and 150.");
    }
}

function registerUser(string $name, int $age): void
{
    if ($age < 0 || $age > 150) {
        throw new InvalidAgeException($age);
    }

    echo "Registered {$name}, age {$age}.\n";
}

try {
    registerUser('Alice', -5);
} catch (InvalidAgeException $e) {
    echo "Registration failed: {$e->getMessage()}\n";
    echo "Offending value was: {$e->age}\n";
}
```

Étendre `\Exception` apporte toute la mécanique standard sans effort : `getMessage()`, `getCode()`, `getPrevious()`, et une trace d'appels via `getTraceAsString()`. L'appel à `parent::__construct()` est ce qui branche votre message sur cette mécanique ; sautez-le et `getMessage()` revient vide. Au-delà, la classe est à vous. `InvalidAgeException` garde l'`$age` fautif dans une propriété en lecture seule, si bien que le bloc `catch` reçoit une donnée structurée, pas seulement une chaîne à décortiquer.

Ce petit motif, une exception précise qui transporte le contexte qui l'a provoquée, revient au [chapitre 14](ch14-00-a-cli-project.md). Autant vous y sentir à l'aise dès maintenant, car la question difficile n'est pas comment lancer. C'est quand.
