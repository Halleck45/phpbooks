# Illustrations for the book

This file lists every drawing referenced by the chapters, with a ready-to-use prompt for each. The chapters already contain the `<img>` tags and alt texts; drop the generated files into `src/images/` under the file names below and they will appear.

The drawings are not decoration. Each one carries an idea the text leans on (a cycle, a flow, a before and after), so it should be possible to understand the idea from the drawing alone.

## Common style

Prepend this block to every prompt so all the drawings look like they come from the same hand:

> Hand-drawn illustration in the style of a clean notebook sketch. Black ink lines drawn with a fine felt-tip pen, slightly imperfect strokes, on a pure white background. One accent color only, a soft blue, used sparingly to highlight what matters. No shading, no gradients, no textures, no 3D, no photorealism. Generous white space, centered composition. Friendly, simple, a little playful, like a diagram drawn on a whiteboard by a good teacher. No watermark, no signature.

Two practical notes:

- Image generators garble words. Each prompt lists the few labels the drawing needs. If the generated text is wrong, regenerate with "no text at all" added to the prompt and add the labels afterwards in an image editor, in a hand-lettered font.
- The PHP mascot is an elephant (the elePHPant). Drawn as a small, round, friendly elephant it makes a good recurring character. If you prefer not to use it, replace it with a simple rounded robot with "PHP" written on its chest, and keep that choice consistent across all drawings.

Priority tells you which drawings the text depends on most. Start with "must have". Format (landscape, portrait, or square) is read by `scripts/generate-illustrations.sh` to pick the image size.

---

## ch00-request-cycle.png

- Chapter: `ch00-00-introduction.md`, after the waiter with no memory paragraph.
- Idea: a PHP request is born, works, answers, and vanishes. Every visit starts from a clean slate.
- Priority: must have.
- Format: landscape.

**Prompt.** A circular diagram with four stages arranged clockwise, connected by curved arrows forming a loop. Top left: a person at a laptop, with a small speech bubble containing a page icon, asking for a web page. Top right: a small friendly elephant (the PHP mascot) waking up, stretching, a "zzz" above its head turning into a lightbulb. Bottom right: the same elephant at a workbench assembling a web page from a few building blocks. Bottom left: the elephant handing the finished page back to the person, and right next to it a small puff of smoke where the elephant has vanished, leaving a perfectly clean, empty workbench. The arrows are drawn in the blue accent color. Labels: "ask", "wake up", "work", "answer and forget".

## ch00-roadmap.png

- Chapter: `ch00-00-introduction.md`, before the paragraph describing the five steps of the book.
- Idea: the book is a journey, and each stop is a bigger project than the last.
- Priority: must have.
- Format: landscape.

**Prompt.** A winding hiking trail drawn from the bottom left to the top right of the image, like a treasure map, with five milestones along the way, each marked by a small wooden signpost. Milestone 1: a tiny terminal window showing one line of text. Milestone 2: a die and a question mark. Milestone 3: an open toolbox with a few simple tools. Milestone 4: a terminal window next to a document and a small gear. Milestone 5: a browser window with a little house drawn inside it. A small walking figure with a backpack stands near the start of the trail. The trail is drawn in the blue accent color. Labels on the signposts: "Hello, world!", "a game", "the basics", "a CLI tool", "a web app".

## ch01-toolkit.png

- Chapter: `ch01-00-getting-started.md`, after the sentence listing the three things you need.
- Idea: three tools, nothing more, laid out like gear before a trip.
- Priority: nice to have.
- Format: landscape.

**Prompt.** Three objects laid side by side on a plain table, seen slightly from above, like equipment laid out before a trip. Left: a terminal window, a dark rectangle with a blinking cursor after a prompt. Middle: a text editor window showing three short lines of code. Right: a small friendly elephant (the PHP mascot) sitting calmly. Nothing else on the table. Labels under each object: "terminal", "editor", "PHP".

## ch01-terminal-chat.png

- Chapter: `ch01-01-installation.md`, in the "Opening a terminal" section.
- Idea: the terminal is a conversation. You say something, the computer answers.
- Priority: must have.
- Format: landscape.

**Prompt.** A person and a laptop facing each other like two friends chatting. The laptop has a small smiling face on its screen. Two speech bubbles: the person's bubble contains "php -v", the laptop's bubble, drawn in the blue accent color, contains "PHP 8.3". Nothing else. Labels: exactly the two bubble texts.

## ch01-two-hats.png

- Chapter: `ch01-01-installation.md`, in the "PHP wears two hats" section.
- Idea: php-cli and php-fpm are the same language in two roles.
- Priority: nice to have.
- Format: landscape.

**Prompt.** The same small friendly elephant (the PHP mascot) drawn twice, side by side, separated by a thin vertical dotted line. Left: the elephant wears a simple flat cap, stands in front of a terminal window, and holds a sheet of paper with a few lines written on it, like a script. Right: the elephant wears a tall chef's hat and stands behind a serving counter, passing a web page through a hatch to a browser window waiting on the other side. Labels: "in the terminal" on the left, "behind a web server" on the right.

## ch01-hello-anatomy.png

- Chapter: `ch01-02-hello-world.md`, right after "Let's take it apart".
- Idea: every character in the three-line program has a job.
- Priority: must have. This one is text-heavy, so it may be easier to draw in a vector editor than to generate: write the code in a monospace font and add hand-drawn callouts around it.
- Format: landscape.

**Prompt.** Three lines of code hand-lettered large in the center of the image, in a monospace style: first line `<?php`, second line empty, third line `echo "Hello, world!\n";`. Five thin callout lines, drawn in the blue accent color, each starting at one part of the code and ending in a short hand-written label in a small rounded frame. Callout 1 from `<?php`: "code starts here". Callout 2 from `echo`: "prints". Callout 3 from the text between quotes: "the text". Callout 4 from `\n`: "new line". Callout 5 from the semicolon: "full stop". Plenty of white space around the code.

## ch01-php-island.png

- Chapter: `ch01-02-hello-world.md`, in the opening tag section.
- Idea: a PHP file is plain text with islands of code. Only the islands are executed; the rest is copied to the output as is.
- Priority: must have.
- Format: landscape.

**Prompt.** A sheet of paper drawn in the center, covered with short wavy lines standing for ordinary text. In the middle of the sheet, a rounded island shape, drawn like a small island seen from above, surrounded by a thin wavy shoreline. On the island's left shore the tag `<?php`, on its right shore the tag `?>`, and between them three short lines of code. Small arrows flow from the wavy text lines straight out to the right, towards a screen drawn at the right edge of the image, showing the same wavy lines unchanged. The island and its tags are highlighted in the blue accent color. Labels: "code" on the island, "sent as is" near the arrows.

## ch01-semicolon-detective.png

- Chapter: `ch01-02-hello-world.md`, in the semicolon section, after the parse error.
- Idea: PHP blames the line below the real mistake.
- Priority: optional, purely for fun.
- Format: landscape.

**Prompt.** A cartoon detective in a trench coat, holding a magnifying glass, pointing an accusing finger at a line of code labeled "line 4". Just above it, a line labeled "line 3" ends with an empty dotted outline where a semicolon should be, with a tiny question mark next to it. A small semicolon character with a mischievous face hides behind line 3, peeking out. The dotted outline is drawn in the blue accent color. Labels: "line 3", "line 4".

## ch01-edit-run-look.png

- Chapter: `ch01-02-hello-world.md`, in the "Running it, again and again" section.
- Idea: the PHP work loop is edit, run, look, and around again. No compile step.
- Priority: must have.
- Format: landscape.

**Prompt.** Three simple icons arranged in a triangle, connected by curved arrows forming a clockwise loop. Top: a pencil writing on a document. Bottom right: a terminal window with a play triangle inside it. Bottom left: a wide-open eye looking at a small window showing a line of output. The arrows are drawn in the blue accent color. Labels next to each icon: "edit", "run", "look".

## ch02-game-rules.png

- Chapter: `ch02-00-guessing-game-tutorial.md`, after the rules paragraph.
- Idea: the game is a dialogue between the player and the computer.
- Priority: must have.
- Format: landscape.

**Prompt.** A three-panel comic strip, panels separated by thin hand-drawn frames. Panel 1: a laptop with a smiling face on its screen and a thought bubble containing a small locked box with a question mark on it, and a tiny sign reading "1 to 100". Panel 2: a person typing, with a speech bubble containing "50". Panel 3: the laptop's speech bubble reads "Too big!" and the person's new speech bubble reads "25". The speech bubbles of the laptop are in the blue accent color. Labels: exactly the texts in the bubbles and on the sign.

## ch02-flowchart.png

- Chapter: `ch02-00-guessing-game-tutorial.md`, in "The game on one drawing", and referred to again at the end of the chapter.
- Idea: the whole algorithm on one page. Every box becomes a few lines of code. This is the central drawing of the chapter.
- Priority: must have. If only one drawing gets done, it is this one.
- Format: portrait.

**Prompt.** A hand-drawn flowchart read from top to bottom, with rounded boxes and diamonds for questions, connected by arrows. From the top: a rounded box "pick a secret number". Below it a box "ask for a guess". Below it a box "read the answer". Below it a diamond "is it a number?" with a "no" arrow that curves back up to the "ask for a guess" box, and a "yes" arrow going down. Below it a diamond "compare to the secret" with three arrows out: one to a box "too small", one to a box "too big", and one to a box "you win!". The "too small" and "too big" boxes both have arrows curving back up to "ask for a guess". The "you win!" box leads down to a final rounded box "stop". All the arrows that go back up are drawn in the blue accent color, the rest in black. Clean, well spaced, easy to follow. Labels: the box and diamond texts exactly as written, plus "yes" and "no".

## ch02-stdin-trim.png

- Chapter: `ch02-00-guessing-game-tutorial.md`, in Step 1, next to the explanation of fgets and trim.
- Idea: typed text travels through STDIN with the Enter key attached, and trim cuts it off.
- Priority: must have.
- Format: landscape.

**Prompt.** Left: a keyboard with a finger pressing the Enter key. From the keyboard, a horizontal tube or pipe runs to the right across the image, carrying three small square tiles in a row, like letter tiles from a board game: "4", "2", and a third tile with the Enter arrow symbol on it. At the right end of the pipe, a box labeled "program" with an open door. Just before the door, a pair of scissors snips the pipe to cut off the third tile, which falls away below. The scissors and the falling tile are in the blue accent color. Labels: "STDIN" on the pipe, "trim()" next to the scissors, "program" on the box.

## ch02-variable-box.png

- Chapter: `ch02-00-guessing-game-tutorial.md`, in Step 1, after the explanation of variables.
- Idea: a variable is a labeled box holding a value.
- Priority: nice to have.
- Format: square.

**Prompt.** A single cardboard box with its lid open, seen from a three-quarter angle, with a paper label taped to its front. Inside the box, the number 42 sits like an object. The label is in the blue accent color. Nothing else in the image. Label on the box: "$guess".

## ch02-string-vs-int.png

- Chapter: `ch02-00-guessing-game-tutorial.md`, in Step 3, next to the explanation of (int).
- Idea: text that looks like a number is not a number. The cast turns one into the other.
- Priority: must have.
- Format: landscape.

**Prompt.** Left side: two small square tiles side by side, like letter tiles, showing "4" and "2", with an opening quotation mark before them and a closing quotation mark after them. A small tag underneath reads "text". Right side: a single solid, bold number 42 with a small tag underneath reading "number". Between the two, a long horizontal arrow in the blue accent color with the label "(int)" written above it. Plenty of white space. Labels: "text", "number", "(int)".

## ch02-loop-track.png

- Chapter: `ch02-00-guessing-game-tutorial.md`, in Step 4, after the explanation of while and break. Step 5 refers to it again for continue.
- Idea: a loop is a track. break is a door out of it, continue is a shortcut back to the start line.
- Priority: must have.
- Format: landscape.

**Prompt.** An oval running track seen from above, with a small runner jogging on it. A start line is drawn across the track at the bottom, with a sign reading "ask". On the right side of the track, a gap in the outer fence with a small open door and an arrow leading away from the track to a sign reading "stop". The door has a sign reading "break". Across the grassy infield, a dotted shortcut path leads from the top of the track back to the start line, with a sign reading "continue". The door, the arrow out, and the shortcut path are in the blue accent color. Labels: "ask", "break", "continue", "stop".

---

## ch03-game-pieces.png

- Chapter: `ch03-00-common-programming-concepts.md`, after the opening paragraph.
- Idea: the guessing game the reader typed is made of five kinds of pieces, and this chapter names them.
- Priority: must have.
- Format: landscape.

**Prompt.** An exploded view, like an assembly diagram for a toy. In the center, a sheet of paper with a few short lines of code sketched as wavy lines, titled guessing_game.php. Around it, five parts pulled out of the sheet and connected to it by thin dotted lines, each part in its own small rounded frame: a cardboard box with a dollar sign on it; two tiles side by side, one showing 42 in quotes and one showing a bold 42; a small machine with a funnel on top and a chute on the side; a sticky note with two slashes on it; and a diamond shape next to a circular arrow. A small friendly elephant (the PHP mascot) stands at the bottom holding a screwdriver. The dotted lines and the frames are in the blue accent color. Labels under the five parts: "variables", "types", "functions", "comments", "control flow".

## ch03-variable-vs-constant.png

- Chapter: `ch03-01-variables-and-mutability.md`, in the Constants section, after the define and const code block.
- Idea: a variable can be changed at any time, a constant cannot. The dollar sign is what tells them apart.
- Priority: must have.
- Format: landscape.

**Prompt.** Two objects side by side, separated by a thin vertical dotted line. Left: a cardboard box with its lid open and a paper label taped to its front reading "$maxRetries", one corner of the label peeling off, with a hand holding a second blank label ready to replace it. Right: a smooth rounded stone, like a small monument, with the name "MAX_RETRIES" carved into it in capital letters, and the number 3 carved below the name. The peeling label and the hand are in the blue accent color. Labels: "$maxRetries" on the box label, "MAX_RETRIES" on the stone, "can change" under the box, "cannot" under the stone.

