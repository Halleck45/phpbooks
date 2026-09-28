# Laravel: Queues and Horizon

**Any slow or non-essential piece of a Laravel request can become a Job, pushed onto a queue and run by a separate worker process.** The user's request finishes at once instead of waiting on it.

```bash
php artisan make:job SendWelcomeEmail
```

```php
class SendWelcomeEmail implements ShouldQueue
{
    use Queueable;

    public function __construct(private User $user) {}

    public function handle(): void
    {
        Mail::to($this->user)->send(new WelcomeEmail($this->user));
    }
}

// dispatching it
SendWelcomeEmail::dispatch($user);
```

```bash
php artisan queue:work
```

That last command is the worker. A process manager such as Supervisor keeps it running; it pulls jobs off the queue (Redis, in most production setups) and executes them.

**Horizon** adds a dashboard on top of Redis queues: throughput, failed jobs, retry controls and per-queue metrics, with no separate monitoring tool.

```bash
composer require laravel/horizon
php artisan horizon:install
php artisan horizon
```

Failed jobs retry with backoff. The ones that fail for good land in a `failed_jobs` table for inspection instead of vanishing.

## When to reach for this

Anything that should not block a web request: sending email, processing an upload, calling a slow third-party API, generating a report. If a user would notice the delay, it belongs on a queue.

## When it's the wrong fit

Work that must complete before the response, such as validating a form before saving it. Queuing that adds latency and complexity where synchronous code was already correct.

> **Under the hood:** Jobs are serialized (usually with PHP's native `serialize()`) before being stored in the queue, which is why job classes should only hold simple, serializable properties like a model ID rather than large objects or open resources; the worker process deserializes and reconstructs the job from scratch when it runs.
