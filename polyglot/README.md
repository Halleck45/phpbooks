# And Now, PHP

A short book (two to three hours of reading) for **developers who already program in another language** and have just landed on a PHP project, and for developers coming back to PHP after years away. It skips the basics and answers one question per chapter: how does PHP do this?

- English source: `src/`
- French version: `fr/` (same files, same structure, shared images)
- Editorial contract: `WRITING.md` (audience, neutrality rules, PHP version fact sheet)
- Illustration prompts: `illustrations.md`

## Building

The book uses mdBook, like the main book in this repository.

```bash
make en          # serve the English book
make fr          # serve the French version
make build       # build both into book/ and book-fr/
make pdf         # print the English book to book.pdf (needs Chrome or Chromium)
make lint        # syntax-check every PHP code block (needs php; use PHP=... for a newer binary)
make illustrations   # generate missing drawings from illustrations.md (needs OPENAI_API_KEY)
```

## Contributing

Read `WRITING.md` first. The book is published under the umbrella of the PHP Foundation and stays neutral: frameworks and tools appear in alphabetical lists, never as recommendations. Every claim about a PHP version must match the fact sheet in `WRITING.md` or php.net.
