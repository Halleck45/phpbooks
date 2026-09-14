# Illustrations for "And Now, PHP"

This file lists every drawing referenced by the chapters, with a ready-to-use prompt for each. The chapters already contain the `<img>` tags and alt texts; drop the generated files into `src/images/` under the file names below and they will appear. `make illustrations` in this folder generates the missing ones through `scripts/generate-illustrations.sh`.

The drawings carry an idea the text leans on (a lifecycle, a before and after, a mental model that differs from another language). It should be possible to understand the idea from the drawing alone.

## Common style

Prepend this block to every prompt so all the drawings look like they come from the same hand:

> Hand-drawn illustration in the style of a clean notebook sketch. Black ink lines drawn with a fine felt-tip pen, slightly imperfect strokes, on a pure white background. One accent color only, a soft blue, used sparingly to highlight what matters. No shading, no gradients, no textures, no 3D, no photorealism. Generous white space, centered composition. Friendly, simple, a little playful, like a diagram drawn on a whiteboard by a good teacher. No watermark, no signature.

Two practical notes:

- Image generators garble words. Each prompt lists the few labels the drawing needs. If the generated text is wrong, regenerate with "no text at all" added to the prompt and add the labels afterwards in an image editor, in a hand-lettered font.
- The PHP mascot is an elephant (the elePHPant). Drawn as a small, round, friendly elephant it makes a good recurring character. Keep it consistent across all drawings.

Priority tells you which drawings the text depends on most. Format (landscape, portrait, or square) is read by the generation script to pick the image size.

---

## ch00-cover.png

- Chapter: `title-page.md`, under the title.
- Idea: developers from many languages all arrive at the same door.
- Priority: must have.
- Format: square.

**Prompt.** A small round friendly elephant (the PHP mascot) holding a wooden signpost with four arrows. Each arrow carries one word: "Python", "JavaScript", "Java", "Go". All four arrows point the same way, toward a single open door on the right of the drawing, with "PHP" written above the door frame. Light coming through the door is drawn in the blue accent color. No other text.

## ch00-two-phps.png

- Chapter: `ch00-introduction.md`, after the paragraph listing what changed in PHP 7 and 8.
- Idea: the PHP of the jokes and the PHP of today are two different animals.
- Priority: must have.
- Format: landscape.

**Prompt.** Two elephants side by side, separated by a thin vertical dotted line. Left: an old, dusty elephant with a few patches sewn on, slumped on a pile of tangled spaghetti-like cables, a small cobweb in the corner. Right: a sleek, upright, modern elephant wearing a small bow tie, standing on a neat stack of labelled boxes. The right-hand side uses the blue accent color on the bow tie and the box labels. Labels: "2005" under the left elephant, "today" under the right one. No other text.

## ch01-request-lifecycle.png

- Chapter: `ch01-how-php-runs.md`, after the paragraph explaining that the web server hands the request to PHP-FPM.
- Idea: a PHP request is born, works, answers, and vanishes. Nothing survives to the next one.
- Priority: must have.
- Format: landscape.

**Prompt.** A circular diagram with four stages arranged clockwise, connected by curved arrows drawn in the blue accent color. Top left: a laptop with a small envelope leaving it, labelled "request". Top right: a small friendly elephant waking up in a completely empty room, stretching. Bottom right: the same elephant at a workbench assembling a page from a few blocks. Bottom left: the elephant handing the finished page to the laptop, and right next to it the room being wiped clean by a broom, with nothing left inside. Labels: "request", "fresh start", "work", "respond and forget".

## ch01-two-runtime-modes.png

- Chapter: `ch01-how-php-runs.md`, in the "Long-running PHP" section.
- Idea: classic FPM gives every request a fresh process; a worker runtime keeps one process alive and passes requests through it.
- Priority: nice to have.
- Format: landscape.

**Prompt.** Two panels side by side. Left panel: a row of four small identical rooms drawn as simple boxes, each with a fresh little elephant inside, one envelope going in and one page coming out of each, the last room shown empty and swept. Caption "one process per request". Right panel: a single larger room with one elephant sitting at a desk, a queue of envelopes lined up at the door and a stack of finished pages on the other side, the elephant clearly staying put. Caption "one process, many requests". The blue accent color highlights the envelopes.

