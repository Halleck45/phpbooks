# Statamic ($ en usage commercial) : un CMS à fichiers plats bâti sur Laravel

Statamic, c'est un éditeur de contenu construit par un développeur Laravel. **Le contenu vit dans des fichiers Markdown et YAML plats, pas dans une base de données**, et Git vous en donne l'historique pour rien. Dessous, c'est toujours une application Laravel : tout ce que vous savez de Laravel (voir [Livrer des comptes utilisateurs](ch04-01-laravel-breeze-fortify.md), [Livrer du travail en arrière-plan](ch11-01-laravel-queues-horizon.md)) reste valable.

```bash
composer create-project statamic/statamic my-site
cd my-site
php please make:user
php artisan serve
```

Les types de contenu (« collections » et « blueprints » chez Statamic) se définissent en YAML, et l'interface d'administration des rédacteurs en est générée :

```yaml
# resources/blueprints/collections/posts/post.yaml
title: Post
sections:
  main:
    fields:
      - handle: title
        field: { type: text, required: true }
      - handle: content
        field: { type: markdown }
      - handle: featured_image
        field: { type: assets, container: images }
```

Les templates s'écrivent dans la syntaxe Antlers propre à Statamic, ou en Blade standard. À vous de voir.

## Licence

Gratuit pour un projet personnel, Statamic exige une licence payante par site dès qu'il est commercial. L'évaluation ne coûte rien ; la livraison à un client est une ligne dans le budget.

## Quand le choisir

Une équipe à l'aise avec Laravel qui construit un site riche en contenu, veut son historique dans Git et se passerait bien d'une base de données pour ses pages.

## Quand ce n'est pas le bon outil

Un client qui a précisément besoin de l'écosystème d'extensions de WordPress, ou un projet trop petit pour que le coût de la licence ait un sens.

> **Sous le capot :** avec du contenu en fichiers plats, Statamic tire sa performance des fonctions de système de fichiers de PHP et de sa couche de cache, pas de requêtes SQL. Pour la plupart des sites de contenu, lire un fichier pré-analysé en cache vaut au moins un aller-retour vers la base, et `git diff` sert de journal d'audit en prime.
