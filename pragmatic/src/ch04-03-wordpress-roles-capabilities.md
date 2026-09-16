# WordPress: Roles, Capabilities, and Application Passwords

WordPress has shipped a complete user and permissions system since long before "auth as a service" was a category. If the site is built on WordPress at all, this is very likely already solved, not a feature to add.

Out of the box, WordPress ships five roles: Subscriber, Contributor, Author, Editor, and Administrator, each with a matching set of capabilities (`edit_posts`, `publish_posts`, `manage_options`, and dozens more). Registration, login, and password reset screens already exist at `/wp-login.php`.

Custom roles and capabilities, when the defaults don't match a client's team structure, take a few lines:

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

For headless or API-driven use (a mobile app, a decoupled frontend calling [the WordPress REST API](ch06-03-wordpress-rest-api.md)), Application Passwords let a user generate a scoped credential without exposing their real login password:

```bash
curl -u "admin:xxxx xxxx xxxx xxxx xxxx xxxx" \
  https://example.com/wp-json/wp/v2/posts
```

## When to reach for this

Any WordPress project. Reimplementing authentication alongside WordPress core rather than extending its role system is almost always wasted effort and a security liability.

## When it's the wrong fit

A headless setup wanting modern token-based auth (JWT, OAuth) instead of Application Passwords benefits from a dedicated plugin (such as the JWT Authentication plugin), since that flow isn't part of WordPress core by default.

> **Under the hood:** WordPress capabilities are just strings checked with `current_user_can()`, stored as serialized PHP data against each role in the database. There's no formal permissions engine, which is exactly why it's so easy to add a custom capability: it's a string in an array, not a schema migration.
