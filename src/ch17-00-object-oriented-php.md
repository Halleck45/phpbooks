# Object-Oriented PHP

<img src="images/ch17-icon.svg" alt="Object-Oriented PHP illustration" width="72">

Chapter 5 gave you the basics of classes: properties, constructors, methods. Chapter 11 added interfaces and traits, PHP's tools for sharing behavior across otherwise unrelated classes. Both were necessary groundwork, and neither one was the main event. This chapter is the main event: real object-oriented design, the kind you'll actually use every day writing PHP, because it's genuinely core to how the language and its ecosystem work: the frameworks you'll eventually reach for, the libraries you'll install, most of the code you'll read that someone else wrote, all of it leans on the ideas in this chapter.

We'll start with `extends` (one class building on another, overriding what it needs to while calling back into the parent's own implementation with `parent::method()`) and with the payoff that makes inheritance worth the trouble in the first place: polymorphism, where code written against a general type works correctly on any specific subclass you hand it, without modification. From there we'll go back to interfaces, this time putting them directly next to abstract classes and asking, honestly, when each one is the right tool: they solve overlapping problems, and knowing which to reach for is a real design skill, not a matter of taste.

The second half of the chapter covers PHP's magic methods: a small set of specially named methods the language calls automatically in specific situations, letting an object behave like a string, or a function, or something with dynamic properties. Some of these are genuinely useful defaults you'll reach for often. Others are powerful enough to make code harder to follow if you lean on them too heavily, and we'll be direct about which is which.

We'll close by building one classic design pattern from scratch, in idiomatic PHP, using nothing more exotic than the interfaces and polymorphism covered earlier in the chapter. Patterns get a reputation for being abstract and academic; seeing one assembled from pieces you already understand, solving a problem you'd actually run into, should put that reputation to rest.
