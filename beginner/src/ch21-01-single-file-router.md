# A Single-File Router with PHP's Built-in Server

A browser asks for `/about`. Somewhere on the server, a piece of code has to answer. Which one? **The part of a web application that turns a URL into a piece of code is called a router**, and every framework has one, however large the framework. Before you use theirs, build the smallest one that could possibly work, so you can see exactly what it does.

## PHP's built-in development server

A request has to be received by a web server, and PHP has one hiding inside the `php` command itself. No Apache, no nginx, nothing to install. It is not made for production. For development, and for learning, it is exactly right:

```console
$ php -S localhost:8000 router.php
[Thu Aug 20 10:00:00 2026] PHP 8.3.0 Development Server (http://localhost:8000) started
```

That command starts a server on port 8000 and sends *every* incoming request through `router.php`. Nothing gets matched to a file on disk automatically. Your script decides, for each request, what to send back. Total visibility, which is exactly what we want.

## The router itself

Create `router.php`:

```php
<?php

$uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

$routes = [
    '/' => function (): string {
        return "Welcome to the home page.\n";
    },
    '/about' => function (): string {
        return "This is a tiny PHP application, built without a framework.\n";
    },
];

header('Content-Type: text/plain');

if (isset($routes[$uri])) {
    echo $routes[$uri]();
} else {
    http_response_code(404);
    echo "404 Not Found: {$uri}\n";
}
```

Read it from the top. **`$_SERVER['REQUEST_URI']` is where PHP puts the path the browser asked for**: `/`, `/about`, whatever was typed or clicked. `parse_url(..., PHP_URL_PATH)` cuts off any query string (`?foo=bar`), so `/about?ref=email` and `/about` land on the same route.

<img src="images/ch21-router-switchboard.png" alt="A request for /about arrives at a lookup table with one row per path; the matching row leads to the code that answers, and a bin at the bottom collects everything else as a 404" width="560">

Then `$routes` is an associative array, a plain lookup table: a path on the left, and on the right a closure that produces the response. **The router looks up the path; if it is a key we know, it calls the closure and echoes what comes back.** Otherwise it answers 404, the way any server does for a page that does not exist.

Try it, with the server still running in another terminal:

```console
$ curl http://localhost:8000/
Welcome to the home page.

$ curl http://localhost:8000/about
This is a tiny PHP application, built without a framework.

$ curl http://localhost:8000/nonexistent
404 Not Found: /nonexistent
```

Now add a route of your own: a `/contact` key with a closure returning any text you like. Save, and ask `curl` for it. No restart needed, since the server runs `router.php` fresh on every request.

## What this is (and isn't) doing

This router knows nothing about path parameters (`/users/{id}`), nothing about HTTP methods (`GET` versus `POST` at the same path), nothing about middleware. Real routers add all of that. Structurally, though, they do what these fifteen lines do: inspect something about the incoming request, and dispatch to a piece of code based on it.

> A router is a lookup table with a 404 at the bottom.

Fifteen lines are enough to see the mechanism. They are not enough to grow on: the moment each route needs real HTML, the closures in that array turn into a tangle. The next section gives each route a proper home.
