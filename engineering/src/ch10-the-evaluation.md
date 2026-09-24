# The Evaluation

**Every figure in this book was checkable when it was written, and every figure in this book will have moved by the time you read it; this chapter exists to hand you the checks themselves, not another number to trust in their place.** A due-diligence reviewer does not finish an evaluation by reading someone else's conclusions. She finishes it by rerunning the parts of the evidence that matter to her own decision, and this chapter is built entirely out of the moments across the nine chapters before it where this book already asked you to do exactly that.

<img src="images/ch10-evaluation.png" alt="A short, hand-checked list with a pencil resting beside it, each line representing one command or public page a reader can verify in an afternoon." width="560">

## What your own machine already knows

Before checking anything about the wider ecosystem, check the specific PHP install you would actually be deploying against. The following script, kept deliberately small, reports the facts [The Runtime](ch02-runtime.md) spent a chapter explaining: which version you are running, whether opcache is actually loaded rather than theoretically available, and whether the JIT is enabled.

```php
<?php

declare(strict_types=1);

function reportRuntimeStatus(): array
{
    return [
        'php_version' => PHP_VERSION,
        'sapi' => PHP_SAPI,
        'opcache_loaded' => extension_loaded('Zend OPcache'),
        'jit_enabled' => function_exists('opcache_get_status')
            && (opcache_get_status(false)['jit']['on'] ?? false),
    ];
}

foreach (reportRuntimeStatus() as $fact => $value) {
    printf("%-15s %s\n", $fact, var_export($value, true));
}
```

Run it with `php status.php` against any environment you are evaluating, including one a vendor hands you with assurances attached. A vendor's claim that "opcache and JIT are both on" is a sentence; this script's output is a fact about that specific machine, and the two are not the same kind of evidence.

## Every check this book already asked of you, in one place

Each earlier chapter ended with something to verify in an afternoon. Rerunning them together, in order, reconstructs this book's entire evidence base from live sources rather than from this book's printed snapshot of them.

```bash
# Chapter 1 and 8: current adoption and version fragmentation
# https://w3techs.com/technologies/details/pl-php

# Chapter 2: your own install's runtime state
php -v
php -i | grep -i opcache

# Chapter 3: professional developer adoption by language
# https://survey.stackoverflow.co (current year's technology results)

# Chapter 4: CPU-bound benchmarks, still actively maintained
# https://benchmarksgame-team.pages.debian.net/benchmarksgame/

# Chapter 6: the PHP core's own contributor activity
# https://github.com/php/php-src

# Chapter 7: live package, version, and install counts
# https://packagist.org/statistics

# Chapter 8: the current support window for your PHP version
# https://php.net/supported-versions.php
```

None of these checks require special access, a paid account, or insider knowledge. That is deliberate: a book that asked you to trust a number you could not independently reach would be asking you to trust it the same way the reputation in [The Reputation](ch01-introduction.md) asked people to trust secondhand impressions of PHP instead of the current language itself, and this book has spent nine chapters arguing against exactly that habit.

## Reading a vendor's own claim the way this book reads its own

The method matters more than the specific list above, because the list will age and the method should not. When a vendor, a framework's own documentation, or a colleague hands you a performance number, a security claim, or an adoption statistic, ask the same three questions this book asked of its own research before printing anything. Where does the number come from, in the source's own words, not a summary of it? What exactly was measured, and does that match what you actually care about, the way [Performance](ch04-performance.md) had to separate a JIT microbenchmark from a web-request benchmark before either one meant anything? And what does the source itself say it does not know, since a source willing to state its own limits is more trustworthy than one that has none?

## A worked example, using this book's own weakest citations

The most useful test of this method is to point it at this book itself. [Who Maintains It](ch06-who-maintains-it.md) cites a JetBrains survey that states its own limitation plainly: results may skew toward JetBrains' own product users. That is a source that passes the test, not because it is unbiased (no survey of self-selected respondents is) but because it tells you which way it likely leans before you have to guess. [Performance](ch04-performance.md) does the opposite kind of honest work: it names a benchmark series, TechEmpower, that stopped publishing, with the exact date, rather than quietly citing its last round as if nothing had changed. And [Governance and Versions](ch08-governance-and-versions.md) leaves a handful of figures, the PHP Foundation's exact funding totals among them, out of its firm claims entirely, because they were confirmed only through a secondary account at the time of writing, not through the Foundation's own page directly. [Sources](appendix-01-sources.md) marks each of those explicitly as pending direct verification instead of printing a number this book cannot stand behind. A source that tells you what it does not know, in its own words, is doing the same work this book has tried to do throughout, and it is the single clearest signal to look for in anything you are handed during your own evaluation.

> **The limit.** A checklist is only as good as the day it was run. Every command and every URL above will return a different number next quarter than it returns today, the same way every figure printed earlier in this book will have moved by the time you read it. This chapter cannot give you a permanently current answer; it can only give you a repeatable way to get a current one, which is the more durable thing to hand you.

**What to verify yourself, one more time.** Pick the single figure in this book that your decision most depends on, whichever chapter it came from, and rerun its source directly before you act on it. If it still says what this book said it says, you have independent confirmation. If it does not, you have caught this book being stale before it cost you anything, which is exactly the outcome the whole approach was built to make possible.

This book opened by separating PHP's reputation from the language currently in front of you. It closes by handing that separation back to you as a method, not a conclusion: the runtime model, the adoption figures, the performance comparisons, the cost structure, the governance process, and the plainly stated limits are only worth as much as your own willingness to check them again. [Sources](appendix-01-sources.md) lists exactly where every figure in this book came from, chapter by chapter, so that checking is never more than one link away.
