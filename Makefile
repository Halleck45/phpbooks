# Local development for The PHP Book.
#
#   make en             serve the English book and open it in the browser
#   make fr             serve the French review copy (fr/) the same way
#   make build          build both languages into book/ and book-fr/
#   make illustrations  generate missing illustrations (needs OPENAI_API_KEY)
#   make clean          remove build output

MDBOOK ?= mdbook
FR_ENV = MDBOOK_BOOK__SRC=fr MDBOOK_BOOK__LANGUAGE=fr MDBOOK_BUILD__BUILD_DIR=book-fr

.PHONY: en fr build build-en build-fr illustrations clean

en:
	$(MDBOOK) serve --open

fr:
	$(FR_ENV) $(MDBOOK) serve --open

build: build-en build-fr

build-en:
	$(MDBOOK) build

build-fr:
	$(FR_ENV) $(MDBOOK) build

illustrations:
	scripts/generate-illustrations.sh

clean:
	rm -rf book book-fr
