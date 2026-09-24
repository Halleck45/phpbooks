# Governance and Versions

**PHP's language changes go through a public proposal-and-vote process that requires a supermajority for anything that changes the language itself, releases ship on a fixed annual schedule with a four-year support window, and core maintenance is funded by a foundation independent of any single company's product roadmap.** That combination, predictable process, predictable cadence, and funding that does not depend on one vendor staying interested, is what an evaluator is actually asking about when they ask "who is in charge of this language."

## The release cadence, and what it commits to

PHP ships one feature release per year, in late November. Each branch then gets two years of active support, meaning bug fixes and security fixes both, followed by two more years of security-only support, four years of support in total before a branch reaches end of life.

| Version | Released | Active support ends | Security support ends |
|---|---|---|---|
| PHP 8.2 | 8 Dec 2022 | 31 Dec 2024 | 31 Dec 2026 |
| PHP 8.3 | 23 Nov 2023 | 31 Dec 2025 | 31 Dec 2027 |
| PHP 8.4 | 21 Nov 2024 | 31 Dec 2026 | 31 Dec 2028 |
| PHP 8.5 | 20 Nov 2025 | 31 Dec 2027 | 31 Dec 2029 |

This table is the single most useful piece of evidence in this chapter, because it converts "is PHP well maintained" into a checkable date specific to the version you are actually running. A branch past its security-support end date is not receiving fixes for newly discovered vulnerabilities, from anyone, and that is a fact about your specific deployment, not an opinion about the language.

<div class="chart">

{{#include charts/ch08-versions.svg}}

</div>

## What the RFC process actually requires

Language changes are proposed and voted on in the open, at a public wiki dedicated to the process, and PHP's own rule requires a two-thirds majority for a change to the language itself to pass, a higher bar than a simple majority. That threshold exists precisely to slow down changes that would break existing code or fragment the language's own consistency, at the cost of moving slower than a benevolent-dictator model might. Neither side of that trade is free, and this book states it both ways rather than presenting the higher bar as an unambiguous good: a supermajority requirement protects stability, and it also means a change with strong majority support but not overwhelming support can still fail.

<img src="images/ch08-governance.png" alt="A single ballot box at the center of a wheel of contributors, with a large majority of the wheel shaded to represent the two-thirds threshold a change needs to pass." width="560">

## Who funds the work

The PHP Foundation was established in November 2021, in response to concern that core-language maintenance had become dependent on the availability of a small number of individual contributors' paid time from their employers, rather than on a funding base broad enough to survive any one employer's decision to reduce that time. The Foundation publishes its funding on a public ledger, showing ongoing contributions from a range of technology companies and open-source organizations with a stake in PHP's continued maintenance. The mechanism matters more than any single contributor's name: funding spread across multiple independent organizations, visible on a public ledger rather than disclosed only in a press release, is a different and more durable arrangement than maintenance that depends on one company's continued goodwill.

Funding of this kind pays for specific, unglamorous work: reviewing and merging RFCs, triaging and responding to security reports against the language's own engine, and doing the release engineering that keeps the annual cadence in the table above actually landing in late November rather than slipping. PHP maintains a dedicated process for handling security reports against the core language, separate from the RFC process used for new features, precisely because a vulnerability report needs a faster, more controlled path than a public debate about a language feature does. This book does not have a dated, primary-sourced count of how many core vulnerabilities that process has handled in a recent window to print here, and it would rather leave the number out than borrow one from a third-party aggregator that was not the process's own account.

Compare this to the alternative most evaluators have implicitly in mind: a language or framework whose direction is set entirely by one company, where a change ships because that company decided to ship it, not because it survived a public vote. That model can move faster in the short term. It also means the language's future is exactly as stable as that one company's continued interest, a risk PHP's multi-sponsor funding and public RFC process are both explicitly structured to avoid, even at the cost of the slower-moving supermajority bar described above.

## Where the tidy cadence meets a messier reality

The release table above describes what PHP ships. It does not describe what is actually running. W3Techs' crawl of live, PHP-running websites, as of 2026-09-17, found 64.1 percent on the PHP 8.x line, 28.1 percent still on 7.x, whose last branch reached end of life in November 2022, and 7.8 percent still on PHP 5.x, out of support since 2018 or 2019. A residual 0.1 percent was still detectable on PHP 4.

That is a market-reality caveat, not a claim about the current language, and the distinction needs holding onto carefully: PHP 8.x's own support story, laid out in the table above, is exactly as predictable as this chapter describes. What a meaningful share of the installed base actually does with that predictability is a separate question, about specific organizations' operational discipline, not about governance. It pairs with, and should never be blended with, the self-reported version split in [Who Maintains It](ch06-who-maintains-it.md): one number describes servers actually running on the internet, the other describes what developers say they personally work in, and a chart that mixes the two is making a comparison that was never apples to apples.

> **The limit.** A governance process this predictable only protects you if your own organization keeps pace with it. The support table above is a promise about what PHP Foundation-backed maintainers will do on a fixed schedule; it is not a promise that your specific deployment will be upgraded before its branch's security support ends. Roughly a third of the PHP-running web is currently not keeping that pace, and [Where PHP Is the Wrong Choice](ch09-wrong-choice.md) treats the risk of inheriting one of those deployments directly.

**What to verify yourself.** Check [php.net/supported-versions.php](https://php.net/supported-versions.php) directly against the version you are running or evaluating, since the dates in the table above will eventually be superseded by a newer release cycle. Then check [w3techs.com/technologies/details/pl-php](https://w3techs.com/technologies/details/pl-php) for the current version-fragmentation split, and compare it to the one printed here to see how much, if at all, the installed base has caught up.

Governance and version support describe how PHP is maintained when everything goes as designed. [Where PHP Is the Wrong Choice](ch09-wrong-choice.md) is where this book turns to what happens when the language itself, not a specific deployment's neglect, is genuinely the wrong tool, and makes that case as plainly as it has made every other one.
