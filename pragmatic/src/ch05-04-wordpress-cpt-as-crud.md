# WordPress: Custom Post Types and ACF as a CRUD Engine

Team members, case studies, product listings: a client on WordPress often needs to manage something that is not a blog post at all. The WordPress admin was not designed as a general CRUD generator, but Custom Post Types plus Advanced Custom Fields (ACF) end up working as one. **A management screen for a new kind of content is a registration call, not a new admin.**

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

That alone adds a list screen to the admin sidebar, with search, bulk actions, and pagination. ACF then adds structured fields through a visual field builder, or from code:

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

The result is a full create, edit, list and delete interface for team members, built from configuration. The `show_in_rest` flag also exposes it through [the WordPress REST API](ch06-03-wordpress-rest-api.md) at no extra cost.

## When to reach for this

A WordPress site that needs a second kind of structured content beyond posts and pages, for a client already at home in the WordPress admin.

## When it's the wrong fit

Relational data with many-to-many relationships and heavy business logic. The post-based model bends a long way, but it stays a content model, not a relational database admin.

> **Under the hood:** Custom Post Types do not create new database tables. Every post type, `post`, `page`, or your own `team_member`, is a row in the same `wp_posts` table, told apart by a `post_type` column. That is why registering a new content type is one function call instead of a migration.