## ch03-type-juggling.png

- Chapter: `ch03-02-data-types.md`, in the type juggling section, after the var_dump code block.
- Idea: the operator decides the conversion. The same two values give a number with plus and a text with dot.
- Priority: must have.
- Format: landscape.

**Prompt.** Two horizontal rows, one above the other. In both rows, the same two inputs on the left: a small square tile showing the digit 5 between quotation marks, and a bold solid number 3. Top row: the two inputs go into a big circled plus sign, and out of it on the right comes a bold solid number 8. Bottom row: the same two inputs go into a big circled dot, and out of it comes a pair of tiles between quotation marks showing 5 and 3 side by side. A small friendly elephant (the PHP mascot) stands between the rows, juggling the inputs with a relaxed expression. The two circled operators are in the blue accent color. Labels: "number" under the 8, "text" under the 53.

## ch03-strict-types-door.png

- Chapter: `ch03-02-data-types.md`, in the type juggling section, after the declare(strict_types=1) code block.
- Idea: with strict types on, a value of the wrong type is stopped at the function's door instead of being quietly converted.
- Priority: must have.
- Format: landscape.

**Prompt.** A doorway with a sign above it reading "strict_types=1", the door opening into a small building labeled "function". A small friendly elephant (the PHP mascot) stands next to the door as a bouncer, wearing a tiny bow tie, one arm raised in a stop gesture. Two visitors are queuing: in front, a bold solid number 4, being waved through the door by the elephant's other arm; behind it, a square tile showing the digit 4 between quotation marks, stopped by the raised arm, with a small speech bubble from the elephant reading "TypeError". The sign and the speech bubble are in the blue accent color. Labels: "strict_types=1", "function", "TypeError".

## ch03-function-machine.png

- Chapter: `ch03-03-how-functions-work.md`, right after the paragraph describing the shape of a function.
- Idea: a function is a named machine. A value goes in through the parameter, a result comes out through return.
- Priority: must have.
- Format: landscape.

**Prompt.** A small friendly machine drawn in the center, like a box with a few rivets and a name plate on the front reading "greet". On top, a funnel with a small label "$name", and a tile with the word Damien in quotes falling into the funnel. On the right side, a chute with a small label "return", and out of it slides a strip of paper reading "Hello, Damien!". A single big crank handle on the left side of the machine. The funnel, the chute and their labels are in the blue accent color. Labels: "greet", "$name", "return", "Damien", "Hello, Damien!".

## ch03-comment-why.png

- Chapter: `ch03-04-comments.md`, in the "What is worth commenting" section, after the bad and good comment code block.
- Idea: a comment that repeats the code is useless, a comment that explains why the code exists is precious.
- Priority: nice to have.
- Format: square.

**Prompt.** A single line of code in the center, hand-lettered in a monospace style: $retries++; Two sticky notes are stuck next to it, one above and one below. The note above reads "add one" and is crossed out with a big X. The note below reads "API is flaky on cold start" and has a small check mark next to it. The note below and its check mark are in the blue accent color. Labels: "add one", "API is flaky on cold start".

## ch03-match-arms.png

- Chapter: `ch03-05-control-flow.md`, in the match section, after the match code block.
- Idea: match routes one value to exactly one arm and produces one result, with no fallthrough.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A railway switch seen from above. A single track comes in from the left carrying a small cart with the number 404 painted on it. The track splits into four parallel arms going to the right, each arm with a small signpost next to it: "2xx", "4xx", "5xx", "default". Only the second arm, "4xx", is connected to the incoming track and is drawn in the blue accent color; the other three are disconnected and drawn in black. At the end of the connected arm, a small station building with a sign reading "Client error". Labels: "404", "2xx", "4xx", "5xx", "default", "Client error".

## ch03-while-vs-dowhile.png

- Chapter: `ch03-05-control-flow.md`, in the Loops section, after the do while code block.
- Idea: while checks the condition before each pass, do while checks it after, so the body of a do while always runs at least once.
- Priority: must have.
- Format: landscape.

**Prompt.** Two small scenes side by side, separated by a thin vertical dotted line, each showing a room with a door and a ticket inspector. Left scene: the inspector stands outside the door, checking a ticket before the visitor enters, and the room behind is empty. Right scene: the visitor is already inside the room, and the inspector stands at the exit checking the ticket on the way out, with a curved arrow leading from the exit back to the entrance. In both scenes the inspector is a small friendly elephant (the PHP mascot) with a cap. The tickets and the curved arrow are in the blue accent color. Labels: "while" above the left scene, "do while" above the right scene, "check first" under the left, "run first" under the right.

---

## ch04-copy-on-write.png

- Chapter: `ch04-01-copy-on-write.md`, in "But it doesn't actually copy on the spot", after the paragraph explaining the first write.
- Idea: after the assignment, two variables share one box. The first write is what makes PHP duplicate it.
- Priority: must have.
- Format: landscape.

**Prompt.** A two-panel before-and-after drawing separated by a thin vertical dotted line, with a big curved arrow going from the left panel to the right panel over the top. Left panel: a single open cardboard box containing three small tiles reading 1, 2 and 3, with two paper labels tied to it by short strings, one reading "$original" and one reading "$copy", and a tiny round counter tag on the corner of the box showing the number 2. Right panel: two separate boxes side by side; the left one has the label "$original" and the tiles 1, 2, 3; the right one has the label "$copy" and the tiles 1, 2, 3 plus a fourth tile reading 4 being dropped in by a small hand from above. The new fourth tile, the second box and the big curved arrow are in the blue accent color. A small friendly elephant (the PHP mascot) stands between the two panels, pushing the second box into place. Labels: "$original", "$copy", "before", "after".

## ch04-two-labels.png

- Chapter: `ch04-02-references.md`, in "Explicit references with `&`", after the paragraph about two labels on the same box.
- Idea: a reference is not a second box, it is a second label on the same box.
- Priority: must have.
- Format: square.

**Prompt.** A single cardboard box with its lid open, seen from a three-quarter angle, in the center of the image, with the number 20 sitting inside like an object. Two paper labels are taped to the front of the box, side by side, one reading "$a" and the other reading "$b". The second label, "$b", is drawn in the blue accent color, with a small ampersand sign floating just above it. Nothing else in the image, plenty of white space. Labels: "$a", "$b", "20".

## ch04-arrays-copy-objects-alias.png

- Chapter: `ch04-02-references.md`, in "Arrays copy, objects don't", after the paragraph comparing `$cartB = $cartA` to `$copy = $original`.
- Idea: two array variables are two boxes with the same content; two object variables are two name tags tied to the same object.
- Priority: must have.
- Format: landscape.

**Prompt.** Two halves separated by a thin vertical dotted line. Left half: two identical open cardboard boxes side by side, each containing the same two small tiles, one label under each box, with a small equals sign drawn between the boxes and a tiny sign above them reading "arrays copy". Right half: one single shopping cart drawn from the side, containing a small book and a pen, with two name tags tied to its handle by two separate strings, one tag reading "$cartA" and the other reading "$cartB", and a tiny sign above reading "objects alias". The two strings and the two name tags on the cart are in the blue accent color. A small friendly elephant (the PHP mascot) sits at the bottom between the two halves, pointing one trunk-tip at each side. Labels: "arrays copy", "objects alias", "$cartA", "$cartB".

## ch04-scope-rooms.png

- Chapter: `ch04-03-scope-and-gc.md`, in "Functions have their own scope", after the room analogy.
- Idea: a function is a closed room with its own shelves. What is on a shelf inside cannot be seen from the hall, and `global` is a small hatch in the wall.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A cross-section of a simple house seen from the front, like a dollhouse. On the left, a wide hall with a shelf holding one cardboard box labeled "$counter". On the right, a smaller closed room with a solid wall between it and the hall, a door marked "greet()" on its front, and inside it a shelf holding one cardboard box labeled "$message". A small friendly elephant (the PHP mascot) stands in the hall, looking at the wall with a puzzled expression and a small question mark above its head, unable to see the box in the room. In the wall between the two spaces, a tiny hatch with a small sign reading "global" is drawn in the blue accent color, with a thin blue arrow going through it from the room towards the hall's box. Labels: "$counter", "greet()", "$message", "global".

## ch04-refcount-cycle.png

- Chapter: `ch04-03-scope-and-gc.md`, in "A brief, honest word about garbage collection", after the paragraph about the counter reaching zero.
- Idea: a value is freed the moment its last label is removed. Two values pointing at each other keep their counters above zero, so a separate collector has to come for them.
- Priority: nice to have.
- Format: landscape.

**Prompt.** Two scenes side by side separated by a thin vertical dotted line. Left scene, read as a short sequence of three small drawings from left to right: a cardboard box with two labels tied to it and a round counter tag showing 2; the same box with one label being untied and floating away, the counter tag showing 1; the same box with no label at all, the counter tag showing 0, tipping into a small waste bin. Right scene: two cardboard boxes facing each other, each with a curved arrow going from itself to the other one, forming a loop, and a counter tag showing 1 on each; no label is attached to either box, and a small friendly elephant (the PHP mascot) approaches from the side holding a broom, coming to sweep them up. The counter tags and the two curved arrows of the loop are in the blue accent color. Labels: "2", "1", "0", "cycle".

---

## ch05-array-vs-class.png

- Chapter: `ch05-00-classes.md`, after the paragraph saying an associative array has no fixed shape.
- Idea: an array is a loose pile of labeled notes, a class is a printed form with fixed fields and its instructions attached.
- Priority: must have.
- Format: landscape.

**Prompt.** Left half: a small cloth bag tipped over, with square sticky notes spilling out in a messy pile, each note carrying one handwritten word: "name", "price", "quantity", and one note where the word is misspelled and crossed out, slightly crooked. Right half: a neat printed form on a clipboard, with three fixed fields drawn as rectangular boxes labeled "name", "price", "quantity", each with a short blank line for a value, and a small tool tag hanging from the bottom of the clipboard on a string, reading "totalPrice()". A small round friendly elephant (the PHP mascot) stands between the two halves, looking at the clipboard with a satisfied smile. The clipboard outline and the hanging tool tag are in the blue accent color. Labels: "array" under the bag, "class" under the clipboard, and the three field names.

## ch05-blueprint-instances.png

- Chapter: `ch05-01-defining-classes.md`, in "Instantiating a class", after the explanation of the arrow operator.
- Idea: one class, as many separate objects as you ask for, each with its own values.
- Priority: must have.
- Format: landscape.

**Prompt.** Top center: a blueprint sheet pinned at its four corners, showing the outline of a rectangle with two empty dotted slots inside it, labeled "width" and "height", and the title "Rectangle" written across the top of the sheet. From the sheet, two arrows go down and apart, each labeled "new", to two separate solid rectangles at the bottom, clearly spaced from each other. The left rectangle is wide and short, with small tags "10" and "4" next to its sides, and the name "$rect" underneath. The right rectangle is a square, with tags "3" and "3", and the name "$rect2" underneath. A small round friendly elephant (the PHP mascot) wearing a hard hat stands between the two rectangles, holding a trowel like a builder. The two "new" arrows are in the blue accent color. Labels: "Rectangle", "width", "height", "new", "$rect", "$rect2".

## ch05-visibility.png

- Chapter: `ch05-01-defining-classes.md`, in the visibility section, right after the private property error.
- Idea: a private property stays inside the walls; the outside reaches it only through the window the class opens, a public method.
- Priority: nice to have.
- Format: square.

**Prompt.** A simple house drawn as a rounded rectangle with a small roof, and a sign on the roof reading "Rectangle". The front wall is cut away on one side so we see inside: two small safes with tiny padlocks, labeled "width" and "height". On the front wall, a closed door with a sign reading "private", and next to it one open service window with a counter, marked "public", where a small round friendly elephant (the PHP mascot) stands behind the counter and hands a slip of paper with "10" written on it to a person waiting outside. The open window and the slip of paper are in the blue accent color. Labels: "Rectangle", "private", "public", "width", "height".

## ch05-logic-with-data.png

- Chapter: `ch05-02-example-classes.md`, after the "try it" about passing a quoted quantity, before the paragraph saying totalPrice lives on Product.
- Idea: with an array, the data and the function that works on it live far apart, held together by fragile string keys; with a class, the method travels with the data.
- Priority: must have.
- Format: landscape.

**Prompt.** A before and after split by a thin vertical dotted line. Left panel: at the far left, an open cardboard box labeled "$item" full of loose paper tags reading "name", "price", "quantity"; at the far right of the panel, a separate small machine with a slot, labeled "lineTotal()"; between the box and the machine, a long, fraying, knotted piece of string with a small question mark hanging from its middle. Right panel: a single neat suitcase labeled "Product" with the same three tags printed cleanly on its side, and a small calculator built into its handle, labeled "totalPrice()". A small round friendly elephant (the PHP mascot) carries the suitcase easily with its trunk, walking to the right. The frayed string and the built-in calculator are in the blue accent color. Labels: "$item", "lineTotal()", "Product", "totalPrice()".

## ch05-this.png

- Chapter: `ch05-03-methods.md`, in the "$this" section, after the paragraph explaining that inside the method $this is $mug.
- Idea: $this is whichever object the method was called on, and only that one.
- Priority: nice to have.
- Format: landscape.

**Prompt.** Two identical wooden product crates side by side in the lower half of the image. The left crate has a coffee mug drawn on its front, the name "$mug" above it, and a hanging price tag reading "8.50" with a small strike through it and "7.65" written next to it. The right crate has a pen drawn on its front, the name "$pen" above it, and a hanging price tag reading "1.10", untouched. At the upper left, a small round friendly elephant (the PHP mascot) says "applyDiscount(10)" in a speech bubble. From the bubble, one thick arrow labeled "$this" curves down and points at the left crate only. Nothing points at the right crate. The arrow and the new price "7.65" are in the blue accent color. Labels: "$mug", "$pen", "$this", "applyDiscount(10)".

---

## ch06-fixed-set.png

- Chapter: `ch06-00-enums.md`, after the paragraph about hoping nobody types shiped.
- Idea: a free string accepts anything, including typos; an enum is a knob with a few engraved positions and nothing in between.
- Priority: must have.
- Format: landscape.

