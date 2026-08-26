# Background Work with Queues and Processes

So a request comes in, PHP handles it, and the process disappears when the response is sent. That's fine for "look up this user and render their profile." It's a problem for "resize this uploaded image, generate three thumbnails, and email a confirmation": nobody wants to stare at a spinner for eight seconds because your code is doing image processing before it can say "Upload successful." The user doesn't need to wait for that work to finish. They just need to know it's been accepted.

The standard PHP answer is: don't do it now. Do it *later*, in a different process.

## Job queues

The pattern looks like this: instead of doing the slow work inline, the request handler packages up what needs to happen, "resize image #482 for user #17," as a small message, and pushes that message onto a queue. Then it responds to the user immediately: "Upload received, processing." Meanwhile, one or more separate PHP processes, called **workers**, sit in a loop watching that queue. As soon as a message appears, a worker picks it up and does the actual work, entirely disconnected from the original request.

The queue itself is usually backed by something built for exactly this job: Redis is a common, lightweight choice; RabbitMQ and Amazon SQS show up in larger systems. PHP frameworks like Laravel and Symfony ship queue abstractions on top of these so you're not hand-rolling the plumbing, but the underlying idea is simple enough that you could build a crude version yourself with nothing more than a database table and a `SELECT ... WHERE processed = false`.

The workers are ordinary PHP, run from the command line, typically kept alive by a process supervisor:

```console
$ php worker.php
Waiting for jobs...
Processing job: resize-image #482
Done.
Waiting for jobs...
```

That worker script loops indefinitely, checking the queue, handling whatever it finds, and looping again: a long-running PHP process, which is exactly the kind of thing that steps outside the shared-nothing model from the previous section. It keeps state (a database connection, maybe a cache of configuration) across many jobs, the way a Node.js server would across many requests.

## Spinning up a separate process directly

Queues are the right tool when you have many small units of work arriving over time. Sometimes what you actually want is simpler: "run this other program right now, and don't wait around for it, or wait, but let it run alongside something else I'm doing." For that, PHP can launch operating-system processes directly.

`proc_open()` is the general-purpose tool for this: it starts an external command (which might itself be another PHP script) and gives you handles to its input, output, and error streams, so you can talk to it while it runs. It's what powers things like Composer's own internal process handling.

There's also the `pcntl` extension, which lets a PHP script fork itself into multiple copies (`pcntl_fork()`), genuinely running PHP code in parallel, as separate OS processes, each with its own memory. It's powerful and, honestly, a little unforgiving: forking is only available on Unix-like systems, not Windows, and reasoning about multiple processes correctly takes real care. It shows up in command-line tools and daemons more than in web applications.

Both are worth knowing exist. Neither is something you should reach for before a job queue, which solves the same underlying problem, "run this later, not now," with far less to get wrong.
