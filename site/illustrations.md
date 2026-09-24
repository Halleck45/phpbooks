# Illustrations for the landing page

Six drawings: one for the top of the page, one per reader. Same format as the `illustrations.md` of the books, read by `scripts/generate-illustrations.sh`. Generate them with `make illustrations` from this folder; the files land in `images/`.

Until a file exists in `images/`, the page borrows a drawing from the books (see the `data-fallback` attributes in `index.html`), so it never looks empty.

No drawing carries any text, so the page can be translated without redrawing. The page blends the white background into its own paper colour and inverts the drawing in dark mode, which only works with black ink, a pure white background and the single blue accent.

## Common style

> Hand-drawn illustration in the style of a clean notebook sketch. Black ink lines drawn with a fine felt-tip pen, slightly imperfect strokes, on a pure white background. One accent color only, a soft blue, used sparingly to highlight what matters. No shading, no gradients, no textures, no 3D, no photorealism. Generous white space, centered composition, nothing touching the edges. Friendly, simple, a little playful, like a diagram drawn on a whiteboard by a good teacher. People and the elephant are always drawn in black ink outline with a white inside, never filled with color. Absolutely no text, no letters, no numbers, no labels anywhere in the image. No watermark, no signature.

The recurring character is the small, round, friendly elephant of the books.

---

## hero.png

- Where: top of the page, next to the question "Where are you with PHP?".
- Idea: the reader is the hero. They stand at the start of their own road, and someone friendly shows them which way it goes.
- Priority: must have.
- Format: landscape.

**Prompt.** A person with a backpack, seen from three-quarters behind, stands in the foreground at a fork where one path splits into five winding trails that spread out toward the horizon. The person is the largest figure in the image and is drawn with the blue accent color on the backpack. Beside them, much smaller, a small round friendly elephant looks up at the person and points its trunk toward one of the trails. Each trail ends far away at a tiny different landmark: a desk with a laptop, a doorway, a small house, a balance scale, a whiteboard.

## beginner.png

- Where: book 01, The PHP Book.
- Idea: a first line of code that works, with someone beside you.
- Priority: must have.
- Format: landscape.

**Prompt.** A young person sitting at a small desk with an open laptop, arms raised in delight. The laptop screen shows a single short horizontal line and a small sparkle, both in the blue accent color. A small round friendly elephant stands beside the desk and gives an encouraging thumbs-up with its trunk. Behind them, a short winding path with three small empty signposts leads off toward the horizon.

## polyglot.png

- Where: book 02, And Now, PHP.
- Idea: you already travel well, this is one more stamp in the passport.
- Priority: must have.
- Format: landscape.

**Prompt.** A border-crossing booth seen from the side. Behind the counter, a small round friendly elephant presses a large rubber stamp onto an open passport; the fresh stamp mark is a simple circle in the blue accent color. In front of the counter stands a relaxed, experienced traveller with a well-worn backpack covered in blank stickers of different shapes: a circle, a hexagon, a square, a triangle. The barrier behind the booth is already lifting.

## pragmatic.png

- Where: book 03, Ship It With PHP.
- Idea: the feature is assembled from big ready-made parts and leaves the workshop today.
- Priority: must have.
- Format: landscape.

**Prompt.** A tidy workshop. A focused person in rolled-up sleeves snaps a large prefabricated block into a nearly finished small house made of five or six such blocks, like oversized building bricks. A small round friendly elephant hands over the last block. That one block is the only blue element of the image, filled with the blue accent color. The elephant itself is drawn like the person: black ink outline, white inside, no blue on it. On the right, a delivery cart waits with its ramp down, ready to carry the house away.

## skeptic.png

- Where: book 04, PHP in 2026, the Facts.
- Idea: nothing is asked on trust, the evidence is on the table.
- Priority: must have.
- Format: landscape.

**Prompt.** A person with crossed arms and one raised eyebrow sits at a table. Across the table, a small round friendly elephant calmly slides a sheet of paper toward them; the sheet shows a simple bar chart with four bars in the blue accent color and no labels. A large magnifying glass lies on the table between them, and a neat stack of other sheets sits next to the elephant.

## engineering.png

- Where: book 05, PHP: A Guide for the Decision Maker.
- Idea: an architecture made of several pieces, and the one that was missing.
- Priority: must have.
- Format: landscape.

**Prompt.** A person in a blazer stands in front of a large whiteboard, hand on chin, studying a system diagram made of six empty rounded boxes connected by straight lines, with one obvious gap in the middle. A small round friendly elephant on a step stool fits the missing box into the gap; that box is drawn in the blue accent color and the lines around it connect to it.