**Prompt.** Two objects side by side, separated by a thin vertical dotted line. Left: a plain rectangular text input field, like a form field on paper, with the word "shiped" hand-written inside it and a small wavy underline beneath the misspelling, plus a tiny worried face next to the field. Right: a round rotary selector knob, like the dial on an old radio, with exactly three positions engraved around it as short tick marks, and a pointer on the knob resting firmly on the middle one. The pointer and the three tick marks are in the blue accent color. A small friendly elephant (the PHP mascot) stands beside the knob, one foot on it, looking satisfied. Labels: "shiped" in the text field, "pending", "shipped", "cancelled" around the knob.

## ch06-suit-singleton.png

- Chapter: `ch06-01-defining-an-enum.md`, after the paragraph explaining that there is exactly one Suit::Hearts in the whole program.
- Idea: a case is a single, unique value; several variables can point at it, but there is still only one of it.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A cork notice board seen from the front with four playing cards pinned to it in a row, each showing only its suit symbol large in the middle: a heart, a diamond, a club, a spade. Below the board, three small paper tags with a hole punched in them, like luggage labels, each tied by a thin piece of string that runs up to the pin of the same card, the heart. The three strings and the heart symbol are in the blue accent color; the other three cards are plain black ink. Labels: "$card", "$first", "$drawn" on the three tags, and "Suit::Hearts" written under the heart card.

## ch06-backed-bridge.png

- Chapter: `ch06-01-defining-an-enum.md`, after the paragraph comparing from() and tryFrom().
- Idea: a backed enum's value is the form a case takes to leave the program and come back; from() and tryFrom() are the checkpoint on the way in, one strict, one forgiving.
- Priority: must have.
- Format: landscape.

**Prompt.** A wide scene read from left to right. Left: the outside world, drawn as a small database cylinder and a sheet of paper with curly braces on it, standing for a JSON document. From them, two small luggage tags travel rightward along a dotted path, one reading "shipped" and one reading "bogus". Center: a small customs booth or border checkpoint with a barrier, staffed by a small friendly elephant (the PHP mascot) wearing a cap and holding a clipboard. Right: a rounded frame standing for the program, inside which the tag "shipped" has been stamped and turned into a neat little badge reading "Status::Shipped". The "bogus" tag is bounced back to the left of the booth along a curved arrow, with a small empty circle next to it reading "null". The booth barrier, the curved bounce arrow and the badge are in the blue accent color. Labels: "shipped", "bogus", "from() / tryFrom()" on the booth, "Status::Shipped" on the badge, "null" next to the bounced tag.

## ch06-match-table.png

- Chapter: `ch06-02-match.md`, after the paragraph describing match as a table read top to bottom.
- Idea: match is a lookup table; the value walks in on the left, the matching row lights up, and its answer comes out on the right.
- Priority: must have.
- Format: landscape.

**Prompt.** A simple hand-drawn table with two columns and three rows in the center of the image, with a thin arrow drawn between the two columns of each row, like the fat arrow of a match arm. Left column, top to bottom: "Pending", "Shipped", "Cancelled". Right column, top to bottom: "Pack the order", "Notify the customer", "Issue a refund". A small round token labeled "Pending" arrives from the left along an arrow and stops beside the first row. That first row is highlighted with a soft blue accent color wash, and a second arrow leaves the right side of that same row towards a speech bubble on the right that reads "Pack the order". The two other rows stay plain black ink. A small friendly elephant (the PHP mascot) points at the highlighted row like a teacher at a blackboard. Labels: the six table cells exactly as listed, "Pending" on the token, "Pack the order" in the speech bubble.

## ch06-unhandled-case.png

- Chapter: `ch06-02-match.md`, after the sentence saying PHP raises an UnhandledMatchError.
- Idea: a new enum case arrives at a match that has no row for it, and instead of being silently ignored it triggers an error.
- Priority: nice to have.
- Format: landscape.

**Prompt.** The same kind of hand-drawn two-column table as a lookup table, with three rows reading "Pending", "Shipped", "Cancelled" in the left column and a short scribble standing for text in each right cell. Below the last row, a dotted outline of an empty fourth row where a row should be. A small round token labeled "Returned" stands in front of the table, at the level of the empty dotted row, looking lost with a tiny question mark above it. To the right, a small friendly elephant (the PHP mascot) raises a stop sign and blows a whistle, with a small jagged burst above its head. The dotted empty row, the stop sign and the jagged burst are in the blue accent color. Labels: "Pending", "Shipped", "Cancelled" in the table, "Returned" on the token, "UnhandledMatchError" in the jagged burst.

## ch06-nullsafe-chain.png

- Chapter: `ch06-03-match-and-nullsafe.md`, after the paragraph explaining that a chain of ?-> stops at the first null.
- Idea: a property chain is a chain of links; when one link is missing, ?-> hands back a null instead of breaking, and the links after it are never touched.
- Priority: must have.
- Format: landscape.

**Prompt.** A horizontal chain of four large oval links drawn from left to right, like links of a real chain, each with a word written inside: "order", "customer", "address", "city". The third link, "address", is drawn only as a faint dotted outline, as if missing, and the fourth link "city" is greyed out and hangs slightly apart, no longer connected. Between the links, small "?->" symbols are written where they join. From the gap where the third link should be, a short curved arrow drops down to a small empty circle beneath the chain reading "null", drawn softly landing on a tiny cushion. The dotted outline of the missing link, the "?->" symbols and the null circle are in the blue accent color. A small friendly elephant (the PHP mascot) stands at the far right, calmly shrugging. Labels: "order", "customer", "address", "city", "?->", "null".

## ch06-chain-vs-table.png

- Chapter: `ch06-03-match-and-nullsafe.md`, after the paragraph comparing the elseif version and the match version.
- Idea: an if/elseif chain is read one step at a time; a match lays the same decisions flat as a table you can take in at a glance.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A before and after picture in two halves separated by a thin vertical dotted line. Left half: a winding staircase going down, drawn in perspective, with four steps, each step carrying a small diamond-shaped question sign with a short word on it, and a tiny walking figure climbing down the steps one at a time, a little tired. The signs read "US?", "CA?", "FR, DE?", "else". Right half: a flat, tidy table with four rows and two columns, seen straight on, the left column reading "US", "CA", "FR, DE", "default", the right column reading "5", "7.50", "9", "15", with a thin arrow between the two cells of each row, and the same tiny figure standing in front of it, taking the whole table in at one glance, with a small lightbulb above its head. The table frame and the lightbulb are in the blue accent color. Labels: the staircase signs and the table cells exactly as listed, plus "if / elseif" under the staircase and "match" under the table.

---

## ch07-one-key.png

- Chapter: `ch07-00-namespaces-and-composer.md`, at the end of the overview, after the paragraph about `require 'vendor/autoload.php'`.
- Idea: one autoloader line opens both the installed packages and your own classes.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A small friendly elephant (the PHP mascot) stands in the center holding up a single large old-fashioned key. On either side of it, two closed doors drawn side by side, each with a small sign above the frame. The left door has a sign reading "vendor/" and a few cardboard boxes visible through its half-open gap. The right door has a sign reading "src/" and a few sheets of code visible through its gap. A dotted line, drawn in the blue accent color, runs from the key to both keyholes at once. A small tag hangs from the key. Labels: "vendor/autoload.php" on the key tag, "vendor/" and "src/" on the door signs.

## ch07-composer-shopping.png

- Chapter: `ch07-01-hello-composer.md`, after the paragraph explaining `composer.lock`.
- Idea: composer.json is the shopping list, vendor/ is what you bring home, composer.lock is the receipt with exact versions.
- Priority: must have.
- Format: landscape.

**Prompt.** Three objects laid left to right on a plain table, connected by two short arrows. Left: a handwritten shopping list on a torn notebook page, with one item written on it and a checkbox. Middle: a paper shopping bag with a small friendly elephant (the PHP mascot) peeking out of it, and a cardboard box labeled with a tiny package icon inside. Right: a long printed till receipt with a serrated bottom edge, showing one line with a precise version number. The receipt is highlighted in the blue accent color. The arrows read left to right: list to bag, bag to receipt. Labels: "composer.json" under the list, "vendor/" under the bag, "composer.lock" under the receipt, and on the receipt line the text "termwind 2.0.1".

## ch07-require-pile.png

- Chapter: `ch07-02-packages-and-autoloading.md`, after the paragraph about forty classes across a dozen packages.
- Idea: before autoloading, a script starts with a tower of require lines; after, one line does the job.
- Priority: nice to have.
- Format: landscape.

**Prompt.** Two sheets of paper side by side, separated by a thin vertical dotted line, like a before and after. Left sheet: the top half is covered by a tall, teetering stack of identical short lines, each one a small rectangle with the word "require" written in it, piled so high they lean and one is falling off. A small friendly elephant (the PHP mascot) at the bottom of the sheet looks up at the pile, worried. Right sheet: a single line at the top, drawn in the blue accent color, reading "require vendor/autoload.php", and below it plenty of clean empty space with the same elephant relaxed, sitting with a cup of tea. Labels: "before" above the left sheet, "after" above the right sheet, "require" on the stacked rectangles, "require vendor/autoload.php" on the single line.

## ch07-autoloader-librarian.png

- Chapter: `ch07-02-packages-and-autoloading.md`, after the paragraph that walks through the flow of `new Cart()`.
- Idea: the autoloader is a librarian. The program asks for a class by name, the librarian finds the file on the shelf and brings it back.
- Priority: must have.
- Format: landscape.

**Prompt.** A library counter seen from the side. On the left, a small friendly elephant (the PHP mascot) stands in front of the counter with a speech bubble containing only the word "Cart?". Behind the counter, a librarian character with round glasses is turning toward a tall bookshelf on the right, one arm stretched out to pull one file from the shelf. The shelf holds a row of upright folders, each with a small tab on its spine; the one being pulled out is drawn in the blue accent color and its tab reads "Cart.php". A curved arrow, also in blue, runs from the shelf back to the elephant to show the file coming back. Labels: "Cart?" in the speech bubble, "Cart.php" on the pulled folder, "autoloader" on a small sign on the counter.

## ch07-same-first-name.png

- Chapter: `ch07-03-namespaces.md`, in the "Why bother" section, after the two Collection code blocks.
- Idea: two classes can share a short name as long as their namespaces differ, like two people with the same first name and different surnames.
- Priority: must have.
- Format: landscape.

**Prompt.** Two small friendly elephants (the PHP mascot) standing side by side, drawn almost identically, both smiling. Each wears a conference-style name badge pinned to its chest. The left badge reads "Collection" in large letters, with a smaller line underneath reading "App\Models". The right badge also reads "Collection" in large letters, with the smaller line reading "Illuminate\Support". The two smaller lines are drawn in the blue accent color. Above them, a thin curved bracket with a small question mark has been crossed out with a single stroke, to show that there is no confusion. Labels: exactly the four badge texts.

## ch07-leading-backslash.png

- Chapter: `ch07-03-namespaces.md`, in the "Fully qualified names" section, after the explanation of the leading backslash.
- Idea: a bare name is looked up inside the current namespace only, while a name starting with a backslash starts from the root of the tree.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A simple upside-down tree diagram, root at the top, drawn with rounded boxes connected by lines. The root box at the top contains a single backslash character. Below it, one box reading "App". Below "App", two boxes side by side: "Models" on the left and "Services" on the right. Below "Models", a small box reading "Product". A tiny friendly elephant (the PHP mascot) stands inside the "Services" box, looking around. From the elephant, a short dotted arrow in black loops inside the "Services" box and ends at a small empty dotted outline with a question mark, showing that a bare name finds nothing there. A second arrow, drawn in the blue accent color, starts from the elephant, climbs up to the root box, then comes back down through "App" and "Models" to land on "Product". Labels: the box texts, plus "Product" next to the dotted arrow and "\App\Models\Product" next to the blue arrow.

## ch07-use-sticky-note.png

- Chapter: `ch07-04-use-keyword.md`, in the "Basic imports" section, after the paragraph following the first code block.
- Idea: a use statement is a sticky note on the first page of a file, telling PHP what a short name stands for, valid for that file only.
- Priority: must have.
- Format: portrait.

**Prompt.** A single sheet of paper drawn upright, slightly tilted, with a curled corner, standing for one source file. At the top of the sheet, a square sticky note stuck at an angle, drawn in the blue accent color, with handwriting on it reading "Product = App\Models\Product". Below the note, the sheet shows a few lines of code as short wavy lines, and in the middle of them one clearly written line reading "new Product()". Next to the sheet, a second sheet stands slightly behind it, with no sticky note and a small grey question mark, to show that the note does not apply to other files. A small friendly elephant (the PHP mascot) points at the sticky note. Labels: "Product = App\Models\Product" on the note, "new Product()" in the code.

## ch07-mirror-tree.png

- Chapter: `ch07-05-organizing-a-project.md`, after the find command listing the files under src/.
- Idea: the folder tree and the namespace tree are mirror images of each other.
- Priority: must have.
- Format: landscape.

**Prompt.** Two small tree diagrams facing each other across a thin vertical line drawn down the middle of the image, like a reflection in a mirror. Left tree, made of small folder icons and document icons: a folder "src" at the top, two folders below it, "Models" and "Services", and under them documents "Product.php" and "Category.php" on the Models side, "Cart.php" on the Services side. Right tree, made of plain rounded boxes with the same layout: "App" at the top, "Models" and "Services" below, and "Product", "Category" and "Cart" under them. Three short horizontal double-headed arrows, drawn in the blue accent color, connect each document on the left to its box on the right at the same height. The vertical mirror line is drawn as a thin hand-drawn line with a tiny mirror frame at the top. Labels: exactly the folder, file and box names.

## ch07-psr4-mapping.png

- Chapter: `ch07-06-psr4.md`, after the composer.json block with the psr-4 mapping.
- Idea: the PSR-4 rule turns a class name into a file path in three mechanical steps.
- Priority: must have.
- Format: landscape.

