# Syntaxe des callables de première classe et closures avancées

`array_map('strlen', ...)`. Cette chaîne de caractères est la façon de passer une fonction en argument depuis les débuts de PHP, et elle a toujours eu quelque chose de bancal : pour votre éditeur, c'est une chaîne qui se trouve contenir un nom de fonction. **PHP 8.1 a donné aux fonctions et aux méthodes un vrai moyen de circuler comme des valeurs.** Cette section le montre, avec deux astuces de `Closure` pour du code plus délibéré. Les closures et les fonctions fléchées elles-mêmes sont au [chapitre 15](ch15-01-closures.md).

## L'ancienne façon de passer une fonction

Avant PHP 8.1, passer une fonction ou une méthode existante à `array_map()` voulait dire une chaîne ou un tableau :

```php
<?php

$lengths = array_map('strlen', ['a', 'bb', 'ccc']);

class Greeter
{
    public function greet(string $name): string
    {
        return "Hello, {$name}!";
    }
}

$greeter = new Greeter();
$greetCallable = [$greeter, 'greet'];

echo $greetCallable('Sam'), "\n"; // Hello, Sam!
```

Ça marche, et vous le verrez dans quantité de code existant. Mais `$greetCallable` n'est qu'un tableau qui contient un objet et une chaîne. Votre éditeur ne peut pas sauter de `'greet'` à la méthode, et une faute de frappe dans le nom n'est détectée qu'à la ligne qui l'appelle.

<img src="images/ch20-callable-handle.png" alt="À gauche, un bout de papier portant le mot strlen, qui flotte avec un point d'interrogation ; à droite, strlen(...) dessiné comme une poignée solide attachée directement à la fonction elle-même" width="560">

## La syntaxe des callables de première classe

**Écrivez le nom de la fonction ou de la méthode suivi de `(...)`, trois points littéraux, et PHP vous rend une `Closure` qui pointe dessus.**

```php
<?php

$lengths = array_map(strlen(...), ['a', 'bb', 'ccc']);

class Greeter
{
    public function greet(string $name): string
    {
        return "Hello, {$name}!";
    }
}

$greeter = new Greeter();
$greetCallable = $greeter->greet(...);

echo $greetCallable('Sam'), "\n"; // Hello, Sam!
```

Même comportement, une différence qui compte : `strlen(...)` et `$greeter->greet(...)` sont de vraies références, et vos outils les comprennent. Le saut vers la définition fonctionne. L'analyse statique vérifie la signature. Renommez `greet()` et la référence périmée est repérée aussitôt, au lieu d'échouer à l'exécution. Ça se lit mieux, aussi : `$greeter->greet(...)` dit « la méthode `greet`, en tant que valeur », et c'est exactement ce qui se passe.

> Une chaîne, c'est un nom écrit sur un bout de papier. `strlen(...)`, c'est une poignée sur la fonction elle-même.

Essayez : écorchez `greet` dans les deux versions. L'ancienne échoue à l'appel. La nouvelle échoue à la ligne qui crée la closure, avant que quoi que ce soit d'autre puisse mal tourner.

## `Closure::fromCallable()`

Parfois, le callable vient de l'extérieur : une valeur de configuration, une chaîne lue dans un fichier. On vous tend l'une des formes traditionnelles et vous voulez un vrai objet `Closure`, pour pouvoir appeler dessus des méthodes comme `bindTo()`. **`Closure::fromCallable()` convertit n'importe quelle forme de callable en `Closure`.**

```php
<?php

$callableFromConfig = 'strtoupper';

$closure = Closure::fromCallable($callableFromConfig);

echo $closure('hello'), "\n"; // HELLO
```

Dans du code neuf, la syntaxe des callables de première classe couvre la plupart des raisons de s'en servir. Vous verrez encore `Closure::fromCallable()` dans le code de bibliothèques qui doivent accepter un callable sous n'importe laquelle de ses formes historiques et le normaliser.

## Les closures statiques

Une closure définie dans une méthode capture discrètement `$this`. La plupart du temps, c'est pratique : la closure peut rappeler l'objet qui l'a créée. Parfois, vous voulez la garantie inverse, parce que la closure va être confiée ailleurs et doit rester autonome. **Marquez-la `static`, et elle ne peut plus toucher l'objet où elle est née.**

```php
<?php

class Report
{
    private string $secret = 'internal data';

    public function makeFormatter(): Closure
    {
        return static function (string $line): string {
            return strtoupper($line);
        };
    }
}

$formatter = (new Report())->makeFormatter();

echo $formatter('quarterly summary'), "\n"; // QUARTERLY SUMMARY
```

<img src="images/ch20-static-closure.png" alt="Deux closures quittent le même objet : une closure ordinaire encore reliée à l'objet par un fil étiqueté $this, et une closure statique dont le fil a été coupé, qui s'éloigne seule" width="560">

Une closure `static function` se comporte exactement comme une closure ordinaire, sauf que `$this` y est indisponible : tenter de l'utiliser est une erreur à la compilation, pas une surprise à l'exécution. Une petite garantie, mais une vraie. Elle dit au lecteur, et à PHP lui-même, que le formateur n'a aucun fil caché vers le `Report` qui l'a créé.
