# A Look at Fibers and Async Libraries

Queues and background processes solve "do this slow thing without blocking the user." They don't solve a narrower, trickier problem: what if you want a *single* PHP process to juggle many slow I/O operations at once, say, making a hundred outgoing HTTP requests and reacting as each one finishes, without waiting for them one at a time? That's the problem async programming exists to solve, and PHP's answer to it, since PHP 8.1, starts with **Fibers**.

## What a Fiber actually is

A Fiber is a way to pause a chunk of PHP code in the middle of running, hand control back to whatever called it, and resume later, exactly where it left off, with all its local state intact. That's it. That's the whole primitive.

```php
<?php

$fiber = new Fiber(function (): void {
    echo "Start\n";
    $value = Fiber::suspend('paused');
    echo "Resumed with: {$value}\n";
});

$result = $fiber->start();
echo "Fiber said: {$result}\n";

$fiber->resume('hello');
```

```console
$ php fiber_demo.php
Start
Fiber said: paused
Resumed with: hello
```

Running this, you can see the back-and-forth: `start()` runs the fiber until it hits `Fiber::suspend()`, at which point control returns to the *caller*, carrying whatever value was passed to `suspend()`. Later, `resume()` picks the fiber back up from that exact point, as if nothing happened in between.

On its own, this doesn't look like much: a fancy way to pause a function. But it's a *primitive*, not a finished tool, in the same sense that a mutex is a primitive and not a finished thread pool. What Fibers give you is a foundation: something that can suspend while it's waiting on slow I/O (a network call, a database query, a file read) and let other work happen during that wait, all inside one PHP process, with no threads and no separate processes involved. This style is called **cooperative multitasking**: nothing is preempted by the system the way OS threads are; each piece of work voluntarily yields control at a suspension point.

## What people actually use

Fibers themselves are low-level: you're not expected to write raw `Fiber::suspend()` calls in application code, any more than you're expected to hand-write TCP packets. They exist mainly so library authors can build event loops and async abstractions on top of them. Three names come up constantly once you go looking:

- **ReactPHP**: an event-driven library built around promises, widely used for things like long-running servers and clients that need to handle many concurrent connections in one process.
- **Swoole** (and its newer sibling, OpenSwoole): a PHP extension, written in C, that replaces the traditional request model entirely with a persistent, coroutine-based server. It's a bigger commitment: your application stays resident in memory across requests, which is powerful and also means the shared-nothing guarantees from earlier in this chapter no longer hold automatically.
- **AMPHP**: another async framework, built directly on Fibers since PHP 8.1, with a design that lets asynchronous code read almost like ordinary sequential code.

All three are genuinely useful, and all three are beyond the scope of this book. If you ever find yourself needing to hold open thousands of concurrent connections, build a real-time chat backend, or squeeze maximum throughput out of a single PHP process, these are the names to search for. For everything else, which, per the start of this chapter, is most PHP work, a queue and a handful of worker processes will take you a very long way.
