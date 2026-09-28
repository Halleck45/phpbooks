# Shipping Background Work

Send the confirmation email later. Resize the uploaded image later. Generate the monthly report at 2 a.m. with nobody watching. Anything that should not block the user's request, or that runs on a schedule rather than in response to one, is background work. **Doing it well means a queue and a worker process, not a `sleep()` call and hope.**

<img src="images/ch11-kitchen-rail.png" alt="A restaurant in cross-section. At the front counter, a small elephant hands a person a receipt at once. In the kitchen behind, a rail of order tickets and two elephants in chef hats working through them one by one" width="560">

- [Laravel: Queues and Horizon](ch11-01-laravel-queues-horizon.md): jobs on a queue, a worker to run them, and a dashboard to watch them.
- [Symfony: The Messenger Component](ch11-02-symfony-messenger.md): one message bus for background jobs and for talking between services.
- [WordPress: WP-Cron and the Action Scheduler](ch11-03-wordpress-wp-cron-action-scheduler.md): what WordPress uses for scheduled tasks, its well-known quirk, and the fix.
