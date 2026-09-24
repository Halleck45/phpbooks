# Cost

**PHP itself is free and permissively licensed, its package ecosystem is free to use at a scale of close to half a million published packages, and the real cost of a PHP application is almost entirely in hosting, staffing, and maintenance discipline, not licensing.** The more useful cost question for an evaluator is not "what does PHP cost" but "what does PHP's architecture let you avoid paying for," and this chapter spends most of its attention there.

## The license, precisely

PHP is distributed under the PHP License, an OSI-approved, permissive license that does not require you to open-source anything you build with it. Today's supported floor for this book, PHP 8.4, ships under version 3.01 of that license. A newer license, version 4, based on the Modified BSD (BSD-3-Clause) text, applies starting with PHP 8.6, which had not shipped as of this writing; treat that as an upcoming change to track, not as something already governing the version you are most likely deploying today. Neither license requires a fee, a registration, or a usage report to anyone.

## What "free" actually includes

Packagist, the public registry that Composer (PHP's dependency manager) resolves packages against, lists close to half a million published packages, with roughly 5.8 million published versions between them, and a cumulative install count approaching 200 billion since the registry's launch in April 2012.

| Metric | Approximate figure |
|---|---|
| Published packages | ~468,000 |
| Published versions | ~5.8 million |
| Cumulative installs since April 2012 | ~200 billion |

Those are live counters, so treat the exact digits as a snapshot rather than a fixed fact, the same discipline this book has applied to every other continuously updated figure. The magnitude is the point: a dependency you need for a PHP project is very likely already published, versioned, and installable through one command, at no cost beyond the time it takes to audit what you are pulling in.

Publishing to Packagist costs nothing and requires no vetting beyond what Composer itself checks mechanically: every install is verified against a hash recorded in the project's lockfile, so a dependency cannot silently change between the version your team reviewed and the version that actually gets installed. That is a real, useful guarantee, and it is also a narrower one than full supply-chain provenance: a hash confirms the code has not changed since it was locked, not that the code was safe when it was first added. The responsibility for that first review still sits with the team pulling the dependency in, in PHP's ecosystem the same as in any other language's.

## What you are not paying for: proprietary orchestration

<img src="images/ch07-cost.png" alt="A single PHP application shown running unchanged across three different, differently shaped hosting environments: a bare-metal server, a small VPS, and a container orchestrator, with no adapter layer between them." width="560">

PHP-FPM's process model, described in [The Runtime](ch02-runtime.md), requires only a POSIX-compliant operating system, a web server, and the PHP runtime itself to serve requests at scale. It does not require a proprietary serverless orchestration layer, and nothing about the architecture forces you to adopt one. That is a real, verifiable, architectural fact, not a claim about any specific hosting company, and this book states it that way on purpose: the same application can run on a bare-metal machine you own, a minimal virtual server, or a container orchestrator, without re-architecting it to fit any one of them.

That property has a specific, current relevance for organizations operating under data-localization requirements or a sovereign-cloud mandate, where compute has to stay on infrastructure that meets a jurisdiction's own residency rules rather than on whichever platform is most convenient. A runtime that does not require a specific vendor's managed orchestration to function is easier to relocate onto infrastructure that meets those rules, because the constraint being satisfied is about where the machine sits, not about which proprietary service the application was written against.

> **The limit.** This portability claim is about the PHP runtime, not about your whole operational stack. A team that has also adopted a cloud-specific managed database, a cloud-specific managed queue, or observability tooling built around one vendor's agent has already reintroduced the same lock-in at those layers, regardless of which language sits in front of them. State this argument as "the runtime does not force cloud lock-in," not as "a PHP application is portable," because the second claim is broader than the evidence supports.

## What PHP gives you for security, by default

Part of PHP's reputation, addressed once in [The Reputation](ch01-introduction.md), includes an assumption that the language is inherently insecure. The current language ships specific, checkable primitives that argue against treating that as still true by default. `password_hash` and `password_verify` provide a maintained, algorithm-agnostic password-hashing API, so an application does not need to hand-roll one. Libsodium bindings have been bundled with PHP since version 7.2, giving direct access to audited cryptographic primitives without a third-party extension. PDO's prepared statements separate a query's structure from its data at the driver level, which is the standard, effective defense against SQL injection when it is actually used. None of these facts make an application secure by themselves; a team that ignores them can still write an insecure application in any language. They do mean the tools to do it correctly are already in the standard library, not an extra purchase or a third-party dependency you have to find and vet first.

## What this chapter cannot price

There are two cost questions this book would like to answer with a number and cannot, and it says so here rather than guessing. A clean, sourced, PHP-versus-other-language hosting-cost comparison does not exist without relying on a specific hosting vendor's own marketing figures, which this book's sourcing rules exclude; the architectural argument above is offered instead of a number precisely because the number is not available without that compromise. The salary and job-demand gap already named in [Who Maintains It](ch06-who-maintains-it.md) applies here too: this book cannot tell you, with a defensible source, whether a PHP developer costs more or less to hire than a developer in another language in your specific market, and a number invented to fill that gap would be worse than no number at all.

**What to verify yourself.** Check [packagist.org/statistics](https://packagist.org/statistics) directly for the current package, version, and install counts, and compare them to the figures printed here; the gap is a live demonstration of how fast the ecosystem is still growing. Then check [php.net/license](https://php.net/license) directly against whichever PHP version you are actually planning to run, since the license version that applies depends on that specific version, not on the one this book treats as current.

Licensing and hosting cost are the parts of total cost of ownership an evaluator can price directly. The parts that are harder to price, how the language is governed, how often it changes, and what happens when a version reaches its support deadline, are exactly what [Governance and Versions](ch08-governance-and-versions.md) covers next.
