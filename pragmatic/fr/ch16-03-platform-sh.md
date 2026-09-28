# Platform.sh ($) : un seul déploiement pour plusieurs frameworks

Platform.sh vend de l'infrastructure sous forme de code, indépendante du framework : **un seul format de configuration, que le projet en dessous soit Laravel, Symfony, WordPress, TYPO3 ou autre chose.** Une agence qui livre sur plusieurs des stacks de ce livre apprend une plateforme de déploiement au lieu de cinq.

```yaml
# .platform.app.yaml
name: app
type: php:8.3
dependencies:
  php:
    composer/composer: "^2"
relationships:
  database: "db:mysql"
hooks:
  build: composer install --no-dev --optimize-autoloader
  deploy: php artisan migrate --force
```

```yaml
# .platform/services.yaml
db:
  type: mysql:8.0
```

```bash
git push platform main
```

Chaque push crée un environnement complet et isolé, avec sa propre base de données et son propre stockage, au lieu de déployer par-dessus un environnement partagé. Prévisualiser une branche comme une application qui tourne devient la routine, pas un montage spécial.

## Tarif

Platform.sh est un service infogéré payant, facturé par projet et par environnement, sans offre gratuite pour la production.

## Quand le choisir

Les agences ou les équipes qui font tourner plusieurs projets sur différents frameworks et CMS PHP, et pour qui un seul flux de déploiement commun compte plus que les facilités propres à chaque plateforme.

## Quand ce n'est pas le bon outil

Un projet unique, engagé sur un framework pour longtemps. Une option native comme [Forge](ch16-01-laravel-forge-vapor.md) ou [l'hébergement WordPress infogéré](ch16-04-wordpress-managed-hosting.md) est plus simple, et souvent moins chère, pour ce cas-là.

> **Sous le capot :** Le modèle d'un environnement par branche fonctionne parce que Platform.sh traite l'infrastructure comme une configuration versionnée à côté de votre code. C'est le réflexe d'un `composer.lock` qui fige les versions des dépendances, étendu à la base de données et aux services dont un déploiement a besoin.
