# Beyond PHP: Other Languages, Other Technologies, and the Engine Itself

## Talking to other languages

Real systems are rarely written in one language, and **the common way to mix them is not to link them together but to have them talk over an API.** Each side exposes a language-neutral interface, over HTTP or gRPC, that any language can call. A PHP backend and a service written in Go or Rust talk to each other this way all day long, neither one aware of what the other is written in.

Two more direct routes exist. FFI (Foreign Function Interface, since PHP 7.4) calls straight into a compiled C library from PHP, without writing a full extension. It is narrow, useful when it applies, and worth knowing about. At the other end of the effort scale, `proc_open()` from [Chapter 18](ch18-02-queues-and-processes.md) simply runs a program written in something else entirely and reads back what it prints.

## Talking to other technologies

[Chapter 10](ch10-03-talking-to-a-database.md) used SQLite because it needed no separate server. **Most production PHP talks to MySQL, MariaDB or PostgreSQL instead**, through the same PDO interface and a different DSN, each with its own SQL dialect quirks worth knowing about.

The queue of [Chapter 18](ch18-02-queues-and-processes.md) scales up into dedicated software like RabbitMQ or Amazon SQS, for background work that must survive a crash or fan out across several workers reliably. Search engines (Elasticsearch, Meilisearch) take over the day a `LIKE '%...%'` query stops being good enough: full-text and faceted search need infrastructure built for exactly that. Cloud services (object storage like S3 and its many compatible alternatives, managed databases, managed queues) are largely the same ideas, run and scaled by someone else.

## Extending the engine itself

The PDO drivers and Xdebug you have already used are PHP extensions: code written in C against the Zend Engine's own API, and installed through PECL. Zephir is a higher-level language that compiles down to a real extension, for teams who want that level of performance without writing raw C by hand.

**This layer is worth knowing about and rarely worth reaching for.** Almost everything an application needs is achievable in ordinary, userland PHP. Writing an extension is a decision for when PHP itself is the bottleneck, not the application sitting on top of it, and that is a rare place to end up.
