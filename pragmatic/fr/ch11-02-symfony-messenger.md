# Symfony : le composant Messenger

Messenger est le bus de messages de Symfony. **La même abstraction sert aux tâches de fond, comme les files de Laravel, et au dialogue entre les parties d'une application ou entre services distincts**, à travers une seule interface.

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

Les messages et leurs handlers ne se rencontrent que par le bus. Le même message `SendWelcomeEmail` pourra plus tard partir vers un autre transport, disons une file partagée avec un autre service, en changeant la configuration et non le code de l'application.

## Quand le choisir

Toute application Symfony qui a besoin de traitements en arrière-plan, et surtout celle qui pourrait un jour avoir besoin d'échanger des messages entre services. Le même composant fait les deux, sans second outil.

## Quand ce n'est pas le bon outil

Un petit script isolé qui fait une chose lente de temps en temps. Un bus de messages complet pour une tâche cron, c'est plus de cérémonie que le problème n'en mérite ; une simple commande [Console](ch02-01-symfony-console-standalone.md) lancée par le cron suffit.

> **Sous le capot :** Messenger route les messages vers leurs handlers grâce au système de types de PHP. L'attribut `#[AsMessageHandler]` et le type déclaré sur `__invoke()` indiquent à Symfony quels messages un handler accepte ; ajouter un type de message revient à définir une classe, pas à l'inscrire à la main dans une table de correspondance.
