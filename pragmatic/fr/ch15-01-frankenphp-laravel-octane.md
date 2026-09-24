# FrankenPHP et Laravel Octane : les performances du mode worker

Le PHP traditionnel reconstruit toute votre application à chaque requête, framework compris : démarrer le conteneur, charger la configuration, puis tout jeter une fois la réponse envoyée. Cette habitude explique en bonne partie la réputation de lenteur de PHP face aux runtimes qui gardent une application résidente en mémoire.

**Le mode worker démarre l'application une fois et sert de nombreuses requêtes avec cette même instance**, en ne réinitialisant entre elles que ce qui doit l'être.

```bash
composer require laravel/octane
php artisan octane:install --server=frankenphp
php artisan octane:start
```

FrankenPHP est un serveur d'applications PHP écrit en Go. Il exécute PHP en mode worker nativement, et en mode classique aussi, avec HTTPS intégré et sans serveur web séparé :

```bash
frankenphp php-server --worker /path/to/public/index.php
```

Le gain est important pour les applications dont le goulot était le démarrage du framework et non leur propre logique. Les benchmarks publiés par les projets montrent un multiple du débit de PHP-FPM pour le même code applicatif, inchangé ; vos propres chiffres dépendront de la part du démarrage dans chaque requête.

La contrepartie mérite d'être dite sans détour. L'état global qui se réinitialisait entre les requêtes, une propriété statique, un singleton qui retient des données de requête, peut maintenant fuir d'une requête à la suivante. Le même processus les sert à la file au lieu de repartir de zéro.

## Quand le choisir

Une application sous charge mesurée, où le profilage (voir [Blackfire](ch15-04-blackfire-profiling.md)) désigne l'amorçage du framework, et non votre logique métier, comme goulot d'étranglement.

## Quand ce n'est pas le bon outil

Un site à faible trafic ou un outil interne. Le mode worker ajoute une catégorie de bugs, l'état qui fuit entre les requêtes, qui ne vaut pas la peine d'être assumée avant d'avoir besoin du débit.

> **Sous le capot :** C'est le problème que [le serveur WebSocket de Reverb](ch07-01-laravel-reverb-livewire.md) résout avec les Fibers, pris par l'autre bout. Au lieu d'un processus qui tient de nombreuses connexions simultanées, le mode worker garde un processus vivant à travers de nombreuses requêtes successives. Les deux existent parce que le modèle « mourir après chaque requête » de PHP, jadis une limite, est devenu optionnel.
