# Cost of Ownership

A language costs you three things: the people who write it, the machines that run it, and the calendar you spend keeping it current. PHP has a figure for each, and each figure has two readings. **PHP developers are numerous and, by the surveys' own medians, paid less than developers of most other languages; the runtime has the fewest moving parts to host, files served by a process pool; and the yearly release cadence imposes a yearly upgrade budget that a large share of the installed base has not been paying.** The cheap reading and the dear reading come from the same sources, and you will need both.

## People

One professional developer in five wrote PHP in the past year. That places it twelfth among languages in the largest developer survey, within a few points of Go and C.

{{#include charts/ch08-developer-usage.svg}}

Another survey agrees on the order of magnitude: 17 percent of respondents used PHP in the JetBrains survey of 2025, and 9 percent named it their primary language. The labour market itself is thinly documented in public. One aggregator of British job advertisements counted 613 permanent positions citing PHP in the six months to September 2026, up from 404 a year earlier, at a median advertised salary of 48,676 pounds, up 14.5 percent. I found no comparable public series for other countries, so I report none.

The salary figure that does exist is the survey median, and it is low.

{{#include charts/ch08-salary.svg}}

Developers using PHP reported a median of 49,586 dollars a year in the last edition of the Stack Overflow survey to publish salaries by language, the second lowest of fifty languages, against 63,694 for JavaScript, 67,723 for Python and 90,221 for Ruby. The figure is worldwide and self-reported, and PHP's respondents live disproportionately in countries with lower wages, so it says less about your city than it appears to. Read it as a cost and PHP staffing is inexpensive in the aggregate. Read it as a signal and the market values the median PHP position below the median position in other languages. If you are building a team, you need both readings.

{{#include charts/ch08-admired.svg}}

Sentiment is harder to price than salary. Among developers who used a language in the past year, 38.9 percent of PHP's users want to keep using it, the lowest of the mainstream languages and well below Rust at 72.4, TypeScript at 58.0 or Python at 56.4. The same year, 58 percent of developers whose main language is PHP said they did not plan to migrate to another. The two figures describe different populations, the occasional user and the specialist, and together they describe a language people are more often assigned to than drawn to. For hiring, that means a large pool and a retention question, and the weighting is yours.

## Machines

A PHP application in production is files on a disk, served by a pool of processes. There is no long-running application process to monitor, restart or drain, no warm-up, no heap to size: that is the shared-nothing model of [The Runtime](ch02-runtime.md), and it gives PHP the fewest moving parts to host. It is why every shared hosting provider in the world offers it, and why the platforms of [Footprint](ch01-footprint.md) can be installed by people who are not engineers. For most applications, a container image of the official `php:8.5-fpm` build, a web server in front and a load balancer are the whole production architecture, and adding capacity is adding a copy.

What you pay for that simplicity is efficiency per machine. In the benchmark of [Throughput and Latency](ch03-throughput-and-latency.md), a framework under PHP-FPM serves a few tens of thousands of requests per second on a large server; a worker runtime multiplies that by three to four, and brings with it the operational discipline of a long-running process. The engine's own progress shows in the same ledger. Badoo reported in 2017 that moving its hundreds of application servers from PHP 5 to PHP 7 saved it about one million dollars in hardware, a self-reported figure from the company's engineering blog. I have no independent measurement of hosting cost per request across languages, and I make no claim about one.

<img src="images/ch08-ledger.png" alt="An open ledger on a desk with three columns headed by small icons: a group of people, a rack of servers, a calendar. An elephant with reading glasses writes in the second column. Beside the ledger, a small stack of coins and a wall calendar with one month circled" width="560">

## Calendar

Wikimedia's upgrade history is public: production moved from PHP 7.4 to 8.1 in March 2025, to 8.3 in November 2025, and was planning 8.5 for late 2026. **A minor version ships every year in late November or early December and is supported for four years, so you must plan one upgrade a year to stay in active support, or one every two to three years to stay in security support.** The work of an upgrade is bounded: the language deprecates in a minor version and removes at the next major, the analysers report the deprecations, and Rector applies the mechanical rewrites. On a well-tested codebase a version upgrade is measured in days, on an untested one in weeks.

The installed base shows what happens when that budget is not paid.

{{#include charts/ch08-php-versions-in-use.svg}}

Among packages installed through Composer, 94 percent of installs in August 2026 ran on PHP 8 and 0.2 percent on PHP 5. WordPress sites reporting to wordpress.org stood at 77 percent PHP 8, 21 percent PHP 7 and 2 percent PHP 5. The web as W3Techs detects it ran 64 percent PHP 8, 28 percent PHP 7 and 8 percent PHP 5, and those last two are versions that have received no security fix since November 2022 and December 2018 respectively. Those are three populations: the developers who build, the sites that update themselves, and the web as it is. The gap between the first and the third is the ecosystem's technical debt, and if you inherit a PHP codebase, ask which population it belongs to before you quote a price.

> The limit: PHP's staffing is cheap by the medians and its hosting has the fewest moving parts, and each of those facts comes with its shadow, a retention question and an installed base of which more than a third runs unsupported versions. Budget the yearly upgrade and hire for the specialist rather than the occasional user, and you get the cheap side of each; skip either, and you get the other.

## What to verify yourself

Search the job boards of your own city for the language, then for the frameworks you would use, and compare the count and the advertised range with the languages you are considering, which beats any worldwide median. Ask your hosting provider or your platform team what PHP version they run today and how they would upgrade it. Then take one open-source PHP project of your codebase's size that is two versions behind, and run Rector's upgrade set on it: the diff it produces is the cost of a version, in front of you.

The cases where this arithmetic stops applying, because PHP is the wrong tool rather than a dear one, are collected in [Where PHP Is the Wrong Choice](ch09-wrong-choice.md).