## ch02-three-arrows.png

- Chapter: `ch02-syntax.md`, at the end of the "Control flow, all at once" section.
- Idea: PHP has three arrow-shaped tokens and each one points at a different kind of thing: `->` at an instance, `::` at a class, `=>` from a key to a value.
- Priority: must have.
- Format: landscape.

**Prompt.** Three wooden signposts side by side on a white background. The first signpost carries a big hand-lettered "->" and its arrow points at a single small round object drawn as a box with a handle, labelled "object". The second signpost carries "::" and points at a rolled blueprint drawn as a scroll with a tiny building sketched on it, labelled "class". The third signpost carries "=>" drawn as a double-lined arrow joining two index cards, the left card labelled "key" and the right card labelled "value". A small friendly elephant stands at the far left, looking at the three signs. The three arrows are drawn in the blue accent color. Labels: "->", "::", "=>", "object", "class", "key", "value".

## ch02-library-drawers.png

- Chapter: `ch02-syntax.md`, in "The trap" section, after the paragraph on inconsistent function naming.
- Idea: the standard library's names accumulated rather than being designed; an editor with completion is the flashlight that finds the right drawer.
- Priority: nice to have.
- Format: portrait.

**Prompt.** A tall old chest of drawers with about eight drawers, drawn slightly crooked. Each drawer has a paper label in a visibly different handwriting: "strpos", "str_replace", "strlen", "array_search", "in_array", "array_key_exists", "str_contains", "ucfirst". Some labels are neat, some scrawled, one is stuck on at an angle. At the bottom, a small friendly elephant holds a flashlight whose beam, drawn in the blue accent color, lights up exactly one drawer, the "str_contains" one, which is slightly open. No other text.

## ch03-strict-gate.png

- Chapter: `ch03-types.md`, at the end of the "What `int` really accepts" section, after the coercion table.
- Idea: in coercive mode PHP reshapes a numeric string into an integer before letting it into the function; in strict mode the same value is turned away.
- Priority: must have.
- Format: landscape.

**Prompt.** A single gate leading into a box labelled "int" on the right, with two lanes approaching it, one above the other, separated by a dashed line. Top lane, labelled "coercive": a small friendly elephant holds a speech bubble containing the characters "12" with quotation marks around them and, with a tiny hammer, reshapes it into a plain "12" without quotes that rolls through the gate. Bottom lane, labelled "strict": the same quoted "12" arrives and a second elephant, arms crossed, holds up a round stop sign in front of it; the value bounces back. The stop sign and the hammer are in the blue accent color. Labels: "coercive", "strict", "int".

## ch03-two-readers.png

- Chapter: `ch03-types.md`, at the end of the "Where the generics went" section.
- Idea: PHP itself reads only the code; a static analyser reads the docblock above it and enforces what the language cannot express.
- Priority: must have.
- Format: landscape.

**Prompt.** In the center, a sheet of paper with two lines: a top line inside a comment-style box reading "list<int>", and below it a plain code line reading "array $items". On the left, a small friendly elephant with reading glasses looks only at the lower line, with a thin sight line drawn to "array $items", and shrugs. On the right, a character drawn as a simple round robot holding a large magnifying glass over the top line "list<int>", nodding, with a small check mark next to its head. The magnifying glass and the check mark are in the blue accent color. Labels: "list<int>", "array $items", "PHP", "analyser".

## ch04-copy-on-write.png

- Chapter: `ch04-arrays.md`, in the "Arrays are values" section, after the paragraph contrasting with JavaScript, Python and Java.
- Idea: an array handed to a function is a copy. The caller's array never changes.
- Priority: must have.
- Format: landscape.

**Prompt.** Two desks side by side. On the left desk, a sheet of paper labelled "cart" with a short list written on it, and a small friendly elephant keeping a hand on it. Between the desks, a photocopier drawn as a simple box, with an arrow from the left sheet into it and an identical sheet coming out toward the right desk. On the right desk, a second elephant writing one extra line onto its copy with a pen. The extra line is drawn in the blue accent color, and only appears on the right-hand sheet. The left sheet is visibly unchanged. Labels: "original" above the left sheet, "copy" above the right sheet. No other text.

