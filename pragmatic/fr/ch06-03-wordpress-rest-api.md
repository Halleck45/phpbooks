# WordPress : l'API REST intégrée

Toute installation WordPress à jour expose déjà une API REST, sans extension ni configuration. **Les articles, les pages, les médias, les utilisateurs et tout type de contenu marqué `show_in_rest` s'interrogent tout de suite :**

```bash
curl https://example.com/wp-json/wp/v2/posts
curl https://example.com/wp-json/wp/v2/posts/42
curl "https://example.com/wp-json/wp/v2/posts?search=laravel&per_page=5"
```

L'éditeur de blocs lui-même tourne sur cette API. Elle est sollicitée à chaque modification de chaque site WordPress ; ce n'est pas un ajout tardif pour les consommateurs externes.

Les types de contenu personnalisés y entrent avec un seul drapeau (voir [Types de contenu personnalisés et ACF comme moteur CRUD](ch05-04-wordpress-cpt-as-crud.md)) :

```php
register_post_type('case_study', [
    'public' => true,
    'show_in_rest' => true,
]);
```

Un endpoint sur mesure, pour tout ce qui ne ressemble ni à un article ni à une page, tient en quelques lignes :

```php
add_action('rest_api_init', function () {
    register_rest_route('myapp/v1', '/stats', [
        'methods' => 'GET',
        'callback' => function () {
            return ['total_posts' => wp_count_posts()->publish];
        },
        'permission_callback' => '__return_true',
    ]);
});
```

Les écritures (`POST`, `PUT`, `DELETE`) exigent une authentification : les [mots de passe d'application](ch04-03-wordpress-roles-capabilities.md) entre serveurs, ou une extension qui ajoute OAuth ou JWT pour des applications clientes tierces.

## Quand le choisir

Une architecture headless où WordPress sert de backend de contenu à un front séparé (une application JavaScript, une application mobile), ou toute intégration qui doit lire du contenu WordPress existant par programme.

## Quand ce n'est pas le bon outil

Un modèle de données qui ne ressemble en rien à des articles, des pages ou un type de contenu personnalisé. Vous vous battez alors contre une API en forme de contenu, et un outil spécialisé ([API Platform](ch06-01-api-platform-from-one-class.md), Laravel) convient mieux.

> **Sous le capot :** le routage et la mise en forme des réponses de l'API REST reposent sur les hooks et les filtres de WordPress, le même couple `add_action`/`add_filter` qui fait vivre les thèmes et les extensions. Il n'y a pas de framework d'API séparé en dessous : c'est le mécanisme d'extension que WordPress utilise depuis 2004, orienté vers du JSON au lieu du HTML.
