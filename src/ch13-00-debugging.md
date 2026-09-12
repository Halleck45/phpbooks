# Debugging PHP

<img src="images/ch13-icon.svg" alt="Debugging PHP illustration" width="72">

Every program in this book so far has been small enough to read start to finish and spot the bug by eye. That stops being true quickly, and the guessing game and the web basics chapter you just finished are already big enough that "just read it carefully" isn't always going to cut it. Debugging is the skill of finding out what a program is actually doing, as opposed to what you meant it to do, and it's worth treating as a skill in its own right rather than something you pick up by accident.

This chapter covers two approaches, and you'll want both. The first, **print debugging**, is the oldest trick in the book: put something in the middle of your code that shows you a value, rerun the program, read the output. It needs nothing but PHP itself, and `var_dump()` and `print_r()` are the tools for it. The second, **step debugging**, is more surgical: pause the program mid-execution, inspect every variable in scope exactly as it stood at that moment, and step forward one line at a time. That takes a tool, **Xdebug**, and a few minutes of setup, but it earns that setup back the first time a bug doesn't announce itself with an obvious wrong value to print.

Neither replaces the error handling from [Chapter 9](ch09-00-error-handling.md): a well-placed exception tells you *that* something went wrong. Debugging is what you reach for to find out *why*, especially when nothing threw at all and the program just quietly produced the wrong answer. The CLI project in [Chapter 14](ch14-00-a-cli-project.md) is exactly the kind of multi-file program where that distinction starts to matter, and where both of these tools earn their keep.
