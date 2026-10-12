# Illustrations for "Ship It With PHP"

This file lists every drawing referenced by the chapters, with a ready-to-use prompt for each. The chapters already contain the `<img>` tags and alt texts; drop the generated files into `src/images/` under the file names below and they will appear. `make illustrations` in this folder generates the missing ones through `scripts/generate-illustrations.sh`. The other books were drawn at medium quality:

```bash
OPENAI_API_KEY=sk-... OPENAI_IMAGE_QUALITY=medium make illustrations
```

Each drawing opens a chapter and carries the chapter's one idea: what the feature looks like once it is shipped, and who does the work. The reader should get the idea from the drawing alone, before reading a line. The drawings carry no product name, no logo and no code: the book compares tools, and a drawing must not look like it takes sides.

## Common style

Prepend this block to every prompt so all the drawings look like they come from the same hand, and from the same hand as the other books in this repository:

> Hand-drawn illustration in the style of a clean notebook sketch. Black ink lines drawn with a fine felt-tip pen, slightly imperfect strokes, on a pure white background. One accent color only, a soft blue, used sparingly to highlight what matters. No shading, no gradients, no textures, no 3D, no photorealism. Generous white space, centered composition. Friendly, practical, a little playful, like a diagram sketched on a whiteboard by a senior colleague who ships. No watermark, no signature. No logos, no brand names, no readable text anywhere in the drawing.

Two practical notes:

- Image generators garble words, so no prompt below asks for any. If a generated image contains text anyway, regenerate with "no text at all" added to the prompt.
- The PHP mascot is an elephant (the elePHPant). Drawn as a small, round, friendly elephant it is the recurring character of every book in this repository. In this book it works alongside a person: it hands over a tool, holds a door, runs the back room. The person is the reader.

Priority tells you which drawings the text depends on most. Format (landscape, portrait, or square) is read by the generation script to pick the image size.

---

## ch00-cover.png

- Chapter: `title-page.md`, under the title.
- Idea: the feature is finished, the last block goes in, and it gets handed over. The same scene as the landing page card for this book.
- Priority: must have.
- Format: square.

**Prompt.** A small house built from large building bricks, drawn in the center. A person and a small round friendly elephant, side by side, place the last brick on the roof together; that one brick is the only element in the blue accent color. To the right, a small delivery trailer waits with its ramp down, ready to take the house away. No text.

## ch00-menu.png

- Chapter: `ch00-00-how-this-book-works.md`, after the first paragraph.
- Idea: the book is a menu ordered by dish, not by ingredient: you pick the feature you were asked for.
- Priority: must have.
- Format: landscape.

**Prompt.** A person seated at a small café table holds a large open menu card. A small round friendly elephant in a waiter's apron stands beside the table with a notepad. On the menu, instead of words, each line is a simple icon followed by a short blank rule: a padlock, a shopping cart, a magnifying glass, an envelope, a speech bubble, a gear. The person's finger points at the padlock line, and that line is drawn in the blue accent color. No text.

## ch01-three-doors.png

- Chapter: `ch01-00-choosing-your-stack.md`, after the first paragraph.
- Idea: every brief describes one of three shapes, and the first job is to recognise which door it points at.
- Priority: must have.
- Format: landscape.

**Prompt.** Three closed doors side by side on a plain wall, each with a simple icon drawn on it instead of a name: a pair of gears on the left door, a pencil over a page on the middle door, a plug and socket on the right door. In front of the doors, a person holds a single sheet of paper and reads it. A small round friendly elephant next to the person points calmly at the middle door. The icon on the middle door and the elephant's pointing arm are in the blue accent color. No text.

## ch02-single-tool.png

- Chapter: `ch02-00-standalone-components.md`, after the first paragraph.
- Idea: for a small job you take one tool off the wall, not the whole machine.
- Priority: must have.
- Format: landscape.

**Prompt.** A workshop. On the left, a large complicated machine sits under a dust sheet, clearly not needed today. On the right, a pegboard wall with a handful of individual hand tools hanging in neat outlines: a wrench, a screwdriver, a small saw, a tape measure, a flashlight. A small round friendly elephant takes just the wrench off the wall and hands it to a person at a small workbench where a single small part waits. The wrench is in the blue accent color. No text.

## ch03-editable-page.png

