# Variable Scope and Garbage Collection

## Functions have their own scope

Every function in PHP gets its own private set of variables, completely separate from whatever's happening outside it. A variable defined in one function simply doesn't exist as far as another function, or the top-level script, is concerned:

```php
<?php
declare(strict_types=1);

function greet(): void
{
    $message = "Hello from inside greet()";
    echo $message . "\n";
}

greet();
echo $message ?? "no such variable out here\n";
```

`$message` inside `greet()` and any `$message` you might have floating around outside it are entirely unrelated, even though they share a name. This is called **local scope**, and it's the sane default: without it, every variable name in every function would be competing for the same shared space, and calling a function you didn't write yourself would be a small act of faith that it hadn't quietly stomped on one of your variables.

## `global`, and why you'll rarely reach for it

PHP does have a way to let a function read and write a variable from the outer, top-level scope: the `global` keyword.

```php
<?php
declare(strict_types=1);

$counter = 0;

function increment(): void
{
    global $counter;
    $counter++;
}

increment();
increment();
echo $counter; // 2
```

It works. It's also almost never the right tool. A function that reaches out through `global` to modify state that lives entirely outside its own parameters and return value is a function whose behavior you can't understand by reading its signature: you have to go find every `global $counter` scattered across the codebase to know who might change it, and in what order. That's the kind of bug that's invisible in a five-line example and genuinely painful in a five-thousand-line application. Prefer passing values in as parameters and getting results back as return values (or, once we reach [Chapter 5](ch05-00-classes.md), storing shared state as a property on an object you pass around deliberately). If you find yourself reaching for `global`, it's usually a sign the function wants a parameter instead.

## `static` variables inside functions

There's a second, much better-behaved way for a function to remember something between calls: a `static` local variable. Unlike an ordinary local variable, which is created fresh and destroyed every time the function runs, a `static` variable keeps its value from one call to the next, but only that one function can see or touch it.

```php
<?php
declare(strict_types=1);

function nextId(): int
{
    static $id = 0;
    $id++;
    return $id;
}

echo nextId(); // 1
echo nextId(); // 2
echo nextId(); // 3
```

`$id = 0` only runs the very first time `nextId()` is called; every call after that picks up wherever the previous one left off. Nothing outside `nextId()` can read or reset `$id`; there's no `global`-style leak here, just a function with a genuinely private memory of its own. It's a handy pattern for small counters, simple caches, or "have I already done this setup step" flags, without reaching for a full object just to hold one number.

## A brief, honest word about garbage collection

You may hear people mention PHP's "garbage collector," usually in the context of memory leaks or long-running scripts, and it's worth knowing roughly what that means even though you'll rarely think about it day to day.

Every value PHP creates (every array, every object) is tracked with a reference count: how many variables currently point at it. When that count drops to zero, because the last variable pointing at it went out of scope or got reassigned, PHP frees the memory immediately. This is the mechanism quietly making copy-on-write work, back in the [first section of this chapter](ch04-01-copy-on-write.md): PHP knows exactly how many places are sharing a given array at any moment.

Reference counting alone has one blind spot: two objects that reference each other form a *cycle*, and a cycle can end up with nothing left in the rest of your program pointing at it, while the two objects inside the cycle still point at each other, so their reference counts never quite reach zero. PHP handles this with a separate cycle collector that runs periodically, finds these orphaned cycles, and cleans them up anyway.

The honest summary: you don't manage memory in PHP. There's no `malloc`, no `free`, no manual bookkeeping of who owns what. Values disappear when nothing needs them anymore, and PHP figures out "nothing needs them anymore" for you, cycles included. That's not a gap compared to languages that make you think about memory explicitly; it's the entire point. Keep the vocabulary in your back pocket for the rare occasion you're debugging memory growth in a long-running script, and otherwise let it do its job.
