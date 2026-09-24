# Symfony : le Security Bundle

Chez Symfony, l'authentification commence par la configuration. **Vous décrivez en YAML comment les utilisateurs sont chargés, comment les mots de passe sont vérifiés et quelles routes exigent quel rôle, et le framework l'applique à chaque requête.** La logique de contrôle, vous ne l'écrivez jamais.

```bash
composer require symfony/security-bundle
```

```yaml
# config/packages/security.yaml
security:
  password_hashers:
    App\Entity\User: 'auto'

  providers:
    app_user_provider:
      entity:
        class: App\Entity\User
        property: email

  firewalls:
    main:
      lazy: true
      provider: app_user_provider
      form_login:
        login_path: app_login
        check_path: app_login
      logout:
        path: app_logout

  access_control:
    - { path: ^/admin, roles: ROLE_ADMIN }
    - { path: ^/account, roles: ROLE_USER }
```

Le Maker Bundle génère l'entité, le formulaire et le contrôleur correspondants en une commande :

```bash
composer require symfony/maker-bundle --dev
php bin/console make:user
php bin/console make:auth
php bin/console make:migration
php bin/console doctrine:migrations:migrate
```

Dans un contrôleur, vérifier une permission tient en une ligne, pas dans un contrôle manuel de la session :

```php
class AdminController extends AbstractController
{
    #[IsGranted('ROLE_ADMIN')]
    public function dashboard(): Response
    {
        // only reachable by ROLE_ADMIN users; Symfony enforces it before this runs
    }
}
```

## Quand le choisir

Toute application Symfony, sans vraie exception. Le Security Bundle est le chemin standard et audité. Bricoler une authentification par session à côté ne ferait que ramener des bugs qu'il a déjà corrigés.

## Quand ce n'est pas le bon outil

Une application Symfony purement API, qui s'authentifie par jetons plutôt que par sessions, utilise toujours le Security Bundle, avec un autre authentificateur (un authentificateur de jeton d'API à la place de `form_login`). Moins un mauvais outil qu'une autre configuration du même composant.

> **Sous le capot :** `#[IsGranted]` est un attribut PHP 8, une métadonnée accrochée à la méthode et lue par Symfony à l'exécution par réflexion. Le même mécanisme, attributs plus réflexion, permet à une seule classe de piloter le routage, la validation et la sérialisation ailleurs dans le framework, sans fichiers de configuration répétitifs.
