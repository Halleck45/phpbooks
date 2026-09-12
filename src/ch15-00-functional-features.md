# Functional Features: Closures and Generators

<img src="images/ch15-icon.svg" alt="Functional Features: Closures and Generators illustration" width="72">

Back in [Chapter 3](ch03-03-how-functions-work.md), you saw that functions in PHP are values: you can hold one in a variable, and you already met the anonymous kind, closures, in passing. This chapter goes back for that material properly, because it's not a curiosity. Passing a small piece of behavior into another function is one of the most common things you'll do in real PHP code, and PHP gives you two ways to write that behavior inline: full closures, which can capture variables from the surrounding scope explicitly, and the terser arrow functions, which capture automatically.

The second half of the chapter is about a different problem entirely: what happens when the *data* you're iterating over is too large, too slow to produce, or simply not something you want to build all at once before you start working with it. That's what generators are for. A generator function looks almost like an ordinary function, but instead of building up a result and returning it in one go, it hands values back to its caller one at a time, pausing itself in between. You'll see exactly how that changes what a function can do, and why it matters.

Once both pieces are on the table, we'll put them to work. The phpgrep command-line tool you built across [Chapter 14](ch14-00-a-cli-project.md) currently reads a whole file and builds an array of every matching line before it prints anything. That's fine for a small file and a genuine problem for a large one. We'll revisit `search()` and rewrite it as a generator, and you'll see the difference it makes concretely, not just in theory.

The chapter closes with an honest look at performance: not benchmarks for their own sake, but a practical comparison of plain loops, generators, and PHP's built-in array functions like `array_map()` and `array_filter()`, so you know which one to reach for and why, rather than picking whichever one you saw most recently in someone else's code.
