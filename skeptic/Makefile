# Local development for "PHP in 2026, the Facts" (the skeptical evaluator book).
#
#   make en             serve the English book and open it in the browser
#   make fr             serve the French version (fr/) the same way
#   make build          build both languages into book/ and book-fr/
#   make pdf            build the English book and print it to book.pdf
#   make pdf-fr         same for the French version, into book-fr.pdf
#   make charts         regenerate the SVG charts from charts/data (needs python3)
#   make illustrations  generate missing illustrations (needs OPENAI_API_KEY)
#   make lint           syntax-check every PHP code block with the local php binary
#   make clean          remove build output

MDBOOK ?= mdbook
FR_ENV = MDBOOK_BOOK__SRC=fr MDBOOK_BOOK__LANGUAGE=fr MDBOOK_BOOK__TITLE="🐘 PHP en 2026, factuellement - 0.1.0" MDBOOK_BUILD__BUILD_DIR=book-fr

CHROME ?= $(shell command -v google-chrome || command -v google-chrome-stable || command -v chromium || command -v chromium-browser)
CHROME_FLAGS = --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=10000

.PHONY: en fr build build-en build-fr pdf pdf-fr charts illustrations lint clean

en:
	$(MDBOOK) serve --open

fr:
	$(FR_ENV) $(MDBOOK) serve --open

build: build-en build-fr

build-en:
	$(MDBOOK) build

build-fr:
	$(FR_ENV) $(MDBOOK) build

pdf: build-en
	$(CHROME) $(CHROME_FLAGS) --print-to-pdf="$(CURDIR)/book.pdf" "file://$(CURDIR)/book/print.html"

pdf-fr: build-fr
	$(CHROME) $(CHROME_FLAGS) --print-to-pdf="$(CURDIR)/book-fr.pdf" "file://$(CURDIR)/book-fr/print.html"

charts:
	python3 charts/build.py

illustrations:
	../scripts/generate-illustrations.sh

lint:
	../scripts/lint-code-blocks.sh src fr

clean:
	rm -rf book book-fr
