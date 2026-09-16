# WordPress: The Built-In REST API

Every modern WordPress install already exposes a REST API, with no plugin and no configuration. Posts, pages, media, users, and any custom post type marked `show_in_rest` are queryable immediately:

```bash
curl https://example.com/wp-json/wp/v2/posts
curl https://example.com/wp-json/wp/v2/posts/42
curl "https://example.com/wp-json/wp/v2/posts?search=laravel&per_page=5"
```

This is also what powers the block editor itself, so it's a well-exercised, production-grade API, not an afterthought bolted on for external consumers.

Custom post types opt in with one flag (see [Custom Post Types and ACF as a CRUD Engine](ch05-04-wordpress-cpt-as-crud.md)):

```php
register_post_type('case_study', [
    'public' => true,
    'show_in_rest' => true,
]);
```

Custom endpoints, for anything the default post/page shape doesn't cover, register in a few lines:

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

Writes (`POST`, `PUT`, `DELETE`) require authentication, typically [Application Passwords](ch04-03-wordpress-roles-capabilities.md) for server-to-server use, or a plugin adding OAuth/JWT for third-party client apps.

## When to reach for this

A headless setup where WordPress is purely the content backend for a separate frontend (a JavaScript app, a mobile app), or any integration that just needs to read existing WordPress content programmatically.

## When it's the wrong fit

A data model that doesn't resemble posts, pages, or a custom post type at all. At that point you're fighting WordPress's content-shaped API rather than benefiting from it, and a dedicated API tool ([API Platform](ch06-01-api-platform-from-one-class.md), Laravel) fits better.

> **Under the hood:** The REST API's routing and response shaping is built on WordPress's long-standing hooks and filters system, the same `add_action`/`add_filter` pattern that powers themes and plugins. There's no separate API framework underneath; it's the same extension mechanism WordPress has used since 2004, pointed at JSON responses instead of HTML.
