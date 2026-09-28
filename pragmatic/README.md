# Ship It With PHP

A feature-first guide for **developers who have a feature to ship and a deadline, not a language to learn**. Every chapter is a request a client might make (user accounts, an admin panel, search, background jobs, a storefront), followed by the two to four PHP ecosystems that ship it, with the command to type first and an honest note on when each one is the wrong fit. Paid products carry a `$` in their title.

- English source: `src/`
- French version: `fr/` (same files, same structure, shared images)
- Illustration prompts: `illustrations.md`

## Building

The book uses mdBook, like the other books in this repository.

```bash
make en          # serve the English book
make fr          # serve the French version
make build       # build both into book/ and book-fr/
make pdf         # print the English book to book.pdf (needs Chrome or Chromium)
make lint        # syntax-check every PHP code block (needs php)
make illustrations   # generate missing drawings from illustrations.md (needs OPENAI_API_KEY)
```

The drawings of the other books were generated at medium quality:

```bash
OPENAI_API_KEY=sk-... OPENAI_IMAGE_QUALITY=medium make illustrations
```

## Contributing

Each ecosystem page keeps the same shape: what the tool does for you, a minimal working example, when to reach for it, when it is the wrong fit, and an optional "Under the hood" box on the language feature that makes the convenience possible. Keep code blocks runnable (`make lint` checks their syntax) and keep the French version aligned with the English one, page for page.