**Prompt.** A horizontal conveyor belt running from left to right, with a rounded label tile riding on it and changing shape at each of three stations. Far left, the tile reads "App\Models\Product". Station 1 is a small machine with a pair of scissors on top, and the tile leaving it reads "Models\Product", with a tiny cut-off scrap reading "App\" falling into a bin below. Station 2 is a small machine with a rotating brush, and the tile leaving it reads "Models/Product.php". Station 3 is a small machine with a stamp, and the tile leaving it, at the far right, reads "src/Models/Product.php". The final tile is drawn in the blue accent color. A small friendly elephant (the PHP mascot) operates the last machine. Labels: the four tile texts, plus "App\" on the scrap and "PSR-4" written on the side of the conveyor belt.

---

## ch08-one-array-many-hats.png

- Chapter: `ch08-00-common-collections.md`, after the paragraph saying arrays deserve to be understood once.
- Idea: one PHP array does the work other languages split across several types.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A single Swiss army knife drawn large in the center, handle horizontal, with four blades fanned open upward at different angles. Each blade is a different simple tool shape: a straight blade, a small key, a flat spatula, an index card on a stick. The handle carries the word "array" in hand lettering. A small round friendly elephant (the PHP mascot) stands at the right, holding the knife up proudly with its trunk. The four blades are outlined in the blue accent color. Labels next to each blade: "list", "dictionary", "stack", "record".

## ch08-append.png

- Chapter: `ch08-01-indexed-arrays.md`, in the Appending section, after the explanation of the empty square brackets idiom.
- Idea: appending with empty brackets means "put this in the next free slot", and PHP already knows which slot that is.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A row of four open-top cardboard boxes side by side on a shelf, seen from a three-quarter angle. The first three boxes contain, drawn as small objects, a milk carton, an egg, and a loaf of bread, and each has a small paper tag hanging from its front reading "0", "1", "2". The fourth box on the right is empty, its tag already reads "3", and it is highlighted in the blue accent color. A small round friendly elephant (the PHP mascot) pushes a fifth object, an apple, toward that empty box with its trunk, with a short motion arrow. Above the elephant, a small speech bubble containing only the two characters "[]". Labels: "0", "1", "2", "3", "[]".

## ch08-filter-gaps.png

- Chapter: `ch08-01-indexed-arrays.md`, in the mental model section, right after the array_filter code block.
- Idea: array_filter removes entries but leaves the remaining keys in place; array_values renumbers them.
- Priority: must have.
- Format: landscape.

**Prompt.** Three horizontal rows of small square boxes stacked vertically, connected by two downward arrows on the left side. Top row: five boxes containing "10", "15", "20", "25", "30", each with a small key tag above it reading "0", "1", "2", "3", "4". Middle row: the same five positions, but the boxes at positions 1 and 3 are only dotted empty outlines with no tag, while "10", "20", "30" remain in place with their tags still reading "0", "2", "4". Bottom row: three boxes "10", "20", "30" pushed together with fresh tags "0", "1", "2". The key tags are in the blue accent color; the dotted empty outlines are also blue. The first downward arrow, between the top and middle rows, is labeled "array_filter". The second arrow, between the middle and bottom rows, is labeled "array_values". Labels: the numbers in the boxes, the tag numbers, "array_filter", "array_values".

## ch08-bytes-vs-chars.png

- Chapter: `ch08-02-strings.md`, in the bytes versus characters section, right after the strlen and mb_strlen code block.
- Idea: the same word is four characters but five bytes; strlen counts one thing and mb_strlen the other.
- Priority: must have.
- Format: landscape.

**Prompt.** The word "café" written large as four separate letter tiles in a row, like board game tiles: "c", "a", "f", "é". Directly under the tiles, a horizontal ruler-like strip divided into five equal cells, aligned so that the first three tiles each sit over one cell and the tile "é" sits over two cells. The two cells under "é" are filled in the blue accent color. Above the tiles, a curly bracket spanning all four with a small hand-written note "4 characters" and next to it the word "mb_strlen". Below the strip, a curly bracket spanning all five cells with the note "5 bytes" and next to it the word "strlen". Nothing else. Labels: "café" on the tiles, "4 characters", "mb_strlen", "5 bytes", "strlen".

## ch08-sprintf-template.png

- Chapter: `ch08-02-strings.md`, in the everyday string functions section, after the paragraph explaining sprintf.
- Idea: sprintf is a fill-in-the-blank form: a template with slots, and values that drop into them in order.
- Priority: optional.
- Format: landscape.

**Prompt.** A single sheet of paper drawn like a form, with one sentence hand-lettered on it: a short blank line, then the words "scored", then a second short blank line, then "on the test". Above the sheet, two small tags float in the air, drawn in the blue accent color, one reading "Alice" and the other reading "92", each with a curved arrow dropping toward its blank: "Alice" toward the first blank, "92" toward the second. Below the sheet, a second smaller sheet shows the finished sentence "Alice scored 92 on the test". Labels: "Alice", "92", "scored", "on the test".

## ch08-array-shelf.png

- Chapter: `ch08-03-associative-arrays.md`, right after the first code block with the prices array.
- Idea: an associative array is the same shelf of boxes as an indexed array, with word tags instead of numbers.
- Priority: must have.
- Format: landscape.

**Prompt.** Two identical wooden shelves drawn one above the other, each holding three open-top boxes seen from the front. On the top shelf, each box has a paper tag reading "0", "1", "2", and the boxes contain a small drawing of an apple, a banana, and a cherry. On the bottom shelf, the boxes contain a small price sign reading "0.50", "0.30", "3.20", and their tags read "apple", "banana", "cherry". All six tags are in the blue accent color. Between the two shelves, a small equals sign drawn by hand, to say the two are the same structure. Labels: "0", "1", "2", "apple", "banana", "cherry", "0.50", "0.30", "3.20".

## ch08-isset-drawers.png

- Chapter: `ch08-03-associative-arrays.md`, in the isset versus array_key_exists section, after the paragraph with the drawer analogy.
- Idea: isset looks inside the drawer and says no when it is empty; array_key_exists only reads the label and says yes.
- Priority: must have.
- Format: landscape.

**Prompt.** A small two-drawer filing cabinet drawn in the center, both drawers pulled open. The top drawer has a label reading "name" and contains a small card reading "Alice". The bottom drawer has a label reading "nickname" and is visibly empty inside, with a tiny "null" written in light strokes at the bottom of the drawer. On the left, a small round friendly elephant (the PHP mascot) wearing round glasses leans in and peers inside the empty bottom drawer, with a speech bubble reading "no". On the right, a second identical elephant only looks at the label of the same bottom drawer from a distance, with a speech bubble reading "yes". The two speech bubbles are in the blue accent color. Under the left elephant the word "isset", under the right elephant the words "array_key_exists". Labels: "name", "Alice", "nickname", "null", "no", "yes", "isset", "array_key_exists".

## ch08-list-of-records.png

- Chapter: `ch08-03-associative-arrays.md`, in the nesting section, right after the books code block.
- Idea: a list of records is an indexed array on the outside and an associative array inside each element.
- Priority: nice to have.
- Format: landscape.

**Prompt.** An open card index box seen from a three-quarter angle, with three index cards standing upright in it, slightly fanned so each is visible. Each card has a small numbered tab on its top edge reading "0", "1", "2". Every card shows the same three short lines, each line starting with a small hand-written field name followed by a short squiggle standing for the value: "title", "author", "year". The numbered tabs are in the blue accent color. Nothing else in the image. Labels: "0", "1", "2", "title", "author", "year".

---

## ch09-two-families.png

- Chapter: `ch09-00-error-handling.md`, after the paragraph saying PHP draws a sharp line between two kinds of trouble.
- Idea: an Error means the code is broken and must be fixed; an exception means someone has a decision to make.
- Priority: must have.
- Format: landscape.

**Prompt.** Two scenes side by side, separated by a thin vertical dotted line. Left: a small friendly elephant (the PHP mascot) holding up a gear with a visible crack and a broken tooth, next to a wrench lying on the ground, with a small speech bubble containing an exclamation mark. Right: the same elephant standing at a fork in a road, in front of a signpost with two arms pointing in different directions, one hand on its chin, with a small speech bubble containing a question mark. The cracked gear and the signpost are in the blue accent color. Labels: "Error" and "fix the code" on the left, "Exception" and "decide" on the right.

## ch09-catch-eats-evidence.png

- Chapter: `ch09-01-fatal-errors.md`, after the paragraph about the catch block eating the only evidence.
- Idea: a broad catch block hides a bug; months later there is nothing left to investigate.
- Priority: nice to have.
- Format: landscape.

**Prompt.** Two panels side by side like a comic strip. Left panel: a round, wide-mouthed creature shaped like a pair of curly braces, swallowing a small torn sheet of paper on which a few wavy lines and a large exclamation mark are written, crumbs falling from its mouth. Right panel: a small calendar on the wall showing many crossed-out days, and a puzzled person on their knees searching a completely empty floor with a magnifying glass, a few drops of sweat around their head. The swallowed sheet of paper is in the blue accent color. Labels: "catch" on the creature, "6 months later" above the right panel.

## ch09-exception-climbs.png

- Chapter: `ch09-02-exceptions.md`, right after the paragraph explaining that control jumps to the nearest matching catch.
- Idea: an exception travels up the call stack, floor by floor, abandoning each function on the way, until something catches it.
- Priority: must have.
- Format: portrait.

**Prompt.** A simple three-storey building drawn in cross-section, like a dollhouse, each floor a rectangle stacked on the previous one. Ground floor: a small friendly elephant (the PHP mascot) pointing at a burst pipe with a puddle, and a small tag on the wall reading "readConfig()". Middle floor: an empty desk with a chair pushed back and a cup left behind, tag reading "the caller". Top floor: a person holding a large open net, catching a small round alarm bell that is rising, tag reading "catch". A dotted arrow in the blue accent color starts at the burst pipe on the ground floor, rises straight through a hole in each ceiling, passing the middle floor without stopping, and ends in the net on the top floor. The bell and the arrow are in the blue accent color. Above the roof, a tiny faded arrow continuing upward with a small cross on it, meaning nobody caught it. Labels: "readConfig()", "the caller", "catch".

## ch09-throwable-tree.png

- Chapter: `ch09-02-exceptions.md`, in the Exception versus Error section, before the paragraph describing the two branches.
- Idea: Throwable is one interface with two parallel branches, Exception for what you can recover from, Error for bugs.
- Priority: must have.
- Format: landscape.

**Prompt.** A small tree seen from the side, drawn simply. The trunk carries a wooden sign reading "Throwable". The trunk splits into exactly two thick branches. The left branch carries a sign reading "Exception" and has three leaves, each a small rounded label: "RuntimeException", "InvalidArgumentException", "JsonException". The right branch carries a sign reading "Error" and has two leaves: "TypeError", "DivisionByZeroError". A small friendly elephant (the PHP mascot) sits at the foot of the tree looking up. The left branch and its leaves are in the blue accent color, the right branch stays black. Labels: exactly the sign and leaf texts.

## ch09-three-roads.png

- Chapter: `ch09-03-to-throw-or-not-to-throw.md`, in the decision order section, before the numbered list.
- Idea: three outcomes, three answers: a normal case returns null, a broken precondition throws, a bug is left to crash.
- Priority: must have.
- Format: landscape.

**Prompt.** A single wooden signpost standing where a path splits into three, seen slightly from the front, with three arms pointing left, straight ahead and right. Each arm has a small icon next to it. Left arm: an empty box with an open lid, and the arm reads "return null". Middle arm: a hand tearing a small contract in two, and the arm reads "throw". Right arm: a small explosion cloud with a wrench in it, and the arm reads "let it crash". Above each arm, a tiny caption: "normal case" on the left, "broken promise" in the middle, "a bug" on the right. A small friendly elephant (the PHP mascot) stands in front of the signpost, looking up at it. The three arms of the signpost are in the blue accent color. Labels: "return null", "throw", "let it crash", "normal case", "broken promise", "a bug".

---

## ch10-request-response.png

- Chapter: `ch10-00-web-development-basics.md`, after the opening paragraph.
- Idea: on the web, the input is an HTTP request and the output is an HTML page. The script in the middle is ordinary PHP.
- Priority: must have.
- Format: landscape.

**Prompt.** A horizontal round trip drawn left to right and back. Left: a laptop with a browser window on its screen, the address bar showing a short URL. From the laptop, a long arrow curves along the top of the image to the right, carrying a small envelope with a tiny form drawn on it, two input lines and a button. Right: a small friendly elephant (the PHP mascot) standing at a desk, holding a sheet of paper with a few lines of code, reading the envelope. From the elephant, a second arrow curves back along the bottom of the image to the laptop, carrying a sheet of paper drawn as a web page with a heading and a few lines of text. Both arrows are drawn in the blue accent color. Labels: "request" above the top arrow, "response" below the bottom arrow, "PHP" on the desk.

## ch10-get-vs-post.png

- Chapter: `ch10-01-forms-and-superglobals.md`, after the paragraph comparing GET and POST.
- Idea: a GET request writes its data on the outside, in the URL, where everyone can read it. A POST request carries its data inside the body.
- Priority: nice to have.
- Format: landscape.

**Prompt.** Two paper envelopes side by side, drawn large, seen from the front. Left envelope: the address line on the front reads "/guestbook?name=Alice", written in plain view, and a small eye is drawn next to it, looking at the text. Right envelope: the address line on the front reads only "/guestbook", and the flap is slightly open showing a folded letter inside with "name=Alice" written on it, half hidden. The visible data on the left envelope and the folded letter on the right are in the blue accent color. Labels: "GET" above the left envelope, "POST" above the right envelope.

## ch10-form-submission.png

- Chapter: `ch10-01-forms-and-superglobals.md`, in the superglobals section, after the paragraph on $_POST, $_GET and $_SERVER.
- Idea: a submitted form travels as a request body, and PHP unpacks it into the $_POST array before the script starts.
- Priority: must have.
- Format: landscape.

