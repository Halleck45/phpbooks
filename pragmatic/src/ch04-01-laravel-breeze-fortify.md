# Laravel: Breeze, Fortify, and Jetstream

**Laravel ships three official answers to "add login," layered by how much you want handed to you.**

**Breeze** installs view files and controllers into your project. You get working registration, login, password reset, and email verification, as code you own and can edit right away.

```bash
composer require laravel/breeze --dev
php artisan breeze:install blade
npm install && npm run dev
php artisan migrate
```

**Fortify** implements the same authentication logic as a backend-only package, with no views. It is meant for a custom frontend or an API.

```bash
composer require laravel/fortify
php artisan vendor:publish --provider="Laravel\Fortify\FortifyServiceProvider"
php artisan migrate
```

**Jetstream** builds on Fortify and adds a full application shell: team management, API tokens, two-factor authentication, and a choice of Livewire or Inertia frontend. It is aimed at SaaS products that need accounts and teams from day one.

```bash
composer require laravel/jetstream
php artisan jetstream:install livewire
npm install && npm run build
php artisan migrate
```

## When to reach for each

Breeze for a straightforward app where you want to see and customize the auth code immediately. Fortify when the frontend is Inertia, a mobile app, or something custom that has no use for Breeze's bundled views. Jetstream when the product is multi-tenant or team-based and you would otherwise build that structure yourself.

## When it's the wrong fit

A single-page marketing site with no user accounts, or a project where WordPress's built-in roles (see [WordPress: Roles, Capabilities, and Application Passwords](ch04-03-wordpress-roles-capabilities.md)) already cover the need without adding a framework.

> **Under the hood:** All three packages lean on Laravel's `Hash` facade, which defaults to bcrypt or argon2id. Both algorithms are slow on purpose, so that brute-forcing stolen password hashes stays impractical. You never call a hashing function yourself; the authentication guard does it on every login attempt.
