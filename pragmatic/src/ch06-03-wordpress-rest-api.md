# WordPress: The Built-In REST API

Every current WordPress install already exposes a REST API, with no plugin and no configuration. **Posts, pages, media, users, and any post type marked `show_in_rest` can be queried right now:**

```bash
curl https://example.com/wp-json/wp/v2/posts
curl https://example.com/wp-json/wp/v2/posts/42
curl "https://example.com/wp-json/wp/v2/posts?search=laravel&per_page=5"
```

The block editor itself runs on this API. It is exercised on every edit of every WordPress site, not bolted on for external consumers.

Custom post types opt in with one flag (see [Custom Post Types and ACF as a CRUD Engine](ch05-04-wordpress-cpt-as-crud.md)):

```php
register_post_type('case_study', [
    'public' => true,
    'show_in_rest' => true,
]);
```

Custom endpoints, for anything the post and page shape does not cover, take a few lines:

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

Writes (`POST`, `PUT`, `DELETE`) require authentication: [Application Passwords](ch04-03-wordpress-roles-capabilities.md) for server-to-server use, or a plugin adding OAuth or JWT for third-party client apps.

## When to reach for this

A headless setup where WordPress is the content backend for a separate front end (a JavaScript app, a mobile app), or any integration that needs to read existing WordPress content programmatically.

## When it's the wrong fit

A data model that looks nothing like posts, pages, or a custom post type. At that point you are fighting a content-shaped API, and a dedicated tool ([API Platform](ch06-01-api-platform-from-one-class.md), Laravel) fits better.

> **Under the hood:** The REST API's routing and response shaping are built on WordPress's hooks and filters, the same `add_action`/`add_filter` pattern behind themes and plugins. There is no separate API framework underneath: it is the extension mechanism WordPress has used since 2004, pointed at JSON instead of HTML.
