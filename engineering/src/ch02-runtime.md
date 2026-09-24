# The Runtime

**PHP executes one request per process or thread, on the Zend Engine, shared-nothing by default: nothing your code puts in memory survives past the response it just sent, unless you explicitly change the serving model to keep the application booted.** That single sentence is the answer to most of the runtime questions an evaluator brings to this book, and it deserves a pause before you read anything else in this chapter, because almost everything else PHP does or does not do well is a consequence of it.

Shared-nothing execution means a request boots the application, runs your code, and tears the whole thing down, every time. A variable you set, a database connection you opened, a cache you warmed in memory: none of it is there for the next request, which gets its own clean boot. This is not an accident of a slow language catching up; it is the model PHP was built around from the start, and it buys you a specific, valuable property. A memory leak in one request cannot accumulate across a thousand requests, because there is no shared memory for it to accumulate in. A crash in one request cannot corrupt the state the next request depends on, because there is no shared state. The cost is the one you would expect: nothing is warm. Every request that needs a database connection opens one; every request that needs the application's routes and configuration loaded rebuilds them, unless something below the language itself is caching the result.

That something is `opcache`. PHP source code is compiled to bytecode before it runs, and by default that compilation happens again on every single request, from scratch. Opcache, bundled with PHP since version 5.5, caches the compiled bytecode in shared memory so the next request skips recompilation. Stated precisely, rather than the way it usually gets described: opcache is a `zend_extension`, and it has to be loaded in `php.ini` to do anything. Most distribution packagers turn it on by default, but PHP itself does not, and "PHP is fast because it caches bytecode" is only true of a specific, checkable configuration, not of the language as installed.

<img src="images/ch02-runtime.png" alt="A single request shown as a small box that boots an application, runs, sends a response, and is torn down completely, with a second, identical box starting fresh beside it, sharing nothing with the first." width="560">

## What the type system actually enforces

The type declarations added since PHP 7 are not decoration. A file that opts in enforces its contracts at the engine level, not just in a linter:

```php
<?php

declare(strict_types=1);

function total(array $prices): float
{
    return array_sum($prices);
}

total(["9.99", "4.50"]); // TypeError: array_sum() argument must be array<float>, string given
```

Without `declare(strict_types=1)`, PHP would coerce a numeric string into a float and run anyway. With it, the mismatch is a `TypeError` at the point it occurs, not a silent corruption three functions downstream. This is the concrete, checkable version of the claim in [The Reputation](ch01-introduction.md) that the type system changed: it is opt-in per file, and it is real once you opt in.

## Serving models: how "shared-nothing" gets bent

Three serving approaches, alphabetically, cover most of how PHP applications run in production today: FrankenPHP, PHP-FPM behind a web server, and RoadRunner. PHP-FPM is the traditional model: a pool of worker processes, each one handling one request at a time, each one restarted periodically, none of them keeping application state between requests. It is the purest expression of shared-nothing, and it is still the default most hosting environments assume.

FrankenPHP and RoadRunner both offer a "worker mode" that bends the shared-nothing default on purpose: the application boots once and stays in memory, handling many requests in sequence without a full reboot between them. FrankenPHP's own documentation describes this plainly, including the trade-off it introduces: PHP's superglobals (`$_GET`, `$_POST`, `$_COOKIE`, `$_FILES`, `$_SERVER`, `$_REQUEST`) are reset automatically between requests, so a worker does not leak one visitor's form data into the next visitor's request, but `$_ENV` is not reset, and anything your own code deliberately stores outside a superglobal will persist unless you clear it yourself. The documentation is candid about why that matters: in its words, PHP "was not originally designed for long-running processes," and the standard mitigation is a periodic worker restart to bound the memory a long-lived process can quietly accumulate. RoadRunner takes a related approach from a different direction, as a Go-based application server managing a pool of long-lived PHP workers that persist across requests rather than being torn down after each one.

## The JIT: a real feature, a narrow benefit

PHP 8.0 added a Just-In-Time compiler, and the RFC that introduced it is unusually direct about what it does and does not help. The compiler translates hot code paths to machine code at runtime, which helps CPU-bound, numeric work substantially. It does comparatively little for a typical web request, because a typical request's time is spent waiting on a database or the network, not executing arithmetic, and the RFC ships its own benchmark showing exactly that gap on a realistic workload.

<div class="chart">

{{#include charts/ch04-jit.svg}}

</div>

Three hundred and twenty-six requests per second with the JIT enabled, compared to three hundred and fifteen without it, on a WordPress request. That is a real, measured, single-digit-percent difference on the workload most PHP installations actually run, and it comes from the RFC that shipped the feature, not from a critic. The JIT is not nothing: it is the reason the numeric-code comparisons in [Performance](ch04-performance.md) look the way they do. It is just not the reason a web application built on PHP gets faster.

## Concurrency without threads

Four options, in the order this book will keep using, cover how PHP code achieves concurrency inside a single process: AMPHP, ReactPHP, Swoole (or OpenSwoole), and, as a language feature rather than a library, Fibers. AMPHP is a set of libraries built around the same event-loop model as the other two, aimed at the same class of I/O-bound concurrency problem: many things waiting at once, handled by one process that never blocks entirely on any single one of them. ReactPHP describes itself, in its own documentation, as a low-level, event-loop-based library aimed at servers and clients that need to hold open many concurrent connections. Swoole describes itself as an event-driven, coroutine-based networking engine written in C for PHP that converts PHP's normally blocking I/O calls into non-blocking calls under its own scheduler. Fibers, added in PHP 8.1, are cooperative: a fiber suspends and resumes itself via `Fiber::suspend()` and `Fiber::resume()`, and only one fiber's code runs at any instant. All of this is concurrency, the ability to have many logical tasks in flight and switch between them while one waits on I/O. None of it is parallelism, the ability to have two tasks actually executing at the same instant on two CPU cores.

> **The limit.** PHP has no native multithreading in userland. The `parallel` and `pthreads` PECL extensions exist and give real OS-thread parallelism, but they are third-party, narrowly adopted, and worth naming honestly as "exists, but niche," not folded silently into the concurrency story above and not omitted from it either. If your workload needs two CPU-bound tasks running at the same literal instant inside one process, nothing in this chapter's list does that, and [Where PHP Is the Wrong Choice](ch09-wrong-choice.md) is where that limit gets its full treatment.

**What to verify yourself.** On any machine with PHP installed, run:

```bash
php -v
php -i | grep -i opcache
```

The first line tells you which PHP version and, usually, which SAPI (FPM, CLI, or something else) you are looking at. The second tells you whether opcache is actually loaded on that specific install, not whether it theoretically could be: a hosting environment's marketing page is not evidence; a grep of your own `phpinfo()` output is.

The runtime model in this chapter, shared-nothing by default, bendable by specific serving layers, concurrent but not parallel, is the fact everything downstream in this book is built on. The next question is not how PHP executes a single request, but who is actually running it, at what scale, and on what evidence, which is where [Who Runs PHP](ch03-who-runs-php.md) picks up.
