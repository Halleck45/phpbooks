# The landing page: one static file, no build step.
#
#   make serve          serve the repository and print the page URL (book links
#                       are relative, so the books must be built: make -C .. build)
#   make illustrations  generate the missing drawings of illustrations.md into
#                       images/ (needs OPENAI_API_KEY)
#   make illustrations ARGS="--force hero"   regenerate one drawing
#   make illustrations ARGS=--dry-run        print the prompts, no API call
#   make webp           convert images/*.png to the light WebP files the page
#                       loads first (needs cwebp); run it after illustrations

PORT ?= 8000

WEBP_WIDTH ?= 1200
PNG = $(wildcard images/*.png)

.PHONY: serve illustrations webp

serve:
	@echo "http://localhost:$(PORT)/site/"
	python3 -m http.server $(PORT) --directory ..

illustrations:
	ILLUSTRATIONS_SPEC="$(CURDIR)/illustrations.md" ILLUSTRATIONS_OUT="$(CURDIR)/images" ../scripts/generate-illustrations.sh $(ARGS)

webp: $(PNG:.png=.webp)

images/%.webp: images/%.png
	cwebp -quiet -q 82 -m 6 -resize $(WEBP_WIDTH) 0 $< -o $@
