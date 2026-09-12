# Talking to a Database with PDO

<img src="images/ch10-icon.svg" alt="Talking to a Database with PDO illustration" width="72">

Every request to `guestbook.php` starts from nothing: PHP, in its classic and still most common form, gives each incoming request a fresh start, running the script from the top and throwing everything away once the response is sent, variables included. Nothing carries over from the last request except what was deliberately saved somewhere. So far, nothing has been. To make messages outlive the request that submitted them, they need to live somewhere PHP can read them back later: a database. ([Chapter 18](ch18-01-request-model.md) covers this shared-nothing request model properly, including why it means PHP rarely needs threads.)

## PDO and SQLite

PHP talks to databases through several extensions, but **PDO**, the PHP Data Objects extension, is worth reaching for first: it gives you one consistent interface across different database engines, so the same code style works whether the data underneath is MySQL, PostgreSQL, or, as here, **SQLite**. SQLite stores an entire database as a single ordinary file, with no separate server process to install or configure, which makes it the right choice for keeping this chapter's "connected technologies" as simple as the PHP itself.

Open a connection near the top of `guestbook.php`:

```php
<?php

$pdo = new PDO('sqlite:' . __DIR__ . '/guestbook.db');
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$pdo->exec('
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        message TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
');
```

`'sqlite:' . __DIR__ . '/guestbook.db'` is a DSN, a data source name, telling PDO which driver to use and where the database lives; the file is created automatically the first time this runs if it doesn't exist yet. `PDO::ATTR_ERRMODE` set to `PDO::ERRMODE_EXCEPTION` is worth setting every time: without it, PDO fails some operations silently, returning `false` instead of raising anything, which is exactly the kind of quiet failure [Chapter 9](ch09-00-error-handling.md) warned against. With it, a bad query throws a `PDOException`, catchable like any other. `CREATE TABLE IF NOT EXISTS` means this line is safe to leave in the script and run on every single request: it does nothing once the table already exists.

## The wrong way to build a query

Before writing the insert, look at the version to avoid:

```php
// Don't do this.
$pdo->exec("INSERT INTO entries (name, message, created_at) VALUES ('$name', '$message', '" . date('c') . "')");
```

If `$message` contains a single quote followed by SQL of an attacker's choosing, that SQL becomes part of the query PHP actually runs: a classic **SQL injection**, in the same family of bug as the XSS from the previous section, just aimed at your database instead of a visitor's browser. String-building a query out of untrusted values is never safe, no matter how carefully the string looks assembled.

## Prepared statements

PDO's real answer is a **prepared statement**: the query's structure is sent to the database first, with placeholders standing in for values, and the actual values are sent separately afterward. The database never treats a value as part of the query's syntax, which closes off injection entirely:

```php
if ($submitted && !$errors) {
    $statement = $pdo->prepare(
        'INSERT INTO entries (name, message, created_at) VALUES (:name, :message, :created_at)'
    );
    $statement->execute([
        'name' => $name,
        'message' => $message,
        'created_at' => date('c'),
    ]);
}
```

`:name`, `:message`, and `:created_at` are named placeholders; `execute()` takes an associative array matching each placeholder to its value. `prepare()` builds the statement once, `execute()` runs it with a specific set of values, and PDO handles quoting and escaping correctly for whatever database is underneath, which is exactly the part that's easy to get wrong by hand.

## Listing what's been said so far

Reading the entries back uses the same `prepare()`-and-`execute()` shape, or, for a query with no values to insert, the simpler `query()`:

```php
$entries = $pdo->query('SELECT name, message, created_at FROM entries ORDER BY id DESC')
    ->fetchAll(PDO::FETCH_ASSOC);
```

`fetchAll(PDO::FETCH_ASSOC)` returns every row as an array of associative arrays, one per row, each key matching a column name: the same shape of data [Chapter 8](ch08-03-associative-arrays.md) already showed you how to work with. Loop over it in the HTML, escaping each value exactly as before:

```php
<h2>Previous entries</h2>
<ul>
    <?php foreach ($entries as $entry) { ?>
        <li>
            <strong><?= htmlspecialchars($entry['name']) ?></strong>:
            <?= htmlspecialchars($entry['message']) ?>
            <em>(<?= htmlspecialchars($entry['created_at']) ?>)</em>
        </li>
    <?php } ?>
</ul>
```

Escaping still applies here, and for the same reason as before: these values came from a visitor, by way of the database, and the database doesn't know or care whether they're safe to print as HTML. Storing a value safely and displaying it safely are two separate jobs, and skipping either one reopens exactly the hole the last section closed.

## What you've built

Reload the guestbook, sign it a few times, and restart `php -S` entirely: the entries are still there, because they never lived in memory in the first place, just in `guestbook.db`, on disk, independent of any one request. That's the whole shape of a real, if tiny, web application: accept input through superglobals, validate it, escape it on the way back out, and persist it safely through prepared statements. The final project, next, builds something structurally larger on the same foundation: more routes, real controller classes, a proper view layer, but nothing about the underlying ideas changes. You've already done the part that actually matters.
