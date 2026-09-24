# Who Runs PHP

**PHP runs the majority of the web by server footprint and a minority of the web by developer headcount, and both of those numbers are true at the same time because they measure different things.** An evaluator who has heard only one of them has heard half the picture, and the half you have heard probably depends on who told you.

By server footprint: W3Techs, which crawls live websites rather than surveying people, puts PHP at **69.9 percent of all websites whose server-side language it can detect**, as of 2026-09-17. That figure moves continuously as the crawl updates, so treat it as a snapshot rather than a constant, the same caveat [The Reputation](ch01-introduction.md) already put on the number. By developer headcount, the picture looks different. The Stack Overflow Developer Survey 2025, drawing on 24,759 professional-developer respondents, found 19.1 percent reporting they use PHP, against 68.8 percent for JavaScript, 54.8 percent for Python, 48.8 percent for TypeScript, 29.9 percent for C#, and 29.6 percent for Java.

<div class="chart">

{{#include charts/ch03-adoption.svg}}

</div>

Read that chart the way it is meant to be read, not the way either side of an argument would prefer. PHP sits behind JavaScript, Python, TypeScript, C#, and Java, and ahead of Go and Ruby, at 17.4 and 6.9 percent respectively. It is not the dominant language among professional developers, and it is not a niche one either; it occupies a specific, middling, well-populated position, and a hostile reader who checks the survey directly will find exactly this chart, not a rounder or friendlier one.

The two numbers are not in tension. They are counting different populations. The W3Techs figure counts running websites, most of which were built once and are maintained lightly if at all; a huge fraction of the web is smaller commerce sites, blogs, and content platforms built on a CMS, and CMS platforms, among them Drupal, Joomla, TYPO3, and WordPress, run on PHP. The Stack Overflow figure counts developers who chose to answer a survey aimed at professionals actively writing code day to day, which is a different, smaller, and more self-selected population than "everyone who has ever deployed a website." Both numbers are honest. Neither one, alone, answers "is PHP the language my new project's target developer pool already knows," which is closer to the developer-headcount question, or "will my application be running alongside a lot of other PHP infrastructure," which is closer to the server-footprint question.

<img src="images/ch03-who-runs.png" alt="A world map with two overlapping layers: a dense shading across most countries representing server footprint, and a smaller, brighter cluster of dots representing the professional developers who write the code." width="560">

For a hiring decision specifically, the developer-headcount number is usually the more useful one, because it is closer to answering "how many people who already know this language could I plausibly hire," while the server-footprint number is closer to answering "how much of the surrounding infrastructure, from hosting control panels to CMS plugins to other companies' internal tools, will assume PHP is in play." Both questions are legitimate parts of a due-diligence review, and conflating them into a single "PHP is popular" sentence loses the distinction an evaluator actually needs.

## A primary-sourced case at scale

Numbers about the web in aggregate are useful, but an evaluator also wants to know what PHP looks like under real, sustained load, not just how often it appears. Wikimedia is one of the few organizations that documents this in detail, in its own words, on its own engineering wiki rather than through a third party. MediaWiki, the software behind Wikipedia and its sister projects, is roughly 70 percent PHP by Wikimedia's own account, amounting to close to two million lines of Wikimedia-maintained PHP code. It runs across seven data centers, three in the United States, two in Europe, one in Asia, and one in South America, behind a layered caching setup (Varnish and Apache Traffic Server in front, APCu and Memcached behind the application) that keeps a top-ten global site responsive under continuous, worldwide traffic.

<div class="chart">

{{#include charts/ch05-datacenters.svg}}

</div>

That geographic spread matters for a reason beyond redundancy: it demonstrates that PHP's shared-nothing request model, explained in [The Runtime](ch02-runtime.md), is not a small-site limitation. A request in each of those seven locations boots, runs, and tears down independently, with no shared memory between them by design, and the aggregate system still serves one of the most-visited sites on the internet, with traffic routed geographically so a visitor is answered by the nearest data center rather than by a single central one. Wikimedia's own documentation is a living wiki page rather than a dated report, so this book cites it by retrieval date, 2026-09-17, and treats it the way any rolling source should be treated: accurate as of the day it was read, not fixed for all time.

What the case study does not do is stand in for a survey. One organization, however large, is an existence proof, not a distribution. It tells you PHP can be operated at that scale by an organization willing to invest in the caching and routing layers around it; it does not tell you what fraction of PHP deployments actually reach that scale, and this book will not imply otherwise by presenting one example as typical.

## Who is correctly excluded

Two names come up reflexively in any "who runs PHP at scale" conversation, and both belong on the other side of the ledger. Meta and Slack are commonly assumed to run PHP because of PHP's historical association with Meta's early engineering culture. Both actually run Hack, a related but distinct language, on HHVM, a runtime that diverged from PHP compatibility years ago. Counting them as PHP evidence would be the kind of cherry-picking this book's own neutrality rule exists to prevent, so they are named here only to be excluded, not to be claimed.

> **The limit.** Beyond Wikimedia, verifiable, primary-sourced, large-scale PHP case studies are harder to produce than the reputation would suggest. Several of the widely repeated figures about other major PHP-running platforms trace back to sponsor blog posts, conference talks summarized secondhand, or vendor material years out of date rather than to a company's own current, dated statement. This book would rather print one case study it can fully stand behind than several it cannot, and it names that trade-off here instead of quietly padding the chapter.

**What to verify yourself.** Open [w3techs.com/technologies/details/pl-php](https://w3techs.com/technologies/details/pl-php) and read the live percentage against the one printed above. Then open the Stack Overflow Developer Survey's technology results for the current year and check where PHP actually sits against the languages your own team already knows, since that comparison, not the aggregate web-share number, is usually the one that matters for a hiring decision.

Adoption answers who is running PHP and at what footprint. It does not answer how fast any of it actually is, which is a separate, frequently conflated question, and the next one this book takes on directly in [Performance](ch04-performance.md).
