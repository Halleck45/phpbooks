# The landing page: one static file, no build step.
#
#   make serve          serve ../_site (the page with the built books) and print
#                       its URL; assemble it first with make -C .. dist
#   make illustrations  generate the missing drawings of illustrations.md into
#                       images/ (needs OPENAI_API_KEY)
#   make illustrations ARGS="--force hero"   regenerate one drawing
#   make illustrations ARGS=--dry-run        print the prompts, no API call
#   make webp           convert images/*.png to the light WebP files the page
#                       loads first (needs cwebp); run it after illustrations
#   make social-card    render social-card.html to images/social-card.png, the
#                       1200x630 link preview of the site and the books (needs
#                       Chrome and network access for the fonts)

PORT ?= 8000

CHROME ?= $(shell command -v google-chrome || command -v google-chrome-stable || command -v chromium || command -v chromium-browser)

WEBP_WIDTH ?= 1200
PNG = $(wildcard images/*.png)

.PHONY: serve illustrations webp social-card

serve:
	@echo "http://localhost:$(PORT)/"
	python3 -m http.server $(PORT) --directory ../_site

illustrations:
	ILLUSTRATIONS_SPEC="$(CURDIR)/illustrations.md" ILLUSTRATIONS_OUT="$(CURDIR)/images" ../scripts/generate-illustrations.sh $(ARGS)

webp: $(PNG:.png=.webp)

images/%.webp: images/%.png
	cwebp -quiet -q 82 -m 6 -resize $(WEBP_WIDTH) 0 $< -o $@

social-card:
	$(CHROME) --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
	  --window-size=1200,630 --virtual-time-budget=10000 \
	  --screenshot="$(CURDIR)/images/social-card.png" "file://$(CURDIR)/social-card.html"
