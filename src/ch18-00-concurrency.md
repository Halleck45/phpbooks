# Concurrency in PHP: A Brief Tour

Here's an unusual thing to say in a programming book: you can skip this chapter, come back to it in a year, and lose nothing. Most PHP developers write years of production code, real code, serving real traffic, without ever touching a thread, a fiber, or a process fork. That's not a gap in their skills. It's how the language was designed to be used, and for the overwhelming majority of PHP work, from small business sites to large e-commerce platforms, it's still the right way to work.

That makes this chapter different from almost every other one in this book. Elsewhere, I've been telling you "this is something you'll use constantly, learn it well." Here, I'm telling you the opposite: this is an advanced, optional tour. Read it to understand why PHP behaves the way it does and what your options are when you eventually hit a case that needs more, not because you need any of it to write ordinary PHP applications.

So why include it at all? Because sooner or later you'll wonder why PHP doesn't have threads the way Java or C# does, or you'll need to send a welcome email without making the user wait for it. This chapter answers those questions at a level that lets you hold an intelligent conversation about them, and know what to search for when the day comes that you actually need more.

We'll look at two things: the request model that made explicit concurrency largely unnecessary in traditional PHP, and the everyday tools (queues, background processes) that PHP developers actually reach for when work needs to happen outside the request/response cycle.
