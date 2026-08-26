# Handling Shutdown and Cleanup

Every PHP script, including the little application you've just built, ends somehow: normally, by running its last line, or abnormally, by a fatal error nobody planned for. Either way, there's often cleanup you want to guarantee happens: closing a file handle, logging that the request finished, flushing something to a database. `try`/`finally` (from [Chapter 9](ch09-00-error-handling.md)) handles the ordinary cases, but it can't save you from a genuine fatal error: the kind that stops execution dead, with no exception to catch. For that, PHP gives you a hook into the very end of the script's life.

## `register_shutdown_function()`

```php
<?php

register_shutdown_function(function (): void {
    echo "Cleaning up before the script ends.\n";
});

echo "Doing regular work.\n";

// Simulate something going badly wrong.
strlen(); // fatal error: too few arguments
```

```console
$ php shutdown_demo.php
Doing regular work.
Cleaning up before the script ends.
Fatal error: Uncaught ArgumentCountError: strlen() expects exactly 1 argument, 0 given...
```

Notice the order: PHP prints the cleanup message *before* the fatal error output, because the shutdown function runs at the true end of the request (after a normal return, after an uncaught exception, and after most fatal errors) regardless of how the script got there. You register a callback once, near the top of your application (or, more realistically, inside a framework's bootstrap code), and PHP guarantees it runs on the way out. It's the closest thing PHP has to "no matter what happens, run this last."

## Where a script's life actually ends

This ties directly back to [Chapter 16](ch16-01-request-model.md)'s shared-nothing request model. In the traditional PHP lifecycle, a script's "end" isn't a vague concept: it's the moment the response has been sent and the process (or thread) handling this one request is about to be recycled or torn down for the next request entirely. Everything that script allocated (variables, objects, open file handles PHP itself manages) is cleaned up as part of that teardown, shutdown functions included. There's no lingering process to leak memory into over time the way a long-running Node.js server can; each request gets a clean slate, and each request's mess, cleaned up or not, dies with it.

That's also why `register_shutdown_function()` matters more in PHP than the phrase "runs at the end" might suggest at first. It's not a background job, and it's not deferred to some later point the way a queued job from Chapter 16 is: it runs synchronously, inline, before this exact request's story is finished, which makes it the right place for things like "log that this request completed" or "release a lock this request was holding," and the wrong place for anything that should happen independently of this request at all.

## Where you've landed

Look back at what this final project actually used: a router built from an array and a handful of `if` statements, controllers that are just plain classes with methods, a view layer that leans on the same PHP-in-HTML style you saw on page one, and now a shutdown hook that closes the loop on a request's lifecycle. None of it required a framework. All of it *is*, in miniature, what a framework provides at scale.

That's a fitting place to leave you. You started this book with `echo "Hello, world!\n";` (about as small as a program can be) and you've ended it wiring together classes, namespaces, interfaces, error handling, and a request lifecycle into something that actually serves web pages. The syntax in between was never really the point; the point was building the judgment to reach for the right piece of it at the right moment. That judgment is the part no book can finish for you: it only comes from writing more PHP than you've written so far. Go write some.
