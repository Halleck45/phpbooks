# README

This repository holds one book per onboarding persona (see `onboarding personas.md`), one folder per book:

- **The PHP Book** (`beginner/`), for *The Absolute Beginner*: a full course for developers new to PHP. See `beginner/README.md`.
- **And Now, PHP** (`polyglot/`), for *The Experienced Polyglot Developer*: a two-to-three-hour read for experienced developers coming from another language, or returning to PHP after years away. See `polyglot/README.md`.
- **ShiPHP It** (`pragmatic/`), for *The Pragmatic Builder*: a feature-first guide to shipping with the PHP ecosystem.
- **PHP in 2026, the Facts** (`skeptic/`), for *The Skeptical Evaluator*: an evidence-based evaluation of PHP, every figure sourced and dated, with the cases where PHP is the wrong choice. See `skeptic/README.md`.

Each folder has its own `Makefile` (`make en`, `make fr`, `make build`, `make pdf`, `make illustrations`, `make lint`); the root `Makefile` dispatches (`make beginner-en`, `make polyglot-fr`, `make skeptic-charts`, `make build`). The scripts in `scripts/` are shared.
