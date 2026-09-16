# Logging That Just Works: Monolog

When something goes wrong in a script that isn't running in a browser, with no one watching, a log line is the only trace it leaves. Monolog is the logging library nearly every PHP framework wraps internally: Laravel's `Log` facade and Symfony's `logger` service are both Monolog with a friendlier front end. Using it directly means every project, framework or not, ends up with logs shaped the same way.

```bash
composer require monolog/monolog
```

```php
<?php
require 'vendor/autoload.php';

use Monolog\Logger;
use Monolog\Handler\StreamHandler;
use Monolog\Handler\RotatingFileHandler;

$log = new Logger('import-job');
$log->pushHandler(new StreamHandler('php://stdout', Logger::INFO));
$log->pushHandler(new RotatingFileHandler(__DIR__ . '/logs/import.log', 14, Logger::DEBUG));

$log->info('Import started', ['file' => 'users.csv']);

try {
    // ... do the work ...
} catch (\Throwable $e) {
    $log->error('Import failed', ['exception' => $e]);
}
```

A single logger can write to several places at once: the console, a rotating file, or a service like Sentry (see [Catching It in Production](ch14-05-sentry-flare-error-tracking.md)), just by adding another handler.

## When to reach for this

Any script or service running outside a request/response cycle: a queue worker, a cron job, a CLI import. If nobody's staring at the terminal when it fails, it needs a log.

## When it's the wrong fit

Inside Laravel or Symfony, use the framework's own `Log` facade or `logger` service. They're Monolog underneath, already configured with sensible handlers, and consistent with how the rest of the app logs.

> **Under the hood:** Monolog implements PSR-3, the standard logging interface most PHP frameworks and libraries expect. That's why a library you `composer require` can accept "a logger" as a constructor argument without caring whether it's Monolog directly or a framework's wrapper around it.
