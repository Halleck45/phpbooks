# PHP books

One folder per book, each an mdBook: `beginner/` (The PHP Book), `polyglot/` (And Now, PHP), `pragmatic/` (Ship It With PHP), `skeptic/` (PHP in 2026, the Facts), `engineering/` (PHP: A Guide for the Decision Maker). `site/` is the landing page that hands each reader their book.

## Build

You need [mdBook](https://rust-lang.github.io/mdBook/) 0.5 and, for the PDF editions, Chrome.

```
make beginner-en      # serve one book, live reload (also polyglot-fr, skeptic-en, ...)
make build            # build every book, both languages
make dist             # assemble the landing page and the books into _site/
make pdf              # print the PDF editions into _site/ as well
make site             # serve _site/ on http://localhost:8000/
```

## Work

The English source of a book lives in `<book>/src/`, the French edition in `<book>/fr/`, same file names. Each book has its editorial guide (`WRITING.md` or `SPEC.md`): read it before editing a chapter. `make lint` runs `php -l` on every PHP block; some chapters use PHP 8.4 syntax, so use a recent binary.

Built-in PHP functions link to the php.net manual through `<book>/theme/phpnet-links.js`. `make phpnet-links` refreshes those copies from the php.net index; commit them.

## Publish

A push to `main` builds everything and deploys `_site/` to GitHub Pages. A tag `vX.Y.Z` also creates a release with the PDF editions attached.
