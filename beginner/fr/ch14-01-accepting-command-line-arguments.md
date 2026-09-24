# Accepter des arguments en ligne de commande

Créez un répertoire pour le projet et, dedans, un fichier `phpgrep.php`. **Tout ce qui est tapé après `php` sur la ligne de commande atterrit dans un tableau nommé `$argv`**, disponible dans tout script lancé depuis un terminal :

```php
<?php
declare(strict_types=1);

var_dump($argv);
```

```console
$ php phpgrep.php apple fruits.txt
array(3) {
  [0]=>
  string(11) "phpgrep.php"
  [1]=>
  string(5) "apple"
  [2]=>
  string(9) "fruits.txt"
}
```

<img src="images/ch14-argv-slots.png" alt="La ligne de commande php phpgrep.php apple fruits.txt, chaque mot après php tombant dans une case numérotée du tableau $argv : le nom du script en case 0, apple en case 1, fruits.txt en case 2" width="560">

Première surprise, si vous n'avez jamais croisé `$argv` : `$argv[0]` n'est pas votre premier argument. C'est le nom du script lui-même. Tout le monde s'y fait prendre une fois. Vos vrais arguments commencent à l'indice `1` : ici, `$argv[1]` est le mot à chercher et `$argv[2]` le fichier dans lequel chercher, et c'est toute l'interface dont phpgrep a besoin.

## Lire deux arguments, mal

La façon la plus directe de les attraper :

```php
<?php
declare(strict_types=1);

$query = $argv[1];
$filename = $argv[2];

echo "Searching for \"{$query}\" in \"{$filename}\"\n";
```

Lancez-le correctement, et ça marche. Lancez-le maintenant avec un argument de moins :

```console
$ php phpgrep.php apple
```

PHP affiche un avertissement pour le `$argv[2]` manquant, le remplace par `null`, et continue en boitant avec une entrée bidon au lieu de s'arrêter pour dire ce qui cloche. Tolérable tant que vous êtes le seul utilisateur. Pas pour un outil que quelqu'un d'autre lancera un jour. Ajoutons une garde à l'entrée :

```php
<?php
declare(strict_types=1);

if (count($argv) < 3) {
    echo "Usage: php phpgrep.php <query> <filename>\n";
    exit(1);
}

$query = $argv[1];
$filename = $argv[2];

echo "Searching for \"{$query}\" in \"{$filename}\"\n";
```

**`exit(1)` arrête le script sur-le-champ et renvoie le nombre `1` au shell comme code de sortie.** Par convention Unix, `0` veut dire « ça a marché » et tout le reste veut dire « quelque chose a mal tourné ». Chaque commande que vous avez enchaînée avec `&&`, chaque `$?` que vous avez vérifié dans un shell repose sur cette convention. phpgrep la respecte dès sa toute première version.

## Donner un toit aux arguments : `GrepOptions`

Deux variables en vrac, ça va pour aujourd'hui. Mais ce projet va grandir, et passer deux chaînes séparées à chaque fonction que vous écrirez devient vite pénible. Mieux vaut les regrouper dans une petite classe dont le seul rôle est de retenir ce qu'on a demandé au programme pour cette exécution :

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

echo "Searching for \"{$options->query}\" in \"{$options->filename}\"\n";
```

Deux propriétés `readonly`, fixées une fois pour toutes par promotion de constructeur, comme au [chapitre 5](ch05-00-classes.md). **Un `GrepOptions` ne change plus une fois construit**, ce qui est exactement ce qu'il faut pour un objet qui représente la demande de l'utilisateur pendant toute la durée d'une exécution. `fromArgv()` est une fabrique statique : donnez-lui le tableau `$argv` brut, elle rend un `GrepOptions` complet. La question « comment analyse-t-on les arguments » a maintenant une réponse, à un seul endroit.

Relancez pour vérifier que rien n'a changé vu de l'extérieur :

```console
$ php phpgrep.php apple fruits.txt
Searching for "apple" in "fruits.txt"
```

Même comportement, meilleure ossature. C'est tout l'intérêt d'introduire la classe aussi tôt : elle ne coûte presque rien maintenant, et c'est précisément la couture dont le reste du chapitre a besoin. La classe gagnera bientôt une troisième propriété. Sa forme et son rôle ne bougeront pas.
