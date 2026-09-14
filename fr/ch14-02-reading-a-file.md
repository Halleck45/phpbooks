# Lire un fichier

phpgrep analyse ses arguments et ne cherche rien. Il est temps de lui donner un fichier. Créez-en un juste à côté de `phpgrep.php` :

```console
$ cat fruits.txt
Apple pie recipe
apple sauce for the win
Banana bread is better
cherry clafoutis
```

Quatre lignes, dont deux parlent de pommes, l'une avec une majuscule et l'autre sans. Ce détail est voulu, et il reviendra.

## Lire tout le fichier en lignes

**La fonction `file()` de PHP lit un fichier directement dans un tableau, un élément par ligne**, exactement la forme qu'attend une recherche ligne par ligne :

```php
<?php

$lines = file($options->filename, FILE_IGNORE_NEW_LINES);
```

<img src="images/ch14-file-to-lines.png" alt="Une feuille de papier passe dans file() et en ressort en pile de bandes séparées, une par ligne, puis dans un tamis marqué str_contains qui ne garde que la bande contenant le mot" width="600">

Le drapeau `FILE_IGNORE_NEW_LINES` retire le `\n` final de chaque ligne au passage, ce qui vous épargne un `trim()` sur chacune ensuite. Vous pourriez obtenir le même résultat avec `file_get_contents()` suivi de `explode("\n", ...)`, et vous verrez souvent ce duo dans du vrai code, surtout quand le contenu brut sert aussi à autre chose. Pour un outil qui pense en lignes, `file()` est la réponse directe.

## Chercher dans chaque ligne

Les lignes en main, `str_contains()` fait la comparaison. Elle est arrivée avec PHP 8, après des années où tout le monde bricolait `strpos($haystack, $needle) !== false`, et elle se lit comme ce qu'elle fait :

```php
<?php
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

if (count($argv) < 3) {
    echo "Usage: php phpgrep.php <query> <filename>\n";
    exit(1);
}

$options = GrepOptions::fromArgv($argv);

$lines = file($options->filename, FILE_IGNORE_NEW_LINES);

foreach ($lines as $line) {
    if (str_contains($line, $options->query)) {
        echo $line . "\n";
    }
}
```

```console
$ php phpgrep.php apple fruits.txt
apple sauce for the win
```

Seule la ligne avec `apple` en minuscules correspond. **`str_contains()` est sensible à la casse** : `"Apple pie recipe"` ne contient pas la sous-chaîne `"apple"`, à cause du A majuscule. Gardez ce fichier et ce comportement en tête. Dans deux sections, ils deviennent le cas de test exact de la recherche insensible à la casse.

## Le fichier qui n'existe pas

Pointez phpgrep vers un fichier qui n'existe pas :

```console
$ php phpgrep.php apple missing.txt

Warning: file(missing.txt): Failed to open stream: No such file or directory in phpgrep.php on line 20
```

Un avertissement, puis rien. `file()` renvoie `false` quand elle ne peut pas ouvrir sa cible, notre `foreach` traite ce `false` comme un tableau vide, et le programme se termine sans résultat et sans explication. **L'outil a l'air d'avoir cherché sans rien trouver, alors qu'il n'a rien lu du tout.** C'est la pire sorte d'échec, la silencieuse.

Colmatons avec l'outil le plus brut qui soit, une vérification avant la lecture :

```php
<?php

if (!file_exists($options->filename)) {
    echo "Error: file \"{$options->filename}\" not found.\n";
    exit(1);
}

$lines = file($options->filename, FILE_IGNORE_NEW_LINES);
```

```console
$ php phpgrep.php apple missing.txt
Error: file "missing.txt" not found.
```

Mieux, parce qu'au moins c'est honnête. Mais regardez ce que cette vérification achète, et ce qu'elle n'achète pas. `file_exists()` ne répond qu'à « y a-t-il quelque chose à ce chemin ». Elle ne dit rien sur le fait que *vous* puissiez le lire : un fichier qui existe mais dont les permissions sont verrouillées passe ce contrôle, puis échoue dans `file()` exactement comme avant, avertissement compris. Et chaque endroit de ce programme qui ouvrira un jour un fichier aurait besoin de la même vérification collée devant, chaque copie étant une occasion d'en oublier une.

<img src="images/ch14-locked-door.png" alt="Deux portes côte à côte : la première manque, il ne reste qu'un cadre vide ; la seconde existe mais porte un cadenas. file_exists() ne voit que le premier problème, is_readable() voit les deux" width="520">

Une garde maladroite et incomplète, à la place d'un mécanisme que PHP prévoit exprès. Il est temps de s'en servir.
