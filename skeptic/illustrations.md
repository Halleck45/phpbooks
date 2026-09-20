# Illustrations for "PHP in 2026, the Facts"

This file lists every drawing referenced by the chapters, with a ready-to-use prompt for each. The chapters already contain the `<img>` tags and alt texts; drop the generated files into `src/images/` under the file names below and they will appear. `make illustrations` in this folder generates the missing ones through `scripts/generate-illustrations.sh`.

Charts are a different thing: they are generated from data by `charts/build.py` and are never drawn by hand, because every bar must be traceable to a sourced figure. The drawings below carry ideas, not numbers: a mental model, a process, a comparison of shapes. A drawing in this book never contains a figure, a percentage or a ranking, so that nothing in it can be mistaken for data.

## Common style

Prepend this block to every prompt so all the drawings look like they come from the same hand, and from the same hand as the other books in this repository:

> Hand-drawn illustration in the style of a clean notebook sketch. Black ink lines drawn with a fine felt-tip pen, slightly imperfect strokes, on a pure white background. One accent color only, a soft blue, used sparingly to highlight what matters. No shading, no gradients, no textures, no 3D, no photorealism. Generous white space, centered composition. Calm and precise, like a diagram drawn on a whiteboard by a good engineer explaining something to a peer. Understated rather than playful. No watermark, no signature. No numbers, no percentages, no rankings anywhere in the drawing.

Two practical notes:

- Image generators garble words. Each prompt lists the few labels the drawing needs. If the generated text is wrong, regenerate with "no text at all" added to the prompt and add the labels afterwards in an image editor, in a hand-lettered font.
- The PHP mascot is an elephant (the elePHPant). Drawn as a small, round, calm elephant it is the recurring character of every book in this repository. In this book it appears less often and never clowns: it stands, points, reads or measures.

Priority tells you which drawings the text depends on most. Format (landscape, portrait, or square) is read by the generation script to pick the image size.

---

## ch00-cover.png

- Chapter: `title-page.md`, under the title.
- Idea: the language is weighed against evidence, and the scale is level: the book neither tips it nor pretends it tips itself.
- Priority: must have.
- Format: square.

**Prompt.** A large, old-fashioned balance scale with two pans, drawn in the center. On the left pan stands a small round calm elephant. On the right pan sits a neat stack of paper sheets, the top sheet showing a few simple horizontal bars like a chart, with no numbers. The beam of the scale is perfectly level. The pointer at the top of the scale, and the bars on the top sheet, are drawn in the blue accent color. No text.

## ch00-two-columns.png

- Chapter: `ch00-how-to-read.md`, after the paragraph listing what is still true of the reputation.
- Idea: the book keeps two columns, what holds for PHP and what holds against it, and fills both.
- Priority: must have.
- Format: landscape.

**Prompt.** A single sheet of paper seen from above, divided into two columns by a hand-drawn vertical line. The left column is headed by a simple check mark and contains three short horizontal bars of different lengths and a tiny round elephant. The right column is headed by a simple cross and contains two short horizontal bars. A hand holding a felt-tip pen is drawing the second bar of the right column, showing that both columns are being filled with the same care. The check mark, the cross and the pen tip are in the blue accent color. No text.

## ch01-backstage.png

- Chapter: `ch01-footprint.md`, after the paragraph on the shape of the platform list.
- Idea: PHP runs the machinery behind the web rather than the part that gets the spotlight.
- Priority: must have.
- Format: landscape.

**Prompt.** A theatre seen from the wings, in a single wide view. On the right, the stage, lit by one spotlight drawn in the blue accent color, where three small animals of different shapes (a fox, a crab, a gecko) take a bow in front of a suggested audience. On the left, backstage in the half-light, a row of calm round elephants operate the machinery: one pulls a rope, one turns a large wheel, one stands at a lighting board with a few switches, one checks a rack of counterweights. Their work is clearly what makes the show on the right run. No text.

## ch02-shared-nothing.png

- Chapter: `ch02-runtime.md`, after the paragraph describing the PHP-FPM pool.
- Idea: each request gets an identical, isolated room, and nothing passes between the rooms.
- Priority: must have.
- Format: landscape.

**Prompt.** A row of six identical small rooms drawn side by side as simple boxes with thin walls, seen from the front, like cells of a filmstrip. In each room, a calm round elephant receives an envelope through a slot on the left wall, works at a small desk, and hands a finished sheet out through a slot on the right wall. The last room on the right is empty and a broom is sweeping it clean. The walls between rooms are solid and unbroken, to show that nothing passes from one room to the next. The envelopes and the finished sheets are drawn in the blue accent color. No text.

## ch04-toll-booths.png

