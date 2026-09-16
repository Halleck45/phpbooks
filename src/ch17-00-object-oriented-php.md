# Object-Oriented PHP

Open a framework, a library, almost any PHP file written by someone else, and you will find classes that build on other classes. Chapter 5 taught you to write a class. Chapter 11 taught you to make unrelated classes promise the same thing with an interface. **This chapter is where those pieces become a design.**

One example runs through the whole chapter: a shop that accepts several kinds of payment. A credit card and a PayPal account do the same job in different ways, and that is precisely the situation object-oriented design was invented for. You make one class build on another with `extends`, override what needs to change while keeping the rest with `parent::`, and then reach the payoff. Code written once against the general idea of a payment method works with every specific kind you hand it, including the kinds you have not written yet. That property has a name, polymorphism, and it is the reason inheritance exists.

Abstract classes and interfaces then get placed side by side. They solve overlapping problems, and choosing between them is a design decision, not a matter of taste.

The second half of the chapter turns to PHP's magic methods, a handful of specially named methods the language calls on its own when an object is printed, used like a string, or asked for a property it does not have. Some are everyday tools. Others make code harder to read than the boilerplate they save, and the chapter says which is which.

The payment example ends up assembled into a classic design pattern, Strategy, using nothing but the interfaces and polymorphism you already have in hand. Patterns have a reputation for being abstract. Watching one come together from familiar pieces, to solve a problem you actually meet, should put that reputation to rest.
