# Patterns and Matching

Pull three values out of an array the plain way and you write three lines: `$name = $row[0];`, then `$age = $row[1];`, then `$city = $row[2];`. Each line repeats the same gesture, and none of them tells the reader what the array looks like. **Destructuring does the same job in one assignment, by drawing the shape you expect on the left of the equals sign.** It is PHP's quietest pattern tool, it gets far less attention than it deserves, and it is what this chapter is about.

You already know the loud one. `match` arrived in [Chapter 6](ch06-02-match.md), next to enums, as the tidy replacement for `switch`. On the page, `match` and destructuring do not look alike. Underneath, they solve the same kind of problem: you hold a shape (an array, a value that could be one of several things), and you want PHP to take it apart for you rather than spelling out the indexing or the comparisons by hand.

Destructuring shows up in more places than you would guess: plain assignment, `foreach`, slots you skip on purpose. Then the syntax itself, nested and keyed, which is where it earns its place in everyday code. The chapter closes on three details of `match` that Chapter 6 had no room for: several conditions in one arm, why the order of arms matters, and arms that are full expressions rather than bare values.

None of this is exotic. It is ordinary, idiomatic PHP, and once it is in your hands, `$row[0]`, `$row[1]`, `$row[2]` on three separate lines will look as dated as a `switch` with six `break`s.
