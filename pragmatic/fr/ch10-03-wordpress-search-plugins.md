# WordPress : extensions de recherche, et quand passer à Elasticsearch

La recherche intégrée de WordPress est une requête `LIKE` sur les titres et le contenu des articles, et ça se voit. Aucun classement par pertinence digne de ce nom, aucune tolérance aux fautes, et un ralentissement net dès que le site compte des milliers d'articles.

**Le remède le plus rapide est une extension qui remplace la requête intégrée sans toucher aux templates.**

```bash
wp plugin install relevanssi --activate
```

Relevanssi réindexe le contenu existant et prend la main sur la requête de recherche. Vous obtenez un score de pertinence et une correspondance approximative, sans modifier une ligne de code ou presque.

Pour les sites plus gros, ou ceux qui ont besoin de filtres à facettes (catégorie et fourchette de prix en même temps, par exemple), une extension adossée à Elasticsearch remplace tout le moteur :

```bash
wp plugin install elasticpress --activate
wp elasticpress index --setup
```

```php
$args = [
    's' => 'wireless mouse',
    'post_type' => 'product',
];
$query = new WP_Query($args); // ElasticPress intercepts this transparently
```

Le code de l'application bouge à peine. `WP_Query` fonctionne comme avant, et ElasticPress lui répond depuis Elasticsearch au lieu de MySQL.

## Quand le choisir

Relevanssi pour la plupart des sites où le reproche porte sur la qualité de la recherche, pas sur le volume. ElasticPress quand le site a assez de contenu, ou des filtres assez compliqués, pour qu'une requête SQL même plus maligne ne soit ni assez rapide ni assez souple.

## Quand ce n'est pas le bon outil

Un petit site de quelques dizaines de pages, où la recherche par défaut répond assez vite et où personne ne s'est plaint. N'ajoutez pas d'infrastructure de recherche avant d'avoir un problème.

> **Sous le capot :** `WP_Query` est l'abstraction centrale de WordPress pour « donne-moi des articles », utilisée par presque tous les thèmes et extensions. ElasticPress se greffe sur cette classe et détourne sa requête au dernier moment, ce qui explique que l'adopter oblige rarement à réécrire le code d'un thème.
