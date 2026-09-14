# And Now, PHP: Writing Guide

This file is the editorial contract for the polyglot book. Read it before writing or editing any chapter. The general house style (rhythm, narrative, no filler) lives in the `book-style` skill and applies on top of everything here.

## 1. The reader

**The Experienced Polyglot Developer. "Skip the basics; just tell me how PHP does it."**

She already programs for a living, in Python, JavaScript or TypeScript, Java, C#, Go, Ruby, or something else. She has just been put on a PHP project. She does not need to be told what a variable, a loop, a class, a closure, a package manager or an HTTP request is. She needs to know, quickly and precisely, how PHP does each of those things, where PHP differs from what she expects, and which of her habits will hurt her.

The same book serves the **returning developer**: someone who wrote PHP 5 years ago (or PHP 5, period) and has to catch up. For her, the delta between the PHP she remembers and the PHP of today is the whole story.

Both readers share one trait: **they are busy and skeptical**. They have heard that PHP is a mess. The book does not argue with that reputation. It shows the current language, plainly, and lets the reader draw her own conclusion.

## 2. The promise

- The whole book reads in **two to three hours**. Around 20,000 words of prose plus code, fifteen short chapters and three appendices. A chapter is 1,200 to 1,800 words of prose. If a chapter grows past that, cut, do not split.
- **Every chapter answers one question: "how does PHP do X?"** It opens on the answer, not on a preamble. The reader who only reads the bold sentences gets the delta.
- **Modern PHP only.** The book describes PHP 8.5 (released November 2025) as the current language and treats 8.4 as the floor a reader will meet on a maintained project. Anything introduced after 8.2 carries its version number the first time it appears, as `(PHP 8.4)` right after the feature name, so the reader knows what her project can use. Legacy PHP appears only in the chapter for returning developers and, briefly, where a modern feature exists precisely to replace an old habit.
- **Compare, but do not translate.** A comparison to another language is a one-sentence anchor ("like Python's `dict`, with the order guaranteed"), never a parallel implementation. The languages used as anchors, in this order of frequency: Python, JavaScript/TypeScript, Java. Go, C#, Ruby and Rust when they make a point sharper. Never assume the reader knows all of them: an anchor must be skippable without losing the PHP explanation.

## 3. Neutrality

The book is published under the umbrella of the PHP Foundation. It promotes the language and its standards, not a vendor, a framework or a product.

- **Frameworks are named only in lists, alphabetically, and never recommended.** The list for full-stack frameworks: CakePHP, Laminas, Laravel, Symfony, Yii. For micro-frameworks and routers: Slim, Mezzio. For CMS and platforms: Drupal, Joomla, TYPO3, WordPress. Use the shortest list that fits the sentence. Never describe one as more popular, better or more modern than another.
- **Tools come in pairs.** When a tool category matters, name at least two options, alphabetically: PHPUnit and Pest for tests; PHPStan and Psalm for static analysis; PHP-CS-Fixer and PHP_CodeSniffer for code style; PhpStorm and VS Code (with a PHP extension) for editors; FrankenPHP, PHP-FPM behind a web server, and RoadRunner for serving. Rector and Xdebug can stand alone: nothing else does what they do.
- **Standards over products.** Prefer PSR interfaces and PER Coding Style (from the PHP-FIG) whenever a chapter needs "the standard way". Composer and Packagist are the package infrastructure of the language and are named freely.
- **No hosting, no cloud, no SaaS names.** The official Docker image (`php:8.5-cli`, `php:8.5-fpm`) is the only third-party runtime mentioned.
- **No individuals, no companies** as examples or authorities. "The RFC process" and "php.net" are the authorities.

## 4. Honesty

- The reputation is addressed once, in the introduction, in a few paragraphs: what was true, what changed, what still bites. After that the book stops defending PHP and simply shows it.
- Real remaining warts are named plainly where the reader will meet them: inconsistent function naming in the standard library, `strlen()` counting bytes, `==` juggling, the `strict_types` switch being per file, arrays copying on assignment, no generics in the language. A wart is followed by the modern practice that neutralises it, not by an apology.
- Do not claim a feature exists unless it is in the fact sheet below. When unsure whether something landed in 8.5 or is still an RFC, leave it out.

