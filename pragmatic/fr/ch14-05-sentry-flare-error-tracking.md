# Attraper l'erreur en production : Sentry et Flare ($)

Les tests attrapent ce que vous avez pensé à tester. L'analyse statique attrape ce que le système de types peut prouver. Ni l'un ni l'autre n'attrape ce qu'un utilisateur fait à 23 h et que personne n'avait prévu. **Le suivi des erreurs, c'est la confiance qui continue après le bouton de déploiement :** vous apprenez qu'une chose a cassé pour une vraie personne au moment où ça arrive, avec la trace d'appels, au lieu d'un mail au support qui dit « ça ne marche pas ».

**Sentry** fonctionne avec tous les frameworks de ce livre, avec des SDK pour Laravel, Symfony et PHP nu.

```bash
composer require sentry/sentry-laravel
php artisan sentry:publish --dsn=your-dsn-here
```

```php
try {
    $order->submit();
} catch (\Throwable $e) {
    \Sentry\captureException($e);
    throw $e;
}
```

Les exceptions non rattrapées sont capturées automatiquement une fois le SDK installé. L'appel manuel ci-dessus sert pour une erreur que vous gérez proprement mais dont vous voulez quand même être informé.

**Flare ($)**, de Spatie, dans l'écosystème Laravel, se limite à Laravel et ajoute à chaque rapport le contexte du framework : quelle route, quelle requête, quel job, à côté de la trace d'appels.

```bash
composer require spatie/laravel-flare
```

## Tarif

Sentry a une offre gratuite utilisable pour les petits projets, puis un plan payant quand le volume d'événements grandit. Flare est un produit payant, avec un essai gratuit mais pas d'offre gratuite dans la durée. Les deux portent le `$` ici, celui de Sentry plus conditionnel que celui de Flare.

## Quand le choisir

Toute application en production. Attendre qu'un utilisateur signale un bug qu'il ne sait pas décrire coûte plus de temps de débogage que l'abonnement.

## Quand ce n'est pas le bon outil

Un prototype, ou un outil interne avec une poignée d'utilisateurs qui viendront vous voir directement quand quelque chose casse. La mise en place ne se justifie pas encore.

> **Sous le capot :** Ces outils se branchent sur les gestionnaires d'exceptions et d'erreurs de PHP lui-même (`set_exception_handler()`, `set_error_handler()`). C'est pour cela que les installer tient en quelques lignes d'amorçage, plutôt qu'en une enveloppe autour de chaque appel de fonction de votre application.
