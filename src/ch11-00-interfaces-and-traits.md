# Interfaces, Traits, and Generic-Style Code

<img src="images/ch11-icon.svg" alt="Interfaces, Traits, and Generic-Style Code illustration" width="72">

Classes give you a template for building objects. Interfaces and traits are the two tools PHP offers for the problem that shows up the moment you have more than one class: how do unrelated pieces of code agree to work together, and how do you avoid retyping the same method five times across five classes that have nothing else in common.

They solve opposite halves of that problem, and it's worth saying so plainly up front because beginners, and more than a few experienced developers coming from other languages, routinely conflate them. An interface is a *contract*: it says "any class claiming this name promises to have these methods," and says nothing whatsoever about how those methods are implemented. A trait is the reverse: it's a literal chunk of implementation, copied wholesale into whichever classes ask for it, and it makes no promise about what those classes are or how they relate to one another. One is a shape you agree to fit. The other is a piece of code you borrow.

This chapter also faces something honest about PHP that surprises people arriving from Java, C#, or TypeScript: PHP has no true generics. You cannot write a `Collection<Product>` and have the language itself refuse to let a `Banana` sneak in. What PHP has instead is a well-worn convention, docblocks read by static analysis tools, that gets you most of the same safety, enforced not by the PHP runtime but by a separate program you run before you ship.

By the end of this chapter you'll know when to reach for an interface, when a trait is actually the right tool, and how to write PHP that behaves, for practical purposes, as if it had generics, even though, strictly speaking, it doesn't.
