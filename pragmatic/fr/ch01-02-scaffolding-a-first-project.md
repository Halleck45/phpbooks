# Un premier projet en moins d'une minute

Lire la documentation d'une stack vous dit ce qu'elle promet. **Lancer sa commande de création pendant soixante secondes vous dit ce qu'elle donne entre les mains.** Voici le chemin le plus court vers chacune des options majeures de ce livre.

## Laravel

```bash
composer create-project laravel/laravel my-app
cd my-app
php artisan serve
```

Une application qui tourne sur `http://localhost:8000`, avec le routage, une connexion à la base de données et un ORM déjà câblés ensemble.

## Symfony

```bash
composer create-project symfony/skeleton my-app
cd my-app
composer require webapp
symfony server:start
```

Le squelette démarre presque nu. `composer require webapp` ajoute Twig, le routage et le composant de formulaires, dont la plupart des sites finissent par avoir besoin de toute façon.

## WordPress

```bash
wp core download --path=my-site
cd my-site
wp config create --dbname=my_site --dbuser=root --dbpass=
wp core install --url=localhost:8080 --title="My Site" --admin_user=admin --admin_password=admin --admin_email=you@example.com
php -S localhost:8080
```

Ou laissez la ligne de commande de côté et utilisez [Local](https://localwp.com), qui enchaîne les mêmes quatre étapes derrière une interface graphique, en à peu près le même temps.

## API Platform

```bash
composer create-project api-platform/api-platform my-api
cd my-api
docker compose up -d
```

Un squelette d'API qui tourne, avec une page de documentation OpenAPI interactive, prêt pour le moment où une seule classe PHP deviendra une API CRUD complète.

## Ce qu'il faut comparer

Pas le temps d'installation : toutes tiennent sous la minute. Comparez ce qui est déjà décidé pour vous quand l'installation se termine. Laravel et Symfony vous tendent une application vide et beaucoup de liberté. WordPress vous tend un site qui fonctionne et se modifie, sans rien de sur mesure dedans. API Platform vous tend une API vide et entièrement documentée. Celle qui semble la plus proche de « terminé » pour votre brief est en général celle sur laquelle continuer.

> **Sous le capot :** les quatre sont des projets Composer : le gestionnaire de paquets de PHP résout un arbre de dépendances et génère un autoloader. WordPress fait exception. Il est antérieur à la popularité de Composer et peut tourner sans lui, même si le développement WordPress d'aujourd'hui passe presque toujours par Composer pour les extensions et les dépendances.
