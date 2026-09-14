# The PHP Request Model: Why PHP Is (Usually) Single-Threaded

If you've used Node.js or a Java application server before, you're used to a program that starts once, stays running, and handles every request that arrives while it's alive. State lives in memory between requests. A variable set while handling one user's request can, if you're not careful, still be sitting there when the next user's request comes in.

PHP, in its classic and still most common form, doesn't work that way. Every HTTP request gets a fresh start: the PHP process (or thread, depending on how your web server is configured) loads your script, runs it from the top, sends a response, and then throws everything away. Every variable, every object, every static property: gone. The next request, even the very next one, starts from absolute zero. Nothing is shared between requests except what you've deliberately put somewhere external: a database, a file, a cache like Redis or Memcached.

This is usually called a **shared-nothing** architecture, and it's the single biggest structural difference between PHP and languages built around long-running server processes. It's baked into how PHP is typically run: under PHP-FPM (the FastCGI Process Manager, the standard way to run PHP behind nginx or Apache in production), a pool of PHP worker processes sits ready, and each incoming request is handed to one of them for exactly as long as it takes to produce a response. When you ran `php hello.php` back in Chapter 1, you saw the same lifecycle in miniature: the interpreter starts, runs your script top to bottom, and exits.

## Why this made threading unnecessary

Threads exist to let one running program do several things at once, safely, while sharing memory. But if your "program" only ever handles one request from start to finish and then vanishes, there's rarely anything to make concurrent *within* it. The concurrency PHP applications need, handling thousands of simultaneous users, is handled a level up, by running many PHP processes side by side, not by making a single PHP process juggle many things internally. Your web server and process manager are already doing the hard part.

This has real, practical upsides. You don't need to reason about race conditions inside a single request the way you would in a multi-threaded Java servlet: two users can't corrupt each other's `$_SESSION` data by both writing to the same variable at once, because there is no shared variable; each gets an entirely separate execution. Entire categories of bugs that plague long-running, shared-memory server processes simply don't arise in classic PHP, because the model rules them out from the start rather than asking you to avoid them through discipline.

## Where it stops being the whole story

None of this means PHP *can't* share state or run things concurrently; it means that, by default, it doesn't, and traditional PHP web applications were designed around that constraint rather than fighting it. A few things are worth flagging as exceptions, which we'll return to shortly:

- Work that needs to happen but shouldn't hold up the response (sending an email, resizing an uploaded image) is typically pushed to a separate process, not run inline.
- Long-running PHP processes do exist: command-line daemons, queue workers, and newer tools like Swoole servers keep a process alive across many units of work, and *there* the shared-nothing guarantee no longer applies automatically.
- Opcache, PHP's bytecode cache, does share compiled code across requests for performance, but that's compiled code, not your application's runtime state.

The next section looks at how PHP applications actually get concurrent-ish work done in practice, without ever needing a thread.
