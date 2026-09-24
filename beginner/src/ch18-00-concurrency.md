# Concurrency in PHP: A Brief Tour

You can skip this chapter, come back to it in a year, and lose nothing.

That is an unusual thing to read in a programming book, so here is why it is true. Most PHP developers write years of production code, real code serving real traffic, without ever touching a thread, a fiber, or a process fork. That is not a gap in their skills. **PHP was designed so that ordinary applications never have to deal with concurrency themselves**, and for the vast majority of PHP work, from a small business site to a large online shop, that is still the right approach.

So this chapter is different from the others. Elsewhere, the book says "you will use this constantly, learn it well". Here it says the opposite: this is a short, optional tour. Nothing in it is needed to write everyday PHP.

Why include it at all? Because sooner or later, two questions come up. Why doesn't PHP have threads the way Java or C# do? And how do you send a welcome email without making the user wait for it? The two questions share an answer, and it takes two short sections to give it: first [the request model](ch18-01-request-model.md), which made explicit concurrency largely unnecessary in PHP, then [queues and background processes](ch18-02-queues-and-processes.md), the everyday tools PHP developers reach for when work has to happen outside the request.

> Nothing here is required. Read it out of curiosity, or keep it for the day you need it.

Either way, you will come out knowing why PHP behaves the way it does, what your options are when the request model is not enough, and what to search for when you need more.
