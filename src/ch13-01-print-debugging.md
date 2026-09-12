# Print Debugging with `var_dump()` and `print_r()`

<img src="images/ch13-icon.svg" alt="Print Debugging with vardump() and printr() illustration" width="72">

You've already met `var_dump()`, briefly, back in [Chapter 3](ch03-02-data-types.md): it's the function that shows you a value's type along with the value itself. That combination is exactly what makes it a debugging tool and not just an inspection one: the bug is very often that a value has the wrong *type*, not the wrong contents, and `echo` alone can't tell you that. `echo $count` prints `5` whether `$count` is the integer `5` or the string `"5"`. `var_dump($count)` prints `int(5)` or `string(1) "5"`, and the difference between those two is frequently the entire bug.

## `var_dump()` on structured data

`var_dump()` isn't limited to a single scalar. Hand it an array or an object and it recurses, showing you the whole shape:

```php
<?php

$user = [
    'name' => 'Alice',
    'age' => '32',
    'active' => true,
    'roles' => ['admin', 'editor'],
];

var_dump($user);
```

```console
array(4) {
  ["name"]=>
  string(5) "Alice"
  ["age"]=>
  string(2) "32"
  ["active"]=>
  bool(true)
  ["roles"]=>
  array(2) {
    [0]=>
    string(5) "admin"
    [1]=>
    string(6) "editor"
  }
}
```

Notice `"age"` came back as `string(2) "32"`, not `int(32)`. If this array came from a form submission (the kind of data [Chapter 10](ch10-01-forms-and-superglobals.md) reads out of `$_POST`), that's expected: everything in `$_POST` arrives as a string, and code further down that assumes `$user['age']` is already an integer is a bug waiting to happen. That's the kind of thing `var_dump()` catches in seconds that a quiet wrong answer three functions later would take much longer to trace back.

You can hand `var_dump()` more than one argument at once, which dumps each in turn: `var_dump($name, $age, $roles)` is shorter than three separate calls.

## `print_r()`: easier to read, less precise

`print_r()` shows the same structural information without the types, in a format that's noticeably easier to scan for a large nested array:

```php
<?php

print_r($user);
```

```console
Array
(
    [name] => Alice
    [age] => 32
    [active] => 1
    [roles] => Array
        (
            [0] => admin
            [1] => editor
        )

)
```

That's a reasonable trade: reach for `print_r()` when you just want to see the shape of something quickly, and `var_dump()` the moment a value's exact type is in question, which it usually is once you're specifically hunting a bug rather than just looking something up. One more difference matters in practice: `print_r()` takes an optional second argument, and passing `true` makes it *return* the formatted string instead of printing it:

```php
<?php

$snapshot = print_r($user, true);
error_log("user state: {$snapshot}");
```

`var_export()` is a third option worth knowing about, closer to `print_r()` than `var_dump()` in what it shows, but it formats its output as valid PHP source rather than a description meant for a human: `var_export($user)` prints something you could paste directly back into a script as an array literal. Handy for capturing a real value as a test fixture.

## The limits of printing things

All three of these share the same weakness: you have to already suspect *where* the problem is before you know where to put the call, and every time you want to look somewhere new, you edit the file and rerun the program. For a script the size of anything so far in this book, that's a fine way to work. Once a bug depends on the exact sequence of several function calls, or shows up only on the fifth iteration of a loop, or lives inside a library you'd rather not edit, printing things stops being surgical and starts being trial and error. The next section covers the tool for that: Xdebug, which lets you pause a running script and look around, instead of guessing where to point a flashlight in advance.
