# WordPress: WP-Cron and the Action Scheduler

WP-Cron is WordPress's built-in scheduling system, and it comes with a well-known quirk worth knowing before you rely on it: it doesn't run on a real system timer. Instead, it checks whether any scheduled task is due every time a visitor loads a page, which means a site with no traffic can silently stop running its scheduled tasks on time.

```php
add_action('daily_report_hook', function () {
    // generate and email the report
});

if (!wp_next_scheduled('daily_report_hook')) {
    wp_schedule_event(time(), 'daily', 'daily_report_hook');
}
```

The standard fix, for anything that actually matters, is disabling WordPress's page-load trigger and calling it from a real system cron job instead:

```php
// wp-config.php
define('DISABLE_WP_CRON', true);
```

```bash
# real crontab entry, running every 5 minutes
*/5 * * * * curl https://example.com/wp-cron.php?doing_wp_cron >/dev/null 2>&1
```

For anything beyond simple scheduled hooks, especially queued background work like sending bulk emails or processing an import, the **Action Scheduler** library (bundled with WooCommerce, but usable standalone) adds a proper queue with retries and logging on top of the same underlying idea:

```php
as_schedule_single_action(time(), 'process_import_batch', ['batch_id' => 42]);

add_action('process_import_batch', function ($batch_id) {
    // process it
});
```

## When to reach for this

WP-Cron with a real system crontab for anything time-sensitive: scheduled reports, subscription renewals, cache warming. Action Scheduler once you need retries, batching, or visibility into whether a background task actually succeeded.

## When it's the wrong fit

High-frequency or high-reliability background processing, where [Laravel's queue system](ch11-01-laravel-queues-horizon.md) or [Symfony Messenger](ch11-02-symfony-messenger.md), both built around a real queue backend from the start, offer a more solid foundation than WordPress's page-load-triggered model.

> **Under the hood:** WP-Cron's "check on every page load" design is a direct consequence of typical shared WordPress hosting historically not allowing users to configure real system cron jobs. It's a reasonable workaround for that constraint, not a design flaw exactly, but one worth overriding the moment your hosting does allow real cron.
