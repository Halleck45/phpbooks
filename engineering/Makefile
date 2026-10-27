# Local development for "PHP: A Guide for the Decision Maker".
#
#   make en             serve the English book and open it in the browser
#   make fr             serve the French version (fr/) the same way
#   make build          build both languages into book/ and book-fr/
#   make pdf            build the English book and print it to book.pdf
#   make pdf-fr         same for the French version, into book-fr.pdf
#   make epub           build the English book and convert it to book.epub (needs pandoc)
#   make epub-fr        same for the French version, into book-fr.epub
#   make charts         regenerate the SVG charts of both languages (needs python3)
#   make illustrations  generate missing illustrations (needs OPENAI_API_KEY)
#   make lint           syntax-check every PHP code block with the local php binary
#   make clean          remove build output

MDBOOK ?= mdbook
FR_ENV = MDBOOK_BOOK__SRC=fr MDBOOK_BOOK__LANGUAGE=fr MDBOOK_BOOK__TITLE="PHP, le guide du décideur" MDBOOK_BOOK__DESCRIPTION="Un guide de quatre-vingt-dix minutes, fondé sur des sources, pour les responsables techniques qui se demandent si PHP a sa place dans leur architecture." MDBOOK_BUILD__BUILD_DIR=book-fr

# Headless Chrome prints mdBook's print.html (the whole book on one page) to PDF.
CHROME ?= $(shell command -v google-chrome || command -v google-chrome-stable || command -v chromium || command -v chromium-browser)
CHROME_FLAGS = --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=10000

.PHONY: en fr build build-en build-fr pdf pdf-fr epub epub-fr charts illustrations lint clean

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

epub: build-en
	../scripts/build-epub.py . src book book.epub

epub-fr: build-fr
	../scripts/build-epub.py . fr book-fr book-fr.epub

charts:
	python3 src/charts/build.py

illustrations:
	../scripts/generate-illustrations.sh
	@[ -e fr/images ] || ln -s ../src/images fr/images

lint:
	../scripts/lint-code-blocks.sh src fr

clean:
	rm -rf book book-fr
