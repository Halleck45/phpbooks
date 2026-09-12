# Validating Input and Preventing Cross-Site Scripting

<img src="images/ch10-icon.svg" alt="Validating Input and Preventing Cross-Site Scripting illustration" width="72">

The previous section left off with a script that prints `$_POST` values straight into HTML, and a demonstration that this lets a visitor's browser render arbitrary markup. Pushed a little further, that's not just an oddity: submit `<script>alert('hello from your own guestbook')</script>` as a message, and the browser executes it. That's **cross-site scripting**, XSS for short: an attacker gets their own JavaScript to run in your page, in your visitors' browsers, under your site's own trust. A guestbook that stores and redisplays messages is a textbook place for it to happen, which makes it a good place to learn to stop it.

## Escaping output

The fix isn't to reject angle brackets outright: it's to make sure any user-supplied text that ends up inside HTML is *escaped* first, so a browser displays it as text rather than parsing it as markup. PHP's tool for this is `htmlspecialchars()`, which converts the characters that matter to an HTML parser (`<`, `>`, `&`, and quotes) into their entity equivalents (`&lt;`, `&gt;`, `&amp;`, and so on):

```php
<?php if ($submitted) { ?>
    <p>Thanks, <?= htmlspecialchars($name) ?>. You wrote: <?= htmlspecialchars($message) ?></p>
<?php } ?>
```

Submit `<script>...</script>` again, and the page now shows the literal text `<script>alert('hello from your own guestbook')</script>` instead of running it. Since PHP 8.1, `htmlspecialchars()` defaults to escaping quotes as well as angle brackets, which is what you want almost every time: the rule worth keeping is simple. **Any value that came from outside your script, printed anywhere inside HTML, goes through `htmlspecialchars()` first, with no exceptions carved out for values that "probably" are safe.** A name field looks harmless right up until someone tests it with a `<script>` tag.

## Validating before you trust the data at all

Escaping protects the *output*. Validation is a separate concern: deciding whether the *input* is even acceptable before your script does anything with it. Expand the form handling to check for problems and collect them:

```php
<?php

$name = '';
$message = '';
$submitted = false;
$errors = [];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name'] ?? '');
    $message = trim($_POST['message'] ?? '');
    $submitted = true;

    if ($name === '') {
        $errors[] = 'Name cannot be empty.';
    } elseif (mb_strlen($name) > 60) {
        $errors[] = 'Name is too long.';
    }

    if ($message === '') {
        $errors[] = 'Message cannot be empty.';
    } elseif (mb_strlen($message) > 500) {
        $errors[] = 'Message is too long.';
    }
}
?>
```

`trim()` clears leading and trailing whitespace, so a message that's nothing but spaces doesn't slip through the empty check. `mb_strlen()`, rather than plain `strlen()`, counts characters rather than bytes, which matters the moment a visitor's name includes anything outside plain ASCII: the same UTF-8 concern [Chapter 8](ch08-02-strings.md) covered for strings generally applies here. Errors accumulate in an array instead of stopping at the first one, so a visitor sees every problem at once rather than fixing them one submission at a time.

Show the errors, and redisplay the submitted values (escaped, same as before) so nobody has to retype a long message just because their name was too short:

```php
<?php if ($errors) { ?>
    <ul>
        <?php foreach ($errors as $error) { ?>
            <li><?= htmlspecialchars($error) ?></li>
        <?php } ?>
    </ul>
<?php } elseif ($submitted) { ?>
    <p>Thanks, <?= htmlspecialchars($name) ?>. You wrote: <?= htmlspecialchars($message) ?></p>
<?php } ?>

<form method="post">
    <p><label>Name: <input type="text" name="name" value="<?= htmlspecialchars($name) ?>"></label></p>
    <p><label>Message: <textarea name="message"><?= htmlspecialchars($message) ?></textarea></label></p>
    <p><button type="submit">Sign the guestbook</button></p>
</form>
```

Notice `value="<?= htmlspecialchars($name) ?>"` inside the `<input>` tag: escaping matters just as much inside an HTML attribute as it does in the page body, since a stray `"` in an unescaped value would let a visitor break out of the attribute and inject their own.

## A related risk worth naming

XSS is about a visitor's browser running an attacker's script inside your page. A different, related risk is **CSRF**, cross-site request forgery, where a different site tricks a visitor's browser into submitting a form to *your* site on their behalf, using whatever session they're already logged into. Defending against it properly, typically a hidden token generated per form and checked on submission, is beyond what this small guestbook needs, but it's worth knowing the term exists for the day you're building something where a forged submission would actually matter.

The guestbook now behaves safely for a single request: it validates what comes in, and escapes what goes back out. What it still doesn't do is remember anything. Reload the page and every message is gone, because nothing has been stored anywhere. That's next.
