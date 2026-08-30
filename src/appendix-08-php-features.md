# H - Covered PHP Features

Every chapter in this book introduces a piece of PHP: a keyword, an operator, a built-in interface, a language mechanism. This appendix pulls them all into one list, each one linked to its entry in the [PHP Dictionary](https://php-dictionary.readthedocs.io/en/latest/), an independent, ever-growing reference of PHP terms, keywords, functions, and jargon. Use it the way you'd use any glossary: when a term from an earlier chapter comes back and you want the short version again, without hunting back through the chapter that first introduced it.

A handful of items below have no dictionary entry yet. They're listed anyway, plainly, without a link.

## Syntax and basics

- [Opening tag `<?php`](https://php-dictionary.readthedocs.io/en/latest/index/php-tag.html): switches the parser from HTML mode into PHP mode.
- [Short echo tag `<?= ?>`](https://php-dictionary.readthedocs.io/en/latest/index/echo-tag.html): shorthand that combines `<?php` with an immediate `echo`.
- [`echo`](https://php-dictionary.readthedocs.io/en/latest/index/echo.html) and [`print`](https://php-dictionary.readthedocs.io/en/latest/index/print.html): output constructs, covered in [Chapter 1](ch01-02-hello-world.md).
- [String interpolation](https://php-dictionary.readthedocs.io/en/latest/index/interpolation.html): embedding variables directly inside a double-quoted string.
- [Comments](https://php-dictionary.readthedocs.io/en/latest/index/comment.html) and [docblocks](https://php-dictionary.readthedocs.io/en/latest/index/docblock.html): `//`, `#`, `/* */`, and the structured `/** */` form tools read, from [Chapter 3](ch03-04-comments.md).

## Types and comparison

- [Type juggling](https://php-dictionary.readthedocs.io/en/latest/index/type-juggling.html): PHP's automatic conversion between types depending on context.
- [Casting](https://php-dictionary.readthedocs.io/en/latest/index/cast.html): explicit conversion with `(int)`, `(string)`, and the rest.
- [Boolean](https://php-dictionary.readthedocs.io/en/latest/index/boolean.html), [`gettype()`](https://php-dictionary.readthedocs.io/en/latest/index/gettype.html), [`var_dump()`](https://php-dictionary.readthedocs.io/en/latest/index/var_dump.html): the scalar type system and how to inspect it, from [Chapter 3](ch03-02-data-types.md).
- [`declare(strict_types=1)`](https://php-dictionary.readthedocs.io/en/latest/index/strict_types.html): opts a file out of implicit scalar coercion.
- [Identical operator `===`](https://php-dictionary.readthedocs.io/en/latest/index/identical.html), [equal operator `==`](https://php-dictionary.readthedocs.io/en/latest/index/equal.html), [loose comparison](https://php-dictionary.readthedocs.io/en/latest/index/relaxed-comparison.html): the two families of comparison and where they diverge.
- [Spaceship operator `<=>`](https://php-dictionary.readthedocs.io/en/latest/index/spaceship.html): three-way comparison, returns `-1`, `0`, or `1`.
- [Union types](https://php-dictionary.readthedocs.io/en/latest/index/union-type.html): a parameter or return type expressed as `int|string`.
- [`TypeError`](https://php-dictionary.readthedocs.io/en/latest/index/typeerror.html): thrown when a value doesn't satisfy a type declaration.
- [Array](https://php-dictionary.readthedocs.io/en/latest/index/array.html): PHP's one compound type doing double duty as list and map, from [Chapter 8](ch08-01-indexed-arrays.md).
- [`array_key_exists()`](https://php-dictionary.readthedocs.io/en/latest/index/array_key_exists.html) and [`isset()`](https://php-dictionary.readthedocs.io/en/latest/index/isset.html): checking for a key versus checking for a non-null value.

## Control flow

- [`if` / `elseif` / `else`](https://php-dictionary.readthedocs.io/en/latest/index/if-then.html) and [conditional structures](https://php-dictionary.readthedocs.io/en/latest/index/conditional-structure.html) generally.
- [`while`](https://php-dictionary.readthedocs.io/en/latest/index/while.html), [`do`-`while`](https://php-dictionary.readthedocs.io/en/latest/index/do-while.html), [`for`](https://php-dictionary.readthedocs.io/en/latest/index/for.html), [`foreach`](https://php-dictionary.readthedocs.io/en/latest/index/foreach.html): the loop constructs, from [Chapter 3](ch03-05-control-flow.md).
- [`break`](https://php-dictionary.readthedocs.io/en/latest/index/break.html) and [`continue`](https://php-dictionary.readthedocs.io/en/latest/index/continue.html): leaving or skipping ahead in a loop, including their optional numeric argument for nested loops.
- [`switch`](https://php-dictionary.readthedocs.io/en/latest/index/switch.html) and [`match`](https://php-dictionary.readthedocs.io/en/latest/index/match.html): the two branch-and-compare constructs, one a statement, one an expression, covered together in [Chapter 6](ch06-02-match.md) and again as pattern syntax in [Chapter 19](ch19-03-match-syntax.md).
- [`list()` / array destructuring](https://php-dictionary.readthedocs.io/en/latest/index/list.html) and [destructuring](https://php-dictionary.readthedocs.io/en/latest/index/destructuring.html) generally: unpacking an array into separate variables in one step, from [Chapter 19](ch19-02-destructuring.md).

## Functions and closures

- Function declarations, [return type declarations](https://php-dictionary.readthedocs.io/en/latest/index/return-type.html), and [default parameter values](https://php-dictionary.readthedocs.io/en/latest/index/default-value.html).
- [`void`](https://php-dictionary.readthedocs.io/en/latest/index/void.html): a return type declaring that a function returns nothing meaningful.
- [Named arguments](https://php-dictionary.readthedocs.io/en/latest/index/named-parameter.html): calling a function by parameter name instead of position.
- [Passing by reference](https://php-dictionary.readthedocs.io/en/latest/index/by-reference.html) versus [passing by value](https://php-dictionary.readthedocs.io/en/latest/index/by-value.html): whether a function can modify the caller's variable.
- [Anonymous functions](https://php-dictionary.readthedocs.io/en/latest/index/anonymous-function.html) and [closures](https://php-dictionary.readthedocs.io/en/latest/index/closure.html): functions as values, with variables captured via `use`, from [Chapter 15](ch15-01-closures.md).
- [Arrow functions (`fn`)](https://php-dictionary.readthedocs.io/en/latest/index/arrow-function.html): single-expression closures with implicit capture of the outer scope.
- [First-class callable syntax `foo(...)`](https://php-dictionary.readthedocs.io/en/latest/index/first-class-callable.html): converting a named function or method reference into a real `Closure`.
- [Generators](https://php-dictionary.readthedocs.io/en/latest/index/generator.html) and [`yield`](https://php-dictionary.readthedocs.io/en/latest/index/yield.html): functions that produce values lazily, one at a time, from [Chapter 15](ch15-02-generators.md).

## Classes and objects

- [Class declarations](https://php-dictionary.readthedocs.io/en/latest/index/class.html), [`new`](https://php-dictionary.readthedocs.io/en/latest/index/new.html), [`instanceof`](https://php-dictionary.readthedocs.io/en/latest/index/instanceof.html), [`clone`](https://php-dictionary.readthedocs.io/en/latest/index/clone.html): the basic vocabulary of object creation.
- [Visibility](https://php-dictionary.readthedocs.io/en/latest/index/visibility.html) (`public`, `protected`, `private`): controlling access to properties and methods.
- [Constructor property promotion](https://php-dictionary.readthedocs.io/en/latest/index/promoted-property.html) and [`readonly` properties](https://php-dictionary.readthedocs.io/en/latest/index/readonly.html): shorthand construction and write-once properties, from [Chapter 5](ch05-01-defining-classes.md).
- [Typed properties](https://php-dictionary.readthedocs.io/en/latest/index/type-declaration-property.html): declaring a property's type up front.
- [`static` properties and methods](https://php-dictionary.readthedocs.io/en/latest/index/static.html), [static variables](https://php-dictionary.readthedocs.io/en/latest/index/static-variable.html), and [late static binding](https://php-dictionary.readthedocs.io/en/latest/index/late-static-binding.html): the several unrelated jobs the `static` keyword does.
- [Inheritance](https://php-dictionary.readthedocs.io/en/latest/index/inheritance.html), [`extends`](https://php-dictionary.readthedocs.io/en/latest/index/extends.html), and [`parent::`](https://php-dictionary.readthedocs.io/en/latest/index/parent.html): building one class on top of another, from [Chapter 17](ch17-01-inheritance-and-polymorphism.md).
- [Abstract classes](https://php-dictionary.readthedocs.io/en/latest/index/abstract-class.html) and [abstract methods](https://php-dictionary.readthedocs.io/en/latest/index/abstract-method.html): base classes that can't be instantiated on their own.
- [Interfaces](https://php-dictionary.readthedocs.io/en/latest/index/interface.html) and [traits](https://php-dictionary.readthedocs.io/en/latest/index/trait.html): shared contracts versus shared implementation, from [Chapter 11](ch11-01-interfaces.md).
- [Constructor (`__construct`)](https://php-dictionary.readthedocs.io/en/latest/index/constructor.html), [destructor (`__destruct`)](https://php-dictionary.readthedocs.io/en/latest/index/destructor.html), and other magic methods: [`__toString()`](https://php-dictionary.readthedocs.io/en/latest/index/__tostring.html), [`__get()` / `__set()`](https://php-dictionary.readthedocs.io/en/latest/index/__get.html), [`__call()`](https://php-dictionary.readthedocs.io/en/latest/index/__call.html), covered in [Chapter 17](ch17-03-magic-methods.md).
- [Generics, via docblocks](https://php-dictionary.readthedocs.io/en/latest/index/generics.html): PHP has no native generics, so static analysis tools read the type from a comment instead, discussed in [Chapter 11](ch11-03-generic-style-code.md).

## Enums

- [Enums](https://php-dictionary.readthedocs.io/en/latest/index/enum.html): pure and backed cases, covered in [Chapter 6](ch06-00-enums.md).

## Namespaces and autoloading

- [Namespaces](https://php-dictionary.readthedocs.io/en/latest/index/namespace.html) and `use` imports: organizing and importing names, from [Chapter 7](ch07-03-use-keyword.md).
- [Autoloading](https://php-dictionary.readthedocs.io/en/latest/index/autoload.html): loading class files on demand instead of with a pile of `require` statements.
- **PSR-4**: the autoloading standard Composer implements, covered in [Chapter 7](ch07-05-psr4.md). Not yet in the dictionary; only mentioned there in passing.

## Error handling

- [`Exception`](https://php-dictionary.readthedocs.io/en/latest/index/exception.html), [`Error`](https://php-dictionary.readthedocs.io/en/latest/index/error.html), [`Throwable`](https://php-dictionary.readthedocs.io/en/latest/index/throwable.html): PHP's two parallel throwable hierarchies, from [Chapter 9](ch09-00-error-handling.md).
- [`try` / `catch` / `finally`](https://php-dictionary.readthedocs.io/en/latest/index/try-catch.html) and [`DivisionByZeroError`](https://php-dictionary.readthedocs.io/en/latest/index/divisionbyzeroerror.html): catching and handling failure.
- [`RuntimeException`](https://php-dictionary.readthedocs.io/en/latest/index/predefined-exception.html): one of PHP's built-in exception subclasses, used as a base in the CLI project starting [Chapter 14](ch14-03-improving-error-handling-and-modularity.md).
- **Custom exception classes** (`extends Exception`): a common idiom, but not yet its own dictionary entry.

## Web and databases

- [Superglobals](https://php-dictionary.readthedocs.io/en/latest/index/superglobal.html), [`$_GET`](https://php-dictionary.readthedocs.io/en/latest/index/%24_get.html), [`$_POST`](https://php-dictionary.readthedocs.io/en/latest/index/%24_post.html), and [`$_SERVER`](https://php-dictionary.readthedocs.io/en/latest/index/%24_server.html): reading a web request's data, from [Chapter 10](ch10-01-forms-and-superglobals.md).
- [`htmlspecialchars()`](https://php-dictionary.readthedocs.io/en/latest/index/htmlspecialchars.html) and [XSS](https://php-dictionary.readthedocs.io/en/latest/index/xss.html): escaping output to stop an attacker's markup from running in someone else's browser, from [Chapter 10](ch10-02-validation-and-xss.md).
- [CSRF](https://php-dictionary.readthedocs.io/en/latest/index/csrf.html): forged cross-site requests, named but not defended against in this book, from [Chapter 10](ch10-02-validation-and-xss.md).
- [PDO](https://php-dictionary.readthedocs.io/en/latest/index/pdo.html), [`PDOException`](https://php-dictionary.readthedocs.io/en/latest/index/pdoexception.html), and [SQLite3](https://php-dictionary.readthedocs.io/en/latest/index/sqlite3.html): a consistent, file-based way to talk to a database, from [Chapter 10](ch10-03-talking-to-a-database.md).
- [Prepared statements](https://php-dictionary.readthedocs.io/en/latest/index/prepared-query.html) and [SQL injection](https://php-dictionary.readthedocs.io/en/latest/index/sql-injection.html): separating a query's structure from its values to stop an attacker from rewriting the query.

## Debugging

- [`var_dump()`](https://php-dictionary.readthedocs.io/en/latest/index/var_dump.html), [`print_r()`](https://php-dictionary.readthedocs.io/en/latest/index/print_r.html), and [`var_export()`](https://php-dictionary.readthedocs.io/en/latest/index/var_export.html): printing a value's structure (and, for `var_dump()`, its type) while chasing a bug, from [Chapter 13](ch13-01-print-debugging.md).
- [Xdebug](https://php-dictionary.readthedocs.io/en/latest/index/xdebug.html): a step debugger and profiler, pausing execution at a breakpoint instead of guessing where to print, from [Chapter 13](ch13-02-xdebug.md).
- [Profiling](https://php-dictionary.readthedocs.io/en/latest/index/profiling.html): measuring where a script actually spends its time, one of Xdebug's other jobs.

## Concurrency

- [`pcntl`](https://php-dictionary.readthedocs.io/en/latest/index/pcntl.html): the extension behind forking and controlling separate OS processes.

## Reflection and attributes

- [Reflection](https://php-dictionary.readthedocs.io/en/latest/index/reflection.html): inspecting classes, methods, properties, and attributes at runtime, from [Chapter 20](ch20-01-reflection.md).
- [Magic constants](https://php-dictionary.readthedocs.io/en/latest/index/magic-constant.html) (`__CLASS__`, `__FUNCTION__`, `__METHOD__`, `__LINE__`, `__FILE__`): compile-time constants describing the code's own location.
- [Attributes `#[...]`](https://php-dictionary.readthedocs.io/en/latest/index/attribute.html): structured metadata attached to code and read back through Reflection, from [Chapter 20](ch20-04-attributes.md).

## Built-in interfaces

- [`Countable`](https://php-dictionary.readthedocs.io/en/latest/index/countable.html): lets `count()` work on a custom object.
- [`ArrayAccess`](https://php-dictionary.readthedocs.io/en/latest/index/arrayaccess.html): enables square-bracket access on a custom object.
- [`Iterator`](https://php-dictionary.readthedocs.io/en/latest/index/iterator.html) and [`IteratorAggregate`](https://php-dictionary.readthedocs.io/en/latest/index/iteratoraggregate.html): the two ways to make an object work in `foreach`, from [Chapter 20](ch20-02-built-in-interfaces.md).

## Odds and ends

- [`global`](https://php-dictionary.readthedocs.io/en/latest/index/global.html): pulling a variable in from the global scope.
- [Copy-on-write](https://php-dictionary.readthedocs.io/en/latest/index/copy-on-write.html): why passing an array by value is cheap until something actually writes to it, from [Chapter 4](ch04-01-copy-on-write.md).
- [Garbage collection](https://php-dictionary.readthedocs.io/en/latest/index/garbage-collection.html): how PHP reclaims memory from objects nobody references anymore.
- [`assert()`](https://php-dictionary.readthedocs.io/en/latest/index/assertion.html): a debug-time sanity check, from [Chapter 12](ch12-00-testing.md).
- [PHPUnit](https://php-dictionary.readthedocs.io/en/latest/index/phpunit.html): the testing framework used throughout the book's later chapters.
- [`getenv()`](https://php-dictionary.readthedocs.io/en/latest/index/getenv.html) and [`$_ENV`](https://php-dictionary.readthedocs.io/en/latest/index/$_env.html): reading environment variables, from [Chapter 14](ch14-05-working-with-environment-variables.md).
- [`fwrite(STDERR, ...)`](https://php-dictionary.readthedocs.io/en/latest/index/fwrite.html): writing to standard error instead of standard output.
- [Output buffering](https://php-dictionary.readthedocs.io/en/latest/index/output-buffering.html): capturing generated output into a buffer instead of sending it immediately.
- [`register_shutdown_function()`](https://php-dictionary.readthedocs.io/en/latest/index/shutdown-function.html): a callback PHP guarantees to run at the end of a script, from [Chapter 21](ch21-03-shutdown-and-cleanup.md).
- **`$this`** and **`STDIN`**: both used constantly from [Chapter 2](ch02-00-guessing-game-tutorial.md) onward, neither has its own dictionary entry yet.
- **`random_int()`**: PHP's cryptographically secure random integer function, also not yet listed.

The gaps are worth noticing as much as the links. A few things this book leans on hard, `$this`, `STDIN`, PSR-4, custom exception classes, don't have an entry in the dictionary yet. If you find yourself explaining one of them to someone else, that explanation is most of a dictionary entry already.
