# Accepting Input with HTML Forms and Superglobals

PHP has no special syntax for "this script is a web page." What it has instead is a handful of arrays that PHP fills in for you before a single line of your code runs, populated from whatever the browser sent along with the request. Those arrays are called **superglobals**, and they're available in every scope without needing `global` or a parameter: no importing, no passing them around, just there.

## A plain HTML form

Start with the form itself. Create `guestbook.php`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Guestbook</title>
    <style>
        body { font-family: sans-serif; max-width: 40em; margin: 2em auto; }
        textarea { width: 100%; }
    </style>
</head>
<body>
    <h1>Guestbook</h1>

    <form method="post">
        <p><label>Name: <input type="text" name="name"></label></p>
        <p><label>Message: <textarea name="message"></textarea></label></p>
        <p><button type="submit">Sign the guestbook</button></p>
    </form>
</body>
</html>
```

Nothing here is PHP yet: it's a `<form>` with `method="post"` and no `action` attribute, which means submitting it sends a `POST` request back to this same URL. `method="get"` is the other common choice, and the difference matters: a `GET` request encodes its data right in the URL (`?name=Alice`), visible in the address bar and in server logs, fine for a search box, wrong for anything sensitive or anything that changes data. A guestbook entry is exactly the kind of thing that belongs in a `POST` body instead.

Serve it with PHP's built-in development server:

```console
$ php -S localhost:8000 guestbook.php
```

Visit `http://localhost:8000` and the form renders, but submitting it does nothing yet: the same page reloads, and whatever you typed is gone. Reading what was submitted is PHP's job, and it hasn't been asked to do it yet.

## Superglobals: `$_GET`, `$_POST`, `$_SERVER`

Three superglobals matter most for a script like this one:

- `$_GET`: an associative array of query-string parameters, populated for any request, but conventionally read on `GET` requests.
- `$_POST`: an associative array of the form fields submitted in a `POST` request's body.
- `$_SERVER`: information about the request and the server itself. `$_SERVER['REQUEST_METHOD']` (`'GET'` or `'POST'`) is what lets one script handle both showing a blank form and processing a submitted one.

There's also `$_REQUEST`, which merges `$_GET`, `$_POST`, and cookie data together. It's convenient and best avoided: your script ends up unable to tell whether a value arrived in the URL or the request body, which matters more than it sounds like it should once security is on the table, in the next section.

## Reading the submission

Add PHP to the top of `guestbook.php`, before the `<!DOCTYPE html>` line:

```php
<?php

$name = '';
$message = '';
$submitted = false;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = $_POST['name'] ?? '';
    $message = $_POST['message'] ?? '';
    $submitted = true;
}
?>
```

The null coalescing operator `??` (from [Chapter 3](ch03-02-data-types.md)) covers the case where a field is missing entirely: a request forged by hand, or a browser quirk, shouldn't produce an "undefined array key" warning. Then, further down the file, show the submission when there is one:

```php
<body>
    <h1>Guestbook</h1>

    <?php if ($submitted) { ?>
        <p>Thanks, <?= $name ?>. You wrote: <?= $message ?></p>
    <?php } ?>

    <form method="post">
```

Reload, fill in the form, and submit it: the page now greets you back with exactly what you typed. Try `curl` instead of a browser, to see the request itself:

```console
$ curl -X POST -d "name=Alice&message=Hello there" http://localhost:8000/
```

The response includes `Thanks, Alice. You wrote: Hello there`, the same greeting, built entirely from `$_POST`.

## The problem you can already see coming

That last `echo`, by way of `<?= ?>`, prints `$name` and `$message` straight into the page, completely unfiltered. Try submitting `<b>bold</b>` as your name. It renders as bold text, not literal angle brackets, which means the guestbook is currently willing to run *any* HTML a visitor types, not just yours. The next section deals with exactly that, before anything gets stored anywhere permanent.
