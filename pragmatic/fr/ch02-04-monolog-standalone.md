# Des logs qui marchent tout de suite : Monolog

Quand un script échoue hors du navigateur, sans personne pour le regarder, une ligne de log est la seule trace qu'il laisse. **Monolog est le logger que presque tous les frameworks PHP enveloppent** : la façade `Log` de Laravel et le service `logger` de Symfony sont l'un comme l'autre Monolog avec une façade plus aimable. Utilisez-le directement et chaque projet, avec ou sans framework, se retrouve avec des logs de la même forme.

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

Un seul logger écrit à plusieurs endroits à la fois : la console, un fichier avec rotation, un service comme Sentry (voir [Attraper l'erreur en production](ch14-05-sentry-flare-error-tracking.md)). Chaque destination est un handler de plus.

## Quand le choisir

Tout script ou service qui tourne hors d'un cycle requête-réponse : un worker de file d'attente, une tâche cron, un import en ligne de commande. Si personne ne fixe le terminal quand il échoue, il lui faut un log.

## Quand ce n'est pas le bon outil

Dans Laravel ou Symfony, utilisez la façade `Log` ou le service `logger` du framework. C'est Monolog dessous, déjà configuré avec des handlers raisonnables, et cohérent avec la façon dont le reste de l'application journalise.

> **Sous le capot :** Monolog implémente PSR-3, l'interface de journalisation standard qu'attendent la plupart des frameworks et bibliothèques PHP. C'est pour cela qu'une bibliothèque installée par `composer require` peut accepter « un logger » dans son constructeur sans se soucier de recevoir Monolog lui-même ou l'enveloppe d'un framework autour.
