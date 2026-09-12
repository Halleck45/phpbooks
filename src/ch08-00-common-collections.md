# Common Collections

<img src="images/ch08-icon.svg" alt="Common Collections illustration" width="72">

You've been using arrays since [Chapter 3](ch03-02-data-types.md), mostly by glimpse: a `$fruits = ["apple", "banana"]` here, a `foreach` there, enough to keep an example moving without stopping to explain itself. That stops now. Arrays are PHP's single most important data structure, used constantly for things other languages hand off to half a dozen specialized types, and they deserve a chapter that actually does them justice rather than one that assumes you'll pick up the rest by osmosis.

The reason PHP gets away with one data structure doing so much work is that a PHP array isn't really a list or a dictionary underneath: it's an ordered map, always, and "list" versus "dictionary" is just a matter of which keys you happen to be using. Understand that one fact early and a lot of otherwise-surprising behavior (why order is preserved, why `array_filter()` leaves gaps in the keys, why `count()` is instant) stops being surprising and starts being obvious.

This chapter also detours into strings, and that's deliberate rather than a change of subject. Strings and arrays are joined at the hip in everyday PHP: you split one into the other, you glue arrays of strings back together, and the moment your strings contain anything beyond plain ASCII (an accented name, a currency symbol, an emoji) you run straight into UTF-8, which PHP handles, but only if you ask it to correctly.

We'll cover three things in turn: indexed arrays, the list-style arrays you already have some intuition for; strings, with an honest look at the byte-versus-character distinction that trips up nearly everyone at some point; and associative arrays, where string keys turn the same underlying structure into something closer to a small, flexible record. By the end, you'll have real command of the tools you'll reach for in nearly every PHP program you write from here on.
