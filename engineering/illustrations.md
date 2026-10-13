# Illustrations for "PHP: A Guide for the Decision Maker"

This file lists every drawing referenced by the chapters, with a ready-to-use prompt for each. The chapters of both languages already contain the `<img>` tags and alt texts; `make illustrations` in this folder generates the missing files into `src/images/` through `scripts/generate-illustrations.sh`, and `fr/images` links to the same folder.

Charts are a different thing: they are generated from data by `src/charts/build.py` and are never drawn by hand. The drawings carry ideas, not numbers: a mental model, a comparison of shapes, a small scene. A drawing in this book never contains a figure, a percentage or a ranking, so that nothing in it can be mistaken for data.

## Common style

Prepend this block to every prompt so all the drawings look like they come from the same hand, and from the same hand as the other books in this repository:

> Hand-drawn illustration in the style of a clean notebook sketch. Black ink lines drawn with a fine felt-tip pen, slightly imperfect strokes, on a pure white background. One accent color only, a soft blue, used sparingly to highlight what matters. No shading, no gradients, no textures, no 3D, no photorealism. Generous white space, centered composition. Calm and precise, like a diagram drawn on a whiteboard by a good engineer explaining something to a peer. Understated rather than playful. No watermark, no signature. No numbers, no percentages, no rankings anywhere in the drawing. No text at all.

Two practical notes:

- Every drawing is a small scene with a character in it, never a bare diagram of boxes and arrows. The PHP mascot is an elephant (the elePHPant), drawn as a small, round, calm elephant; it is the recurring character of every book in this repository. In this book it stands, waits, counts, serves or reads. It never clowns. A person may appear beside it when the scene needs a reader's stand-in.
- Image generators garble words. No prompt below asks for any text; if letters appear, regenerate.

Priority tells you which drawings the text depends on most. Format (landscape, portrait, or square) is read by the generation script to pick the image size.

---

## ch01-reputation.png

- Chapter: `ch01-introduction.md`, after the ecosystem paragraph.
- Idea: the reputation is an old photograph of the language; the language standing in front of you today is not the one in the photograph.
- Priority: must have.
- Format: landscape.

**Prompt.** A person holds up an old, yellowed, curling photograph at arm's length and compares it with what stands in front of them. The photograph shows a small scruffy elephant sitting in a tangle of cables, surrounded by scattered loose pages and a sagging cardboard box. In front of the person stands the same elephant today: a calm round elephant, tidy, standing straight beside a neat, closed toolbox and a short stack of squared, well-ordered sheets. The person's eyebrows are raised. The toolbox latch and the edge of the top sheet are drawn in the blue accent color. No text.

## ch02-runtime.png

- Chapter: `ch02-runtime.md`, after the opcache paragraph.
- Idea: shared-nothing. Every request gets a room that has been reset; nothing of the previous guest remains.
- Priority: must have.
- Format: landscape.

**Prompt.** A hotel corridor seen from the side, with three identical small rooms whose doors stand open, drawn like the cells of a filmstrip. In the left room, a guest carrying one envelope has just walked in and sits down at a small desk. In the middle room, a calm round elephant in a housekeeping apron strips the bed, empties the wastepaper basket into a cart and wipes the desk clean, so that nothing from the previous guest is left. The right room is perfectly made, empty, waiting. The walls between the rooms are solid and unbroken. The housekeeping cart and the fresh folded sheets on it are drawn in the blue accent color. No text.

## ch03-who-runs.png

- Chapter: `ch03-who-runs-php.md`, after the two-populations paragraph.
- Idea: two honest counts that measure different things: most of the shops carry the sign, few of the people on the pavement wear the badge.
- Priority: must have.
- Format: landscape.

**Prompt.** A town street in a single wide view. A long row of small shopfronts runs across the drawing, and almost every shop has a small round elephant sign hanging above its door; only two or three shops have a different, plain sign. On the pavement in front of the shops, a loose crowd of about fifteen people stands chatting; only three of them wear a small elephant badge on their jacket. At the street corner, a calm round elephant holds a clipboard and counts, one hand pointing up at the shop signs and the other pointing at the badges in the crowd. The shop signs and the badges are drawn in the blue accent color. No text, no digits.

## ch04-performance.png

- Chapter: `ch04-performance.md`, after the Benchmarks Game table.
- Idea: speed depends on what you measure. In a pure sprint the elephant runs mid-pack; on a web request every runner is stuck waiting at the same counter.
- Priority: must have.
- Format: landscape.

