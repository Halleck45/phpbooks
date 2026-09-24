# Blackfire ($) : trouver le vrai goulot d'étranglement

Chaque remède de ce chapitre suppose que vous savez déjà ce qui est lent. Trompez-vous et vous perdez plus de temps que le remède n'en aurait coûté : un cache devant une requête qui n'a jamais été le goulot ne corrige rien. **Blackfire profile une vraie requête et montre où sont partis le temps et la mémoire, fonction par fonction.**

```bash
composer require blackfire/php-sdk --dev
blackfire run php artisan test
```

Ou, pour une requête en ligne, enveloppez-la directement :

```bash
blackfire curl https://example.com/checkout
```

Le profil est un graphe d'appels : quelle fonction a appelé laquelle, combien de temps chacune a pris, combien de fois elle a tourné. Les coupables habituels remontent tout de suite. Une boucle de requêtes N+1. Une API externe appelée à chaque itération quand une fois aurait suffi. Une étape de template qui domine la requête alors qu'elle semble anodine dans le code.

```php
// what profiling often reveals: 200 queries where one would do
foreach ($orders as $order) {
    echo $order->customer->name; // N+1: one query per order
}

// the fix, informed by the profile rather than a guess
$orders = Order::with('customer')->get();
```

## Tarif

Blackfire a une offre gratuite pour un usage individuel. La collaboration en équipe et le profilage continu en CI sont payants, d'où le `$` pour tout ce qui dépasse l'usage solo et occasionnel.

## Quand le choisir

Le moment où une page ou un point d'entrée est signalé lent et où la cause ne saute pas aux yeux à la lecture du code. Profilez d'abord, corrigez ensuite. L'ordre inverse gâche un cycle.

## Quand ce n'est pas le bon outil

Une page dont personne ne s'est plaint et qu'aucune métrique n'a signalée. Les outils de profilage servent aux problèmes mesurés, pas à l'inquiétude devant des problèmes hypothétiques.

> **Sous le capot :** Blackfire est une extension PHP qui se branche sur le mécanisme d'appel de fonctions du Zend Engine et chronomètre chaque appel de façon transparente. C'est pour cela que le profilage ajoute un surcoût mesurable, et qu'on le lance sur une requête à la demande plutôt que sur tout le trafic de production.