## ch04-array-vs-collection.png

- Chapter: `ch04-arrays.md`, in the "When an array is not enough" section, after the paragraph about wrapping an array in a class.
- Idea: a bare array accepts anything; a small collection class only accepts the shape you declared and offers the operations you chose.
- Priority: nice to have.
- Format: landscape.

**Prompt.** Left: an open wooden crate labelled "array", with mismatched objects tossed in, a shoe, a teacup, a number, a letter, spilling over the edge. Right: a neat closed box labelled "Orders" with a single shaped slot on its lid, and a hand dropping in a piece that fits the slot exactly, while a piece of another shape lies rejected beside the box. On the side of the box, a small counter window and a handle. The fitting piece and the slot are drawn in the blue accent color. Labels: "array", "Orders". No other text.

## ch05-closure-snapshot.png

- Chapter: `ch05-functions-and-closures.md`, in the "Closures capture by value" section, after the paragraph explaining that `use` copies at creation time.
- Idea: a closure takes a snapshot of the variables it captures. Changing the outer variable afterwards does not reach the closure.
- Priority: must have.
- Format: landscape.

**Prompt.** Left: a desk with a label card reading "rate" and the value "0.2" on it, and a small friendly elephant holding an instant camera, taking a photograph of the card. A printed photo slides out of the camera, showing the card with "0.2". Right: the same desk a moment later, the label card now crossed out and rewritten "0.5", while the elephant, standing apart, still holds the printed photo clearly reading "0.2". The photo is framed in the blue accent color. Labels: "rate 0.2" on the photo, "rate 0.5" on the desk card. No other text.

## ch06-handle-vs-copy.png

- Chapter: `ch06-classes.md`, at the end of the "Objects travel by handle" section.
- Idea: assigning an array duplicates the box; assigning an object adds a second string to the same box.
- Priority: must have.
- Format: landscape.

**Prompt.** Two panels side by side, separated by a thin vertical dotted line. Left panel: two variable tags drawn as small luggage labels, "$a" and "$b", each tied by a string to its own separate cardboard box; both boxes contain the same three little shapes, and a small "copy" arrow between them. Caption "array". Right panel: two luggage labels "$a" and "$b" both tied by strings to one single cardboard box with a small round elephant peeking out of it. Caption "object". The strings and the caption words are drawn in the blue accent color. No other text.

## ch07-enum-boundary.png

- Chapter: `ch07-enums-and-match.md`, after the paragraph about `cases()` and `->name`.
- Idea: `from()` and `tryFrom()` are the gate where a raw scalar becomes an enum case, and unknown values are turned away.
- Priority: must have.
- Format: landscape.

**Prompt.** A small sorting office drawn as a simple building, with three pigeonholes on its wall labelled "Draft", "Published", "Archived", each holding one identical little round elephant. On the left, a conveyor belt carries two paper tickets toward a door marked "from". The first ticket reads "published" and a blue accent arrow routes it into the "Published" pigeonhole. The second ticket reads "deleted" and is bounced back by a small barrier with a sign reading "null". Labels only: "Draft", "Published", "Archived", "from", "published", "deleted", "null".

## ch08-throwable-tree.png

- Chapter: `ch08-errors-and-exceptions.md`, after the paragraph describing the `Exception` family.
- Idea: everything catchable descends from `Throwable`, in two families: engine errors and your exceptions.
- Priority: must have.
- Format: landscape.

**Prompt.** A simple tree diagram drawn upside down like a family tree, root at the top. The root node is a rounded box labelled "Throwable". Two branches go down. The left branch ends in a box labelled "Error" with a small gear icon next to it, and under it three small leaves labelled "TypeError", "ValueError", "UnhandledMatchError". The right branch ends in a box labelled "Exception" with a small pencil icon next to it, and under it three small leaves labelled "RuntimeException", "InvalidArgumentException", and one leaf labelled "yours" drawn in the blue accent color. Branch lines are thin ink; the "yours" leaf is the only blue element.