**Prompt.** Three stages left to right, connected by arrows. Left: a simple web form drawn as a small window with two fields, the first filled with "Alice" and the second with "Hello", and a button below. Middle: an envelope in flight along the arrow, with a strip of text on it reading "name=Alice&message=Hello". Right: a small friendly elephant (the PHP mascot) opening the envelope and placing its contents into a cardboard box with two labeled compartments, the first compartment holding "Alice" and the second holding "Hello". The box is labeled "$_POST" on the front. The box and its label are in the blue accent color. Labels: "name" and "message" on the two compartments, "$_POST" on the box, "name=Alice&message=Hello" on the envelope.

## ch10-escaping.png

- Chapter: `ch10-02-validation-and-xss.md`, in the escaping section, right after the code block with htmlspecialchars().
- Idea: raw text is read by the browser as markup; escaped text is displayed as the characters themselves.
- Priority: must have.
- Format: landscape.

**Prompt.** Two horizontal rows, one above the other, separated by a thin dotted line. Top row: on the left a small tile reading "<b>hi</b>", an arrow pointing right directly to a browser window on the right that displays the word "hi" in heavy bold letters, with a small worried face drawn next to the browser. Bottom row: on the left the same tile reading "<b>hi</b>", an arrow pointing right that passes through a small machine drawn as a rounded box labeled "htmlspecialchars()", out of which comes a tile reading "&lt;b&gt;hi&lt;/b&gt;", then an arrow to a browser window that displays the literal text "<b>hi</b>" in plain letters, with a small relieved face next to it. The machine and the escaped tile are in the blue accent color. Labels: "<b>hi</b>", "htmlspecialchars()", "&lt;b&gt;hi&lt;/b&gt;", "raw" next to the top row, "escaped" next to the bottom row.

## ch10-validate-escape.png

- Chapter: `ch10-02-validation-and-xss.md`, in the validation section, after the paragraph explaining trim, mb_strlen and the errors array.
- Idea: validation guards the input door, escaping guards the output door. Two separate jobs, two separate places.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A simple house drawn in the center of the image, seen from the front, with a door on its left wall and a door on its right wall. Above the house a small sign reads "PHP". At the left door stands a small friendly elephant (the PHP mascot) in a doorman's cap, holding a clipboard, checking a queue of small tiles waiting to come in; one tile reading "Alice" is waved in, and one very long tile that does not fit through the door is turned away with a polite hand gesture. At the right door, a second copy of the elephant wraps each tile leaving the house in a protective bubble before it heads toward a browser window drawn at the right edge. The clipboard and the protective bubbles are in the blue accent color. Labels: "validate" above the left door, "escape" above the right door, "browser" under the browser window.

## ch10-prepared-statement.png

- Chapter: `ch10-03-talking-to-a-database.md`, in the prepared statements section, just before the code block.
- Idea: the query's shape is sent first with empty slots, the values arrive separately and can never be read as SQL.
- Priority: must have.
- Format: landscape.

**Prompt.** Two numbered steps drawn left to right, with a database drawn as a stack of three cylinders on the right side of the image. Step 1, top half: a small friendly elephant (the PHP mascot) hands the database a rigid stencil card reading "INSERT ... VALUES (:name, :message)", with two empty rectangular cut-outs where the two placeholders are, like a form with blank slots. Step 2, bottom half: the same elephant hands the database two small sealed envelopes, one labeled "Alice" and one labeled "Hello", and the database is dropping each envelope into its matching slot in the stencil card. The two empty slots and the two envelopes are in the blue accent color. Labels: "1. the query" above the stencil, "2. the values" above the envelopes, ":name" and ":message" next to the slots.

---

## ch11-shape-vs-borrow.png

- Chapter: `ch11-00-interfaces-and-traits.md`, after the paragraph "One is a shape you agree to fit. The other is a piece of code you borrow."
- Idea: an interface is a shape that many different things can fit; a trait is a page of code copied into unrelated classes.
- Priority: must have.
- Format: landscape.

**Prompt.** Two scenes side by side, separated by a thin vertical dotted line. Left scene: a flat board standing upright with a single star-shaped hole cut out of it, and three very different objects lined up in front of it (a mug, a book, a toy car), each with a small star-shaped peg on its front that matches the hole exactly. One of them is halfway through the hole. The cut-out hole is drawn in the blue accent color. Right scene: a small friendly elephant (the PHP mascot) holding a glue stick, pasting a photocopied sheet of paper with a few code lines drawn as wavy strokes into an open binder, while an identical sheet is already glued into a second, different-looking binder next to it. The two pasted sheets are drawn in the blue accent color. Labels: "interface" under the left scene, "trait" under the right scene.

## ch11-interface-socket.png

- Chapter: `ch11-01-interfaces.md`, in the "Why bother: programming against the interface" section, after the paragraph explaining that printSummary() never changes.
- Idea: a function typed against an interface is a wall socket: it only cares about the shape of the plug, not what is behind it.
- Priority: must have.
- Format: landscape.

**Prompt.** On the right, a single wall socket drawn on a plain wall, large and simple, with a small sign above it. On the left, three very different devices, drawn simply: a desk lamp, a laptop, and an electric kettle. Each device has a cord ending in exactly the same two-pin plug, and all three cords converge toward the one socket. The plugs and the socket opening are drawn in the blue accent color, so the eye sees at once that the shape is what matches. Small tags hang from each cord. Labels: "Formattable" on the sign above the socket, "InvoiceLine", "Refund" and "ShippingFee" on the three tags.

## ch11-trait-paste.png

- Chapter: `ch11-02-php-traits.md`, after the paragraph explaining that both classes now have log(), getLog() and $log without having written them.
- Idea: a trait is code pasted into unrelated classes; they share the code but stay unrelated.
- Priority: nice to have.
- Format: landscape.

**Prompt.** Two large rectangular boxes side by side, drawn like two open file folders standing upright, clearly different from each other: the left one has a small coin icon on its tab, the right one a small bar chart icon on its tab. Between and slightly above them, a small friendly elephant (the PHP mascot) holds a glue stick in its trunk. Inside each folder, the same small sheet of paper is glued at the same spot, showing three short wavy lines of code, with a tiny heading. The two glued sheets and the glue stick are drawn in the blue accent color. No arrow, no line, nothing connecting the two folders to each other. Labels: "PaymentProcessor" on the left tab, "ReportGenerator" on the right tab, "log()" as the heading of both sheets.

## ch11-two-checkpoints.png

- Chapter: `ch11-03-generic-style-code.md`, in "The workaround" section, after the paragraph explaining that PHPStan flags a mismatch that PHP itself ignores.
- Idea: the docblock is checked by a separate program before shipping; PHP itself never checks it at runtime.
- Priority: must have.
- Format: landscape.

**Prompt.** A horizontal conveyor belt runs from left to right across the whole image, carrying small boxes toward a door at the far right marked with a tiny rocket. Along the belt, two checkpoints drawn as simple gates. At the first gate, on the left, a stern inspector with round glasses holds a clipboard and reads a sign posted on the gate; the inspector stops a banana sitting on the belt with an open hand, while boxes drawn with a small product tag pass through. The sign on the gate and the stopped banana are drawn in the blue accent color. At the second gate, closer to the door, a small friendly elephant (the PHP mascot) sits relaxed with its eyes closed and lifts the barrier for everything, boxes and all. Labels: "PHPStan" on the first gate, "@param Product[]" on the sign the inspector reads, "php" on the second gate.

---

## ch12-tireless-checker.png

- Chapter: `ch12-00-testing.md`, after the paragraph defining an automated test.
- Idea: a human cannot keep "what might have broken" in their head; a test runs the same check for the thousandth time without tiring.
- Priority: must have.
- Format: landscape.

**Prompt.** Two scenes side by side, separated by a thin vertical dotted line. Left: a person sitting at a laptop with a worried face, surrounded by four or five small thought bubbles, each containing a tiny question mark and a small broken-looking object (a cracked gear, a torn page, a wobbly box). Right: a small friendly elephant (the PHP mascot) standing calmly at a clipboard, ticking boxes on a short checklist with a pencil, every box already checked; a small counter above the clipboard shows the number 1000. The check marks and the counter are in the blue accent color. Labels: "what did I break?" over the left scene, "run 1000" on the counter.

## ch12-test-scale.png

- Chapter: `ch12-01-writing-tests.md`, after the "try it" paragraph in "Your first test".
- Idea: an assertion puts what you expected and what you got on the two pans of a scale; the test passes when they balance.
- Priority: must have.
- Format: landscape.

**Prompt.** A classic two-pan balance scale drawn in the center, perfectly level. On the left pan, a solid hand-lettered number 56. On the right pan, a small rectangle drawn 8 wide and 7 tall, with a tiny "8" along its top edge and a tiny "7" along its side. Below the scale, a small friendly elephant (the PHP mascot) looks up at it and gives a thumbs up with its trunk curled. A large check mark in the blue accent color floats above the scale. Labels: "expected" under the left pan, "actual" under the right pan.

## ch12-equals-vs-same.png

- Chapter: `ch12-01-writing-tests.md`, in the assertions section, after the paragraph comparing assertEquals to == and assertSame to ===.
- Idea: assertEquals accepts a number and a text that look alike; assertSame checks the type too and stops the text.
- Priority: must have.
- Format: landscape.

**Prompt.** Two small garden gates side by side, each with a sign on top and a gatekeeper elephant (the PHP mascot) standing next to it. Approaching each gate from the left are the same two travelers: a solid bold number 1, and a small square letter tile showing 1 between two quotation marks, like a tile from a board game. Left gate: both travelers have passed through and stand happily on the far side, gate wide open. Right gate: the bold number 1 has passed through, but the elephant holds up its trunk like a stop sign in front of the quoted tile, which stays outside with a small sweat drop. The stop gesture and the two gate signs are in the blue accent color. Labels: "assertEquals" on the left sign, "assertSame" on the right sign.

## ch12-filter-funnel.png

- Chapter: `ch12-02-running-tests.md`, at the end of the "Filtering by name" section.
- Idea: the suite holds hundreds of tests, and filter and group let only the ones you care about through.
- Priority: nice to have.
- Format: portrait.

**Prompt.** A tall funnel drawn in the center of the image. Above it, a big loose heap of small paper sheets pouring in, each sheet with a few scribbled lines and a tiny check mark, standing for test files. On the side of the funnel, two thin horizontal sieves are drawn inside it, one below the other, each with a small tag. At the narrow bottom of the funnel, only two sheets drop out onto a small terminal window that shows two dots. The two sieves and the two surviving sheets are in the blue accent color. Labels: "filter" on the upper sieve tag, "group" on the lower sieve tag.

## ch12-mirror-tree.png

- Chapter: `ch12-03-test-organization.md`, right after the directory listing at the top.
- Idea: the tests folder is a mirror image of the src folder, every class has a twin test class with a Test suffix.
- Priority: must have.
- Format: landscape.

**Prompt.** Two simple folder trees drawn facing each other, like an object and its reflection across a vertical dotted line in the middle. Left tree: a folder icon at the top, with two file icons hanging below it. Right tree: a folder icon at the top with two file icons in the exact same positions. Thin dashed lines in the blue accent color connect each left file to its twin on the right, crossing the mirror line horizontally. The right-hand file icons each carry a small tag with the word Test. A small friendly elephant (the PHP mascot) stands at the bottom holding a hand mirror. Labels: "src" on the left folder, "tests" on the right folder, "Rectangle" on the first left file, "RectangleTest" on the first right file.

## ch12-unit-vs-integration.png

- Chapter: `ch12-03-test-organization.md`, after the paragraph defining an integration test.
- Idea: a unit test checks one piece alone and is fast; an integration test checks pieces working together with real external things and is slower.
- Priority: must have.
- Format: landscape.

**Prompt.** Two scenes side by side, separated by a thin vertical dotted line. Left: a single gear sitting alone on a small workbench, with a magnifying glass over it and a stopwatch next to it whose hand has barely moved. Right: three gears meshed together, one of them connected by a short cable to a small database cylinder and another to a sheet of paper standing for a file, with a stopwatch next to them whose hand has gone most of the way around. The stopwatch hands and the cables are in the blue accent color. A small friendly elephant (the PHP mascot) peeks in from the bottom between the two scenes. Labels: "unit" under the left scene, "integration" under the right scene.

---

## ch13-two-ways.png

- Chapter: `ch13-00-debugging.md`, after the sentence announcing two ways to look inside a running program.
- Idea: print debugging is a flashlight pointed at one suspected spot; step debugging is a pause button that freezes the whole program so you can read everything.
- Priority: must have.
- Format: landscape.

**Prompt.** Two scenes side by side, separated by a thin vertical dotted line. Left: a dark corridor drawn as a tall stack of horizontal lines of code, mostly left blank and unlit. A small friendly elephant (the PHP mascot) holds a flashlight whose cone of light, drawn in the blue accent color, lights exactly one line of code, on which a small tag reads 42. Everything outside the cone stays plain. Right: the same elephant stands in front of a large round pause button (two vertical bars) drawn in the blue accent color, with its trunk pressing the button. Next to it, a strip of code lines like a film strip, with one line frozen mid-way and a small magnifying glass hovering over a little panel listing three short variable lines. Labels: "print" under the left scene, "pause" under the right scene.

## ch13-echo-vs-var-dump.png

- Chapter: `ch13-01-print-debugging.md`, after the bold sentence about the wrong type versus the wrong contents.
- Idea: echo prints the number 5 and the text "5" the same way; var_dump shows the type and makes the difference visible.
- Priority: must have.
- Format: landscape.

**Prompt.** A two-row comparison table drawn by hand, with no ruled grid, just generous spacing. On the far left, two input values stacked vertically: on the top row a bold solid number 5, on the bottom row a small square letter tile showing 5 between an opening and a closing quotation mark. In the middle column, headed by a small tag reading echo, both rows show exactly the same plain output, the character 5, with a small puzzled face and a question mark between them to show they cannot be told apart. In the right column, headed by a small tag reading var_dump, the top row shows int(5) and the bottom row shows string(1) "5", the two answers clearly different, circled in the blue accent color. A tiny friendly elephant at the bottom right points at the circled answers. Labels: "echo", "var_dump", "int(5)", "string(1) "5"".

