# Footprint

Your first question is who actually runs on this, at what scale, and whether the answer is a list of logos or a list of documents. **PHP is the server-side language of about seven websites in ten among those whose language can be detected, and that share has been falling for a decade**. Both halves of that sentence matter, and neither means much until you know what the survey counts.

## What the web share measures

{{#include charts/ch01-server-side-languages.svg}}

W3Techs, the survey company behind the figure, inspects a sample of more than twenty million websites every day and detects the server-side language from response headers, cookies, file extensions and similar traces. The percentage is taken over the sites whose language could be detected at all, so a site behind a framework that leaves no trace is not counted. Each site is counted once, and the whole of wordpress.com or wix.com weighs as much as a personal blog. A site may also use several languages, which is why the columns do not add up to one hundred.

On the same date JavaScript on the server stands at 7.5 percent, Ruby at 7.1, Java at 5.4, Scala at 5.0, ASP.NET at 4.2 and Python at 1.1. Within its limits the survey is stable in what it says: the bulk of the addressable web runs on PHP, mostly through WordPress, and the languages people talk about more are small on this measure. Scala ahead of ASP.NET is the reminder that the survey counts what its detection can see, and that a few platforms leave a signature out of proportion to their use.

{{#include charts/ch01-server-side-trend.svg}}

PHP's share on this measure was 80.6 percent on 1 January 2015, 75.2 on 1 January 2025 and 72.4 on 1 January 2026, then 69.9 in September 2026. **The trend is down, and you should see it before anything else.** The decline accelerated in 2025 and 2026, and the share that left PHP went mostly to server-side JavaScript, which W3Techs noted in July 2026 had overtaken Ruby as the second language. Two facts sit side by side here: an installed base on the public web that nothing else matches, and a curve that is not moving in PHP's favour.

## The platforms

Most of that installed base is products, not custom code. WordPress alone runs 40.2 percent of all websites, which is 58.8 percent of the sites that use a detectable content management system, and the next PHP-based systems, Joomla, Drupal, PrestaShop and TYPO3, are each under two percent. WooCommerce, the commerce plugin for WordPress, is on 8.0 percent of all websites and represents 47.7 percent of detected e-commerce systems.

{{#include charts/ch01-cms.svg}}

The platforms also publish their own counts, each with its own bias. Moodle, the learning platform, reports 146,634 registered sites and 531 million users, counting only the sites that chose to register. Nextcloud reports more than 500,000 servers. Drupal counts 470,795 sites reporting their version through its update module, an undercount of sites that disabled it. PrestaShop states nearly 250,000 sites and more than 22 billion euros of sales through them in 2024, a self-reported figure. Shopware cites an EHI study placing it on 115 of the 1,000 largest German B2C shops in 2025, and Matomo, the analytics platform, states more than 1.4 million websites. Adobe publishes no merchant count for Adobe Commerce, so I give none.

No single number in that list matters as much as its shape. Content management, commerce, learning, file sharing and analytics are the categories where a product is installed on a server and left to run for years, and they are the categories that PHP software dominates. That is where the share of the previous section comes from.

<img src="images/ch01-backstage.png" alt="A theatre seen from the wings. On the stage, in a spotlight, a few small animals of different shapes take a bow. Backstage, in the half-light, a row of calm elephants operate the ropes, the counterweights and the lighting board that make the show run" width="560">

## Organisations that say so themselves

A company appears here only when its own engineers or its own documents say it runs PHP, and the date of that document is part of the evidence.

**Wikimedia Foundation.** Wikipedia and its sister projects run on MediaWiki, a PHP application served by PHP-FPM. The foundation's audited financial statements state more than 19.4 billion page views per month across its projects. Its production moved from PHP 8.1 to PHP 8.3 on 25 November 2025, and at the time of writing the migration to PHP 8.5 was planned for late 2026. The same infrastructure ran on HHVM until 2019, when the foundation completed its move back to the PHP interpreter. The foundation also reports peaks of 800,000 requests per second across its seven data centres, a figure that counts requests at the edge, most of which are served by the cache layer and never reach PHP, so do not read it as PHP throughput.

**Automattic.** WordPress.com and Tumblr are stated by Automattic to "run on PHP primarily". WordPress VIP, the company's enterprise hosting arm, publishes 2.4 trillion requests served per year and 22 billion requests on the night of the 2024 United States election, figures that include its CDN.

**Etsy.** The marketplace's engineering careers page states that engineers "primarily code in PHP and JavaScript", alongside Java, Go and Swift. Etsy moved its production to PHP 7 in 2016 and documented the move at the time with its production graphs.

**Mailchimp.** The company's developer blog describes its job runner and its application monolith in PHP, and its 2025 and 2026 engineering job postings ask for PHP alongside React and Go. No scale figure is published.

**Bumble (Badoo).** The engineering blog described, in 2017, more than three million lines of PHP and hundreds of application servers moved to PHP 7, with a stated saving of one million dollars in hardware. That figure is nine years old and you should weigh it as such; the company's current job postings still list PHP next to Go.

**Public sector.** The European Commission's websites run on Drupal, which their pages declare in their metadata. Commission staff presented the platform at Drupal4Gov EU in January 2026, at 770 live sites, a figure reported by attendees that I could not confirm in a Commission publication. The White House website runs on WordPress, hosted on WordPress VIP under a FedRAMP Moderate authorisation. Germany's federal Government Site Builder, the standard CMS of federal authorities, is built on TYPO3 and serves more than 80 authorities and 250 websites. Australia's GovCMS platform states more than 370 government sites on Drupal, and 77 councils in the United Kingdom share the LocalGov Drupal distribution.

## Who left, and who never was

The list of companies that stopped using PHP is as instructive as the list above, and it is shorter than the reputation suggests.

Meta and Slack are the two names most often cited for PHP at scale, and neither runs PHP. Both run Hack, a language Facebook announced in 2014, on HHVM, a virtual machine it had developed for PHP since 2011 and which dropped compatibility with PHP in 2019. Slack removed its last PHP code for the move to HHVM 4 and today maintains about five million lines of Hack. Both companies show that a codebase started in PHP can grow very large, and neither says anything about the PHP interpreter, so I never count them.

Zalando rewrote its Magento shop in Java in 2010, by the account of a former engineer. Trivago replaced a large PHP codebase with a TypeScript application between 2020 and 2021. Dailymotion, which served its site from PHP and Symfony from 2005, states in a 2026 job posting that it is "gradually reducing PHP" and that new development happens in Go, Java and Python. BlaBlaCar, a Symfony shop in 2015, describes in its postings a migration "from a PHP/Symfony stack towards a Java/JS-dominated one". Those are the cases I found with a primary source, and they share a pattern: a company whose product had outgrown a web monolith moved its services to a compiled or JVM language, as companies leaving Ruby or Python do at the same stage.

## The developer population

Web share measures servers. Surveys measure people, and they place PHP lower.

| Measure | Where PHP stands | Source and date |
|---|---|---|
| Used in the past year, professional developers | 19.1 percent, 12th language | Stack Overflow survey, 2025 |
| Used in the past year, weighted sample | 17 percent, 13th language | JetBrains Developer Ecosystem, 2025 |
| Primary language | 9 percent, 9th | JetBrains Developer Ecosystem, 2025 |
| Monthly contributors on GitHub | 6th language, unchanged since 2023 | GitHub Octoverse, October 2025 |
| Pull requests and Stack Overflow tags | 4th, tied with C# | RedMonk, January 2026 |
| Search engine mentions | 14th, 1.04 percent | TIOBE, September 2026 |

Each of these measures something different, and each has a known bias: the Stack Overflow sample is self-selected among its users, the JetBrains sample is weighted toward its customers, GitHub counts open-source activity, and TIOBE counts search results. Read together, they say that between one developer in six and one in five wrote PHP in the past year, that PHP is a first language for fewer people than it is a second, and that its activity on public repositories is steady. JetBrains describes PHP as in "long-term decline" alongside Ruby and Objective-C, while the same report's PHP-specific survey found that 58 percent of PHP developers do not plan to migrate to another language. What this means for hiring is a question for [Cost of Ownership](ch08-cost.md).

> The limit: the footprint is wide and old. Its width comes from products more than from custom applications, its age shows in the share of the installed base still on unsupported versions, and the language's share of developers is smaller than its share of running servers. If you are choosing a language for a new service, weigh the second fact more than the first.

## What to verify yourself

Open the W3Techs pages for server-side languages and for content management systems; they are updated daily and the historical view is public. For Wikimedia, the Phabricator tasks I cite are readable without an account and show the migration work as it happened, with dates. For any company named here, search its engineering blog and its job postings yourself, and treat the absence of PHP in recent postings as the signal it is.

Scale of deployment says nothing about how a request is served. That is where the runtime comes in.
