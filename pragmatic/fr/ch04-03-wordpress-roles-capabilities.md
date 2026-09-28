# WordPress : rôles, capacités et mots de passe d'application

WordPress livre un système complet d'utilisateurs et de permissions depuis bien avant que « l'authentification en tant que service » ne soit une catégorie. **Si le site est bâti sur WordPress, les comptes sont déjà réglés**, ce n'est pas une fonctionnalité à ajouter.

Par défaut, WordPress fournit cinq rôles : abonné, contributeur, auteur, éditeur et administrateur. Chacun porte un jeu de capacités (`edit_posts`, `publish_posts`, `manage_options` et des dizaines d'autres). Les écrans d'inscription, de connexion et de réinitialisation du mot de passe existent déjà sous `/wp-login.php`.

Quand les rôles par défaut ne correspondent pas à l'équipe du client, des rôles et des capacités sur mesure tiennent en quelques lignes :

```php
add_role('reviewer', 'Reviewer', [
    'read' => true,
    'edit_posts' => true,
    'publish_posts' => false,
]);

if (current_user_can('publish_posts')) {
    // show the publish button
}
```

En headless ou par API (une application mobile, un front découplé qui appelle [l'API REST de WordPress](ch06-03-wordpress-rest-api.md)), les mots de passe d'application donnent à un utilisateur un identifiant à portée limitée, sans exposer son vrai mot de passe :

```bash
curl -u "admin:xxxx xxxx xxxx xxxx xxxx xxxx" \
  https://example.com/wp-json/wp/v2/posts
```

## Quand le choisir

Tout projet WordPress. Réimplémenter l'authentification à côté du cœur, au lieu d'étendre ses rôles, est du temps perdu et un risque de sécurité.

## Quand ce n'est pas le bon outil

Une installation headless qui veut une authentification par jetons (JWT, OAuth) plutôt que des mots de passe d'application. Ce flux n'est pas dans le cœur de WordPress et demande une extension, comme JWT Authentication.

> **Sous le capot :** les capacités de WordPress sont de simples chaînes vérifiées par `current_user_can()`, stockées en données PHP sérialisées pour chaque rôle dans la base. Il n'y a pas de moteur de permissions formel, et c'est ce qui rend l'ajout d'une capacité si facile : une chaîne dans un tableau, pas une migration de schéma.
