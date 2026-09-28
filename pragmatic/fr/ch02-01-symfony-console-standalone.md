# Outils en ligne de commande : Symfony/Console

La prochaine fois que vous lancerez `composer require` ou `php artisan migrate`, vous utiliserez le composant Console de Symfony. Composer et l'Artisan de Laravel sont tous deux construits dessus. Rien de tout cela n'exige le reste de Symfony. **Console est un paquet autonome qui transforme une classe PHP en véritable outil en ligne de commande**, avec arguments, options, sortie en couleur et barres de progression, et rien d'autre attaché.

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

## Quand le choisir

Tout travail que quelqu'un lance à la main ou depuis une entrée cron : un import de données, un nettoyage, une étape de déploiement. Il bat un script PHP brut dès qu'il vous faut des arguments, des options, ou une sortie qu'un humain doit lire et à laquelle il doit pouvoir se fier.

## Quand ce n'est pas le bon outil

Si le « script » est le début d'une application web, ou si vous êtes déjà dans un projet Laravel ou Symfony, utilisez `artisan` ou le `bin/console` de l'application. Un second point d'entrée en ligne de commande à côté du premier n'aide personne.

> **Sous le capot :** une commande Console est une classe PHP ordinaire avec une méthode `configure()` et une méthode `execute()`. Pas de runtime spécial, pas de binaire compilé, juste l'interpréteur PHP que vous avez déjà, pointé vers un script au lieu d'une requête de navigateur.
