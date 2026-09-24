# C - Glossary

The terms I use that you may not know if you come from another ecosystem, in alphabetical order.

**Active support.** The first two years of a PHP release branch, during which bugs and security issues are fixed in monthly point releases. Two years of security support follow, with security fixes only. See [Governance and Longevity](ch07-governance.md).

**Composer.** The dependency manager of the PHP ecosystem, comparable to npm, pip or Maven. It reads `composer.json`, resolves the versions, writes `composer.lock` and generates the autoloader that maps class names to files.

**Fiber.** A stackful coroutine, added in PHP 8.1: a function that can suspend itself and be resumed later by whoever holds it. The language provides the mechanism only, and scheduling belongs to libraries. See [Concurrency](ch04-concurrency.md).

**FrankenPHP.** An application server for PHP, written in Go on top of the Caddy web server. It runs PHP either in the classic one-process-per-request mode or in a worker mode that keeps the application booted between requests. See [The Runtime](ch02-runtime.md).

**Hack and HHVM.** Hack is a language that forked from PHP at Facebook in 2014, and HHVM is its virtual machine. HHVM dropped support for PHP itself in 2019. Organisations that run Hack do not run PHP, and I do not count them as PHP users.

**JIT.** The just-in-time compiler that has shipped inside OPcache since PHP 8.0, compiling hot code paths to machine code. It benefits CPU-bound code far more than typical web requests, and I say so wherever a JIT figure appears.

**NTS and ZTS.** Non-thread-safe and Zend-thread-safe builds of the interpreter. The standard build is NTS, because the process model never needed threads. ZTS builds exist for embedding and for the `parallel` extension.

**OPcache.** The extension that keeps the compiled form of every PHP file in shared memory, so that a file is parsed and compiled once rather than on every request. It has been standard in production since PHP 5.5.

**p50, p95, p99.** Percentiles of a latency distribution: the response time under which 50, 95 or 99 percent of requests complete. A benchmark that reports only the average hides the tail, which is why I prefer sources that publish percentiles.

**Packagist.** The public package registry Composer uses by default, comparable to npmjs.com or PyPI.

**PER Coding Style.** The coding style standard maintained by the PHP-FIG and the successor of PSR-12. Tools such as PHP-CS-Fixer and PHP_CodeSniffer enforce it.

**PHP-FIG.** The PHP Framework Interoperability Group, which publishes the PSR standards so that libraries from different authors fit together.

**PHP-FPM.** The FastCGI Process Manager, the standard way to run PHP behind a web server. It keeps a pool of worker processes, each handling one request at a time.

**Preloading.** An OPcache feature (PHP 7.4) that compiles a list of files once at startup and keeps them linked in memory, so that no class needs autoloading during a request.

**PSR.** PHP Standards Recommendation, a numbered interoperability standard published by the PHP-FIG: PSR-4 for autoloading, PSR-3 for logging, PSR-7 for HTTP messages, and so on.

**Rector.** A tool that rewrites PHP code automatically: it upgrades syntax from one version to the next, applies refactorings and removes deprecated calls. Teams use it for large-scale version upgrades.

**RFC.** Request for Comments, the document through which any change to the language is proposed, discussed on the internals mailing list and voted on. A change to the language requires a two-thirds majority. See [Governance and Longevity](ch07-governance.md).

**RoadRunner.** An application server for PHP written in Go. It keeps worker processes alive and passes requests to them over a protocol, so that the application is booted once rather than on every request.

**Shared-nothing.** The execution model in which each request starts with fresh memory, runs, responds and is discarded, sharing nothing with the previous or the next request. Most of PHP's operational properties follow from it. See [The Runtime](ch02-runtime.md).

**Static analysis.** Reading code without running it, to find type errors and other defects. PHPStan and Psalm are the two analysers of the PHP ecosystem, and both understand a docblock type syntax richer than the language's own.

**Swoole and OpenSwoole.** A C extension and its fork. Each gives PHP an event loop, coroutines and a built-in HTTP server, for workloads that need many concurrent connections in one process.

**TechEmpower Framework Benchmarks.** A public, continuously run benchmark suite that compares hundreds of web frameworks across languages on a fixed set of tests (JSON serialisation, single and multiple database queries, "fortunes" HTML rendering, plaintext). I cite it with its round number, its hardware and the test, and I say what each test measures.

**W3Techs.** A web survey company that publishes the usage of server-side technologies across a sample of more than twenty million websites. Its figures count only the sites whose language can be detected, which biases them in ways I state when I use them.

**Worker mode.** A way of running PHP in which the application is booted once and kept in memory, and each worker process handles many requests in sequence. FrankenPHP and RoadRunner offer it, among others. It removes the per-request startup cost at the price of the shared-nothing guarantee.
