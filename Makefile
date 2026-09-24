# One book per persona, one folder per book. Each folder has its own Makefile
# with the same targets (en, fr, build, pdf, pdf-fr, illustrations, lint, clean).
#
#   make beginner-en        serve The PHP Book (beginner/) in English
#   make polyglot-fr        serve And Now, PHP (polyglot/) in French
#   make build              build every book, both languages
#   make lint               syntax-check the code blocks of every book
#   make clean              remove all build output
#   make phpnet-links       refresh <book>/theme/phpnet-links.js (php.net function links)
#   make site               serve the landing page with the built books (site/)
#   make dist               assemble the landing page and every book into _site/
#   make pdf                print the books that have a PDF edition, into _site/ too
#
# Any target of a book Makefile works as <book>-<target>.

BOOKS = beginner polyglot pragmatic skeptic engineering
PDF_BOOKS = beginner polyglot skeptic
DIST = _site

.PHONY: build lint clean phpnet-links site dist pdf $(foreach b,$(BOOKS),$(b)-%)

build lint clean:
	@for b in $(BOOKS); do $(MAKE) -C $$b $@; done

phpnet-links:
	python3 scripts/build-phpnet-links.py

site: dist
	$(MAKE) -C site serve

# _site/ mirrors the published layout: the landing page at the root, each book
# under its folder name, the French edition under <book>/fr/.
dist: build
	rm -rf $(DIST)
	mkdir -p $(DIST)
	cp site/index.html $(DIST)/
	cp -r site/images $(DIST)/images
	@for b in $(BOOKS); do \
	  cp -r $$b/book $(DIST)/$$b; \
	  if [ -d $$b/fr ]; then cp -r $$b/book-fr $(DIST)/$$b/fr; fi; \
	done

pdf: dist
	@for b in $(PDF_BOOKS); do \
	  $(MAKE) -C $$b pdf pdf-fr && cp $$b/book.pdf $$b/book-fr.pdf $(DIST)/$$b/; \
	done

$(foreach b,$(BOOKS),$(b)-%):
	$(MAKE) -C $(word 1,$(subst -, ,$@)) $(patsubst $(word 1,$(subst -, ,$@))-%,%,$@)
