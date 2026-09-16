# Symfony: The Security Bundle

Symfony's approach to authentication is configuration-first: you describe, in YAML, how users are loaded, how passwords are checked, and which routes require which role, and the framework enforces it on every request without you writing the enforcement logic by hand.

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

Inside a controller, checking permission is a one-line call, not a manual session check:

```php
#[IsGranted('ROLE_ADMIN')]
public function dashboard(): Response
{
    // only reachable by ROLE_ADMIN users; Symfony enforces it before this runs
}
```

## When to reach for this

Any Symfony application, essentially without exception. The Security Bundle is the standard, well-audited path, and hand-rolling session-based authentication next to it would only reintroduce bugs it already solved.

## When it's the wrong fit

An API-only Symfony app authenticating via tokens instead of sessions still uses the Security Bundle, just configured with a different "guard" (an API token authenticator instead of `form_login`), so this is rarely a "wrong fit" so much as a different configuration of the same component.

> **Under the hood:** The `#[IsGranted]` attribute is a PHP 8 attribute, metadata attached directly to the method, read by Symfony at runtime via reflection. It's the same underlying mechanism (attributes plus reflection) that lets a single class definition drive routing, validation, and serialization elsewhere in the framework without repetitive configuration files.
