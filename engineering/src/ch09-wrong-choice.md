# Where PHP Is the Wrong Choice

**PHP is the wrong choice for true parallel computation, for machine learning and numeric data science work, and for an organization that cannot commit to upgrading before a branch's security support ends; it is a weaker but not impossible choice for native desktop or mobile applications and for workloads with heavy, sustained CPU computation.** This chapter exists so the rest of this book can be believed, and it names each of these plainly, with the evidence behind it, rather than softening the ones that complicate a simple story.

## No true parallelism, by design

[The Runtime](ch02-runtime.md) already named this limit once: PHP has no native multithreading in userland. Fibers, added in PHP 8.1, give cooperative concurrency, one fiber suspending itself so another can run, which is genuinely useful for I/O-bound work but is not parallelism, because only one fiber's code executes at any given instant. The `parallel` and `pthreads` PECL extensions give real operating-system-thread parallelism, and they are real, current, and worth naming rather than omitting; they are also third-party and narrowly adopted, which is a fair reason to treat them as an exception rather than a default answer. If your workload is defined by needing two CPU-bound tasks to run at the literal same instant inside one process, nothing in PHP's default toolchain does that, and no serving layer or async library changes it, because the limit is in the language runtime itself, not in how you deploy it.

The same architectural gap shows up in real-time, bidirectional communication. A WebSocket connection that needs to stay open and push data to a client without the client asking for it does not fit cleanly into PHP-FPM's one-request-in, one-response-out model; it becomes workable through the same async libraries, Swoole or OpenSwoole in particular, already introduced in [The Runtime](ch02-runtime.md), or through a serving layer built for long-lived connections. That is a real, working answer, not a dead end, but it is an added piece of infrastructure a request-response-native language like PHP needs for a job some other runtimes handle as a first-class case.

## The CPU-bound comparison, stated correctly

[Performance](ch04-performance.md) already showed the counterintuitive half of this limit: PHP is faster than Python on CPU-bound microbenchmarks, not slower. The defensible version of the "PHP is slow" limit is narrower and still real: PHP trails compiled and JIT-mature languages, Go, Rust, Java, and C#, on sustained CPU throughput.

| Comparison | What the evidence shows |
|---|---|
| PHP vs Python, CPU-bound tasks | PHP faster, by roughly 1.5 to 2x |
| PHP vs compiled/JIT-mature languages | PHP slower; this book has no single clean multiplier to print |

A workload that is genuinely CPU-bound, heavy numeric simulation, large-scale in-memory data transformation, anything where the bottleneck is arithmetic rather than waiting on a network or a database, is a workload PHP is architecturally not the fastest available tool for. That does not mean PHP cannot do it; it means the honest comparison set is Go, Rust, Java, and C#, not Python, and a vendor or a team that frames this limit against the wrong reference class is either uninformed or shading the comparison in PHP's favor.

## Native mobile and desktop apps: weaker than assumed, not solved

The traditional answer here was simple: PHP has no first-party toolkit for building native desktop or mobile applications, full stop. That answer is a year or two out of date. NativePHP, a community project built specifically on top of Laravel, one of the frameworks named in this book's fixed list, packages a PHP application into desktop and mobile app-store builds, and its own documentation claims production deployments as of 2026. Naming it once, here, with that date, is more honest than pretending the gap is still absolute; naming it repeatedly, or treating it as equivalent in maturity to Swift, Kotlin, or a mature cross-platform toolkit, would overstate what a single, young, framework-specific community project has actually proven at scale. The honest framing is that no first-party toolkit exists, a community solution does, and it is unproven at the maturity level a decision maker would want before betting a flagship product on it.

<img src="images/ch09-wrong-choice.png" alt="A decision tree with PHP as the trunk and several branches, some ending in a checkmark, others ending in a small warning flag, representing a workload where PHP is not the right fit on its own." width="560">

## Machine learning and numeric data science

This gap is real, and this book would rather make the ecosystem-density argument than borrow a usage statistic that is not actually about PHP. There is no PHP equivalent to NumPy, pandas, PyTorch, or TensorFlow with comparable maturity, community size, or hardware-acceleration support. You can check this yourself directly: search Packagist's own categories, or PHP's own extension index, for numeric computing or machine-learning tooling, and compare what you find to the equivalent search in Python's package index. The gap is not a matter of opinion, and it does not require a borrowed survey statistic to demonstrate; it is visible directly in what each ecosystem has actually built.

## Long-running processes: partially solved, precisely

[The Runtime](ch02-runtime.md) and [Scale](ch05-scale.md) both already cover this: FrankenPHP's own documentation states plainly that PHP "was not originally designed for long-running processes," and worker-mode serving mitigates the resulting memory-growth risk without eliminating it, which is why periodic worker restarts are the documented, standard mitigation rather than an admission of failure. That is a fair, non-defensive summary of a real limit, sourced from the vendor's own candor about it rather than from a critic.

## No generics

PHP has no generics in the language itself. PHPStan and Psalm, the two static-analysis tools named throughout this book, both read the same `@template` docblock convention to approximate generic types, which gives you real, useful type-checking at development time, entirely outside the language engine: nothing about a generic type declared this way is enforced when the code actually runs. A codebase that leans on this convention is choosing a real, working substitute, not the language feature itself, and the distinction matters if your evaluation criteria specifically require compile-time generic enforcement rather than an opt-in static-analysis approximation of it.

## The market-reality caveat, not a language caveat

[Governance and Versions](ch08-governance-and-versions.md) already gave you the number: roughly 28 percent of PHP-running websites are still on the 7.x line, unsupported since November 2022, and close to 8 percent are still on PHP 5, unsupported since 2018 or 2019. Inheriting one of those deployments, through an acquisition, a legacy internal tool, or a vendor relationship, is inheriting a real security and maintenance liability. This is not a claim about the current language, which is actively maintained on the schedule described in [Governance and Versions](ch08-governance-and-versions.md); it is a claim about what a specific organization did, or failed to do, with an old version of it, and an evaluator doing due diligence on an existing codebase should treat the two as entirely separate risk assessments.

> **The limit, stated once more, directly.** None of the gaps in this chapter are solved by picking a different PHP framework, and this book will not imply otherwise. Where they are solved at all, they are solved by adding a second, purpose-built tool alongside PHP, not by PHP alone.

**What to verify yourself.** Read PHP's own Fibers documentation and decide for yourself whether cooperative concurrency actually covers your workload, rather than taking this chapter's summary as the final word. Then run the specific numeric or data-heavy task closest to your actual workload against both a PHP implementation and whatever language you would otherwise use, the same rerun-it-yourself standard [Performance](ch04-performance.md) already asked of you, since a real benchmark of your own task beats any general comparison this book can print.

Every limit in this chapter has the same shape: PHP plus one additional, purpose-built piece of infrastructure, not a wholesale replacement. [The Evaluation](ch10-the-evaluation.md) closes this book by turning that shape, and every sourced figure before it, into something you can check yourself, on your own machine, before you decide anything.