## 5. Chapter shape

1. **The answer first.** The first paragraph states how PHP does the thing. Bold the key sentence.
2. **Code before prose.** Show a complete, runnable example, then explain the parts that differ from the reader's expectations. Skip what needs no explanation.
3. **The trap.** Each chapter names the one or two mistakes a polyglot makes here, in a `> ` quote or a short paragraph, with the fix.
4. **One or two illustrations**, placed at the exact point where a drawing beats a paragraph. `<img src="images/chNN-name.png" alt="..." width="560">` for landscape, `width="420"` for portrait. Register each drawing in `illustrations.md` with its prompt.
5. **Close on the idea or on the next chapter's question**, never on a summary.

## 6. Code conventions

- Every full example starts with `<?php` and `declare(strict_types=1);`. Fragments (a few lines inside a paragraph) may skip both.
- Examples are complete and runnable with `php file.php` unless the text says otherwise. Output goes in a trailing comment (`// 42`) or in a separate ```text block when longer than a line.
- Follow PER Coding Style: four spaces, opening brace on its own line for classes and functions, on the same line for control structures, `camelCase` methods, `PascalCase` classes, `SCREAMING_SNAKE_CASE` constants.
- Only single quotes for plain strings, double quotes when interpolating.
- No framework code, no vendor packages in examples, except Composer itself and the tools chapter. Everything runs on a bare PHP install.
- Fenced blocks are tagged ```php, ```bash for shell commands, ```json for `composer.json`, ```text for output. The linter (`make lint`) checks every ```php block with `php -l`.
- The `$` sigil, `->`, `::`, `=>` and `...` are named the first time they appear, once.

## 7. Prose conventions

- English source in `src/`, French version in `fr/`, same file names, same structure, same images. The French is a translation with the same voice, not a summary. Code stays identical; comments inside code stay in English; the `alt` text and the `title` are translated.
- No em dash (—) or en dash (–) anywhere. Commas, colons, parentheses, or a new sentence.
- Second person, present tense. "You" is the reader. No "we".
- Numbers in prose only when they change what the reader does.
- Chapters never say "next chapter" or "previous chapter". Link by title: `[Types](ch03-types.md)`.
- Section titles are short noun phrases, no colons, no puns that do not survive translation. Chapter titles are plain nouns ("Types", "Arrays", "Classes"), never a wink at the reader.
- **No staccato.** The tell of generated prose is the short punchline closing every paragraph ("The language did not.", "That is the whole model.", "No `&` is involved."), the elliptical contrast ("Arrays copy. Objects, no."), the counted announcement ("Three facts about this switch", "Four rules define it"), the "Here is the short answer" opener, and the literary inversion. Write connected sentences, the way a senior colleague writes an email: subject, verb, complement, and a second clause when the ideas belong together. One short sentence for emphasis per chapter is plenty.

## 8. Fact sheet: what exists, by version

Use these lists. If a feature is not here, verify on php.net before writing it, or leave it out.

**PHP 8.0 (Nov 2020).** Named arguments. Attributes (`#[...]`). Constructor property promotion. Union types (`int|string`). `match` expression. Nullsafe operator (`?->`). `mixed` and `static` return types. `throw` as an expression. `str_contains()`, `str_starts_with()`, `str_ends_with()`. `Stringable` interface. `WeakMap`. JIT compiler. Saner string-to-number comparisons (`0 == "foo"` is now `false`). Trailing comma in parameter lists. Consistent `TypeError` and `ValueError` from internal functions.

**PHP 8.1 (Nov 2021).** Enums (pure and backed). `readonly` properties. First-class callable syntax (`strlen(...)`). Fibers. `new` in initializers (default parameter values, attribute arguments). Pure intersection types (`A&B`). `never` return type. `final` class constants. Array unpacking with string keys. `array_is_list()`. Explicit octal notation (`0o16`).

