# PHP in 2026, the Facts

A short book (ninety minutes to two hours of reading) for **engineers who have to be convinced that PHP is worth their time**. It answers the questions an evaluator asks, who runs on it, how fast it is, how it scales, who maintains it, what it costs, where it is the wrong choice, and it answers them with figures that carry a source and a date.

- English source: `src/`
- French version: `fr/` (same files, same structure, shared images)
- Editorial contract: `WRITING.md` (audience, sourcing rules, neutrality rules)
- Charts: `charts/build.py` generates every SVG chart in `src/charts/` and `fr/charts/` from the data files in `charts/data/`. Each data file carries the source of its figures.
- Illustration prompts: `illustrations.md`
- Sources: `src/appendix-01-sources.md`, one numbered entry per figure used in the book.

## Building

The book uses mdBook, like the other books in this repository.

```bash
make en          # serve the English book
make fr          # serve the French version
make build       # build both into book/ and book-fr/
make pdf         # print the English book to book.pdf (needs Chrome or Chromium)
make charts      # regenerate the charts from charts/data (needs python3)
make lint        # syntax-check every PHP code block (needs php)
make illustrations   # generate missing drawings from illustrations.md (needs OPENAI_API_KEY)
```

## Contributing

Read `WRITING.md` first. The book is published under the umbrella of the PHP Foundation and stays neutral: no superlatives, frameworks and tools in alphabetical lists, organisations named only with a primary source. A figure without an entry in the sources appendix does not go in the book. When a figure ages, update the data file, rerun `make charts`, and update the appendix entry.