- Chapter: `ch03-00-shipping-a-content-site.md`, after the first paragraph.
- Idea: the client rearranges the page themselves, and your job was the palette they may pick from.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A large sheet pinned to a wall like a poster, divided into a few rectangular blocks: a heading block, an image block with a simple mountain icon, two text blocks drawn as ruled lines. A person is moving one of the blocks to a new place on the sheet with both hands. Beside them, a small round friendly elephant holds a small painter's palette with only three color spots on it, one of them in the blue accent color, the block being moved also in the blue accent color. No text.

## ch04-front-desk.png

- Chapter: `ch04-00-shipping-user-accounts.md`, after the first paragraph.
- Idea: sign-up, login and permissions are a reception desk that already exists; nobody should build a new one.
- Priority: must have.
- Format: landscape.

**Prompt.** A hotel-style reception desk. Behind it, a small round friendly elephant in a small cap checks a badge held out by a person at the front of a short queue of three people. On the wall behind the desk, a rack of keys on hooks, and next to it a door with a padlock icon on it. The badge and the padlock icon are in the blue accent color. No text.

## ch05-generated-desk.png

- Chapter: `ch05-00-shipping-an-admin-back-office.md`, after the first paragraph.
- Idea: from one description of the data, the whole back office comes out ready: list, form, filters.
- Priority: must have.
- Format: landscape.

**Prompt.** A small round friendly elephant feeds a single sheet of paper, drawn with a few short lines standing for a class definition, into the slot of a simple box-shaped machine with a crank. Out of the other side of the machine, on a conveyor, comes a complete office desk with drawers, a filing cabinet, a form on a clipboard and a small table with rows, all assembled. A person at the end of the conveyor looks pleased and holds a coffee mug. The sheet going in is in the blue accent color. No text.

## ch06-service-hatch.png

- Chapter: `ch06-00-shipping-an-api.md`, after the first paragraph.
- Idea: an API is a service hatch with a posted menu: whoever queues up gets served the same way, and the menu stays true to what is on the shelves.
- Priority: must have.
- Format: landscape.

**Prompt.** A wall with a service hatch, seen from the customers' side. Behind the hatch, a small round friendly elephant stands in front of shelves of neatly labelled boxes, handing a small parcel through. In the queue at the hatch, three different customers: a smartphone with little legs, a laptop with little legs, and a small robot. Pinned to the wall next to the hatch, a printed board with a short list of icons and blank rules, like a posted menu. The parcel being handed over and the board's frame are in the blue accent color. No text.

## ch07-switchboard.png

- Chapter: `ch07-00-shipping-real-time-features.md`, after the first paragraph.
- Idea: the server pushes; every open screen lights up at the same moment without anyone pressing refresh.
- Priority: must have.
- Format: landscape.

**Prompt.** On the left, a small round friendly elephant sits at an old-fashioned telephone switchboard and plugs in one cable. From the switchboard, several wires run to the right and end at four small windows drawn as simple squares, each with a person looking at a screen. All four screens light up at the same instant, drawn with small radiating lines, and the lit screens and the one cable being plugged in are in the blue accent color. Nobody touches their screen. No text.

## ch08-shared-cabinet.png

- Chapter: `ch08-00-shipping-file-storage.md`, after the first paragraph.
- Idea: "our own Dropbox" is a shared cabinet with locks on some drawers and a copy in the cloud, and it already exists.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A tall shared filing cabinet with many drawers, two of them carrying a small padlock. A small round friendly elephant takes a folder from an open drawer and hands it through a small window to three devices waiting outside: a laptop, a phone and a desktop computer with little legs. Above the cabinet, a simple cloud outline contains the same folder drawn again, connected to the cabinet by a dotted line. The folder and the dotted line are in the blue accent color. No text.

## ch09-shop-counter.png

- Chapter: `ch09-00-shipping-a-storefront.md`, after the first paragraph.
- Idea: a store is a counter, a cart, and a cash box you do not open yourself: payment is handed to a specialist.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A small shop interior. A person pushes a shopping cart with a few boxes in it toward a counter. Behind the counter, a small round friendly elephant in an apron holds out a receipt. On the counter, a cash box with a large padlock, and a small chute leading from the cash box through the wall to the outside, showing the money goes somewhere else to be handled. The padlock and the chute are in the blue accent color. No text.

## ch10-librarian.png

- Chapter: `ch10-00-shipping-search.md`, after the first paragraph.
- Idea: a good search understands the request before it is finished, typo included.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A library counter. A person writes on a small request slip; the slip shows a scribble with one crossed-out squiggle, standing for a typo. On the other side of the counter, a small round friendly elephant with reading glasses is already holding out the right book, drawn with a small star on its cover, before the person has finished writing. Behind the elephant, a wall of small card-catalog drawers. The book's star and the crossed-out squiggle are in the blue accent color. No text.

