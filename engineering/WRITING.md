# PHP guide for the decision maker

This file is the editorial contract for the decision leader book. Read it before writing or editing any chapter. The general house style (rhythm, narrative, no filler) lives in the `book-style` skill and applies on top of everything here. This book is published under the umbrella of the PHP Foundation and is meant to sit on php.net, so it is held to a higher standard than the other books in this repository: every sentence must survive a hostile reader with a search engine.

## 1. The reader

**The Decision Maker or Engineering Leader. "Show me how PHP completes my architecture."**

A person deciding whether their company or team should adopt PHP for a new project. She needs to work with various languages, services and application. She focuses on orchestrating them together, each with their strength.

She is not hostile, she needs to shepherd contradictory constraints. She reads the way a due-diligence reviewer reads: she looks for the source behind a number, she notices when a comparison is cherry-picked, she trusts a document more when it states its own limits. One unsourced superlative and she closes the tab.

## 2. The promise

- The whole book reads in **ninety minutes to two hours**. Ten short chapters and three appendices, about 15,000 words of prose. A chapter is 1,200 to 1,800 words. If a chapter grows past that, cut, do not split.
- **Every chapter answers one question an evaluator asks**: who runs on it, how fast is it, how does it scale, who maintains it, what does it cost, where is it the wrong choice.
- **Every figure has a source and a date, in the appendix, never in the sentence.** The full citation (publisher, URL, date the data refers to, date it was checked) lives in [Sources](appendix-01-sources.md), chapter by chapter, one entry per figure. The prose carries no citation parenthesis and no reference number: they make a page unreadable and they read as generated. The prose names the publisher in words only when it changes the reading ("a hosting vendor's own benchmark", "by the account of a former engineer", "Wikimedia's audited financial statements"). A number the appendix does not list does not go in the book.
- **The book states what it does not know.** When a figure is vendor-run, self-reported, or measured on a synthetic benchmark, the sentence says so, in the same breath as the number.
- **The book says where PHP loses.** A chapter that only contains good news is rewritten. The chapter [Where PHP Is the Wrong Choice](ch09-wrong-choice.md) exists so that the rest of the book can be believed.

## 3. Neutrality

