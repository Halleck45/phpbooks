# Beyond PHP: Other Languages, Other Technologies, and the Engine Itself

## Talking to other languages

- **FFI** (Foreign Function Interface, since PHP 7.4): calling directly into a compiled C library from PHP, without writing a full extension. Narrow, useful when it applies, worth knowing exists.
- **APIs** (HTTP, gRPC): the far more common way real systems mix languages, not by linking them together in one process, but by having each side expose a language-neutral interface that any language can call. A PHP backend and a service written in Go or Rust talk to each other this way constantly, neither one aware what the other is written in.
- **`proc_open()`**, from [Chapter 18](ch18-02-queues-and-processes.md): the low-effort version, shelling out to a program written in something else entirely and reading back what it prints.

## Talking to other technologies

- **Databases beyond SQLite**: [Chapter 10](ch10-03-talking-to-a-database.md) used SQLite because it needed no separate server. MySQL, MariaDB, and PostgreSQL are what most production PHP talks to instead, through the same PDO interface, a different DSN, and each with its own SQL dialect quirks worth knowing about.
- **Message queues**: [Chapter 18](ch18-02-queues-and-processes.md)'s queue example, scaled up with dedicated software like RabbitMQ or Amazon SQS, for background work that needs to survive a crash or fan out across multiple workers reliably.
- **Search engines** (Elasticsearch, Meilisearch): for the moment a `LIKE '%...%'` query stops being good enough, full-text and faceted search need infrastructure built for exactly that.
- **Cloud services**: object storage (S3 and its many compatible alternatives), managed databases, managed queues, largely the same ideas as above, run and scaled by someone else.

## Extending the engine itself

- **PHP extensions**: the mechanism behind the PDO drivers and Xdebug you've already used, written in C against the Zend Engine's own API, and installed through PECL.
- **Zephir**: a higher-level language that compiles down into a real PHP extension, for teams who want extension-level performance without writing raw C by hand.
- Worth knowing this layer exists, rarely worth reaching for. Almost everything an application needs is achievable in ordinary, userland PHP; writing an extension is a decision for when PHP itself is the bottleneck, not the application sitting on top of it, and that's a rare place to end up.
