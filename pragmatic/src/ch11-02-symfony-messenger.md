# Symfony: The Messenger Component

Messenger is Symfony's message bus: the same abstraction handles background jobs (like Laravel's queues) and messaging between different parts of an application, or even between separate services, through one consistent interface.

```bash
composer require symfony/messenger
```

```php
final class SendWelcomeEmail
{
    public function __construct(public readonly int $userId) {}
}

#[AsMessageHandler]
final class SendWelcomeEmailHandler
{
    public function __invoke(SendWelcomeEmail $message): void
    {
        $user = $this->users->find($message->userId);
        $this->mailer->send(new WelcomeEmail($user));
    }
}

// dispatching it, anywhere in the app
$this->bus->dispatch(new SendWelcomeEmail($user->getId()));
```

```yaml
# config/packages/messenger.yaml
framework:
  messenger:
    transports:
      async: '%env(MESSENGER_TRANSPORT_DSN)%'
    routing:
      App\Message\SendWelcomeEmail: async
```

```bash
php bin/console messenger:consume async
```

Because messages and their handlers are decoupled through the bus, the same `SendWelcomeEmail` message could later be routed to a completely different transport, a message queue shared with another service, for instance, by changing configuration rather than application code.

## When to reach for this

Any Symfony application needing background processing, and especially useful when the project might eventually need actual service-to-service messaging, since the same component handles both without a second tool.

## When it's the wrong fit

A single, small script that just needs to do one slow thing occasionally. Reaching for a full message bus for a single cron job is more ceremony than the problem needs; a plain [Console](ch02-01-symfony-console-standalone.md) command run on a schedule is enough.

> **Under the hood:** Messenger routes messages to handlers using PHP's type system: the `#[AsMessageHandler]` attribute plus the type-hint on `__invoke()` tells Symfony which messages a handler accepts, so adding a new message type is a matter of defining a class, not registering it in a lookup table by hand.