**PHP 8.2 (Dec 2022).** `readonly` classes. Disjunctive normal form types (`(A&B)|null`). Standalone `true`, `false` and `null` types. Dynamic properties deprecated (create them and you get a deprecation; `#[\AllowDynamicProperties]` opts a class back in). `#[\SensitiveParameter]`. Constants in traits. `Random\Randomizer` and the `random` extension. `enum` constants fetch in const expressions.

**PHP 8.3 (Nov 2023).** Typed class constants. `#[\Override]` attribute. `json_validate()`. Dynamic class constant fetch (`Foo::{$name}`). `readonly` properties can be reinitialised inside `__clone()`. `Randomizer::getBytesFromString()`, `Randomizer::getFloat()`. Negative indices in arrays are consistent. `mb_str_pad()`.

**PHP 8.4 (Nov 2024).** Property hooks (`get` and `set` on a property). Asymmetric visibility (`public private(set)`). `new` without parentheses when chaining (`new Foo()->bar()`). Lazy objects (`ReflectionClass::newLazyGhost()`, `newLazyProxy()`). `#[\Deprecated]` attribute. `array_find()`, `array_find_key()`, `array_any()`, `array_all()`. `mb_trim()`, `mb_ltrim()`, `mb_rtrim()`, `mb_ucfirst()`, `mb_lcfirst()`. New DOM extension with an HTML5 parser (`Dom\HTMLDocument`). BCMath object API (`BcMath\Number`). PDO driver subclasses (`Pdo\Sqlite`, `Pdo\Mysql`, `Pdo\Pgsql`) with `Pdo::connect()`. `request_parse_body()`. Implicitly nullable parameter types (`Foo $x = null` without `?`) deprecated. `exit` and `die` are functions.

**PHP 8.5 (Nov 2025).** Pipe operator (`$x |> f(...)`). `clone` with property updates (`clone($obj, ['prop' => $value])`). `#[\NoDiscard]` attribute (warn when a return value is ignored), with the `(void)` cast to silence it deliberately. `array_first()`, `array_last()`. Closures and first-class callables allowed in constant expressions (attribute arguments, default values, constants). Attributes on constants. New `uri` extension (`Uri\Rfc3986\Uri`, `Uri\WhatWg\Url`). Fatal errors now include a backtrace. `get_error_handler()`, `get_exception_handler()`. `#[\DelayedTargetValidation]`. `PHP_BUILD_DATE` constant. Deprecations: passing `null` to non-nullable internal parameters keeps its 8.1 deprecation; the backtick shell-execution operator is deprecated.

**Not in the language, and the book says so:** generics (use docblocks plus PHPStan or Psalm), multithreading in userland (see the concurrency chapter), operator overloading, a `Result` type, macros, structural typing.

**Gone (removed or deprecated), for the returning developer:** `mysql_*` functions (removed in 7.0), `register_globals` and magic quotes (5.4), `each()` (removed 8.0), `create_function()` (8.0), `__autoload()` (8.0), `${}` string interpolation (deprecated 8.2), dynamic properties (deprecated 8.2), `utf8_encode()` and `utf8_decode()` (deprecated 8.2), implicit nullable types (deprecated 8.4), the `(unset)` cast (removed 8.0), `ereg_*` functions (removed 7.0), `split()` (removed 7.0), PHP 4 style constructors named after the class (removed 8.0). Since PHP 5.6 the default internal encoding is UTF-8, so `mb_internal_encoding('UTF-8')` at the top of every file is no longer needed.

## 9. Before handing in a chapter

- `grep -n '—\|–'` returns nothing.
- `make lint` passes, or the failures are all in blocks marked with a `// PHP 8.4` or `// PHP 8.5` comment on the first line (the local PHP may be older).
- Every `<img>` has a matching entry in `illustrations.md`.
- Every internal link points at a file listed in `src/SUMMARY.md`.
- Read the bold sentences alone. They tell the chapter's story.
- Read the first sentence. It is the answer, not an announcement.
