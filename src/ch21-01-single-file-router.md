# A Single-File Router with PHP's Built-in Server

<img src="images/ch21-icon.svg" alt="A Single-File Router with PHP's Built-in Server illustration" width="72">

Every web framework, no matter how large, is built on the same basic question: a request comes in for some URL: how does that turn into which piece of code runs? The mechanism that answers that question is called a **router**. Before reaching for a framework's version, it's worth building the smallest one that could possibly work, so you can see exactly what it's doing.

## PHP's built-in development server

PHP ships with a small web server built into the CLI binary itself: no Apache, no nginx, nothing to install. It's not meant for production, but it's genuinely useful for development and, here, for learning:

```console
$ php -S localhost:8000 router.php
[Thu Aug 20 10:00:00 2026] PHP 8.3.0 Development Server (http://localhost:8000) started
```

That command starts a server on port 8000 and routes *every* incoming request through `router.php`. Nothing about matching URLs to files happens automatically: your script decides, for every single request, what to do with it. That's exactly what we want: total visibility into the mechanism.

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

`$_SERVER['REQUEST_URI']` is where PHP puts the path the browser actually asked for: `/about`, `/`, whatever was typed or clicked. `parse_url(..., PHP_URL_PATH)` strips off any query string (`?foo=bar`), so `/about?ref=email` and `/about` both resolve to the same route. From there, `$routes` is just an associative array mapping a path to a closure that produces the response: look up the URI, and if it's a key we recognize, call the matching closure and echo whatever it returns. If it isn't, respond with a 404, the same way a real server would.

Try it:

```console
$ curl http://localhost:8000/
Welcome to the home page.

$ curl http://localhost:8000/about
This is a tiny PHP application, built without a framework.

$ curl http://localhost:8000/nonexistent
404 Not Found: /nonexistent
```

## What this is (and isn't) doing

This router has no path parameters (`/users/{id}`), no HTTP-method awareness (`GET` versus `POST` at the same path), and no middleware. Real routers add all of that, but structurally, they're doing exactly what's happening here: inspecting something about the incoming request, and dispatching to a piece of code based on it. You've just seen the entire mechanism laid bare, in about fifteen lines.

The next section grows this router into something shaped more like a real application, replacing these inline closures with proper controller classes and adding a view layer for the HTML they'll eventually need to produce.
