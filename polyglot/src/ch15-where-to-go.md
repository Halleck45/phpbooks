# Where to Go from Here

The book stops here. The language does not, and neither does the project you were handed. **Four places keep you current, and none of them belongs to a vendor.**

## The manual

[php.net](https://www.php.net/) is the reference, and it is a good one. Every function has a page with its signature, its changelog by version, and examples that run. The user-contributed notes under each page are a mixed bag; the text above them is not. Bookmark the migration guides, one per version ([php.net/manual/en/migration85.php](https://www.php.net/manual/en/migration85.php) and its siblings): they list every deprecation and every new feature, and reading the one for your project's next version is the cheapest upgrade planning you will do.

## The RFC wiki

Every change to the language goes through a public proposal, a discussion on the internals mailing list, and a vote by the core developers. The proposals live at [wiki.php.net/rfc](https://wiki.php.net/rfc), accepted, declined, and in progress. **Reading the accepted RFCs for a version tells you not just what changed but why**, with the alternatives that were rejected and the arguments against. When a feature looks odd, its RFC usually explains the constraint that made it so.

## The Foundation and the FIG

The [PHP Foundation](https://thephp.foundation/) funds the core developers who maintain the interpreter and shepherds the language's direction. Its blog reports on releases and on what is being worked on. The [PHP-FIG](https://www.php-fig.org/) (Framework Interoperability Group) publishes the PSRs and the PER Coding Style, the interfaces and conventions that let libraries from different authors work together. When a codebase mentions PSR-something, the FIG site has the two-page spec.

## The framework your project uses

Most PHP projects sit on a framework, and the framework's own documentation is where to learn it. Full-stack frameworks: CakePHP, Laminas, Laravel, Symfony, Yii. Micro-frameworks built around PSR-15 middleware: Mezzio, Slim. Content platforms with their own conventions: Drupal, Joomla, TYPO3, WordPress.

One habit pays off from the first day. **When you read framework code, sort what you see into two piles: the language, and the framework.** A `readonly` promoted constructor, an enum in a `match`, a `?->` chain: that is PHP, and it means the same thing everywhere. A facade, a service container binding, a magic `__call` that routes to a query builder: that is the framework, and it is documented by the framework. Confusing the two piles is how people come to believe that PHP is whatever their first framework made it look like.

## A longer road

This book skipped the basics on purpose. If you want the ground-up version, with a small game, a command line tool and a web application built from nothing, the companion volume, [*The PHP Book*](https://thephpbook.readthedocs.io/), takes that road at a walking pace. It is published from the same repository as this one.

Beyond the written word, PHP has user groups in most cities and conferences on most continents. A room full of people who have solved the problem you are about to meet is worth an afternoon.

## The promise

Two to three hours ago, you opened a codebase and saw `$this->` and `::` and a runtime model you did not recognise. **You now know how PHP runs, how it types, how it packages code, and where it will surprise you.** The old reputation is filed where it belongs, in the chapter about the past.

The codebase is legible. Go read it.
