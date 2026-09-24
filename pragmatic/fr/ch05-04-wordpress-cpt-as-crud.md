# WordPress : types de contenu personnalisés et ACF comme moteur CRUD

Membres de l'équipe, études de cas, fiches produits : un client sous WordPress a souvent besoin de gérer quelque chose qui n'est pas du tout un article de blog. L'administration de WordPress n'a pas été pensée comme un générateur de CRUD, mais les Custom Post Types alliés à Advanced Custom Fields (ACF) finissent par en faire office. **Un écran de gestion pour un nouveau type de contenu, c'est un appel d'enregistrement, pas une nouvelle administration.**

```php
add_action('init', function () {
    register_post_type('team_member', [
        'label' => 'Team Members',
        'public' => true,
        'show_in_rest' => true,
        'menu_icon' => 'dashicons-groups',
        'supports' => ['title', 'thumbnail'],
    ]);
});
```

Cela seul ajoute un écran de liste dans le menu de l'administration, avec recherche, actions groupées et pagination. ACF y ajoute ensuite des champs structurés, depuis son constructeur visuel ou depuis le code :

```php
acf_add_local_field_group([
    'key' => 'group_team_member',
    'title' => 'Team Member Details',
    'fields' => [
        ['key' => 'field_role', 'label' => 'Role', 'name' => 'role', 'type' => 'text'],
        ['key' => 'field_linkedin', 'label' => 'LinkedIn', 'name' => 'linkedin', 'type' => 'url'],
    ],
    'location' => [[['param' => 'post_type', 'operator' => '==', 'value' => 'team_member']]],
]);
```

Résultat : une interface complète de création, d'édition, de liste et de suppression pour les membres de l'équipe, construite par configuration. Le drapeau `show_in_rest` l'expose en prime dans [l'API REST de WordPress](ch06-03-wordpress-rest-api.md).

## Quand le choisir

Un site WordPress qui doit gérer un deuxième type de contenu structuré, au-delà des articles et des pages, pour un client déjà à l'aise dans l'administration de WordPress.

## Quand ce n'est pas le bon outil

Des données relationnelles avec des relations plusieurs-à-plusieurs et une logique métier lourde. Le modèle fondé sur les posts se plie loin, mais il reste un modèle de contenu, pas une administration de base relationnelle.

> **Sous le capot :** les Custom Post Types ne créent aucune table. Chaque type, `post`, `page` ou votre `team_member`, est une ligne de la même table `wp_posts`, distinguée par une colonne `post_type`. C'est pour cela qu'enregistrer un nouveau type de contenu tient en un appel de fonction et non en une migration.
