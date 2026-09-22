# One book per persona, one folder per book. Each folder has its own Makefile
# with the same targets (en, fr, build, pdf, pdf-fr, illustrations, lint, clean).
#
#   make beginner-en        serve The PHP Book (beginner/) in English
#   make polyglot-fr        serve And Now, PHP (polyglot/) in French
#   make build              build every book, both languages
#   make lint               syntax-check the code blocks of every book
#   make clean              remove all build output
#   make phpnet-links       refresh <book>/theme/phpnet-links.js (php.net function links)
#   make site               serve the draft landing page (site/)
#
# Any target of a book Makefile works as <book>-<target>.

BOOKS = beginner polyglot pragmatic skeptic engineering

.PHONY: build lint clean phpnet-links site $(foreach b,$(BOOKS),$(b)-%)

build lint clean:
	@for b in $(BOOKS); do $(MAKE) -C $$b $@; done

phpnet-links:
	python3 scripts/build-phpnet-links.py

site:
	$(MAKE) -C site serve

$(foreach b,$(BOOKS),$(b)-%):
	$(MAKE) -C $(word 1,$(subst -, ,$@)) $(patsubst $(word 1,$(subst -, ,$@))-%,%,$@)
