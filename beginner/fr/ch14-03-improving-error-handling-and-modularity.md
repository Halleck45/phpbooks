# Refactoriser pour la modularité et la gestion des erreurs

Tout ce que fait phpgrep tient dans un seul script, de haut en bas : analyser les arguments, vérifier le fichier, le lire, boucler, afficher. Très bien pour trente lignes. Ça cesse de l'être dès que vous voulez tester une pièce sans lancer tout le programme, et c'est exactement là que ce projet se dirige. **Cette section découpe phpgrep en morceaux qu'on peut appeler séparément**, et remplace la rustine `file_exists()` par le mécanisme que PHP a conçu pour ça : une exception.

<img src="images/ch14-split.png" alt="Avant et après : à gauche, un long script qui fait tout ; à droite, le même programme en trois petits fichiers dans un dossier src, plus un script d'entrée mince qui se contente de les relier" width="600">

## Une exception qui porte un nom

Le [chapitre 9](ch09-00-error-handling.md) a plaidé pour lancer une exception précise et bien nommée plutôt que renvoyer une valeur sentinelle ou afficher une erreur en espérant que quelqu'un la vérifie. `RuntimeException` est la bonne classe de base pour « quelque chose a mal tourné pendant l'exécution, et l'appelant mérite une chance de s'en occuper ». Étendez-la avec un nom qui dit exactement ce qui s'est passé :

```php
<?php
// src/FileNotFoundException.php
declare(strict_types=1);

final class FileNotFoundException extends RuntimeException
{
}
```

C'est toute la classe. Elle n'ajoute aucun comportement, et elle n'en a pas besoin. **Toute sa valeur tient dans son nom.** Un `catch (FileNotFoundException $e)` dit à qui le lit précisément quel échec est traité, sans aller lire le code qui l'a lancé.

## Extraire `search()`

Sortez maintenant la lecture et la comparaison du script pour les mettre dans une fonction avec un vrai nom et un vrai contrat : elle prend un `GrepOptions`, renvoie les lignes qui correspondent, et lance une exception si le fichier ne peut pas être lu :

```php
<?php
// src/search.php
declare(strict_types=1);

require_once __DIR__ . '/FileNotFoundException.php';

function search(GrepOptions $options): array
{
    if (!is_readable($options->filename)) {
        throw new FileNotFoundException("Cannot read file: {$options->filename}");
    }

    $lines = file($options->filename, FILE_IGNORE_NEW_LINES);

    $matches = [];
    foreach ($lines as $line) {
        if (str_contains($line, $options->query)) {
            $matches[] = $line;
        }
    }

    return $matches;
}
```

`is_readable()` est un vrai progrès par rapport à `file_exists()`. Elle vérifie que le fichier existe *et* que le processus courant a la permission de le lire, ce qui est la condition dont `file()` a réellement besoin. Que l'un ou l'autre échoue, et `search()` lance aussitôt son exception, en nommant le fichier. Pas d'avertissement sur un flux que personne ne regarde, pas de résultat vide et muet, juste un échec net qu'un appelant peut attraper.

`GrepOptions` passe aussi dans son propre fichier, sans changement :

```php
<?php
// src/GrepOptions.php
declare(strict_types=1);

final class GrepOptions
{
    public function __construct(
        public readonly string $query,
        public readonly string $filename,
    ) {
    }

    public static function fromArgv(array $argv): self
    {
        return new self(
            query: $argv[1],
            filename: $argv[2],
        );
    }
}
```

## Le script d'entrée, réduit au câblage

Avec `GrepOptions` et `search()` dans `src/`, `phpgrep.php` se réduit à ce qu'il aurait toujours dû être : la partie qui parle au monde extérieur, et rien d'autre.

```php
<?php
// phpgrep.php
declare(strict_types=1);

require __DIR__ . '/src/GrepOptions.php';
require __DIR__ . '/src/FileNotFoundException.php';
require __DIR__ . '/src/search.php';

function main(array $argv): int
{
    if (count($argv) < 3) {
        echo "Usage: php phpgrep.php <query> <filename>\n";
        return 1;
    }

    $options = GrepOptions::fromArgv($argv);

    try {
        $matches = search($options);
    } catch (FileNotFoundException $e) {
        echo "Error: {$e->getMessage()}\n";
        return 1;
    }

    foreach ($matches as $line) {
        echo $line . "\n";
    }

    return 0;
}

exit(main($argv));
```

Regardez `main()` : **elle renvoie un code de sortie au lieu d'appeler `exit()` elle-même.** Le processus se termine à un seul endroit, la dernière ligne du fichier. Une fonction qui renvoie une valeur au lieu de tuer le processus est une fonction qu'on peut appeler de n'importe où, et « n'importe où » inclut un test, où vous préférez nettement récupérer les erreurs de `main()` sous forme de valeur à vérifier plutôt que de voir votre lanceur de tests disparaître au milieu de la suite.

```console
$ php phpgrep.php apple fruits.txt
apple sauce for the win

$ php phpgrep.php apple missing.txt
Error: Cannot read file: missing.txt
```

Même comportement vu de l'extérieur, et c'est voulu. Rien de *ce que* fait phpgrep n'a changé dans cette section, seulement la façon dont il est construit.

> Un refactoring qui change le comportement n'est pas un refactoring. C'est une réécriture déguisée.

Ce qui a changé, c'est que `search()` et `GrepOptions` vivent maintenant dans des fichiers qui ne font jamais `exit`, jamais `echo`, et ne touchent jamais à `$argv`. Pour la première fois, un test peut les appeler directement. C'est ce que fait la section suivante.
