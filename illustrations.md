# Illustrations for chapters 0, 1 and 2

This file lists every drawing referenced by the rewritten introduction, Getting Started and Guessing Game chapters, with a ready-to-use prompt for each. The chapters already contain the `<img>` tags and alt texts; drop the generated files into `src/images/` under the file names below and they will appear.

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
