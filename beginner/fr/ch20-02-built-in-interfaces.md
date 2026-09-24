# Interfaces natives : Countable, ArrayAccess, IteratorAggregate

Appelez `count()` sur un objet que vous avez écrit, et PHP refuse : il compte des tableaux, pas des objets. Écrivez `$config['debug']`, et l'objet n'a aucune idée de ce que signifient des crochets. Mettez-le dans un `foreach`, et vous obtenez ses propriétés, pas les choses qu'il contient. **Un petit jeu d'interfaces natives règle les trois cas. Implémentez-en une, et la syntaxe de PHP se met à traiter votre objet comme un tableau.**

Une interface, comme l'a montré le [chapitre 11](ch11-00-interfaces-and-traits.md), est un contrat : implémentez ses méthodes et votre classe peut aller partout où ce contrat est attendu. Ces trois-là viennent de la SPL (Standard PHP Library), et la partie qui attend le contrat, c'est PHP lui-même.

<img src="images/ch20-three-sockets.png" alt="Un objet dessiné comme une boîte avec trois prises sur le côté, chacune recevant la fiche d'un morceau de syntaxe PHP : count(), les crochets et foreach" width="560">

## `Countable`

La plus petite. **Implémentez une méthode `count()`, et la fonction native `count()` de PHP l'appelle pour vous.**

```php
<?php

class Playlist implements Countable
{
    private array $tracks = [];

    public function add(string $track): void
    {
        $this->tracks[] = $track;
    }

    public function count(): int
    {
        return count($this->tracks);
    }
}

$playlist = new Playlist();
$playlist->add('Track One');
$playlist->add('Track Two');

echo count($playlist); // 2
```

Rien ici ne fait plus que ce que ferait `$playlist->count()`. Ce qui change, c'est ce que lit l'appelant : `count($playlist)` dit « cette chose est une collection », et c'est exactement l'impression que vous voulez donner à la prochaine personne qui utilisera votre classe.

## `ArrayAccess`

`ArrayAccess` est la plus spectaculaire. **Implémentez ses quatre méthodes, et les crochets fonctionnent sur votre objet.**

```php
<?php

class Config implements ArrayAccess
{
    private array $values = [];

    public function offsetExists(mixed $offset): bool
    {
        return isset($this->values[$offset]);
    }

    public function offsetGet(mixed $offset): mixed
    {
        return $this->values[$offset] ?? null;
    }

    public function offsetSet(mixed $offset, mixed $value): void
    {
        $this->values[$offset] = $value;
    }

    public function offsetUnset(mixed $offset): void
    {
        unset($this->values[$offset]);
    }
}

$config = new Config();
$config['debug'] = true;

echo $config['debug'] ? "on\n" : "off\n"; // on
echo isset($config['missing']) ? "yes\n" : "no\n"; // no
```

Chaque méthode répond à une forme de la syntaxe. `offsetSet` s'exécute pour `$config['debug'] = true`, `offsetGet` pour la lecture de `$config['debug']`, `offsetExists` pour `isset($config[...])`, et `offsetUnset` pour `unset($config[...])`. En dessous, `Config` reste un objet ordinaire avec un tableau privé ordinaire. `ArrayAccess` permet seulement au monde extérieur de s'adresser à lui avec la syntaxe des tableaux, et ça se lit bien pour un objet de configuration ou une enveloppe typée autour d'une collection.

Essayez : faites lever une exception à `offsetSet` quand `$offset` n'est pas une chaîne de caractères. Le code appelant ne change pas, et l'objet refuse désormais ce qu'un simple tableau aurait accepté sans broncher.

## `IteratorAggregate`

La troisième fait fonctionner votre objet dans un `foreach`. **`IteratorAggregate` demande une seule méthode, `getIterator()`, qui renvoie quelque chose de déjà itérable**, en général un `Generator` du [chapitre 15](ch15-02-generators.md). Vous n'écrivez pas la logique d'itération ; vous la désignez.

```php
<?php

class Playlist implements IteratorAggregate
{
    private array $tracks = [];

    public function add(string $track): void
    {
        $this->tracks[] = $track;
    }

    public function getIterator(): Generator
    {
        foreach ($this->tracks as $track) {
            yield $track;
        }
    }
}

$playlist = new Playlist();
$playlist->add('Track One');
$playlist->add('Track Two');

foreach ($playlist as $track) {
    echo "{$track}\n";
}
```

```console
$ php playlist.php
Track One
Track Two
```

Le `foreach` ne sait pas, et ne cherche pas à savoir, que `$playlist` n'est pas un tableau. Il a demandé à PHP où étaient les valeurs, et `IteratorAggregate` a répondu. Il existe aussi une interface de plus bas niveau, `Iterator`, avec `current()`, `next()`, `valid()` et compagnie, pour le cas rare où vous devez piloter l'état de l'itération à la main. Presque toujours, `IteratorAggregate` est celle qu'il faut choisir, parce que le générateur tient la comptabilité à votre place.

Réunissez les trois sur une même classe et elle devient indiscernable, du point de vue de l'appelant, d'un tableau, tout en conservant la validation et la structure interne qu'un tableau ne pourrait jamais imposer.

> Implémentez l'interface, et la syntaxe suit. En dessous, l'objet garde sa propre structure et ses propres règles.