## ch13-breakpoint.png

- Chapter: `ch13-02-xdebug.md`, in "Connecting an editor", after the bold sentence saying execution stops before running the marked line.
- Idea: at a breakpoint the program is frozen between the lines already run and the line about to run, and every variable can be read at that instant.
- Priority: must have.
- Format: landscape.

**Prompt.** On the left, an editor window drawn as a simple rounded rectangle containing seven short horizontal lines standing for lines of code, with a narrow margin to their left. The first three lines are drawn with a faint check mark in the margin, meaning they have already run. The fourth line has a solid round dot in the margin, drawn in the blue accent color, and a small arrow in the same blue pointing at that line from the left. The lines below the fourth are drawn lighter, still to come. On the right, a smaller panel drawn like a sticky note, showing three short variable lines: name = "", errors = [ ], and a third line of wavy text. A thin line connects the blue dot to the sticky note. A small friendly elephant sits at the bottom, looking at the note through a magnifying glass. Labels: "breakpoint" next to the dot, "variables" at the top of the sticky note.

## ch13-step-over-into-out.png

- Chapter: `ch13-02-xdebug.md`, after the paragraph describing step over, step into and step out.
- Idea: the three moves of a step debugger are three routes through the same code: jump to the next line, descend inside the function call, climb back to the caller.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A single simple diagram. In the center, a vertical column of four short horizontal lines standing for lines of code in a main script; the second line ends with a small box labeled f( ), a function call. To the right of that box, a smaller indented column of three short lines standing for the inside of the function, connected to the box by a thin bracket. Three curved arrows drawn in the blue accent color: the first hops from the second main line straight down to the third main line, passing over the function box, labeled "over"; the second leaves the function box and dives into the first line of the indented column, labeled "into"; the third starts at the last line of the indented column and climbs back up and left to the third main line, labeled "out". Plenty of white space, nothing else. Labels: "over", "into", "out", "f( )".

---

## ch14-phpgrep.png

- Chapter: `ch14-00-a-cli-project.md`, after the opening paragraph that names phpgrep.
- Idea: phpgrep takes a file and a word, and gives back only the lines that contain the word.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A small friendly elephant (the PHP mascot) standing on the left, holding a large magnifying glass over a sheet of paper in the center. The sheet shows six short wavy lines standing for text. Two of those lines are highlighted with a soft blue marker stroke, and inside each highlighted line one small word is drawn slightly darker, as if it were the word being searched. To the right of the sheet, an arrow points to a small terminal window showing exactly two lines, the same two highlighted lines, copied out. The magnifying glass rim and the two highlighted lines are in the blue accent color. Labels: "apple" written on a small tag hanging from the magnifying glass, "phpgrep" written above the terminal window.

## ch14-argv-slots.png

- Chapter: `ch14-01-accepting-command-line-arguments.md`, right after the var_dump console output.
- Idea: every word typed after php lands in a numbered slot of $argv, and slot 0 is the script name, not the first argument.
- Priority: must have.
- Format: landscape.

**Prompt.** At the top, a command line hand-lettered in a monospace style: "php phpgrep.php apple fruits.txt". Below it, a row of three open boxes drawn side by side like compartments of a tray, each with a small number tag on its front: 0, 1, 2. Three curved arrows drop from the command line into the boxes: "phpgrep.php" falls into box 0, "apple" into box 1, "fruits.txt" into box 2. The word "php" at the start of the command line has no arrow and is slightly grayed, with a tiny crossed-out mark under it. The three arrows are in the blue accent color. The box 0 has a small hand-written note beside it. Labels: "$argv" written above the row of boxes, "0", "1", "2" on the boxes, "the script itself" as the note next to box 0.

## ch14-file-to-lines.png

- Chapter: `ch14-02-reading-a-file.md`, after the file() code snippet.
- Idea: file() cuts a file into one string per line, and str_contains() then keeps only the lines holding the word.
- Priority: must have.
- Format: landscape.

**Prompt.** A left-to-right flow in three stages. Left: a single sheet of paper with four short wavy lines of text. A thick arrow points right into a small box shaped like a paper shredder with a wide slot. Out of the shredder, in the middle, come four separate horizontal strips of paper stacked vertically, each carrying one of the wavy lines. A second arrow points right into a round kitchen sieve drawn from the side. Out of the sieve, on the right, only one strip comes through and lands in a small tray; the three other strips are drawn falling below the sieve. The strip that passes and the two arrows are in the blue accent color. Labels: "file()" on the shredder, "str_contains()" on the sieve, "matches" on the tray.

## ch14-locked-door.png

- Chapter: `ch14-02-reading-a-file.md`, in "The file that isn't there", after the paragraph on the limits of file_exists().
- Idea: file_exists() only checks that something is there; is_readable() also checks that you may open it.
- Priority: nice to have.
- Format: landscape.

**Prompt.** Two front doors side by side on a plain wall, each with a small name plate. The left door is missing entirely: only an empty door frame with nothing inside it, and a small question mark floating where the door should be. The right door is present and solid, but a large padlock hangs on it and a chain runs across it. In front of the doors, a small friendly elephant (the PHP mascot) looks at the two doors with a puzzled expression. Two thin check marks are drawn under the doors: under the left door a single check mark labeled file_exists with a cross next to it; under the right door two check marks. The padlock and chain are in the blue accent color. Labels: "missing" on the left name plate, "no permission" on the right name plate, "file_exists()" under the left door, "is_readable()" under the right door.

## ch14-split.png

- Chapter: `ch14-03-improving-error-handling-and-modularity.md`, after the opening paragraph.
- Idea: before, one long script does everything; after, three small files do the work and a thin entry script only wires them together.
- Priority: must have.
- Format: landscape.

**Prompt.** A before and after split by a thin vertical dotted line. Left half: one tall sheet of paper covered from top to bottom with dense wavy lines of code, slightly curling at the bottom as if too long, with a small tired face drawn on it. Right half: a small folder drawn open, containing three short sheets of paper side by side, each with only a few wavy lines. Above the folder, a fourth, very short sheet with three lines and three small arrows from it going down to the three sheets in the folder, like plugs connecting to sockets. The three arrows and the folder outline are in the blue accent color. Labels: "before" above the left half, "after" above the right half, "phpgrep.php" on the short top sheet, "src/" on the folder tab, and "GrepOptions", "search", "FileNotFoundException" on the three small sheets.

## ch14-red-green.png

- Chapter: `ch14-04-testing-the-librarys-functionality.md`, after the paragraph explaining the first red run.
- Idea: test-driven development is a loop: write a failing test, write just enough code to pass it, tidy up, repeat.
- Priority: must have.
- Format: landscape.

**Prompt.** Three simple icons arranged in a triangle, connected by curved arrows forming a clockwise loop. Top: a small traffic light with only its top lamp lit, drawn with an X inside it, next to a tiny sheet of paper with a check-list. Bottom right: the same traffic light with only its bottom lamp lit, drawn with a check mark inside it, next to a small sheet with a few lines of code. Bottom left: a broom sweeping a few loose bits of code into a neat pile. The lit bottom lamp of the green light and the three arrows are in the blue accent color; the top lamp is drawn in black ink only. Labels next to each icon: "red", "green", "refactor".

## ch14-env-sticky-note.png

- Chapter: `ch14-05-working-with-environment-variables.md`, after the paragraph explaining why an environment variable rather than a third argument.
- Idea: an environment variable is set once for the shell session, and every command run afterward inherits it.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A large terminal window drawn as a rounded rectangle with a thin title bar. A square sticky note is stuck on the top right corner of the window frame, slightly tilted, with one short line hand-written on it. Inside the window, three prompt lines one below the other, each starting with a dollar sign and followed by a short command, and next to each command a tiny round smiling face looking up toward the sticky note, with a thin dotted line of sight from each face to the note. The sticky note is in the blue accent color. Labels: "PHPGREP_IGNORE_CASE=1" on the sticky note, and "php phpgrep.php" as the command on each of the three prompt lines.

## ch14-two-streams.png

- Chapter: `ch14-06-writing-to-stderr.md`, after the paragraph describing the error line landing in results.txt.
- Idea: a program has two output streams. STDOUT can be redirected into a file; STDERR keeps going to the screen. They never mix.
- Priority: must have.
- Format: landscape.

**Prompt.** In the center left, a small box representing a program, with a small friendly elephant (the PHP mascot) peeking out of it. Two pipes leave the box toward the right, one above the other, drawn like plumbing with a slight bend. The upper pipe ends in a document icon, a sheet of paper with a few clean wavy lines, and a tap or valve is drawn on this pipe just before the sheet. The lower pipe ends in a monitor screen showing one short line with a small warning triangle next to it. The two pipes are clearly separate and never cross. The upper pipe is in the blue accent color, the lower pipe in black ink. Labels: "STDOUT" on the upper pipe, "STDERR" on the lower pipe, "results.txt" under the sheet, ">" written on the valve.

---

## ch15-use-copy-vs-ref.png

- Chapter: `ch15-01-closures.md`, after the explanation of the `makeCounter()` example, before the "try it" paragraph.
- Idea: `use ($x)` gives the closure a photograph of the value; `use (&$x)` ties the closure to the original box.
- Priority: must have.
- Format: landscape.

**Prompt.** Two panels side by side, separated by a thin vertical dotted line. In both panels, on the left, the same cardboard box with its lid open and a paper label reading "$x", with the number 2 sitting inside. Left panel: a small friendly elephant (the PHP mascot) walks away to the right, holding up a Polaroid photograph that shows the same box with the 2 inside; the photograph is drawn in the blue accent color. Right panel: the same elephant stands at a distance on the right and holds one end of a rope whose other end is tied around the box; the rope is drawn in the blue accent color. Nothing else in the image. Labels: "use ($x)" above the left panel, "use (&$x)" above the right panel, "a copy" under the photograph, "the same box" under the rope.

## ch15-array-vs-generator.png

- Chapter: `ch15-02-generators.md`, right after the paragraph explaining that a function containing `yield` does not run its body when called.
- Idea: an array function bakes every loaf before handing over the tray; a generator hands one loaf at a time, on request.
- Priority: must have.
- Format: landscape.

**Prompt.** Two horizontal scenes stacked one above the other, separated by a thin dotted line, each showing a bakery counter with a small friendly elephant (the PHP mascot) as the baker on the left and a customer on the right. Top scene: the elephant pushes a huge tray stacked with a dozen loaves across the counter all at once, the customer waits with arms crossed, a small clock hangs on the wall behind. Bottom scene: the elephant hands a single loaf across the counter, one more loaf sits in a small oven behind it, and the customer's speech bubble contains a short word; the single loaf being handed over and the speech bubble are drawn in the blue accent color. Labels: "array" on the top scene, "generator" on the bottom scene, "next?" inside the speech bubble.

## ch15-yield-bookmark.png

- Chapter: `ch15-02-generators.md`, in "Watching the laziness happen", after the paragraph that walks through the order of the console output.
- Idea: `yield` hands a value out and leaves a bookmark in the function; the next request reopens the function at the bookmark.
- Priority: nice to have.
- Format: landscape.

**Prompt.** An open book in the center of the image standing for a function, its two pages covered with short wavy lines standing for code, with one line in the middle of the right page written out as the word "yield". A ribbon bookmark, drawn in the blue accent color, sticks out of the book exactly at that line. From the "yield" line, an arrow points right to a small square tile bearing the number "1", which is being received by a hand reaching in from the right edge of the image. Below, a second arrow drawn in the blue accent color curves from that hand back to the bookmark. Generous white space around the book. Labels: "yield" on the page, "1" on the tile, "next" along the returning arrow.

## ch15-grep-stream.png

- Chapter: `ch15-03-improving-our-cli-project.md`, right after the `searchLines()` code block.
- Idea: before, the whole file and every match are loaded at once and the screen stays blank; after, lines flow one at a time through the function to the screen and memory holds a single line.
- Priority: must have.
- Format: landscape.

**Prompt.** Two horizontal scenes stacked one above the other, separated by a thin dotted line. Top scene: a very tall document, taller than the small friendly elephant (the PHP mascot) standing next to it, is being lifted whole into a cardboard box labeled "memory" that bulges and strains at the seams; beside the box, a tall stack of paper strips grows upward; on the far right, a computer screen is completely blank. Bottom scene: the same tall document lies flat on the left, a single paper strip is drawn out of it like a thread, passes through a small funnel held by the elephant in the middle, and continues straight onto the computer screen on the right, where one line of text already shows; the box labeled "memory" is now small and holds just one strip. The thread of paper and the line on the screen are drawn in the blue accent color. Labels: "before" at the top left, "after" at the bottom left, "memory" on both boxes.

## ch15-three-ways.png

- Chapter: `ch15-04-performance.md`, right after the console block with the benchmark numbers.
- Idea: three runners on the same track: the loop is fast and light, the array functions carry two heavy sacks, the generator is light but stops at every step to hand over one value.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A running track seen from the side with three lanes, a finish line drawn as a vertical checkered ribbon on the right, and three small friendly elephants (the PHP mascot) racing from left to right. Top lane: an elephant sprinting, closest to the finish line, carrying a tiny cup in its trunk. Middle lane: an elephant a little further back, bent under two enormous sacks, one on each shoulder. Bottom lane: an elephant furthest back, also carrying a tiny cup, stopped mid-stride to hand a small square tile up to a hand reaching down from the top of the image, with a dotted trail of small footprints behind it showing many earlier stops. The three cups and the two sacks each carry a small tag, drawn in the blue accent color. Labels: "loop", "array functions", "generator" written on the lanes, and "2 MB" on each cup and "66 MB" on the sacks.

---

## ch16-script-signpost.png

- Chapter: `ch16-01-customizing-composer.md`, in the scripts section, after the paragraph on the script name being the contract.
- Idea: the team only sees the short script name; the real command behind it can change without anyone noticing.
- Priority: nice to have.
- Format: portrait.

