# Symfony: The Messenger Component

Messenger is Symfony's message bus. **The same abstraction handles background jobs, like Laravel's queues, and messaging between parts of an application or between separate services**, through one interface.

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

Messages and handlers only meet through the bus. The same `SendWelcomeEmail` message can later be routed to a different transport, say a queue shared with another service, by changing configuration rather than application code.

## When to reach for this

Any Symfony application that needs background processing, and especially one that may one day need service-to-service messaging. The same component handles both, without a second tool.

## When it's the wrong fit

A single small script that does one slow thing now and then. A full message bus for one cron job is more ceremony than the problem needs; a plain [Console](ch02-01-symfony-console-standalone.md) command on a schedule is enough.

> **Under the hood:** Messenger routes messages to handlers using PHP's type system: the `#[AsMessageHandler]` attribute plus the type-hint on `__invoke()` tells Symfony which messages a handler accepts, so adding a new message type is a matter of defining a class, not registering it in a lookup table by hand.
