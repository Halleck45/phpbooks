# Améliorer notre projet en ligne de commande

Lancez `phpgrep` sur un fichier de log de deux gigaoctets et regardez. Rien ne se passe pendant un long moment. Puis toutes les lignes trouvées déboulent d'un coup. La fonction `search()` que vous avez écrite au [chapitre 14](ch14-00-a-cli-project.md) en est la cause :

```php
<?php
declare(strict_types=1);

function search(GrepOptions $options): array
{
    $contents = file_get_contents($options->filename);

    if ($contents === false) {
        throw new RuntimeException("Could not read file: {$options->filename}");
    }

    $matches = [];

    foreach (explode("\n", $contents) as $line) {
        $haystack = $options->ignoreCase ? strtolower($line) : $line;
        $needle = $options->ignoreCase ? strtolower($options->query) : $options->query;

        if (str_contains($haystack, $needle)) {
            $matches[] = $line;
        }
    }

    return $matches;
}
```

Deux choses se produisent en même temps. `file_get_contents()` lit le fichier *entier* dans une seule chaîne avant que `search()` fasse quoi que ce soit d'autre, et `$matches` grossit tant que la boucle tourne. Avec un demi-million de lignes correspondantes, `search()` ne rend rien tant qu'elle n'a pas construit un tableau qui les contient toutes. **Le fichier complet et toutes les lignes trouvées sont en mémoire en même temps**, et l'utilisateur ne voit rien avant que la dernière ligne ait été examinée.

## Réécrire `search()` en générateur

Maintenant que vous connaissez `yield`, la première correction est directe : cessez d'accumuler dans `$matches`, et faites un `yield` de chaque ligne trouvée à l'instant où vous la trouvez. Un second changement va avec. `file_get_contents()` chargerait encore tout le fichier d'entrée de jeu, alors remplacez-le par `fopen()` et `fgets()`, qui lisent une ligne à la fois. Sinon le générateur serait paresseux sur un fichier déjà entièrement en mémoire, ce qui rate la moitié de l'intérêt :

```php
<?php
declare(strict_types=1);

function searchLines(GrepOptions $options): Generator
{
    $handle = fopen($options->filename, 'r');

    if ($handle === false) {
        throw new RuntimeException("Could not read file: {$options->filename}");
    }

    $needle = $options->ignoreCase ? strtolower($options->query) : $options->query;

    while (($line = fgets($handle)) !== false) {
        $haystack = $options->ignoreCase ? strtolower($line) : $line;

        if (str_contains($haystack, $needle)) {
            yield $line;
        }
    }

    fclose($handle);
}
```

<img src="images/ch15-grep-stream.png" alt="Avant : le fichier entier est soulevé en mémoire et les lignes trouvées s'empilent pendant que l'écran reste vide. Après : les lignes traversent la fonction une par une jusqu'à l'écran, et la mémoire ne contient qu'une seule ligne" width="600">

Le fichier est maintenant lu une ligne à la fois, et chaque ligne trouvée sort par `yield` dès qu'elle est repérée, avant même que la suivante soit lue. **À tout moment, la fonction ne tient qu'une ligne, et rien d'autre.** Le contrôle d'erreur a bougé lui aussi : plus de `file_get_contents()` pour échouer, c'est `fopen()` qui signale un fichier introuvable, avec la même `RuntimeException` que vous avez rencontrée au [chapitre 9](ch09-02-exceptions.md).

Cette exception cache une subtilité, qui mérite une explication franche. Comme le corps de `searchLines()` contient `yield`, appeler `searchLines($options)` n'en exécute rien, `fopen()` compris. **L'exception ne part pas quand vous appelez la fonction. Elle part quand quelqu'un commence à itérer.** Et ça change l'endroit où il faut l'attraper.

## Mettre à jour `phpgrep.php`

Le script principal change à peine : il boucle toujours sur ce que la recherche lui donne et affiche chaque ligne. Mais le `try`/`catch` doit désormais entourer la boucle, pas seulement l'appel :

```php
<?php
declare(strict_types=1);

require __DIR__ . '/vendor/autoload.php';

$options = GrepOptions::fromArgv($argv);

try {
    foreach (searchLines($options) as $line) {
        echo $line;
    }
} catch (RuntimeException $e) {
    fwrite(STDERR, "Error: {$e->getMessage()}\n");
    exit(1);
}
```

Essayez la mauvaise version : gardez le `try` autour du seul appel, placez le `foreach` après le `catch`, et lancez `phpgrep` sur un fichier qui n'existe pas. Le bloc `try` se termine sans broncher, puisque rien n'a encore ouvert le fichier, et l'exception jaillit du `foreach` quelques lignes plus bas, sans personne pour l'attraper, avec une trace d'appels à la place de votre message d'erreur bien propre.

> Avec un générateur, l'erreur se produit là où les valeurs sont tirées, pas là où la fonction est appelée. Attrapez-la là.

## Pourquoi ça vaut le coup

Relancez `phpgrep` sur ce même fichier de deux gigaoctets. Avec le `search()` qui renvoie un tableau, vous attendez que le fichier entier soit parcouru, puis un demi-million de lignes s'affichent en une seule rafale, après que le programme les a toutes gardées en mémoire. Avec `searchLines()`, **la première ligne apparaît presque tout de suite**, avant que le reste du fichier ait été lu, parce que `foreach` n'avait besoin que d'une valeur pour commencer à afficher. Et la mémoire reste plate pendant toute l'exécution, quelle que soit la taille du fichier ou le nombre de résultats, parce que le programme ne tient qu'une ligne à la fois. Jamais « toutes les lignes trouvées jusqu'ici », jamais le fichier entier.

C'est le marché que propose un générateur : des résultats plus tôt, et un plafond de mémoire qui ne bouge pas, quelle que soit la taille de l'entrée.
