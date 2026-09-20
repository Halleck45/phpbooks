# Performance

**How fast PHP is depends entirely on what you measure: on a typical web request it is fast because most of the request's time is spent waiting on a database or the network, not on PHP itself, and on CPU-bound computation it is faster than Python and slower than compiled or JIT-mature languages such as Go, Rust, Java, and C#.** Both halves of that sentence are load-bearing, and a benchmark that only shows you one of them is not showing you the whole picture.

"Fast" is doing three different jobs in most performance conversations, and it is worth separating them before looking at a single number. Throughput, how many requests a fixed amount of hardware can serve per second, is what capacity planning cares about. Latency, how long one specific request takes to answer, is what a user waiting on a page load cares about. Raw computational speed, how quickly a fixed piece of arithmetic finishes, is what a background job doing heavy numeric work cares about. PHP's shared-nothing, request-per-process model, covered in [The Runtime](ch02-runtime.md), makes the first two mostly a function of how much I/O your request does and how well your serving layer is tuned, not a function of the language's raw arithmetic speed. The third is where the language itself is the bottleneck, and it is the one this chapter spends the most care on, because it is also the one most often measured with a synthetic microbenchmark and then quietly applied to a claim about web performance, a substitution this chapter tries hard not to make.

## The benchmark this book cannot use

The industry's standard cross-language web-framework benchmark, TechEmpower Framework Benchmarks, was discontinued on 24 March 2026, and its GitHub repository is now archived. The last completed round, Round 23, published 17 March 2025, covered more than 330 framework implementations across languages, and it is worth stating the discontinuation plainly, with its date, rather than quietly citing an outdated round as if it were still current: a reader who goes looking for a newer round will find only the archive notice, and this book would rather explain the gap than pretend it does not exist. This is also why this chapter leans more heavily on two other sources: a benchmark shipped by PHP's own JIT proposal, and an independently maintained cross-language benchmark suite that is still active.

## What the JIT actually buys you on a web request

[The Runtime](ch02-runtime.md) already introduced PHP's Just-In-Time compiler and the RFC's own admission that it helps CPU-bound code far more than typical web code. The same benchmark is the cleanest performance evidence in this book, precisely because it comes from the people who built the feature and had every incentive to show it in the best light.

<div class="chart">

{{#include charts/ch04-jit.svg}}

</div>

Three hundred and twenty-six requests per second with the JIT on, three hundred and fifteen without it, on a WordPress request. That is roughly a three percent difference, on a real application, from the RFC that introduced the feature. The reason is architectural, not a tuning failure: a WordPress request spends most of its time in database queries and I/O, not in the numeric computation the JIT accelerates. If your evaluation criteria include "will enabling the JIT make my web application meaningfully faster," the honest answer, from PHP's own numbers, is usually not much, and any benchmark claiming otherwise on a web workload deserves a second look at what it actually measured.

The JIT is not pointless; it is aimed at a narrower target than "PHP" in general. A CLI script doing image processing in a tight loop, a background worker running a numeric simulation, a queue consumer doing heavy string or array transformation with no network call in the middle: these are the workloads where the compiler's gains actually show up, because they are CPU-bound in the way a WordPress request is not. An evaluator deciding whether to enable the JIT should ask what fraction of the actual workload is arithmetic versus waiting, not whether the JIT exists.

## The comparison PHP usually loses on the wrong axis

The most common performance criticism of PHP compares it to Python and calls it slow. The Computer Language Benchmarks Game, an independently maintained, actively updated cross-language suite, tells a different story on CPU-bound tasks. Testing PHP 8.4.1 against Python 3.13 on tasks including fannkuch-redux, n-body, and spectral-norm, three classic CPU-bound benchmarks with no I/O to hide behind, PHP came out **faster than Python on most of them, by roughly one and a half to two times**.

| Task | What it stresses | Which language was faster |
|---|---|---|
| fannkuch-redux | Permutation generation, tight loops | PHP |
| n-body | Floating-point arithmetic, simulation | PHP |
| spectral-norm | Matrix and vector math | PHP |

This matters for how you frame the limit, not just for the number itself. **"PHP is slow" is not true relative to Python; it is true relative to compiled and JIT-mature languages.** A comparison that stops at Python and calls the result settled is comparing PHP to the wrong reference class, and a due-diligence reviewer who runs this benchmark herself will find the same ranking this book prints. This is also the finding most likely to surprise a reader who arrived with the reputation described in [The Reputation](ch01-introduction.md) already in mind: a language remembered as slow turns out to beat one of the languages most associated with well-regarded data and scripting work, on the specific axis both languages are actually being measured on.

<img src="images/ch04-performance.png" alt="A simple racetrack with PHP shown ahead of Python but behind Go, Rust, Java, and C#, illustrating that the comparison depends entirely on which lane you are standing in." width="560">

> **The limit.** PHP trails compiled and JIT-mature languages, Go, Rust, Java, and C#, on sustained CPU-bound throughput, and this book does not have a single, clean, primary-sourced multiplier to put a number on that gap the way it can for Python. That is a real limit of the available evidence, not a claim that the gap is small: a workload that is genuinely CPU-bound, doing heavy numeric computation with little I/O to overlap it with, is a workload PHP is architecturally not the fastest tool for, and [Where PHP Is the Wrong Choice](ch09-wrong-choice.md) treats that case directly.

**What to verify yourself.** The Computer Language Benchmarks Game publishes its full, current results at its own site, and its methodology page explains exactly what hardware and what version of each language it used; rerun a task that resembles your own workload rather than trusting the summary table. If you want to see PHP's request-handling throughput for yourself instead of trusting either benchmark, the most honest test is the one described in [The Evaluation](ch10-the-evaluation.md): run your own representative workload against your own PHP version, with opcache and JIT in the state you would actually deploy them.

Raw speed on a single machine is one part of a capacity question. The part that usually matters more in production is what happens as load grows and you add machines, which is where [Scale](ch05-scale.md) picks up.
