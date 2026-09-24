# WordPress : WP-Cron et l'Action Scheduler

WP-Cron est le planificateur intégré de WordPress, et il a une particularité à connaître avant de s'y fier. **Il ne tourne pas sur une horloge système : il vérifie s'il y a des tâches en retard à chaque fois qu'un visiteur charge une page.** Un site sans trafic peut cesser d'exécuter ses tâches planifiées à l'heure, sans prévenir.

```php
add_action('daily_report_hook', function () {
    // generate and email the report
});

if (!wp_next_scheduled('daily_report_hook')) {
    wp_schedule_event(time(), 'daily', 'daily_report_hook');
}
```

Le remède habituel, pour tout ce qui compte, consiste à désactiver le déclenchement au chargement de page et à appeler WP-Cron depuis un vrai cron système :

```php
// wp-config.php
define('DISABLE_WP_CRON', true);
```

```bash
# real crontab entry, running every 5 minutes
*/5 * * * * curl https://example.com/wp-cron.php?doing_wp_cron >/dev/null 2>&1
```

Au-delà des simples hooks planifiés, et surtout pour du travail en file comme un envoi d'e-mails en masse ou un import, la bibliothèque **Action Scheduler** ajoute une vraie file d'attente, avec relances et journal, sur la même idée. Elle est livrée avec WooCommerce et fonctionne aussi seule.

```php
as_schedule_single_action(time(), 'process_import_batch', ['batch_id' => 42]);

add_action('process_import_batch', function ($batch_id) {
    // process it
});
```

## Quand le choisir

WP-Cron avec un cron système pour tout ce qui a une contrainte horaire : rapports planifiés, renouvellements d'abonnement, préchauffage de cache. Action Scheduler dès que vous avez besoin de relances, de traitement par lots, ou d'un moyen de savoir si une tâche de fond a réussi.

## Quand ce n'est pas le bon outil

Les traitements en arrière-plan à haute fréquence ou à haute fiabilité. [Les files de Laravel](ch11-01-laravel-queues-horizon.md) et [Symfony Messenger](ch11-02-symfony-messenger.md) ont été bâtis dès le départ autour d'un vrai serveur de file, et reposent sur un sol plus ferme qu'un déclenchement au chargement de page.

> **Sous le capot :** le principe « vérifier à chaque chargement de page » de WP-Cron vient des hébergements mutualisés WordPress qui, historiquement, ne laissaient pas l'utilisateur configurer de cron système. C'est un contournement raisonnable de cette contrainte, pas un défaut de conception, et il faut le neutraliser dès que votre hébergement autorise un vrai cron.
