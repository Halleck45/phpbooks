# Where PHP Is the Wrong Choice

An evaluation that cannot name the cases where its subject loses is not an evaluation, and PHP loses in several. **PHP is the wrong choice for CPU-bound computation, for services whose job is to hold many long-lived connections, for anything that runs outside a server, and for teams whose skills, platform and scale have already carried them somewhere else.** In each of those cases the honest advice is rarely "rewrite everything" and more often "not this part", with a different tool for the part.

## Computation

The n-body program takes 204 seconds in PHP with the JIT off, against 8.6 for Node.js, and the JIT narrows that gap without closing it, as [Throughput and Latency](ch03-throughput-and-latency.md) showed. On code that keeps a core busy, the interpreter sits in the class of Python and Ruby, an order of magnitude behind V8, the JVM, .NET, Go and Rust. Around it there is no numerical stack of any depth: no array library with the reach of NumPy, no dataframe library with the reach of pandas, no machine learning framework that a research team would recognise. The packages that exist are few and maintained by small groups, and I found no scale figure to cite for any of them.

If your product is a model, a simulation, a signal processing pipeline or a large batch computation, use Python for the ecosystem or a compiled language for the speed. If that product also has a web front, the front is where PHP may still fit.

## Long-lived connections

Ten thousand idle connections cost ten thousand processes under PHP's default model, and a process is too expensive to spend on an idle socket. The async runtimes of [Concurrency](ch04-concurrency.md) exist and perform, the Swoole entry serving 3.5 million pipelined requests per second on the plaintext test. But they are libraries with their own I/O clients rather than a property of the language, and most of the ecosystem's packages were written for the blocking model. A chat backend, a multiplayer game server, a trading gateway, a streaming pipeline or a push notification service is the normal case for Node.js, Go, Elixir and Erlang, Java or C#, and those ecosystems have the libraries to match.

Latency budgets under a millisecond fall on the same side. The floor of a PHP-FPM request is below a millisecond on an idle machine, and nothing built on it stays there under load, so a system with that budget is written in a compiled language.

## Outside the server

PHP is a language for servers. It has a command-line interpreter and a great deal of tooling is written with it, but for desktop applications, mobile applications, browsers, embedded devices or the distribution of a standalone binary to end users, it has no story that any team should build on. If your users do not run a PHP interpreter, write the tool you give them in something else.

<img src="images/ch09-toolbox.png" alt="A workshop wall with tools hung in outlines. An elephant stands in front of it, putting a wrench back in its outline and reaching for a different tool. On the bench below, a half-finished object that clearly needs the second tool" width="560">

## Language-level guarantees

A `match` with a missing arm throws at runtime. That one fact describes the type system of [The Language in 2026](ch05-the-language.md): it is enforced at runtime, at the boundaries of functions and properties, with no generics in the language, no compile step, no ownership or lifetime model and no exhaustiveness checking. The ecosystem's answer is a static analyser run at its strictest level in every build, which gives a typed project most of what a compiler would, and many large PHP codebases live with that answer. If "the compiler guarantees it" is a requirement for you rather than a preference, because of the domain, the regulator or the size of the codebase, TypeScript, Java, C#, Kotlin, Go or Rust will serve you better, and I will not argue otherwise.

## Teams and scale

One professional developer in five wrote PHP last year, one in eleven names it a primary language, and its share of the web has fallen from 80 to 70 percent in a decade. The share of developers is smaller than the share of running servers. [Footprint](ch01-footprint.md) also documents the companies that left PHP, and they left for Java, Go or TypeScript when a web monolith had grown into a set of services: Zalando in 2010, Trivago in 2021, Dailymotion and BlaBlaCar in 2025 and 2026. Their public documents give the architecture as the reason, not the runtime's cost.

If your engineers already work in another language, on a platform built for it, adding PHP for a new service gains you little. The runtime's advantages, described throughout this book, are advantages of simplicity, and a second stack removes them. And if your company has reached the scale where it rewrites its monolith into typed compiled services, you are following a pattern in which PHP is the thing being left, as Ruby and Python are at the same stage elsewhere.

## Where the doubt does not apply

The same evidence supports the opposite verdict, and without adjectives. Request-and-response web applications at any scale you are likely to reach: content, commerce, back offices, APIs, the platforms of [Footprint](ch01-footprint.md) and the custom applications built beside them. Teams that value a runtime with no process to babysit and a deployment that is a file copy. Organisations that must run software for a decade on hosting they do not control, where the installed base and the four-year support window matter more than throughput. And products whose hard part is the domain rather than the machine, which is most products.

> The limit of this chapter: it names the cases the evidence covers. A domain I have not measured I have not judged, and if yours is one of them, run the week that follows before believing either the reputation or me.

## What to verify yourself

Write down the one workload in your product that worries you most, and look for it above. If it is here, the advice stands unless your own measurement contradicts it. If it is not, [An Evaluation in One Week](ch10-evaluation.md) exists for it.
