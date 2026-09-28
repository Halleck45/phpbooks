# WordPress: WP-Cron and the Action Scheduler

WP-Cron is WordPress's built-in scheduler, and it has a quirk to know before you rely on it. **It does not run on a system timer: it checks for due tasks every time a visitor loads a page.** A site with no traffic can quietly stop running its scheduled tasks on time.

```php
add_action('daily_report_hook', function () {
    // generate and email the report
});

if (!wp_next_scheduled('daily_report_hook')) {
    wp_schedule_event(time(), 'daily', 'daily_report_hook');
}
```

The standard fix, for anything that matters, is to disable the page-load trigger and call it from a system cron job instead:

```php
// wp-config.php
define('DISABLE_WP_CRON', true);
```

```bash
# real crontab entry, running every 5 minutes
*/5 * * * * curl https://example.com/wp-cron.php?doing_wp_cron >/dev/null 2>&1
```

Beyond simple scheduled hooks, and especially for queued work such as bulk emails or an import, the **Action Scheduler** library adds a proper queue with retries and logging on the same idea. It ships with WooCommerce and works standalone.

```php
as_schedule_single_action(time(), 'process_import_batch', ['batch_id' => 42]);

add_action('process_import_batch', function ($batch_id) {
    // process it
});
```

## When to reach for this

WP-Cron with a system crontab for anything time-sensitive: scheduled reports, subscription renewals, cache warming. Action Scheduler once you need retries, batching, or a way to see whether a background task succeeded.

## When it's the wrong fit

High-frequency or high-reliability background processing. [Laravel's queues](ch11-01-laravel-queues-horizon.md) and [Symfony Messenger](ch11-02-symfony-messenger.md) were built around a queue backend from the start, and stand on firmer ground than a page-load trigger.

> **Under the hood:** WP-Cron's "check on every page load" design comes from shared WordPress hosting that historically did not let users configure system cron jobs. It is a reasonable workaround for that constraint rather than a design flaw, and one to override the moment your hosting allows real cron.