**Prompt.** In the foreground, a tall wooden signpost planted in the ground with one arrow-shaped sign reading "composer test", and three small friendly elephants (the PHP mascot) standing in front of it, all looking at the sign, one of them pointing at it. Behind the signpost, a theater curtain drawn half open, and behind the curtain, partly hidden, a long messy command line written on a scroll with a few flags and switches, deliberately too small and too far to read. Only the signpost and its sign are in the blue accent color. Labels: "composer test" on the sign, nothing else readable.

## ch16-psr4-vs-files.png

- Chapter: `ch16-01-customizing-composer.md`, in the files autoloading section, after the paragraph about helpers.php being available everywhere.
- Idea: PSR-4 fetches one class file only when it is asked for; a files entry keeps its file open on the desk at all times.
- Priority: must have.
- Format: landscape.

**Prompt.** Two scenes side by side, separated by a thin vertical dotted line. Left: a small friendly elephant (the PHP mascot) dressed as a librarian, standing on a step stool, pulling a single book out of a tall bookshelf full of neatly labeled books, in answer to a small speech bubble from a person at the edge of the frame containing the words "Search class?". Right: the same elephant sitting at a desk, and on the desk one open notebook lying flat, always there, with a small clock on the wall above it. The single book being pulled on the left and the open notebook on the right are in the blue accent color. Labels: "psr-4, on demand" under the left scene, "files, every time" under the right scene.

## ch16-packagist-directory.png

- Chapter: `ch16-02-publishing-to-packagist.md`, in the "You don't upload anything" section, right after the bold sentence.
- Idea: Packagist is a directory that points to Git repositories, not a warehouse holding the code.
- Priority: must have.
- Format: landscape.

**Prompt.** Center: a large open phone book, drawn as a thick book lying open, with one entry visible on the page, a package name and a small arrow next to it. Right: a cloud-shaped Git repository icon, a simple cloud with a branching commit symbol inside it, and the arrow from the phone book entry points straight at this cloud. Left: a small friendly elephant (the PHP mascot) at a terminal, with a speech bubble containing "composer require", and a dotted path drawn from the elephant to the phone book, then following the arrow to the cloud. Behind the phone book, crossed out with a light X, a small warehouse building, to show the code is not stored there. The arrow and the dotted path are in the blue accent color. Labels: "packagist" on the cover of the book, "composer require" in the bubble, "your repo" under the cloud.

## ch16-semver-tags.png

- Chapter: `ch16-02-publishing-to-packagist.md`, in the "Versions come from Git tags" section, after "The tag is the release."
- Idea: a Git tag pushed to the repository becomes, by itself, a version listed on Packagist.
- Priority: must have.
- Format: landscape.

**Prompt.** A horizontal timeline of Git commits drawn as a row of small circles connected by a line, left to right. Three of the circles have a small triangular flag planted on them, like flags on a golf course, reading "v1.0.0", "v1.0.1" and "v1.1.0". Above the timeline, on the right, a simple web page card with the word "packagist" at the top and a short list of three lines below it, "1.0.0", "1.0.1", "1.1.0", each line connected by a thin curved arrow to its flag on the timeline. The flags and the arrows are in the blue accent color. Labels: the three flag texts, the three list lines, and "packagist" on the card.

## ch16-path-symlink.png

- Chapter: `ch16-03-composer-monorepos.md`, after the paragraph explaining that Composer creates a symlink rather than a copy.
- Idea: vendor/phpgrep/core in the CLI project is not a copy; it is a link tied to the real core folder next door.
- Priority: must have.
- Format: landscape.

**Prompt.** Two large folder icons side by side on the same shelf, seen from the front, like two cardboard file boxes. The left one is labeled "phpgrep-core" and holds a few sheets of paper sticking out of the top. The right one is labeled "phpgrep-cli" and contains, drawn inside it, a smaller nested folder labeled "vendor" holding a tiny empty folder outline. From that tiny empty folder, a piece of string runs out of the right box, across the shelf, and is tied to the sheets of paper inside the left box, like a luggage tag on a string. A small friendly elephant (the PHP mascot) stands between the two boxes holding a pencil, having just edited one of the sheets in the left box, with three small motion lines showing the string tugging. The string is in the blue accent color. Labels: "phpgrep-core", "phpgrep-cli", "vendor", and "symlink" written along the string.

## ch16-global-vs-project.png

- Chapter: `ch16-04-installing-global-tools.md`, after the paragraph about ten projects with ten copies of PHPStan.
- Idea: one copy of a tool per project is duplication; one global copy on a shelf serves every project.
- Priority: must have.
- Format: landscape.

**Prompt.** A before-and-after drawing split in two by a thin vertical dotted line. Left half: four folder icons in a row, each labeled "project", and inside each one an identical small wrench icon, four wrenches in total, drawn to look repetitive and slightly crowded. Right half: the same four folders in a row, now empty, and above them a single shelf mounted on the wall holding one wrench, with four thin lines running from the wrench down to each folder. The single wrench on the shelf and its four lines are in the blue accent color. Labels: "each project" under the left half, "global" under the right half.

## ch16-lifecycle-hook.png

- Chapter: `ch16-05-extending-composer.md`, right after the JSON example with post-install-cmd.
- Idea: composer install has stages, and a script attached to one of them runs by itself when that stage is reached.
- Priority: must have.
- Format: landscape.

**Prompt.** A horizontal conveyor belt or timeline read left to right. At the left end, a terminal window with the text "composer install" typed in it. Along the belt, three simple stages drawn as small stations: a box being downloaded from a cloud, then a stack of boxes being placed into a folder labeled "vendor", then a small bell mounted on a post at the end of the belt. The bell is ringing, with motion lines, and a thin arrow goes from the bell down to a small friendly elephant (the PHP mascot) already at work below the belt, running a script drawn as a sheet of paper with a play triangle on it. Nobody is at the terminal anymore; the chair in front of it is empty. The bell, its motion lines and the arrow to the elephant are in the blue accent color. Labels: "composer install" in the terminal, "vendor" on the folder, "post-install-cmd" next to the bell.

---

## ch17-family-tree.png

- Chapter: `ch17-01-inheritance-and-polymorphism.md`, after the paragraph that defines overriding, before the paragraph on `parent::`.
- Idea: a subclass inherits everything from its parent, replaces only what it overrides, and `parent::` reaches back up to the replaced method.
- Priority: must have.
- Format: landscape.

**Prompt.** A small family tree of three rounded boxes drawn like index cards. One card at the top center, two cards below it side by side, each of the two lower cards connected to the top card by a straight line ending in a hollow triangle arrowhead pointing up at the top card. The top card has a title "PaymentMethod" and one line inside reading "charge()". The bottom left card has a title "CreditCard" and one line inside reading "charge()". The bottom right card has a title "PayPal" and one line inside reading "charge()". From the "charge()" line of the CreditCard card, a curved arrow drawn in the blue accent color loops up to the "charge()" line of the top card, with the word "parent::" written along it. The word "extends" is written in small letters next to the two straight lines. A small friendly elephant (the PHP mascot) sits at the bottom right corner, looking up at the tree. Labels: "PaymentMethod", "CreditCard", "PayPal", "charge()", "parent::", "extends".

## ch17-one-slot.png

- Chapter: `ch17-01-inheritance-and-polymorphism.md`, in the polymorphism section, right after the sentence "That is polymorphism."
- Idea: code written against the base type accepts any subclass, including the ones not written yet, because they all fit the same slot.
- Priority: must have.
- Format: landscape.

**Prompt.** A wall-mounted mailbox drawn large on the right side of the image, with a single horizontal letter slot on its front. The slot outline is drawn in the blue accent color and the words "PaymentMethod" are written just above it. The mailbox itself bears the label "processPayment()". On the left, three envelopes of exactly the same size line up toward the slot, the first one already halfway in. The first envelope has a small credit card drawn on it and the label "CreditCard". The second envelope has a small at-sign drawn on it and the label "PayPal". The third envelope is blank with a large question mark on it and is carried by a small friendly elephant (the PHP mascot) waiting patiently in line. A short blue arrow points from the envelopes toward the slot. Labels: "processPayment()", "PaymentMethod", "CreditCard", "PayPal".

## ch17-blueprint-vs-badge.png

- Chapter: `ch17-02-abstract-classes.md`, after the paragraph "A contract the language enforces, bundled with shared code written once", before the TIP callout.
- Idea: an abstract class is a half-built house you inherit, foundation included and walls to fill in; an interface is a badge that unrelated objects can all wear.
- Priority: must have.
- Format: landscape.

**Prompt.** Two scenes side by side, separated by a thin vertical dotted line. Left scene: a small house under construction seen from the front. Its foundation is a thick solid slab drawn with firm black lines and labeled "receipt()". Above the slab, the walls and roof are drawn only as a dotted outline in the blue accent color, with the label "charge()" written inside the empty outline and a tiny hand-drawn sign reading "to fill in" leaning against it. Above the left scene the title "abstract class". Right scene: three clearly different objects standing in a row, a shopping bag, a sheet of paper with a few lines of text, and a small browser window. Each of the three wears the very same small round badge pinned to it, drawn in the blue accent color, and each badge reads "Formattable". Above the right scene the title "interface". Labels: "abstract class", "interface", "receipt()", "charge()", "to fill in", "Formattable".

## ch17-magic-buttons.png

- Chapter: `ch17-03-magic-methods.md`, at the end of the `__toString()` section, after the paragraph on the return type.
- Idea: you write what a magic method does, and PHP itself decides when to call it, triggered by the situation the object is in.
- Priority: nice to have.
- Format: landscape.

**Prompt.** In the center, an object drawn as a rounded box with a small friendly face, sitting inside a line of hand-lettered text so that the text reads "Total:" on its left and "USD" on its right, as if the box had been dropped into a sentence. On the side of the box, three small round push buttons stacked vertically, each with a tiny label next to it: "__toString", "__get", "__call". A small friendly elephant (the PHP mascot) stands next to the box and presses the top button, "__toString", with the tip of its trunk. That pressed button and a short burst of motion lines around it are drawn in the blue accent color; the other two buttons stay black and white. A small speech bubble from the box reads "49.99". Labels: "__toString", "__get", "__call", "Total:", "USD", "49.99".

## ch17-strategy-socket.png

- Chapter: `ch17-04-oop-design-patterns.md`, at the end of "The idea" section, after the sentence defining the context.
- Idea: the context is a socket, each strategy is a plug of the matching shape, and plugs can be swapped without touching the device.
- Priority: must have.
- Format: landscape.

**Prompt.** A simple boxy device drawn in the center, like a small appliance with a single dial, labeled "Checkout" on its front. On its right side, one socket with a distinctive rounded-trapezoid opening, its outline drawn in the blue accent color, with the label "PaymentMethod" written under it. Two plugs with exactly that rounded-trapezoid shape and a short cord: one plug is inserted in the socket and bears a small credit card icon with the label "CreditCard"; the other plug lies on the table just below with a small at-sign icon and the label "PayPal". A curved double-headed arrow in the blue accent color connects the two plugs, showing that they swap places. A small friendly elephant (the PHP mascot) holds the loose plug, ready to swap it in. Labels: "Checkout", "PaymentMethod", "CreditCard", "PayPal".

---

## ch18-always-on-vs-fresh-start.png

- Chapter: `ch18-01-request-model.md`, after the paragraph describing the fresh start of every request.
- Idea: a long-running server keeps its memory from one visitor to the next; a PHP request starts at a clean desk every time.
- Priority: must have.
- Format: landscape.

**Prompt.** Two scenes side by side, separated by a thin vertical dotted line. Left: a tall server tower drawn as a small building with all its lights on, and in front of it a plain rounded robot sitting at a desk cluttered with sticky notes, folders and a coffee mug; three visitors walk past that same desk one after another, and the pile of notes on the desk grows with each one. Right: a small friendly elephant (the PHP mascot) at a perfectly clean, empty desk, facing a single visitor; just below, a short three-frame strip shows the same desk being wiped with a cloth, a small puff of smoke, and a brand new clean desk with the next visitor arriving. The clean desks and the wiping cloth are in the blue accent color. Labels: "always on" under the left scene, "fresh start" under the right scene.

## ch18-worker-pool.png

- Chapter: `ch18-01-request-model.md`, in the "Why this made threading unnecessary" section, after the post office analogy.
- Idea: PHP serves many users at once by running many processes side by side, one request each, not by making one process juggle.
- Priority: must have.
- Format: landscape.

**Prompt.** A post office seen from the front, with a row of six identical counters, each staffed by a small friendly elephant (the PHP mascot), each serving exactly one visitor standing in front of it. At the entrance on the left, a short queue of waiting visitors and a signpost with an arrow directing the first of them to the one counter that is empty, where its elephant waves. Above the whole row of counters, a long banner. The signpost, its arrow and the banner are in the blue accent color. Labels: "PHP-FPM" on the banner, "next free" on the signpost.

## ch18-job-queue.png

- Chapter: `ch18-02-queues-and-processes.md`, in the "Job queues" section, right after the paragraph describing the message pushed onto the queue.
- Idea: the request hands out a ticket right away and drops the job onto a queue; workers in the back room do the slow work later.
- Priority: must have.
- Format: landscape.

**Prompt.** A dry cleaner counter. Left: a visitor handing a small framed picture over the counter to a small friendly elephant (the PHP mascot) standing behind it; the elephant hands back a small numbered ticket with one hand and, with its trunk, drops a small envelope onto a conveyor belt behind it. The conveyor belt runs from the counter to the right, carrying three envelopes in a row, through a doorway in a thin wall, into a back room. In the back room, two more elephants wearing aprons: one takes an envelope off the belt, the other resizes a picture with a large pair of scissors. The ticket, the envelopes and the conveyor belt are in the blue accent color. Labels: "request" above the counter, "queue" on the belt, "workers" above the back room.

---

## ch19-shape-stencil.png

- Chapter: `ch19-01-all-the-places-for-patterns.md`, in "The two spellings", after the bracket-form example.
- Idea: a destructuring pattern is a stencil the same shape as the data; each value drops through its hole into the variable with the matching name.
- Priority: must have.
- Format: landscape.

