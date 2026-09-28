# Templating Without a Framework: League/Plates

The moment a script has to produce HTML instead of a JSON blob or a log line, `echo` statements mixed into the logic become unreadable fast. **Plates is a templating engine written in plain PHP: no new syntax**, just PHP files with layouts, sections, and automatic escaping, usable from any script.

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

`$this->e()` escapes output. It is the same protection Twig or Blade gives you, spelled out instead of hidden behind a different syntax.

## When to reach for this

A small internal tool, a report generator, or a script that renders a handful of HTML pages and doesn't justify a full framework's templating stack.

## When it's the wrong fit

Once a project grows components, includes, and more than a handful of pages. A framework's own engine (Blade in Laravel, Twig in Symfony) then earns its keep with component reuse and asset compilation, features Plates leaves out on purpose to stay small.

> **Under the hood:** Plates templates are PHP files, so there is no compile step and no template cache to reason about. That simplicity is the whole point of the library, and it is what a framework's own templating engine trades away in exchange for more features.
