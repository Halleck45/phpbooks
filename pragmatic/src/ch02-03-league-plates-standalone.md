# Templating Without a Framework: League/Plates

The moment a script needs to produce HTML instead of a JSON blob or a log line, mixing `echo` statements into PHP logic gets unreadable fast. Plates is a native-PHP templating engine: no new syntax to learn, just plain PHP files with layouts, sections, and automatic escaping, usable in any script.

```bash
composer require league/plates
```

```php
<?php
require 'vendor/autoload.php';

use League\Plates\Engine;

$templates = new Engine(__DIR__ . '/templates');

echo $templates->render('profile', ['name' => 'Ada']);
```

```php
<?php // templates/layout.php ?>
<!doctype html>
<html>
<head><title><?= $this->e($title ?? 'My Site') ?></title></head>
<body>
    <?= $this->section('content') ?>
</body>
</html>
```

```php
<?php // templates/profile.php ?>
<?php $this->layout('layout', ['title' => 'Profile']) ?>

<?php $this->start('content') ?>
    <h1>Hello, <?= $this->e($name) ?></h1>
<?php $this->stop() ?>
```

`$this->e()` escapes output automatically, the same protection Twig or Blade gives you, just spelled out explicitly instead of hidden behind different syntax.

## When to reach for this

A small internal tool, a report generator, or a script that renders a handful of HTML pages and doesn't warrant installing a full framework's templating stack.

## When it's the wrong fit

Once a project grows components, includes, and more than a handful of pages, a framework's own templating engine (Blade in Laravel, Twig in Symfony) earns its keep with features like component reuse and asset compilation that Plates deliberately leaves out to stay small.

> **Under the hood:** Because Plates templates are just PHP files, there's no separate compile step or template cache to reason about. That simplicity is the entire point of the library, and it's also exactly what a framework's own templating engine trades away in exchange for more features.