**Prompt.** Top center: a horizontal tray holding two large number tiles side by side, "4" and "7", with a small square bracket drawn at each end of the tray so it reads like an array. Just below the tray, a flat stencil sheet with two cut-out holes exactly aligned with the two tiles, the stencil drawn in the blue accent color, with "$x" written next to the left hole and "$y" next to the right hole. Below the stencil, two open cardboard boxes with paper labels, and dotted vertical arrows showing the "4" tile falling through the left hole into the box labeled "$x" and the "7" tile falling through the right hole into the box labeled "$y". A small friendly elephant (the PHP mascot) stands at the right, one hand raised as if it just dropped the stencil in place. Plenty of white space. Labels: "4", "7", "$x", "$y".

## ch19-keyed-pick.png

- Chapter: `ch19-02-destructuring.md`, in "Keyed destructuring", after the sentence about naming only the keys you want.
- Idea: keyed destructuring takes only the fields you name and leaves the rest of the array untouched.
- Priority: must have.
- Format: portrait.

**Prompt.** A small chest of drawers seen from the front, three drawers stacked vertically, each with a paper label on its front: "name" on the top drawer, "age" on the middle drawer, "email" on the bottom drawer. The top two drawers are pulled open, and a small friendly elephant (the PHP mascot) standing beside the chest holds two labeled boxes in its trunk and arms, "$name" and "$age", into which two curved arrows in the blue accent color flow from the open drawers. The bottom "email" drawer is firmly shut, with a tiny padlock-shaped doodle or a small "zzz" to show it is left alone. Nothing else in the frame. Labels: "name", "age", "email", "$name", "$age".

## ch19-swap.png

- Chapter: `ch19-02-destructuring.md`, in "Swapping two variables", after the code example.
- Idea: the right-hand array is built first, capturing both values, and only then poured back into the variables, which is why the swap needs no temporary variable.
- Priority: nice to have.
- Format: landscape.

**Prompt.** Two panels side by side separated by a thin vertical dotted line, read left to right with a small circled "1" and "2" in the top corners. Panel 1: two open cardboard boxes with labels "$a" and "$b", the first holding a large tile "1", the second a tile "2"; above them a flat tray drawn in the blue accent color being filled by two curved arrows, one carrying the "2" from the second box into the tray's left slot and one carrying the "1" from the first box into the tray's right slot, so the tray now reads 2 then 1. Panel 2: the same tray tipping over and pouring its two tiles straight down into the two boxes, which now read "2" in "$a" and "1" in "$b". A small friendly elephant (the PHP mascot) holds the tray in panel 2. Labels: "$a", "$b", "1", "2".

## ch19-first-match-wins.png

- Chapter: `ch19-03-match-syntax.md`, in "Order matters: first match wins", after the grade example.
- Idea: match tests arms from top to bottom and stops at the first that fits, so overlapping conditions must be ordered from most restrictive to least.
- Priority: must have.
- Format: portrait.

**Prompt.** Three round kitchen sieves stacked vertically with space between them, seen slightly from the side, held in a simple wooden frame. The top sieve has the finest mesh, the middle one a medium mesh, the bottom one a coarse mesh. A small tag hangs from each sieve: "90+" on the top, "80+" on the middle, "70+" on the bottom, and next to each tag a letter in the blue accent color: "A", "B", "C". A small ball marked "85" is drawn twice with a dotted trajectory: once falling through the top sieve, once resting caught on the middle sieve, with the "B" next to that sieve circled in the blue accent color. A small friendly elephant (the PHP mascot) peers at the middle sieve from the side. Labels: "90+", "80+", "70+", "A", "B", "C", "85".

---

## ch20-tool-drawer.png

- Chapter: `ch20-00-advanced-features.md`, after the opening paragraph.
- Idea: the chapter is a drawer of specialty tools you rarely need but are glad to know about.
- Priority: nice to have.
- Format: landscape.

**Prompt.** A wooden workshop drawer pulled open, seen from slightly above and in front, with a small friendly elephant (the PHP mascot) peeking over its edge. Inside the drawer, four objects laid neatly in foam cutouts, each with a small paper tag: a magnifying glass, a three-pin electrical plug, a coiled rope with a hook on its end, and a luggage tag with a hash sign drawn on it. The objects are simple and clearly separated. The paper tags are drawn in the blue accent color. Labels on the tags: "reflection", "interfaces", "callables", "attributes".

## ch20-reflection-xray.png

- Chapter: `ch20-01-reflection.md`, in the Reflection section, after the paragraph describing ReflectionClass.
- Idea: Reflection is an X-ray. The object stays closed, and you still see everything inside it.
- Priority: must have.
- Format: landscape.

**Prompt.** Left: a closed cardboard box with a label reading "UserRepository", sitting on a table. Right: an X-ray screen on a stand, like at an airport security check, showing the same box in outline with its contents revealed: three horizontal bars stacked inside, like bones, labeled "find", "save" and "connect". The third bar, "connect", has a small padlock drawn next to it. A small friendly elephant (the PHP mascot) stands behind the screen looking at it with interest. The revealed bars on the screen are drawn in the blue accent color. Labels: "UserRepository", "find", "save", "connect".

## ch20-three-sockets.png

- Chapter: `ch20-02-built-in-interfaces.md`, after the paragraph about the SPL and the contract.
- Idea: each built-in interface is a socket on your object that one piece of PHP syntax can plug into.
- Priority: must have.
- Format: landscape.

**Prompt.** In the center, a rounded rectangular object, like a small appliance, with a label reading "Playlist" on its front. On its right side, three electrical sockets stacked vertically. Three cables come from the right edge of the image, each ending in a plug that fits one socket, and each cable starts from a small rounded frame containing a piece of code. From top to bottom: "count()", "[ ]", "foreach". The top plug is already inserted, the other two are just about to be. The three plugs and cables are drawn in the blue accent color. Labels: "Playlist", "count()", "[ ]", "foreach".

## ch20-callable-handle.png

- Chapter: `ch20-03-advanced-closures.md`, at the end of "The old way of passing a function around".
- Idea: a string is a name written on a note. First-class callable syntax is a real handle on the function.
- Priority: must have.
- Format: landscape.

**Prompt.** Two halves separated by a thin vertical dotted line. Left half: a small square paper note, slightly crumpled, with the word "strlen" written on it, floating in the air with a question mark above it, and below it a machine-like box with a gear on it, standing alone with nothing connecting the note to the box. Right half: the same machine box, but this time a solid rope with a sturdy handle at its end is tied directly to the box, and the handle bears the text "strlen(...)". The rope and handle are drawn in the blue accent color. Labels: "strlen" on the note, "strlen(...)" on the handle.

## ch20-static-closure.png

- Chapter: `ch20-03-advanced-closures.md`, in the Static closures section, after the code.
- Idea: an ordinary closure keeps a thread back to the object that created it. A static closure has that thread cut.
- Priority: nice to have.
- Format: landscape.

**Prompt.** On the left, a rounded box with a label reading "Report", drawn like a small building or object. Two small balloon shapes float away from it toward the right, each representing a closure, drawn as a rounded blob with a tiny pair of curly braces on it. The upper balloon is still attached to the Report box by a thin string with a small tag on it reading "$this". The lower balloon is drifting free: its string has been cut, with a pair of scissors drawn next to the cut and a small loose end of string hanging from the balloon. The cut string, the scissors and the free balloon are drawn in the blue accent color. Labels: "Report", "$this", "static".

## ch20-attribute-tag.png

- Chapter: `ch20-04-attributes.md`, at the end of "Defining and attaching an attribute".
- Idea: an attribute is a tag hanging on a method, inert until Reflection reads it and turns it into a routing table entry.
- Priority: must have.
- Format: landscape.

**Prompt.** Three stages from left to right. Left: a rounded box representing a method, with the text "index()" on it, and a paper luggage tag hanging from its corner by a small string; the tag reads "Route". Middle: a large magnifying glass held by a small friendly elephant (the PHP mascot), hovering over the tag, with a few short lines drawn around the lens to show it is reading. Right: a small hand-drawn table with a single row, framed like a notebook page, reading "GET /users -> index". A curved arrow leads from the magnifying glass to the table. The luggage tag and the arrow are drawn in the blue accent color. Labels: "index()", "Route", "Reflection" under the magnifying glass, "GET /users -> index" in the table.

---

## ch21-router-switchboard.png

- Chapter: `ch21-01-single-file-router.md`, in "The router itself", after the paragraph explaining REQUEST_URI and parse_url.
- Idea: a router is a lookup table. The incoming path is matched against its keys, and everything else falls into the 404 bin.
- Priority: must have.
- Format: landscape.

**Prompt.** Left: a browser window with a small envelope flying out of it towards the right, the envelope carrying the text "/about". Center: a small friendly elephant (the PHP mascot) standing in front of a large wall panel drawn like an old telephone switchboard or a hotel key board, with two rows. Each row has a path written on the left and a small socket on the right, and from each socket a wire runs to a small box on the far right of the image, each box showing a short line of text like a note card. The elephant holds the incoming envelope and plugs its wire into the row whose label matches, "/about". That row, its wire and its box are drawn in the blue accent color. Below the panel, a small waste basket on the floor with "404" written on it, where an envelope with a scribbled unknown path is dropping in. Labels: "/", "/about", "404".

## ch21-output-buffer.png

- Chapter: `ch21-02-mvc-structure.md`, in "Views: PHP's original superpower", after the paragraph explaining extract, ob_start and ob_get_clean.
- Idea: output buffering catches what a view prints instead of letting it reach the browser, and hands it back as a string.
- Priority: nice to have.
- Format: landscape.

**Prompt.** Two panels side by side, separated by a thin vertical dotted line. In both panels, at the top, a sheet of paper standing for a view file, showing a few short lines of HTML tags with one small highlighted island of PHP in the middle, and from the bottom of the sheet a stream of tiny characters pours out like water from a tap. Left panel: the stream falls straight down into a browser window at the bottom, where the same characters appear as a rendered page. Right panel: a bucket catches the stream before it reaches anything, and the bucket is being handed to the right, towards a small box with a gear on it, the controller; the bucket is drawn in the blue accent color, and on its side is written "ob_start()". Labels: "browser" under the left panel, "ob_start()" on the bucket, "controller" on the box.

## ch21-request-path.png

- Chapter: `ch21-02-mvc-structure.md`, in "Wiring the router to controllers", after "Follow one request all the way through."
- Idea: the round trip of a request. Browser to router to controller to render to view, and the HTML back to the browser. This is the central drawing of the chapter.
- Priority: must have.
- Format: landscape.

**Prompt.** A flow read from left to right along the top of the image, then returning along the bottom, like a loop. Top left: a browser window with a small envelope leaving it, the envelope marked "/". First stop: a signpost or small lookup table with two rows, one row highlighted, labeled "router". Second stop: a small box with a gear drawn on it, labeled "controller". Third stop: a funnel labeled "render()", into which a sheet of paper is being fed, the sheet showing a few HTML tags with one small island of PHP, labeled "view". Out of the bottom of the funnel comes a rolled-up page marked "HTML". Along the bottom of the image, a long curved arrow carries that page back to the browser on the left, where it appears rendered on the screen. The forward arrows along the top are black; the return arrow along the bottom and the HTML page it carries are in the blue accent color. A small friendly elephant (the PHP mascot) stands near the router, pointing the way. Labels: "router", "controller", "render()", "view", "HTML".

## ch21-shutdown-hook.png

- Chapter: `ch21-03-shutdown-and-cleanup.md`, in the register_shutdown_function section, after the "Try it" paragraph.
- Idea: whichever way a script ends, it passes through the shutdown function before it is gone.
- Priority: must have.
- Format: landscape.

**Prompt.** Three paths drawn as simple roads coming from the left of the image, converging on a single door in the center right. Each road starts from a small sheet of paper standing for a script. First sheet: a few lines of code with a check mark at the bottom, its road labeled "last line". Second sheet: a few lines with a small lightning bolt bursting from the middle, its road labeled "exception". Third sheet: a few lines with a big cross over the bottom half, its road labeled "fatal error". The three roads merge into one and lead to a single open door frame drawn in the blue accent color, with a sign above it reading "shutdown". In the doorway, a small friendly elephant (the PHP mascot) holds a broom and sweeps a little pile of dust out. Beyond the door, on the right edge, only a small puff of smoke and white space. Labels: "last line", "exception", "fatal error", "shutdown".

---

## ch22-map.png

- Chapter: `ch22-00-where-to-go-from-there.md`, after the paragraph "Most of what remains is not PHP the language but PHP in context".
- Idea: the road of the book ends at a crossroads, and five roads lead on from it. The reader picks one.
- Priority: must have.
- Format: landscape.

**Prompt.** A treasure-map style drawing seen slightly from above. From the bottom left, a single winding trail arrives at a crossroads in the center of the image; along that incoming trail, drawn faintly, three tiny milestones already passed: a terminal window, a die, and a small browser window with a house inside. At the crossroads stands a small round friendly elephant (the PHP mascot) wearing a backpack, looking up at a tall wooden post with five signpost arrows pointing in five different directions, each toward a short trail that fades out at the edge of the paper. Next to each fading trail, one small icon: a toolbox, a stack of three layers, a padlock, a bridge, and a group of three little people. The five signpost arrows and the five outgoing trails are in the blue accent color. Plenty of white space. Labels on the signposts: "frameworks", "architecture", "security", "beyond PHP", "people".

## ch22-community.png

- Chapter: `ch22-05-community.md`, before the closing paragraph "The fastest way to grow past this book is to talk to people who already have".
- Idea: the book ends, the people continue. The reader steps off the last page toward a group that is already there and waving.
- Priority: nice to have.
- Format: landscape.

**Prompt.** Bottom left: a large open book seen from a three-quarter angle, its last page turned, lying flat like a landing stage. A small round friendly elephant (the PHP mascot) with a backpack steps off the edge of the last page onto a short dotted path that leads to the right. Right side: a relaxed group of four or five simply drawn people of different heights standing around a whiteboard on an easel, on which a tiny box-and-arrow diagram is sketched; one person turns toward the elephant and waves it over, another holds a mug. The dotted path and the waving arm are in the blue accent color. Generous white space above. Labels: "the book" near the book, "the people" near the group.
