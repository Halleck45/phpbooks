# C - Built-in Interfaces and Magic Methods

Two reference tables: the SPL interfaces that let your objects plug into PHP's built-in language features, and the magic methods that let your objects hook into behavior PHP would otherwise handle for you.

## Built-in interfaces

| Interface | Implementing it gets you |
|---|---|
| `Countable` | Your objects work with `count()` |
| `ArrayAccess` | Your objects support `$obj[$key]` syntax: read, write, isset, and unset |
| `Iterator` | Your objects work directly in `foreach`, with full control over the iteration |
| `IteratorAggregate` | Your objects work in `foreach` by delegating to another iterator, usually a `Generator` |
| `Stringable` | Your objects can be used anywhere a string is expected |

`Stringable` is the odd one out: it was added in PHP 8, and you rarely need to implement it explicitly, since any class that defines `__toString()` is automatically treated as implementing it. It exists mostly so type declarations can say "anything printable," rather than listing every class that happens to have a `__toString()` method.

Full examples of all five, including what `Iterator` demands of you that `IteratorAggregate` doesn't, are in [Chapter 20](ch20-02-built-in-interfaces.md).

## Magic methods

| Method | Called when |
|---|---|
| `__construct` | An object is created |
| `__destruct` | An object is about to be destroyed |
| `__get` | Reading an inaccessible or undefined property |
| `__set` | Writing to an inaccessible or undefined property |
| `__call` | Calling an inaccessible or undefined instance method |
| `__callStatic` | Calling an inaccessible or undefined static method |
| `__toString` | The object is used in a string context |
| `__invoke` | The object is called as if it were a function |
| `__clone` | The object is duplicated with `clone` |

"Magic" is PHP's word for methods the language calls for you, by naming convention, rather than you calling directly. Useful for building things like lazy-loaded properties or fluent proxies, easy to overuse into code nobody can trace by reading it. Full treatment, with the tradeoffs, in [Chapter 17](ch17-03-magic-methods.md).
