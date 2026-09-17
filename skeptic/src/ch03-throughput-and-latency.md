# Throughput and Latency

How fast is it, on which measure, and against whom: your second question, and the one where hype does the most damage. **On the largest public benchmark that compares web frameworks across languages, PHP entries span two orders of magnitude depending on the runtime they run on, from the top forty overall to the bottom tenth, so the language alone predicts nothing and the deployment predicts almost everything.** A figure that wide only helps you when it comes with its round, its hardware and its test, and every figure here carries all three.

## The engine's history

The interpreter itself, on CPU-bound code, improved by a large step once and by small steps since. The step was PHP 7.0, in December 2015, which replaced the engine's internal data structures. The vendor of the engine claimed at the time that execution time was "often halved" compared with PHP 5.6, in a white paper without a published methodology. An independent run on one machine, with every version of the interpreter from 5.6 to a PHP 8.0 development build, agrees on the shape: the PHPBench score, a synthetic suite of interpreter micro-benchmarks, went from 288,000 on PHP 5.6 to 620,000 on PHP 7.0, then rose in smaller steps, between nothing and thirteen percent per version, to 876,000 on the 8.0 build.

{{#include charts/ch03-engine-progression.svg}}

Since PHP 8.0 the interpreter's speed on web applications has been flat, and the sources that measure it say so themselves. A hosting company that publishes yearly benchmarks measured WordPress at 146 requests per second on PHP 8.2 and 148 on PHP 8.5 on the same machine, and wrote that "incremental releases rarely produce large speed jumps on their own". The measurement is the hosting vendor's own, run at fifteen concurrent requests on a thirty-core machine, so it measures response time rather than capacity. Expect a current PHP version to be roughly twice as fast as PHP 5 on the interpreter's own work, and expect nothing from a minor version upgrade beyond bug fixes and features.

## The cross-language benchmark

TechEmpower's Framework Benchmarks is a public suite that ran hundreds of web frameworks, in dozens of languages, through the same six tests on the same hardware, with every implementation contributed and maintained by volunteers in a public repository. Its last completed round is Round 23, dated 24 February 2025, run on a server with a Xeon Gold 6330 processor, 28 cores and 56 threads, and a 40 gigabit network. The project's repository was archived on 24 March 2026, so Round 23 is the final round and its figures are the last of their kind. Nothing else compares this many frameworks under one protocol, which is why I keep them, and the tests measure different things, which is why each figure names its test.

The Fortunes test is the closest to a web page: one database query returning a dozen rows, one HTML template rendered with escaping. On that test, 510 entries completed Round 23. The chart picks sixteen of them, the overall leaders, the mainstream framework of each major language and the PHP entries at each kind of runtime, and the raw table with every entry is stored beside the book's chart data, so you can make your own selection.

{{#include charts/ch03-techempower-fortunes.svg}}

Read the PHP bars from the top. The fastest PHP entries, on the workerman and Swoole runtimes with raw SQL and no framework, sit at rank 31 to 38 of 510, above 730,000 requests per second, ahead of the plain ASP.NET Core entry, the Go entries and Spring. A full-stack PHP framework with a full ORM on a worker runtime, the Ubiquity entry, reaches 428,000 at rank 92. Plain PHP under PHP-FPM and nginx, the standard deployment, reaches 146,000 at rank 248, about a third ahead of Gin and FastAPI. The two most used PHP frameworks under PHP-FPM sit near the bottom, Symfony at 26,000 and Laravel at 16,000, below Rails at 43,000 and Django at 32,000. One benchmark supports both the claim that PHP can be among the fastest web runtimes and the claim that a typical PHP application is among the slowest, and you should expect to hear both together.

Part of the spread is the runtime. An entry that keeps the application booted between requests removes the boot cost that dominates a framework's request time.

{{#include charts/ch03-runtime-effect.svg}}

The same Symfony code moves from 26,000 requests per second under PHP-FPM to 74,000 under FrankenPHP and 111,000 under Swoole, and the same Laravel code from 16,000 to 50,000 under workerman. The rest of the spread is the entry itself. TechEmpower entries are maintained by whoever cares to, and a slow entry can reflect a dated configuration as much as the framework. The Laravel entry under RoadRunner, at 8,000, is slower than under PHP-FPM; I have no explanation for it and report it as measured.

The other tests move the ranks but not the story. On the JSON serialisation test, which has no database, the Swoole entry reaches 2.5 million requests per second at rank 73, plain PHP-FPM 428,000 and Laravel under PHP-FPM 27,000, while ASP.NET Core stands at 1.4 million, Node.js at 1.1 million, Spring at 328,000 and Django at 167,000. On the twenty-query test, which is bound by the database driver, the leaders of every language converge under 90,000 and the fastest PHP entries sit at 56,000, ahead of FastAPI at 37,000 and Spring at 32,000.

## Latency

Throughput says how many requests a machine can absorb. Latency says how long one user waits, and it is dominated by what the request waits for, not by the interpreter. Tideways, a profiler vendor and a founding member of The PHP Foundation, measured a PHP-FPM hello-world behind nginx on an eight-core virtual machine and reported a 99th percentile of 0.9 milliseconds at 18,000 requests per second. That is the floor: the interpreter and the process manager together cost under a millisecond when there is nothing else to do, and everything above it is the application and its dependencies.

The most useful public latency figures come from an organisation that publishes its own targets and its own dashboards. Wikimedia's engineering guidelines require a GET request to complete in 50 milliseconds at the median and 200 milliseconds at the 99th percentile of the time spent in PHP, and 500 milliseconds at the 99th percentile for a POST. Its Grafana instance is public and shows the measured distribution for the requests that reach the application servers, that is, the cache misses and the logged-in users, which are the expensive ones. On the day this chapter was checked the median was about 170 milliseconds and the tail well above the target, for pages that include rendering wikitext from a cold parser cache. I give you the dashboard rather than the snapshot, because a week of it tells you more than an hour.

## Where PHP loses

**On CPU-bound code with no I/O, PHP is an interpreter with an optional JIT, and it is slower than a JIT-compiled runtime such as V8 by an order of magnitude.** The Computer Language Benchmarks Game, which compares contributed programs on the same small tasks, puts the fastest single-threaded n-body program at 2.2 seconds in Rust, 3.1 in C#, 6.0 in Java, 6.4 in Go, 8.6 in Node.js, 167 in Ruby with YJIT, 204 in PHP 8.4 and 360 in Python 3.13.

{{#include charts/ch03-cpu-bound.svg}}

The chart carries its caveats. The PHP programs are run with a JIT buffer configured but with `opcache.jit` left at its PHP 8.4 default, which is disabled, so they measure the interpreter alone; the JIT RFC reports a four-fold gain on Mandelbrot with the JIT on, which would narrow the gap without closing it. The programs are also contributed, so they measure the best program someone bothered to write. With both caveats, the order stands. For numerical work, simulation, parsing large inputs in a loop or anything that keeps a core busy, PHP is in the class of Python and Ruby, not in the class of Node.js, and thirty to a hundred times behind Go, Java, C# and Rust on this program. [Where PHP Is the Wrong Choice](ch09-wrong-choice.md) draws the consequence.

> The limit: PHP's good throughput figures come from worker runtimes and raw database access, which a typical team does not run on day one. Its typical figures, a full-stack framework under PHP-FPM, sit with Rails and Django, at a few tens of thousands of requests per second on a large machine, which is more than most applications will ever receive. And on CPU-bound work the interpreter is an order of magnitude behind V8.

## What to verify yourself

The TechEmpower toolset still runs from its archived repository with Docker, and the raw Round 23 tables for six tests are stored in the book's `charts/raw/` folder as CSV, so you can check my selection above and make any other. Closer to home, take the application you would build, or an equivalent open-source one, run it under PHP-FPM and under one worker runtime on the same machine, and measure with `wrk` at the concurrency you expect in production; the ratio you obtain is the only one that matters. For latency, open Wikimedia's public "Backend Pageview Timing" dashboard and read a week of it.

Throughput assumes the requests are independent. The next question is what happens when they are not.
