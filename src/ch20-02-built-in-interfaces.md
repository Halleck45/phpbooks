# Built-in Interfaces: Countable, ArrayAccess, IteratorAggregate

Back in [Chapter 11](ch11-00-interfaces-and-traits.md) you learned that an interface is a contract: implement its methods, and your class can be used anywhere that contract is expected. PHP takes that idea one step further with a small set of built-in interfaces, part of the SPL (Standard PHP Library), that don't just describe a contract for your own code: they plug your objects directly into PHP's own syntax. Implement one, and ordinary language constructs like `count()`, `$object['key']`, or `foreach` start working on your object as if it were a native array.

## `Countable`

Implement `count(): int`, and PHP's built-in `count()` function will call it for you:

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

Nothing here is more powerful than just calling `$playlist->count()` directly, but `count($playlist)` reads as "this behaves like a collection," which is exactly the impression you want to give the next person using your class.

## `ArrayAccess`

`ArrayAccess` is the more dramatic one: implement its four methods, and square-bracket syntax works on your object.

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

`offsetSet` backs `$config['debug'] = true`, `offsetGet` backs reading `$config['debug']`, `offsetExists` backs `isset($config[...])`, and `offsetUnset` backs `unset($config[...])`. Underneath, `Config` is still an ordinary object with an ordinary private array; `ArrayAccess` just lets the outside world address it with array syntax, which is a genuinely nice fit for something like a configuration object or a typed collection wrapper.

## `IteratorAggregate`

The third makes your object work directly in a `foreach`. Rather than implementing iteration logic yourself, `IteratorAggregate` asks for a single method, `getIterator()`, that hands back something already iterable, usually a `Generator` (from [Chapter 15](ch15-02-generators.md)):

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

That last `foreach` doesn't know or care that `$playlist` isn't a plain array; it just works, because `IteratorAggregate` told PHP where to find the values. There's also a lower-level `Iterator` interface, with methods like `current()`, `next()`, and `valid()`, for cases where you need finer control over iteration state; `IteratorAggregate` is the one you'll reach for almost always, since it lets a `Generator` do the bookkeeping for you.

Together these three interfaces are how you make a custom object feel native (indistinguishable, at the call site, from an array) while keeping whatever internal structure and validation your class actually needs.
