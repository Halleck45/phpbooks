# Symfony: The Security Bundle

Symfony's approach to authentication is configuration first. **You describe in YAML how users are loaded, how passwords are checked, and which routes need which role, and the framework enforces it on every request.** You never write the enforcement logic yourself.

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

The Maker Bundle generates the matching entity, form, and controller in one command:

```bash
composer require symfony/maker-bundle --dev
php bin/console make:user
php bin/console make:auth
php bin/console make:migration
php bin/console doctrine:migrations:migrate
```

Inside a controller, checking a permission is one line, not a manual session check:

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

## When to reach for this

Any Symfony application, with no real exception. The Security Bundle is the standard, audited path. Hand-rolling session authentication next to it would only bring back bugs it already fixed.

## When it's the wrong fit

An API-only Symfony app that authenticates with tokens instead of sessions still uses the Security Bundle, with a different authenticator (an API token authenticator instead of `form_login`). Less a wrong fit than a different configuration of the same component.

> **Under the hood:** `#[IsGranted]` is a PHP 8 attribute, metadata attached to the method and read by Symfony at runtime through reflection. The same mechanism, attributes plus reflection, lets a single class drive routing, validation, and serialization elsewhere in the framework without repetitive configuration files.