## ch11-kitchen-rail.png

- Chapter: `ch11-00-shipping-background-work.md`, after the first paragraph.
- Idea: the counter answers at once; the slow work goes on a ticket rail in the back kitchen, handled by workers in order.
- Priority: must have.
- Format: landscape.

**Prompt.** A restaurant seen in cross-section. On the left, the front counter, where a person receives a small receipt immediately from a smiling round friendly elephant. On the right, through a pass-through window, the kitchen: a rail with a row of order tickets clipped to it, and two more round elephants in chef hats working through the tickets one by one, one of them stirring a pot. The tickets on the rail are in the blue accent color. No text.

## ch12-helpline.png

- Chapter: `ch12-00-shipping-an-ai-feature.md`, after the first paragraph.
- Idea: adding an AI feature means calling a specialist over the phone and writing the answer into your own form, not building the specialist.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A small round friendly elephant sits at an ordinary office desk, holding a telephone handset to its ear with one hand and writing on a form with the other. The telephone cord runs out of the drawing to the right, toward a distant building drawn as a simple outline with a small spark or lightbulb icon on its roof. On the desk, a stack of similar forms already filled. The cord and the spark are in the blue accent color. No text.

## ch13-linked-pages.png

- Chapter: `ch13-00-shipping-multi-language-multi-site.md`, after the first paragraph.
- Idea: a translated page is a linked twin of the original, not a copy of the site, and a missing translation shows as a gap.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A page tree drawn as a simple organisation chart: one page at the top, three pages below it, two more under one of them. Next to each page, one or two smaller twin pages connected to it by short dotted lines, drawn slightly offset like a shadow. One page has its twin drawn only as a dotted outline, clearly missing. A small round friendly elephant stands at the bottom of the tree holding a pen, looking at the missing twin. The dotted links and the missing outline are in the blue accent color. No text.

## ch14-gates.png

- Chapter: `ch14-00-shipping-confidence.md`, after the first paragraph.
- Idea: tests, analysis and audits are gates on the way to the truck, and a cracked crate never reaches the road.
- Priority: must have.
- Format: landscape.

**Prompt.** A conveyor belt carries wooden crates from left to right toward the open back of a delivery truck. Along the belt, three simple archway gates, each with one icon above it: a check mark, a magnifying glass, a padlock. One crate with a visible crack is being lifted off the belt by a small round friendly elephant just before the first gate; the other crates continue to the truck, where a person loads them. The three icons and the crack are in the blue accent color. No text.

## ch15-bottleneck.png

- Chapter: `ch15-00-shipping-fast-at-scale.md`, after the first paragraph.
- Idea: measure first: one narrow section of the pipe is the whole problem, and it is rarely the one you guessed.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A run of wide pipes drawn across the picture, with water flowing through, shown by small motion lines. One short section in the middle is much narrower than the rest, and small droplets queue up before it. A small round friendly elephant with a stopwatch in one hand points at exactly that narrow section, while a person behind it is about to tighten a valve on a completely different, wide part of the pipe. The narrow section and the stopwatch are in the blue accent color. No text.

## ch16-loading-dock.png

- Chapter: `ch16-00-shipping-to-production.md`, after the first paragraph.
- Idea: shipping means the truck actually leaves, checklist done, and someone stays responsible for the road.
- Priority: must have.
- Format: landscape.

**Prompt.** A loading dock. A delivery truck, doors just closed, pulls away from the dock toward a small city skyline in the distance. On the dock, a small round friendly elephant lifts the ramp with one hand and holds a clipboard with the other, all boxes on the clipboard ticked. Next to it, a person waves at the truck with one hand and holds a wrench in the other, ready for the next thing. The ticks on the clipboard and the truck's tail lights are in the blue accent color. No text.

## ch17-open-door.png

- Chapter: `ch17-00-where-to-go-from-there.md`, after the first paragraph.
- Idea: the door to the engine room was open all along; the reader walks through when the curiosity comes.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A small round friendly elephant holds a door open. Through the doorway, a tidy workshop: a car engine on a stand, a few hand tools on a wall, a stool. In front of the door, a person in work clothes with a tool belt stands on the threshold, one foot inside, looking at the engine with curiosity. Light coming through the doorway onto the floor is in the blue accent color. No text.