## ch08-error-handler-funnel.png

- Chapter: `ch08-errors-and-exceptions.md`, right after the `set_error_handler` example.
- Idea: one handler turns every engine warning into an exception, so there is a single failure path.
- Priority: nice to have.
- Format: portrait.

**Prompt.** A large funnel drawn in the center. Falling into it from above are several small crumpled paper notes labelled "warning", "notice", "deprecated". Out of the narrow spout at the bottom comes a single neat envelope, drawn in the blue accent color, stamped with the word "exception". The envelope lands inside a rectangular box at the bottom labelled "try". A small friendly elephant stands next to the funnel holding it steady. No other text.

## ch09-autoload-lookup.png

- Chapter: `ch09-composer-and-namespaces.md`, after the `spl_autoload_register` example.
- Idea: a class name is turned into a file path, one namespace segment per folder.
- Priority: must have.
- Format: landscape.

**Prompt.** On the left, a small friendly elephant holds a slip of paper reading "App\Billing\Invoice". A dotted line in the blue accent color runs from the slip to the right, across a tall filing cabinet with three drawers stacked vertically. The drawers are labelled, top to bottom, "App", "Billing", "Invoice.php". The bottom drawer is pulled open and a page with a few code lines sticks out of it. The dotted line touches each drawer label in turn before ending at the open drawer. No other text.

## ch09-install-vs-update.png

- Chapter: `ch09-composer-and-namespaces.md`, after the paragraph explaining `config.platform.php` and scripts.
- Idea: `composer install` reproduces the lock file exactly; `composer update` resolves anew and rewrites it.
- Priority: nice to have.
- Format: landscape.

**Prompt.** Two panels separated by a thin vertical dotted line. Left panel, captioned "install": a small friendly elephant reads a ledger with a padlock drawn on its cover and stacks a few boxes on a shelf, each box matching a line in the ledger, with a checkmark in the blue accent color next to each line. Right panel, captioned "update": the same elephant looks at a bulletin board pinned with several small notices showing version numbers like "2.1", "2.3", "3.0", picks one new box, and with the other hand writes into the same ledger, now open and unlocked. Captions are the only text.

## ch10-bytes-vs-characters.png

- Chapter: `ch10-standard-library.md`, at the end of the "Strings are bytes" section, after the heredoc example.
- Idea: the same word measured two ways: plain functions count bytes and split the accented letter, the `mb_` functions count characters.
- Priority: must have.
- Format: landscape.

**Prompt.** The word "café" drawn twice, one above the other. Top row: five square boxes in a line, the first three holding "c", "a", "f", and the last two together holding the accented "é" visibly split across both boxes by a jagged line; above the row a plain wooden ruler with a tag reading "strlen = 5". Bottom row: four rounded tiles holding "c", "a", "f", "é" cleanly, one letter per tile; above it a ruler in the blue accent color with a tag reading "mb_strlen = 4". A small friendly elephant on the right points at the bottom row with an approving nod. Labels: "strlen = 5", "mb_strlen = 4". No other text.

## ch10-immutable-dates.png

- Chapter: `ch10-standard-library.md`, at the end of the "Dates" section.
- Idea: a mutable date object changes under every reference that points at it; an immutable one hands back a new value and stays put.
- Priority: nice to have.
- Format: landscape.

**Prompt.** Two panels separated by a thin vertical dotted line. Left panel: a single tear-off calendar page labelled "DateTime" with an arrow curling out of it and back into itself; the date on the page is scribbled over with a new date, and two small strings tied to the page lead to two little worried faces, showing that both see the change. Right panel: a calendar page labelled "DateTimeImmutable" sitting untouched, with a straight arrow producing a fresh second page beside it that carries the new date, drawn in the blue accent color; a small friendly elephant stands next to it, calm. Labels: "DateTime", "DateTimeImmutable". No other text.

## ch11-request-response.png

- Chapter: `ch11-web-request.md`, at the end of the "Reading the request" section.
- Idea: PHP has already unpacked the request into a few arrays before the script starts, and whatever the script prints becomes the response.
- Priority: must have.
- Format: landscape.

