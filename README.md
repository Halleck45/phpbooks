# README

This repository holds one book per onboarding persona (see `onboarding personas.md`), one folder per book:

- **The PHP Book** (`beginner/`), for *The Absolute Beginner*: a full course for developers new to PHP. See `beginner/README.md`.
- **And Now, PHP** (`polyglot/`), for *The Experienced Polyglot Developer*: a two-to-three-hour read for experienced developers coming from another language, or returning to PHP after years away. See `polyglot/README.md`.
- **ShiPHP It** (`pragmatic/`), for *The Pragmatic Builder*: a feature-first guide to shipping with the PHP ecosystem.
- **PHP in 2026, the Facts** (`skeptic/`), for *The Skeptical Evaluator*: an evidence-based evaluation of PHP, every figure sourced and dated, with the cases where PHP is the wrong choice. See `skeptic/README.md`.

Each folder has its own `Makefile` (`make en`, `make fr`, `make build`, `make pdf`, `make illustrations`, `make lint`); the root `Makefile` dispatches (`make beginner-en`, `make polyglot-fr`, `make skeptic-charts`, `make build`). The scripts in `scripts/` are shared.

`site/` holds a draft landing page that presents the books and helps a visitor pick one (see `site/README.md`).

In every book, calls to PHP built-in functions link to the php.net manual, in code blocks and in inline code. The script is `scripts/phpnet-links.src.js`; `make phpnet-links` refreshes the function list from the php.net index and writes one copy per book into `<book>/theme/phpnet-links.js` (mdBook only ships `additional-js` files that live inside the book folder). Commit the copies: Read the Docs builds with `mdbook build` alone.