- **No superlatives, no marketing vocabulary.** Banned words: powerful, robust, blazing, seamless, modern (as praise), enterprise-grade, battle-tested, world-class, best-in-class, industry-leading, elegant, vibrant, thriving. A fact replaces the adjective, or the adjective goes.
- **Comparisons are symmetrical.** If a chart shows PHP ahead of a language on one measure, the text names a measure where the same language is ahead of PHP, when one exists. A comparison never omits the mainstream option a reader would expect to see (Node.js, Python, Java, C#, Go, Ruby).
- **Frameworks and tools are named only in alphabetical lists and never recommended.** Full-stack frameworks: CakePHP, Laminas, Laravel, Symfony, Yii. Micro-frameworks: Mezzio, Slim. CMS and platforms: Drupal, Joomla, TYPO3, WordPress. Commerce: Adobe Commerce (Magento Open Source), PrestaShop, Shopware, Sylius, WooCommerce. Tests: Pest, PHPUnit. Static analysis: PHPStan, Psalm. Code style: PHP-CS-Fixer, PHP_CodeSniffer. Editors: PhpStorm, VS Code. Serving: FrankenPHP, PHP-FPM behind a web server, RoadRunner. Async: AMPHP, ReactPHP, Swoole or OpenSwoole. Never describe one as more popular, better or more modern than another. Rector, Xdebug, Composer and Packagist stand alone.
- **Organisations are named only with a primary source.** A company appears in the book when its own engineering blog, conference talk, public repository, job posting or annual report says it runs PHP in production, and the appendix links to that document with its date. An organisation whose evidence is older than five years is presented with its date, so the reader can weigh it. Organisations that run Hack on HHVM (Meta, Slack) are not presented as PHP users; where the reader would expect them, the book says precisely what they run.
- **No hosting, no cloud, no SaaS names**, except as the publisher of a benchmark or a survey the book cites, named as such.
- **No individuals** as authorities. "The RFC process", "php.net", "the PHP Foundation" are the authorities.

## 4. Honesty

- The reputation is addressed once, in the first chapter, without defensiveness. What was true, what changed, what is still true.
- Real remaining limits are named plainly where the evaluator will look for them: no threads in userland, a synchronous runtime by default, CPU-bound throughput below compiled languages and below JIT-heavy runtimes, a standard library with historical inconsistencies, no generics in the language, a hosting ecosystem that still runs old versions. A limit is followed by the current practice around it, not by an apology and not by a counter-argument.
- Benchmarks are presented with their round, hardware, test and date, with the sentence explaining what the test measures and what it does not. Synthetic gains (bench.php, JIT micro-benchmarks) are never presented as web-application gains.
- Do not claim a feature exists unless it is in the fact sheet of `polyglot/WRITING.md` or on php.net. When unsure whether something landed in a release or is still an RFC, leave it out.
- Projections are not facts. The book describes the announced release plan as announced, with the phrase "as of September 2026".

## 5. Chapter shape

1. **The engineering leader's question first.** The first paragraph states the question and gives the short, sourced answer. Bold the key sentence.
2. **Evidence before argument.** A chart or a table, then the prose that reads it. The prose never says more than the chart shows.
3. **The limit.** Each chapter names where PHP falls short on the chapter's own question, in a `> ` quote or a short paragraph.
4. **What to verify yourself.** Each chapter ends with one or two things the reader can check in an afternoon (a command, a public dashboard, a benchmark to rerun), so the book asks to be verified rather than trusted.
5. **One drawing and one or two charts** per chapter. Drawings: `<img src="images/chNN-name.png" alt="..." width="560">`, registered in `illustrations.md` with their prompt. Charts: `{{#include charts/chNN-name.svg}}`, generated by `charts/build.py` from `charts/data/*.json`, never drawn by hand, so every bar on every chart is traceable to a data file that carries its source.
6. **Close on the idea or on the next question**, never on a summary.

## 6. Charts

- One chart shows one thing. One axis, never two scales on one chart.
- Horizontal bars for magnitudes with a label per bar; lines for change over time; a stacked bar for shares that add to one hundred. No pie charts, no 3D, no gradients.
- One hue (blue) for PHP, neutral grey for everything else, so the chart does not editorialise through color. Text and axes use `currentColor` so the chart reads in both the light and the dark theme.
- Every chart carries its source line at the bottom: publisher, data date, test or method in five words.
- A chart is accompanied by a short table in the text or in [Sources](appendix-01-sources.md) with the same figures, so nothing depends on reading a bar length.
- French charts are generated by the same script with translated labels into `fr/charts/`.

## 7. Code conventions

Code is rare in this book: a few examples in the language chapter and in the evaluation chapter. Where it appears, the conventions of `polyglot/WRITING.md` apply: `<?php` and `declare(strict_types=1);` on complete examples, PER Coding Style, ```php fences checked by `make lint`, ```bash for commands, ```text for output. No framework code, no vendor packages except Composer and the tools chapter.

## 8. Prose conventions

- English source in `src/`, French version in `fr/`, same file names, same structure, same images. The French is a translation with the same voice. Code stays identical, comments inside code stay in English, `alt` texts and titles are translated.
- No em dash (—) or en dash (–) anywhere. Commas, colons, parentheses, or a new sentence.
- Second person, present tense. "You" is the reader, addressed directly: "your question", "if you are building a team", never "an evaluator" or "the reader" in the third person. "I" is the author, used sparingly for what the author measured, found, refused or could not confirm; never "the book" as a subject. No "we".
- Numbers in prose only when they change the reader's judgment. Round to what the source supports: "about three quarters" when the source says 74.2 percent and the decimal does not matter.
- Chapters never say "next chapter" or "previous chapter". Link by title: `[The Runtime](ch02-runtime.md)`.
- **No staccato.** The tell of generated prose is the short punchline closing every paragraph, the elliptical contrast, the counted announcement, the "Here is the short answer" opener, and the literary inversion. Write connected sentences, the way a senior colleague writes a memo: subject, verb, complement, and a second clause when the ideas belong together. One short sentence for emphasis per chapter is plenty.
- No rhetorical questions addressed to the reader's doubts ("Still not convinced?"). The reader's doubt is respected, not teased.

## 9. Before handing in a chapter

- `grep -n '—\|–'` returns nothing.
- Every number in the chapter is in `appendix-01-sources.md`, under the chapter's heading, with a URL and its dates.
- Every chart has a data file in `charts/data/` with a `source` field.
- Every `<img>` has a matching entry in `illustrations.md`.
- Every internal link points at a file listed in `src/SUMMARY.md`.
- Search the chapter for the banned words of section 3.
- Read the bold sentences alone. They tell the chapter's story, and the story includes at least one limit.
- Ask: if a competitor's advocate read this chapter, which sentence would they attack? Fix that sentence.
