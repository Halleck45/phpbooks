# Appendix C: Vocabulary

Terms are defined the way this book uses them, in plain language, with a pointer to the chapter where each one is explained in context.

**Composer.** PHP's dependency manager. Resolves a project's required packages against Packagist, records the exact versions installed in a lockfile, and verifies each install against a hash so a dependency cannot silently change underneath a project after it was reviewed. See [Cost](ch07-cost.md).

**Coroutine.** A unit of execution that can pause itself and hand control back, then resume later from the same point, without the operating system tearing it down and rebuilding it. PHP's Fibers and libraries such as ReactPHP and Swoole are built around this idea. See [The Runtime](ch02-runtime.md).

**Fibers.** A PHP 8.1 language feature giving cooperative concurrency: a fiber suspends itself via `Fiber::suspend()` and resumes via `Fiber::resume()`. Only one fiber's code executes at any instant, which makes this concurrency, not parallelism. See [The Runtime](ch02-runtime.md).

**FPM (FastCGI Process Manager).** PHP's standard worker-process manager: a pool of processes, each handling one request at a time, each one shared-nothing with respect to every other. The traditional, most widely deployed way PHP applications are served. See [The Runtime](ch02-runtime.md) and [Scale](ch05-scale.md).

**JIT (Just-In-Time compiler).** Added in PHP 8.0. Translates hot code paths to machine code at runtime. Helps CPU-bound, numeric workloads substantially; helps a typical web request, whose time is mostly spent waiting on I/O, by only a small margin. See [The Runtime](ch02-runtime.md) and [Performance](ch04-performance.md).

**Opcache.** A bundled `zend_extension`, present since PHP 5.5, that caches compiled bytecode in shared memory so it does not have to be recompiled on every request. Must be explicitly loaded in `php.ini`; not automatically active from PHP core alone. See [The Runtime](ch02-runtime.md).

**Packagist.** The public package registry Composer resolves dependencies against. Free to publish to and free to use. See [Cost](ch07-cost.md).

**PSR (PHP Standards Recommendation).** A shared convention, adopted voluntarily by framework and library authors through a standards process rather than mandated by the language itself, covering things like autoloading, logging interfaces, and HTTP message shapes, so independently written libraries can be relied on to interoperate. See [The Reputation](ch01-introduction.md).

**RFC (Request for Comments).** PHP's public process for proposing and voting on changes to the language itself, conducted on a dedicated wiki. A change to the language requires a two-thirds majority to pass. See [Governance and Versions](ch08-governance-and-versions.md).

**SAPI (Server API).** The interface between the PHP engine and whatever is running it, FPM, the CLI, or another server module. `PHP_SAPI` reports which one a given process is running under. See [The Evaluation](ch10-the-evaluation.md).

**Shared-nothing.** PHP's default execution model: each request boots the application, runs, sends a response, and is torn down, with no memory or state carried over to the next request. The property that makes horizontal scaling straightforward, and the reason anything meant to persist has to live outside the PHP process. See [The Runtime](ch02-runtime.md) and [Scale](ch05-scale.md).

**Static analysis.** Checking code for errors, including type mismatches, without running it. PHPStan and Psalm are the two static-analysis tools this book names; both also approximate generic types through a shared docblock convention that the language engine itself does not enforce. See [Who Maintains It](ch06-who-maintains-it.md) and [Where PHP Is the Wrong Choice](ch09-wrong-choice.md).

**Worker mode.** A serving approach, offered by FrankenPHP and RoadRunner, that keeps a PHP application booted in memory across many requests instead of tearing it down after each one. Superglobals are reset automatically between requests; anything else your code deliberately persists is not, which is why worker restarts are the standard, documented mitigation for long-running memory growth. See [The Runtime](ch02-runtime.md).
