# Structuring a Small MVC-Style App

The previous section's router works, but it doesn't scale past a handful of routes: every route's logic lives inline, as a closure, tangled up with the routing itself. Real applications separate those concerns: the classic split is **Model, View, Controller**, usually shortened to MVC. We won't build a full framework's worth of it, but the shape is worth having: a **controller** decides what should happen for a given request, and a **view** decides how the result gets turned into HTML. Two or three routes are enough to see the pattern clearly.

## Controllers

A controller, at this scale, is nothing more exotic than a class whose methods each handle one route and return a response body as a string:

```php
<?php

class HomeController
{
    public function index(): string
    {
        return render('home', ['title' => 'Welcome']);
    }
}

class AboutController
{
    public function show(): string
    {
        return render('about', [
            'title' => 'About',
            'description' => 'A tiny PHP application, built without a framework.',
        ]);
    }
}
```

Nothing here talks to `$_SERVER` or knows what URI it was reached by: that's the router's job, not the controller's. Each method's only responsibility is producing a response, which keeps it easy to reason about, and easy to test in isolation.

## Views: PHP's original superpower

`render()` is where the view layer lives, and it's worth pointing out something PHP has been good at from the very start: PHP *is* a templating language underneath the programming language; that was literally its original purpose, before it grew everything else. A "view" here is just an ordinary PHP file with HTML in it and small islands of PHP for the dynamic parts, the same `<?php ... ?>`-in-HTML style you'd have used to build the very first pages this book showed you.

Create `views/home.php`. Unlike the other code samples in this book, this one is an HTML file with small islands of PHP in it, not a PHP file in its own right, so it doesn't open with `<?php`:

```html
<!DOCTYPE html>
<html>
<head><title><?= htmlspecialchars($title) ?></title></head>
<body>
    <h1><?= htmlspecialchars($title) ?></h1>
    <p>This page was rendered from views/home.php.</p>
</body>
</html>
```

And a small helper that includes a view file with data made available to it:

```php
<?php

function render(string $view, array $data = []): string
{
    extract($data);
    ob_start();
    include __DIR__ . "/views/{$view}.php";
    return ob_get_clean();
}
```

`extract()` turns each key of `$data` into a local variable: `'title' => 'Welcome'` becomes a variable `$title`, visible inside the included file. `ob_start()` and `ob_get_clean()` are output buffering: instead of letting the included file's HTML print straight to the browser, we capture it as a string and hand it back, so the controller can return it like any other value. Notice `<?= $title ?>` inside the view: the `<?= ?>` tag is shorthand for `<?php echo ?>`, and it's routed through `htmlspecialchars()` here specifically to avoid rendering user-influenced data as raw HTML.

## Wiring the router to controllers

Update `router.php` to dispatch to controller methods instead of inline closures:

```php
<?php

require __DIR__ . '/render.php';
require __DIR__ . '/controllers.php';

$uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

$routes = [
    '/' => [HomeController::class, 'index'],
    '/about' => [AboutController::class, 'show'],
];

if (isset($routes[$uri])) {
    [$class, $method] = $routes[$uri];
    echo (new $class())->{$method}();
} else {
    http_response_code(404);
    echo "404 Not Found: {$uri}";
}
```

The `$routes` array now maps each path to a `[class, method]` pair instead of a closure, destructured right there with `[$class, $method] = $routes[$uri]`, the syntax from [Chapter 17](ch17-02-destructuring.md). `new $class()` instantiates the controller, and `->{$method}()` calls the matching method on it. It's a small amount of machinery, but it's genuinely the same idea every framework's router is built on: look at the request, find a class and method responsible for it, call it, return what it gives you.
