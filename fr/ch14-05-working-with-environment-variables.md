# Travailler avec les variables d'environnement

`GrepOptions` porte un drapeau `ignoreCase` et `search()` le respecte, mais `fromArgv()` le fixe toujours à `false` en dur. Personne ne peut l'activer depuis un terminal. Réglons ça avec une variable d'environnement plutôt qu'un troisième argument.

Pourquoi pas simplement `$argv[3]` ? Parce qu'ignorer la casse tient plus de la préférence durable que de la décision prise à chaque recherche. C'est quelque chose que vous voudrez peut-être actif pour toutes les recherches d'une session, sans retaper une option à chaque fois. **Une variable d'environnement se règle une fois et se transmet à chaque commande lancée ensuite**, jusqu'à ce que vous fermiez le terminal ou la retiriez. C'est exactement l'outil qu'il faut pour une préférence.

<img src="images/ch14-env-sticky-note.png" alt="Une fenêtre de terminal avec un post-it PHPGREP_IGNORE_CASE=1 collé sur son cadre, et une rangée de petites commandes dans la fenêtre qui lèvent toutes les yeux vers le post-it" width="520">

## La lire avec `getenv()`

```php
<?php
// src/GrepOptions.php
declare(strict_types=1);

final class GrepOptions
{
    public function __construct(
        public readonly string $query,
        public readonly string $filename,
        public readonly bool $ignoreCase,
    ) {
    }

    public static function fromArgv(array $argv): self
    {
        return new self(
            query: $argv[1],
            filename: $argv[2],
            ignoreCase: getenv('PHPGREP_IGNORE_CASE') !== false,
        );
    }
}
```

**`getenv('PHPGREP_IGNORE_CASE')` renvoie la valeur de la variable sous forme de chaîne si elle est définie, et le booléen `false` si elle n'est pas définie du tout.** C'est pour cela que le test est `!== false`, et non une tentative d'interpréter la valeur. Résultat : `PHPGREP_IGNORE_CASE=1` active le drapeau, mais `PHPGREP_IGNORE_CASE=` sans rien après le `=` aussi. Une chaîne vide reste une valeur, et définir la variable, quelle qu'elle soit, compte comme « activé ». Si ce flou vous gêne, vous avez raison de le remarquer. Le resserrer (par exemple en exigeant que la valeur soit exactement `"1"`) est une bonne amélioration à faire de votre côté, une fois le chapitre terminé.

## À l'essai

```console
$ php phpgrep.php APPLE fruits.txt
```

Aucune sortie : `APPLE`, comparé en respectant la casse, n'apparaît ni dans la ligne `Apple` ni dans la ligne `apple`. Activez le drapeau :

```console
$ PHPGREP_IGNORE_CASE=1 php phpgrep.php APPLE fruits.txt
Apple pie recipe
apple sauce for the win
```

Écrire `PHPGREP_IGNORE_CASE=1` juste avant la commande, sur la même ligne, ne la définit que pour cette exécution. C'est un idiome courant du shell pour un réglage qui ne doit pas survivre à la commande qui le porte. Exportez-la à la place, et elle reste pour tout le reste de la session :

```console
$ export PHPGREP_IGNORE_CASE=1
$ php phpgrep.php APPLE fruits.txt
Apple pie recipe
apple sauce for the win
```

## `getenv()` contre `$_ENV`

PHP expose aussi l'environnement via la superglobale `$_ENV`, et il vaut la peine de savoir pourquoi ce chapitre ne l'a pas choisie. `$_ENV` n'est remplie que selon le réglage `variables_order` du `php.ini`. Sur beaucoup d'installations par défaut, surtout celles réglées pour servir des pages web, le `E` manque à ce réglage, et `$_ENV` reste vide quoi que contienne l'environnement du processus. `getenv()` n'a pas cette dépendance : elle interroge directement le système d'exploitation, à chaque appel, et se comporte pareil dans un script CLI, une requête web et tous les hébergements que vous êtes susceptible de croiser. Pour un outil censé tourner partout où on l'installe, cette constance vaut bien une syntaxe un peu moins à la mode.