**Prompt.** Left: an open envelope labelled "request" from which four small trays slide out, stacked and labelled "GET", "POST", "COOKIE", "SERVER". The trays feed into the middle of the drawing, a sheet of paper standing upright labelled "script" with a few lines of squiggle on it and a small friendly elephant reading it. From the bottom of the sheet, printed text flows like a ribbon into a second, closed envelope on the right labelled "response"; a small sticker on the envelope's corner reads "headers". Arrows drawn in the blue accent color from left to right. Labels: "request", "GET", "POST", "COOKIE", "SERVER", "script", "headers", "response". No other text.

## ch11-middleware-onion.png

- Chapter: `ch11-web-request.md`, in "The standards layer" section, after the PSR list.
- Idea: PSR-15 middleware wraps the handler in layers; the request passes inward through each layer and the response passes back out through the same layers.
- Priority: nice to have.
- Format: square.

**Prompt.** An onion cut in half seen from the front, drawn as four concentric rings. From the outside in, the rings are labelled "logging", "auth", "CORS", and the small centre is a box labelled "handler". A single arrow labelled "request" enters from the left edge and crosses every ring to reach the centre; a second arrow labelled "response" leaves the centre and exits through the same rings on the right edge. Both arrows in the blue accent color. A small friendly elephant sits at the bottom right holding a tiny knife, having just cut the onion. Labels: "logging", "auth", "CORS", "handler", "request", "response". No other text.

## ch12-analyser-xray.png

- Chapter: `ch12-tooling.md`, at the end of the "Static analysis" section.
- Idea: a static analyser sees through every file at once and follows a value to the place where it breaks, before anything runs.
- Priority: must have.
- Format: landscape.

**Prompt.** A small round friendly elephant holding up a rectangular x-ray screen in front of a stack of three or four overlapping sheets of paper drawn as code files (just horizontal lines for code). Seen through the screen, a dotted line in the blue accent color leaves one sheet, crosses into another, and ends at a small round mark with a tiny "null" label next to a hand-drawn arrow symbol. The elephant looks calm and attentive. Labels: "null" only. No other text.

## ch13-processes-vs-loop.png

- Chapter: `ch13-concurrency-and-performance.md`, after the paragraph contrasting Node's event loop with PHP's process pool.
- Idea: an event loop keeps many connections alive in one process; PHP gives every request its own process. Same amount of work, two ways to hold it.
- Priority: must have.
- Format: landscape.

**Prompt.** Two panels side by side separated by a thin dotted vertical line. Left panel: one elephant juggling six balls at once, arms up, slightly tense expression, balls drawn in the blue accent color. Caption "event loop". Right panel: a row of six small identical elephants standing side by side, each calmly holding a single blue ball in its trunk. Caption "process pool". The number of balls is the same on both sides.

## ch13-where-time-goes.png

- Chapter: `ch13-concurrency-and-performance.md`, at the end of the "Measuring" section.
- Idea: in one web request, the interpreter is a thin slice; waiting on the database and other services is the bulk. Optimise where the time is.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A single long horizontal bar drawn like a timeline, divided into four segments of very different widths. From left to right: a thin segment labelled "PHP", a long segment labelled "database" filled with the blue accent color, a medium segment labelled "HTTP call", and a thin segment labelled "PHP" again. Below the bar, a small round friendly elephant holds a magnifying glass over the long blue database segment. Labels: "PHP", "database", "HTTP call", "PHP".

## ch14-before-after.png

- Chapter: `ch14-returning-developer.md`, right after the opening paragraphs, before the first pair.
- Idea: every old habit has a modern replacement; the old column is crossed out, the new one is what you write today.
- Priority: must have.
- Format: landscape.

**Prompt.** A whiteboard with two columns separated by a vertical line. Left column, written in black ink and each line struck through with a single stroke: "mysql_query", "array()", "require_once", "global $db". Right column, written in the blue accent color, one line facing each crossed-out one: "PDO", "[ ]", "autoload", "__construct(...)". A small round friendly elephant stands at the bottom right holding a marker, having just finished the right-hand column. Labels: "then" above the left column, "now" above the right column. No other text.
