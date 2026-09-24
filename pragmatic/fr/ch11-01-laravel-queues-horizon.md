# Laravel : files d'attente et Horizon

**Tout ce qui est lent ou accessoire dans une requête Laravel peut devenir un Job, poussé dans une file d'attente et exécuté par un processus worker séparé.** La requête de l'utilisateur se termine tout de suite au lieu d'attendre.

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

Cette dernière commande, c'est le worker. Un gestionnaire de processus comme Supervisor le maintient en vie ; il prend les jobs dans la file (Redis, dans la plupart des installations de production) et les exécute.

**Horizon** ajoute un tableau de bord par-dessus les files Redis : débit, jobs en échec, relances à la main et métriques par file, sans outil de supervision à part.

```bash
composer require laravel/horizon
php artisan horizon:install
php artisan horizon
```

Les jobs en échec sont relancés avec un délai croissant. Ceux qui échouent pour de bon atterrissent dans une table `failed_jobs`, où vous pouvez les examiner, au lieu de disparaître.

## Quand le choisir

Tout ce qui ne doit pas bloquer une requête web : envoyer un e-mail, traiter un fichier envoyé, appeler une API tierce lente, générer un rapport. Si l'utilisateur remarquerait le délai, ça va dans une file.

## Quand ce n'est pas le bon outil

Le travail qui doit être terminé avant la réponse, comme valider un formulaire avant de l'enregistrer. Le mettre en file ajoute de la latence et de la complexité là où le code synchrone était déjà juste.

> **Sous le capot :** les jobs sont sérialisés (en général avec le `serialize()` natif de PHP) avant d'être rangés dans la file. C'est pour cela qu'une classe de job ne devrait porter que des propriétés simples et sérialisables, comme l'identifiant d'un modèle, plutôt que de gros objets ou des ressources ouvertes ; le worker désérialise et reconstruit le job de zéro au moment de l'exécuter.
