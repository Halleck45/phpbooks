# FrankenPHP and Laravel Octane: Worker Mode Performance

Traditional PHP rebuilds your whole application on every request, framework included: boot the container, load the configuration, then throw it all away once the response is sent. That habit is a large part of why PHP earned a reputation for being slower than runtimes that keep an application resident in memory.

**Worker mode boots the application once and handles many requests against that same booted instance**, resetting only what needs resetting between them.

```bash
composer require laravel/octane
php artisan octane:install --server=frankenphp
php artisan octane:start
```

FrankenPHP is a PHP application server written in Go. It runs PHP in worker mode natively, and in classic mode too, with built-in HTTPS and no separate web server:

```bash
frankenphp php-server --worker /path/to/public/index.php
```

The gain is large for applications whose bottleneck was framework boot time rather than their own logic. Benchmarks published by the projects show a multiple of PHP-FPM's throughput for the same application code, unchanged; your own numbers depend on how much of each request was boot.

The trade-off deserves a plain statement. Global state that used to reset between requests, a static property, a singleton holding request data, can now leak from one request to the next. The same process serves them in sequence instead of starting fresh.

## When to reach for this

An application under measured load where profiling (see [Blackfire](ch15-04-blackfire-profiling.md)) shows framework bootstrap, not your own business logic, as the bottleneck.

## When it's the wrong fit

A low-traffic site or an internal tool. Worker mode adds a category of bug, state leaking between requests, that is not worth taking on before you need the throughput.

> **Under the hood:** This is the same problem [Reverb's WebSocket server](ch07-01-laravel-reverb-livewire.md) solves with Fibers, approached from the other side. Instead of one process holding many concurrent connections, worker mode keeps one process alive across many sequential requests. Both exist because PHP's "die after every request" model, once a limitation, became optional.
