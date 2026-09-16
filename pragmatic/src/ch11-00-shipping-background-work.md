# Shipping Background Work

Sending the confirmation email later, resizing the uploaded image later, generating the monthly report at 2 a.m. without a human watching: anything that shouldn't block the user's request, or that needs to happen on a schedule rather than in response to one, is background work. Doing this well means a queue and a worker process, not a `sleep()` call and hope.

- [Laravel: Queues and Horizon](ch11-01-laravel-queues-horizon.md) covers Laravel's job queue system and its dashboard for monitoring it.
- [Symfony: The Messenger Component](ch11-02-symfony-messenger.md) covers Symfony's message bus, built for both background jobs and inter-service messaging.
- [WordPress: WP-Cron and the Action Scheduler](ch11-03-wordpress-wp-cron-action-scheduler.md) covers what WordPress uses for scheduled tasks, and its well-known quirks.
