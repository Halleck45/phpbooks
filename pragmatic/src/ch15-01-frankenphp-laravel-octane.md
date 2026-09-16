# FrankenPHP and Laravel Octane: Worker Mode Performance

Traditional PHP rebuilds your entire application, framework included, from scratch on every single request: booting the container, loading configuration, all of it, discarded the moment the response is sent. That's a large part of why PHP earned a reputation for being slower than runtimes that keep an application resident in memory.

Worker mode changes that: boot the application once, then handle many requests against that same booted instance, resetting only what needs resetting between them.

```bash
composer require laravel/octane
php artisan octane:install --server=frankenphp
php artisan octane:start
```

FrankenPHP is a modern PHP application server, written in Go, that runs PHP in worker mode natively (as well as classic mode), with built-in HTTPS and no separate web server needed:

```bash
frankenphp php-server --worker /path/to/public/index.php
```

The performance gain is substantial for applications that were previously bottlenecked on framework boot time rather than actual business logic: benchmarks commonly show several times the throughput of classic PHP-FPM for the same application code, unchanged.

The tradeoff is real and worth stating plainly: global state that used to reset automatically between requests (a static property, a singleton holding request-specific data) can now leak between requests if you're not careful, since the same PHP process handles many requests in sequence rather than starting fresh each time.

## When to reach for this

An application under real, measured load where profiling (see [Blackfire](ch15-04-blackfire-profiling.md)) shows framework bootstrap overhead, not your own business logic, as the actual bottleneck.

## When it's the wrong fit

A low-traffic site or internal tool. Worker mode adds a category of bug (accidental state leakage between requests) that isn't worth taking on before you actually need the throughput.

> **Under the hood:** This is the exact same problem [Reverb's WebSocket server](ch07-01-laravel-reverb-livewire.md) solves with Fibers, approached from the opposite direction: instead of one process holding many concurrent connections, worker mode keeps one process alive across many sequential requests. Both exist because PHP's traditional "die after every request" model, once a limitation, became optional.