- Chapter: `ch04-concurrency.md`, after the paragraph on the cost of memory per idle connection.
- Idea: a pool of processes serves one connection per booth; an event loop passes many connections through one lane. Both handle traffic, differently.
- Priority: must have.
- Format: landscape.

**Prompt.** A motorway toll plaza seen from above, in a single wide view, split in two by a thin dotted line. On the left half, a row of five toll booths, a calm round elephant in each booth, exactly one small car stopped at each booth and a short queue of two or three cars behind each. On the right half, a single lane with an automatic gate drawn as a simple barrier with a small antenna, where a long line of small cars flows through without stopping, and one elephant sits above the lane at a control panel with a few lights. Both halves carry the same number of cars. The cars are drawn in the blue accent color. No text.

## ch06-conveyor.png

- Chapter: `ch06-ecosystem.md`, after the paragraph on `composer audit` and PIE.
- Idea: dependencies arrive as sealed crates checked against a pinned list before they reach the workbench.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A conveyor belt enters from the left carrying wooden crates, each with a small paper label. At the right end of the belt, a workbench where a calm round elephant assembles a machine from parts taken out of the crates. Between the belt and the bench, a second elephant holds a clipboard and compares each arriving crate with the list on it; a small padlock is drawn next to the list. On the wall above the bench hangs a second copy of the same list. The padlock and the labels on the crates are drawn in the blue accent color. No text.

## ch07-vote.png

- Chapter: `ch07-governance.md`, after the paragraph listing declined RFCs.
- Idea: a change enters the language by a public vote with a high bar, and the bar is visible to everyone.
- Priority: must have.
- Format: landscape.

**Prompt.** A round table seen from directly above, with about twelve calm round elephants seated around it. A single sheet of paper lies in the centre of the table. Most of the elephants raise one hand; three or four keep both hands on the table. On the wall behind the table, drawn as a simple rectangle, a horizontal gauge partly filled, with a small triangular marker placed two thirds of the way along its length and the filled part ending just past the marker. The filled part of the gauge and the raised hands are drawn in the blue accent color. No text, no digits.

## ch08-ledger.png

- Chapter: `ch08-cost.md`, after the paragraph on hosting cost per machine.
- Idea: cost of ownership has three columns, people, machines and calendar, and each is written down.
- Priority: nice to have.
- Format: landscape.

**Prompt.** An open accounting ledger lying on a desk, seen from slightly above. Its page is ruled into three columns, each headed by a small hand-drawn icon instead of a word: a group of three people, a rack of servers, a wall calendar. A calm round elephant wearing reading glasses holds a pen and writes a line in the middle column. Beside the ledger, a small neat stack of coins and a wall calendar on the desk with one month circled. The circle on the calendar and the pen tip are drawn in the blue accent color. No text, no digits.

## ch09-toolbox.png

- Chapter: `ch09-wrong-choice.md`, after the section on running outside the server.
- Idea: a good engineer puts a tool back and takes another when the job calls for it; no tool is the wrong tool, only the wrong job.
- Priority: must have.
- Format: landscape.

**Prompt.** A workshop wall with a pegboard where tools hang inside their painted outlines: a wrench, a saw, a plane, pliers, a small hammer. A calm round elephant stands in front of the wall, one hand putting a wrench back into its outline, the other hand reaching for the saw. On the workbench below lies a half-finished wooden object with a clear cut line marked on it, which obviously needs the saw. The marked cut line and the outline of the saw are drawn in the blue accent color. No text.

## ch10-week.png

- Chapter: `ch10-evaluation.md`, after the day-three section.
- Idea: five days, five boxes, ticked one after another; the evaluation is a finite, ordinary piece of work.
- Priority: must have.
- Format: landscape.

**Prompt.** A wall with a horizontal strip of five identical square boxes drawn on it, like a week planner, each box empty of text. A calm round elephant stands on a small wooden stool and ticks the third box with a pen; the first two boxes already carry a tick, the fourth and fifth are empty. On the floor beneath the strip sit an open laptop and a small server box with a blinking light. The three ticks and the pen are drawn in the blue accent color. No text, no digits.

## ch05-two-listings.png

- Chapter: `ch05-the-language.md`, after the pipe operator example.
- Idea: the PHP the reader remembers and the PHP of today are two different listings, and the second is shorter.
- Priority: nice to have.
- Format: landscape.

**Prompt.** Two code listings lying side by side on a desk, seen from above, drawn as sheets of paper with abstract lines standing for code (no readable words). The left sheet is yellowed, dense, with long lines, two coffee-ring stains and a few wavy underlines. The right sheet is clean white, shorter, with clear indentation and a few short segments highlighted in the blue accent color, standing for type annotations. A calm round elephant with a pen in hand reads the right-hand sheet. No text.