**Prompt.** A running track seen from the side, with two parallel lanes, one above the other. In the top lane, a plain sprint: a hare leads clearly, a calm round elephant runs second, a tortoise runs last. In the bottom lane, the same three runners are all stopped halfway along, standing in a short queue at a service counter, while a clerk behind the counter rummages through tall filing cabinets; nobody in that lane is running. Beside the track, a person holds a stopwatch and looks from one lane to the other, unsure which race to time. The stopwatch and the small bell on the counter are drawn in the blue accent color. No text, no digits.

## ch05-scale.png

- Chapter: `ch05-scale.md`, after the state-outside-the-process section.
- Idea: horizontal scaling. Identical stalls, any customer at any stall, one shared warehouse behind them, and adding capacity means unfolding one more stall.
- Priority: must have.
- Format: landscape.

**Prompt.** A market square seen from slightly above. A row of five identical small market stalls, a calm round elephant serving at each one, with customers queuing freely at whichever stall is shortest. Behind the whole row stands one large shared warehouse with a single wide door, and a small cart carries goods from that door to the stalls. At the right end of the row, a person in a work vest wheels in a sixth stall, still folded flat, ready to be unfolded and added to the line. The folded stall and the warehouse door are drawn in the blue accent color. No text.

## ch06-maintains.png

- Chapter: `ch06-who-maintains-it.md`, after the local-talent section.
- Idea: a large population of experienced workers whose practices vary from bench to bench; the auditor looks at the bench, not at the species.
- Priority: must have.
- Format: landscape.

**Prompt.** An open workshop with six workbenches in two rows, a calm round elephant working at each one. Four benches are tidy, with a small checklist pinned on the wall above and a little test rig with a lamp on the bench. Two benches are cluttered, with loose parts and no checklist above them. A person with a clipboard walks slowly between the benches, looking at the benches and the pinned checklists rather than at the elephants. The pinned checklists and the lamps of the test rigs are drawn in the blue accent color. No text, no digits.

## ch07-cost.png

- Chapter: `ch07-cost.md`, at the start of the no-proprietary-orchestration section.
- Idea: the same application, in the same suitcase, moves between a garage, a rented room and a container yard without being repacked, and the price tag is blank.
- Priority: must have.
- Format: landscape.

**Prompt.** A calm round elephant walks along a path carrying one small suitcase, drawn three times along the same path like three frames of a comic strip, each time passing through a different doorway: first a plain brick garage with a roll-up door, then a small rented room with a single window, then a yard of large stacked shipping containers. The suitcase is identical in all three frames and fits through every doorway without being opened. On the first frame, a small price tag hangs from the suitcase handle, completely blank. The suitcase is drawn in the blue accent color. No text, no digits.

## ch08-governance.png

- Chapter: `ch08-governance-and-versions.md`, after the RFC section.
- Idea: changes are voted in public with a high bar, releases follow the calendar, and old releases sit on a dusty shelf.
- Priority: must have.
- Format: landscape.

**Prompt.** The inside of a plain village hall. At the front, a calm round elephant stands at a lectern beside a simple ballot box. In the audience, rows of calm round elephants on wooden chairs; most of them raise one hand, a few keep their hands in their lap. On the side wall hangs a long yearly wall calendar strip with one month circled, and under it four shelves, each holding one plain box; the box on the lowest shelf is covered in dust and cobwebs, the one on the highest shelf is new. The raised hands and the circled month are drawn in the blue accent color. No text, no digits.

## ch09-wrong-choice.png

- Chapter: `ch09-wrong-choice.md`, after the native-apps section.
- Idea: for some jobs the right answer is a different tool, and the honest shopkeeper says so.
- Priority: must have.
- Format: landscape.

**Prompt.** The counter of a tool-hire shop. A calm round elephant stands in front of the counter holding up a hammer, offering it. Behind the counter, a shopkeeper with reading glasses shakes their head gently and points over their shoulder at a heavy drill press on the shelf behind them. On the counter between them lies a sheet with a simple sketch of the job: a stack of thick metal plates with a row of holes to be drilled, which obviously needs the drill press. The drill press and the holes on the sketch are drawn in the blue accent color. No text.

## ch10-evaluation.png

- Chapter: `ch10-the-evaluation.md`, after the opening paragraph.
- Idea: the reader runs the checks themselves, at their own table, against the book's list.
- Priority: must have.
- Format: landscape.

**Prompt.** A kitchen table seen from slightly above. A person types on an open laptop; the screen shows only a few plain horizontal lines of output, no readable words. Beside the person, a calm round elephant sits on a chair holding a printed sheet with a short list of empty tick boxes down one side, comparing the sheet with the screen; two boxes are already ticked and the elephant is ticking the third with a pen. A mug of coffee stands on the table. The ticks and the pen are drawn in the blue accent color. No text, no digits.
