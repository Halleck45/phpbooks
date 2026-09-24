# Constantes magiques et Reflection

Votre code sait en général ce qu'il est : vous l'avez écrit. Mais il arrive qu'un programme doive se poser la question pendant qu'il tourne. Un logger veut dire quelle méthode a émis un avertissement. Un outil de test veut la liste des méthodes d'une classe qu'il n'a jamais vue. **PHP répond à ces questions avec deux outils de tailles très différentes : une poignée de constantes magiques pour les questions simples, et la Reflection, une API complète, pour les questions détaillées.**

## Les constantes magiques

Le logger d'abord.

```php
<?php

class Logger
{
    public function warn(string $message): void
    {
        echo __CLASS__ . '::' . __FUNCTION__ . " at line " . __LINE__ . ": {$message}\n";
    }
}

(new Logger())->warn('Disk space low');
```

```console
$ php logger.php
Logger::warn at line 7: Disk space low
```

La méthode `warn()` n'écrit jamais son propre nom, et pourtant la sortie affiche `Logger::warn` et un numéro de ligne. **`__CLASS__`, `__FUNCTION__` et `__LINE__` sont remplies par PHP avant l'exécution, avec le nom de la classe, le nom de la fonction et la ligne où elles apparaissent.** Deux autres font le même travail : `__METHOD__` donne les deux noms d'un coup, sous la forme `Class::method`, et `__FILE__` donne le chemin complet du fichier courant.

On les dit magiques parce que leur valeur dépend de l'endroit où vous les écrivez. Essayez : décalez la ligne du `echo` d'un cran en insérant une ligne vide au-dessus, puis relancez. Le `7` devient un `8`.

Il n'y a rien de sorcier là-dessous. L'analyseur remplace chaque constante par une valeur toute simple, donc elles ne coûtent rien et ne peuvent pas se tromper. C'est ce qu'il faut à une ligne de log : d'où vient le message, sans un nom codé en dur qui dérivera le jour où quelqu'un renommera la méthode.

> Une constante magique est une étiquette que l'analyseur coud dans votre code. Elle indique toujours l'endroit où l'on se trouve.

## La Reflection

Les constantes magiques renseignent le code sur lui-même. **La Reflection permet au code d'examiner d'autre code, classe par classe et méthode par méthode, comme des données qu'il interroge à l'exécution.**

```php
<?php

class UserRepository
{
    public function find(int $id): ?string
    {
        return "User #{$id}";
    }

    public function save(string $name): void
    {
        // ...
    }

    private function connect(): void
    {
        // ...
    }
}

$reflection = new ReflectionClass(UserRepository::class);

foreach ($reflection->getMethods(ReflectionMethod::IS_PUBLIC) as $method) {
    echo $method->getName() . "\n";
}
```

```console
$ php reflect.php
find
save
```

`ReflectionClass` enveloppe une classe et en expose la forme : `getMethods()`, `getProperties()`, `getConstructor()`, et d'autres. Chacune renvoie d'autres objets de réflexion, `ReflectionMethod` ou `ReflectionProperty`, que vous interrogez à leur tour sur les paramètres d'une méthode, leurs types, ou le caractère `readonly` d'une propriété. Passer `ReflectionMethod::IS_PUBLIC` écarte `connect()`, l'aide privée, et ne laisse que l'interface publique. Les attributs, plus loin dans ce chapitre, se relisent de la même manière.

<img src="images/ch20-reflection-xray.png" alt="Une boîte fermée étiquetée UserRepository vue à travers un écran à rayons X qui révèle ses trois méthodes, find, save et connect, cette dernière dessinée derrière un petit cadenas" width="560">

Voyez-la comme une radiographie. L'objet reste fermé, et vous avez pourtant une image complète de ce qu'il y a dedans.

## Où vous la croiserez vraiment

Soyez honnête sur la fréquence à laquelle vous écrirez `new ReflectionClass(...)` vous-même : rarement. **La Reflection existe pour que d'autres outils puissent travailler sur des classes qu'ils n'ont jamais vues.** Un conteneur d'injection de dépendances lit les paramètres d'un constructeur pour savoir quoi lui passer. PHPUnit s'en sert pour trouver vos méthodes de test. Laravel et Symfony s'y appuient en permanence, sous le capot.

Vous utiliserez la Reflection à travers ces outils bien plus souvent que directement. Mais la prochaine fois qu'un framework fera quelque chose d'apparemment magique avec une classe que vous venez d'écrire, vous saurez ce qui s'est passé. Il a pris une radio.
