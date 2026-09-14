# C - Vocabulary

The words that come up in PHP conversations and rarely anywhere else. One or two sentences each.

**SAPI.** Server API: the layer that connects the interpreter to whatever runs it. The command line, PHP-FPM, `mod_php` and the embedded runtimes are all SAPIs over the same engine.

**CLI.** The command-line SAPI, invoked as `php file.php`. It has no execution time limit and no memory limit by default, unlike the web SAPIs.

**FPM.** FastCGI Process Manager: a pool of PHP processes waiting for requests behind a web server. The standard way to serve PHP.

**FastCGI.** The protocol the web server uses to hand a request to FPM and read the response back.

**mod_php.** The Apache module that embeds PHP in the web server process itself. Older than FPM and still around.

**OPcache.** The bytecode cache. Compiled files stay in shared memory so the next request skips parsing. On in every serious setup.

**JIT.** Just-in-time compilation of hot code to machine code, inside OPcache, since 8.0. Helps CPU-bound scripts; changes little for typical web traffic.

**Preloading.** An OPcache option that compiles and links a set of files once at server start, so every request begins with them already loaded.

**APCu.** A memory cache shared between the PHP processes of one machine. For values you compute once and read often, when an external store is overkill.

**Extension.** A compiled C module that adds functions or classes to PHP: `pdo_mysql`, `intl`, `mbstring`, `xdebug`. `php -m` lists the loaded ones.

**PECL.** The historical repository of extensions not bundled with PHP, with its own installer.

**PIE.** The newer installer for extensions, Composer-style, meant to succeed the PECL workflow.

**ZTS and NTS.** Thread-safe and non-thread-safe builds of the interpreter. NTS is the default and the one FPM uses; ZTS exists for the rare threaded SAPIs and the `parallel` extension.

**php.ini.** The configuration file. The CLI and FPM read different ones, which explains most "it works in the terminal" mysteries.

**Composer.** The package manager. Reads `composer.json`, writes `composer.lock`, fills `vendor/`, generates the autoloader.

**Packagist.** The public package registry Composer fetches from.

**vendor.** The folder Composer installs packages into. Never edited, never committed.

**Autoload.** The mechanism that loads a class file the first time the class is used, so no `require` line is ever written by hand.

**PSR-4.** The standard mapping from namespace to folder that autoloaders follow: `App\Billing\Invoice` lives in `src/Billing/Invoice.php`.

**PHP-FIG.** Framework Interoperability Group: the body that publishes the PSRs and the coding style.

**PSR.** PHP Standards Recommendation: a numbered interface or convention (PSR-3 logging, PSR-7 HTTP messages, PSR-15 middleware) that libraries agree on so they can be swapped.

**PER Coding Style.** The current code style standard from the FIG, successor of PSR-12. What formatters enforce.

**RFC.** Request for Comments: the public proposal every language change goes through before a vote of the core developers.

**PHP Foundation.** The non-profit that, since 2021, employs core developers to maintain and advance the interpreter.

**php-src.** The source repository of the interpreter itself, written in C.

**Zend Engine.** The core of the interpreter: the compiler and the executor. The name survives in a few settings and error messages.

**Superglobal.** A built-in array visible in every scope: `$_GET`, `$_POST`, `$_SERVER`, `$_COOKIE`, `$_FILES`, `$_SESSION`, `$_ENV`.

**Docblock.** A `/** ... */` comment above a symbol, carrying `@param` and `@return` annotations that editors and static analysers read. Where generics live.

**Attribute.** Structured metadata attached to a class, method, property or parameter with `#[...]`, read through reflection. What annotations were in Java.

**Trait.** A block of methods and properties copied into any class that `use`s it. Horizontal reuse without inheritance.

**Enum.** A type with a fixed set of named cases, optionally backed by an int or a string, with methods and interfaces. Since 8.1.

**Fiber.** A stackful coroutine that can suspend and resume from anywhere in its call stack. The primitive async libraries build on; not something application code drives directly.

**Generator.** A function that `yield`s values one at a time and keeps its state between calls. Lazy iteration without building an array.

**SPL.** Standard PHP Library: the bundled set of data structures, iterators, exceptions and interfaces such as `ArrayIterator`, `SplQueue`, `Countable`, `RuntimeException`.

**PDO.** PHP Data Objects: the database abstraction with one API over every driver, prepared statements included.

**mbstring.** The multibyte string extension. `mb_strlen`, `mb_substr` and friends count characters where the plain functions count bytes.

**intl.** The internationalisation extension: collation, number and date formatting, Unicode normalisation, wrapping the ICU library.

**Xdebug.** The step debugger and profiler. Development only.

**PHPUnit.** The xUnit-style test framework most PHP tests are written with.

**Pest.** A test framework with a describe-and-expect syntax, running on PHPUnit's engine.

**PHPStan.** A static analyser that finds type errors and impossible code without running it, with levels from 0 to 10.

**Psalm.** The other static analyser, with levels from 8 down to 1 and a focus on type soundness and taint analysis.

**Rector.** An automated refactoring tool that rewrites code to a newer PHP version or a newer library API.

**phpt.** The test file format of the interpreter itself, in `php-src`. You meet it if you contribute to PHP or read its bug reports.

**strict_types.** The per-file declaration `declare(strict_types=1);` that makes scalar type mismatches on calls from that file throw instead of coerce.

**Copy-on-write.** The engine trick that makes array assignment cheap: the copy shares memory with the original until one of them is modified.

**Late static binding.** `static::` resolving to the class the call was made on, not the class where the method is written. `self::` is the other one.

**Magic method.** A method with a reserved double-underscore name that the engine calls on its own: `__construct`, `__toString`, `__get`, `__call`, `__clone`, `__invoke`.
