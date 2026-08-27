# Programming a Guessing Game

Let's build something: not a "hello world," but an actual small program, with input, output, a loop, and a decision to make on every pass through it. We'll write a number-guessing game: the computer picks a secret number, you guess, and it tells you whether to go higher or lower until you get it.

You won't understand every keyword we use here yet, and that's fine: that's the point. Chapter 3 will go back and explain each piece properly. For now, just type along, run it, and get a feel for what PHP code looks like in motion.

## Setting up

Create a file called `guessing_game.php`:

```php
<?php

echo "Guess the number!\n";
echo "Please input your guess.\n";

$guess = trim(fgets(STDIN));

echo "You guessed: {$guess}\n";
```

Run it:

```console
$ php guessing_game.php
Guess the number!
Please input your guess.
42
You guessed: 42
```

Two new things worth pausing on.

`fgets(STDIN)` reads one line of input from the terminal, keyboard and all. `STDIN` is a built-in constant pointing at standard input, the same channel every command-line tool reads from. It hands you back a string that includes the trailing newline you pressed Enter with, which is almost never what you want, so we immediately strip it with `trim()`.

`$guess` is a variable: in PHP, every variable name starts with `$`. No declaration keyword, no type up front; you just assign to it and it exists. We'll spend real time on this in the next chapter.

And `"You guessed: {$guess}\n"` is *string interpolation*: inside a double-quoted string, `{$guess}` is replaced with the variable's value. The curly braces aren't strictly required for a simple variable like this one (`"You guessed: $guess\n"` works too), but they remove any ambiguity about where the variable name ends, which matters the moment you're interpolating something like `{$user->name}`.

## Generating a secret number

PHP's built-in `random_int()` gives us a cryptographically solid random integer in a range: overkill for a guessing game, but it's also the *correct default* to reach for whenever you need randomness, so we may as well build the habit now:

```php
<?php

$secretNumber = random_int(1, 100);

echo "Guess the number!\n";
echo "The secret number is between 1 and 100.\n";
echo "Please input your guess.\n";

$guess = trim(fgets(STDIN));

echo "You guessed: {$guess}\n";
```

Try running this a few times. Notice the secret number changes, but you can't tell, because we're not comparing anything yet. Let's fix that.

## Comparing the guess to the secret number

```php
<?php

$secretNumber = random_int(1, 100);

echo "Guess the number!\n";
echo "Please input your guess.\n";

$guess = (int) trim(fgets(STDIN));

if ($guess < $secretNumber) {
    echo "Too small!\n";
} elseif ($guess > $secretNumber) {
    echo "Too big!\n";
} else {
    echo "You win!\n";
}
```

One quiet but important change: `(int)` in front of `trim(fgets(STDIN))`. Everything read from the keyboard arrives as a *string*: even if the user typed `42`, what we actually get is the three characters `"42"`, not the number 42. Comparing a string to an integer with `<` and `>` mostly does the right thing in PHP thanks to a feature called type juggling, but "mostly" is exactly the kind of word that should make you nervous. Casting explicitly with `(int)` converts the string to a real integer, on purpose, so there's no ambiguity about what we're comparing. We'll dig into type juggling (and why to be deliberate about it) in the next chapter.

## Looping until the right guess

Right now the program checks one guess and quits, win or lose. Let's let the player keep trying:

```php
<?php

$secretNumber = random_int(1, 100);

echo "Guess the number!\n";

while (true) {
    echo "Please input your guess.\n";
    $guess = (int) trim(fgets(STDIN));

    if ($guess < $secretNumber) {
        echo "Too small!\n";
    } elseif ($guess > $secretNumber) {
        echo "Too big!\n";
    } else {
        echo "You win!\n";
        break;
    }
}
```

`while (true)` loops forever, on purpose: this is the standard PHP idiom for "keep going until something inside the loop tells you to stop." That something is `break`, which exits the loop immediately. Put the `break` only in the winning branch, and the loop naturally keeps asking until the player gets it right.

## Handling bad input

There's still a rough edge: if someone types `banana` instead of a number, `(int) "banana"` quietly becomes `0`, no error, no warning, just a wrong answer treated as a real guess. Whether that's acceptable depends on your program, but let's handle it properly, the way you would in real code, using `is_numeric()` to check before we trust the input:

```php
<?php

$secretNumber = random_int(1, 100);

echo "Guess the number!\n";

while (true) {
    echo "Please input your guess.\n";
    $input = trim(fgets(STDIN));

    if (!is_numeric($input)) {
        echo "That doesn't look like a number, try again.\n";
        continue;
    }

    $guess = (int) $input;

    if ($guess < $secretNumber) {
        echo "Too small!\n";
    } elseif ($guess > $secretNumber) {
        echo "Too big!\n";
    } else {
        echo "You win!\n";
        break;
    }
}
```

`continue` is `break`'s sibling: instead of exiting the loop, it jumps straight back to the top for the next iteration, skipping everything below it. Here, a bad guess just asks again, no crash, no wrong-guess penalty for a typo.

## Where we've landed

Around thirty lines, and it already has input, output, a loop, a conditional, a bit of type conversion, and some input validation, which is a fair chunk of what real programs are made of, guessing games included. Keep this file around; we'll revisit small CLI programs like this one throughout the book, and by [Chapter 13](ch13-00-a-cli-project.md) you'll be structuring something a good deal more serious than a guessing game.
