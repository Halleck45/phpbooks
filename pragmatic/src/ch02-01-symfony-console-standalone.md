# Command-Line Tools: Symfony/Console

The next time you run `composer require` or `php artisan migrate`, you are using Symfony's Console component. Composer and Laravel's Artisan are both built on it. None of that needs the rest of Symfony. **Console is a standalone package that turns a PHP class into a proper command-line tool**, with arguments, options, colored output, and progress bars, and nothing else attached.

```bash
composer require symfony/console
```

```php
<?php
// bin/console
require __DIR__.'/../vendor/autoload.php';

use Symfony\Component\Console\Application;
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

#[AsCommand(name: 'app:import-users', description: 'Import users from a CSV file')]
class ImportUsersCommand extends Command
{
    protected function configure(): void
    {
        $this->addArgument('file', InputArgument::REQUIRED, 'Path to the CSV file');
    }

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $rows = array_map('str_getcsv', file($input->getArgument('file')));
        $output->writeln(sprintf('<info>Imported %d rows.</info>', count($rows)));

        return Command::SUCCESS;
    }
}

$app = new Application('My Tool', '1.0.0');
$app->add(new ImportUsersCommand());
$app->run();
```

```bash
php bin/console app:import-users users.csv
```

## When to reach for this

Any job that someone runs by hand or from a cron entry: a data import, a cleanup task, a deploy step. It beats a raw PHP script the moment you need arguments, flags, or output a human has to read and trust.

## When it's the wrong fit

If the "script" is the beginning of a web application, or if you are already inside a Laravel or Symfony project, use `artisan` or the app's own `bin/console`. A second command-line entry point next to the first one helps nobody.

> **Under the hood:** Console commands are ordinary PHP classes with a `configure()` and an `execute()` method. There is no special runtime and no compiled binary, just the PHP interpreter you already have, pointed at a script instead of a browser request.
