# Logging That Just Works: Monolog

When a script fails outside a browser, with nobody watching, a log line is the only trace it leaves. **Monolog is the logger nearly every PHP framework wraps**: Laravel's `Log` facade and Symfony's `logger` service are both Monolog with a friendlier front end. Use it directly and every project, framework or not, ends up with logs shaped the same way.

```bash
composer require monolog/monolog
```

```php
<?php
require 'vendor/autoload.php';

use Monolog\Level;
use Monolog\Logger;
use Monolog\Handler\StreamHandler;
use Monolog\Handler\RotatingFileHandler;

$log = new Logger('import-job');
$log->pushHandler(new StreamHandler('php://stdout', Level::Info));
$log->pushHandler(new RotatingFileHandler(__DIR__ . '/logs/import.log', 14, Level::Debug));

$log->info('Import started', ['file' => 'users.csv']);

try {
    // ... do the work ...
} catch (\Throwable $e) {
    $log->error('Import failed', ['exception' => $e]);
}
```

One logger writes to several places at once: the console, a rotating file, a service like Sentry (see [Catching It in Production](ch14-05-sentry-flare-error-tracking.md)). Each destination is one more handler.

## When to reach for this

Any script or service that runs outside a request and response cycle: a queue worker, a cron job, a CLI import. If nobody is staring at the terminal when it fails, it needs a log.

## When it's the wrong fit

Inside Laravel or Symfony, use the framework's own `Log` facade or `logger` service. They are Monolog underneath, already configured with sensible handlers, and consistent with how the rest of the app logs.

> **Under the hood:** Monolog implements PSR-3, the standard logging interface most PHP frameworks and libraries expect. That is why a library you `composer require` can accept "a logger" in its constructor without caring whether it gets Monolog itself or a framework's wrapper around it.
