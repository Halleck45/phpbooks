# Final Project: Building a Simple Web Application

Time to put it all together. Over the last eighteen chapters you've picked up classes and constructor promotion, namespaces and Composer, arrays and collections, exceptions, interfaces: a real working vocabulary of modern PHP. This chapter's project is where those pieces stop being separate lessons and become one small, coherent thing: a tiny web application, built from nothing but PHP itself.

There's no framework here, deliberately. Not because frameworks are bad (you'll likely use Laravel or Symfony professionally, and you should) but because using one before you've built something without it means taking its conveniences on faith. A router, a controller, a view: these are just words for patterns that fall naturally out of solving the same small problems every web application faces. Build them yourself once, at this small scale, and everything a framework does later will read as "oh, that's the thing I already understand," rather than as magic.

We'll start with the simplest possible router: a single file, PHP's own built-in development server, and a few `if` statements deciding what to send back. Then we'll grow that into something shaped like MVC, with real controller classes and PHP's original superpower, templating, put to proper use. Finally, we'll look at how a request's lifecycle actually ends, and use that moment to run cleanup code reliably, which ties back directly to the request model from [Chapter 16](ch16-01-request-model.md).

By the end, you'll have a working application in well under two hundred lines of code, and a clear-eyed sense of what's actually happening underneath the frameworks you'll reach for next.
