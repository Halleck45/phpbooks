# WordPress: Custom Post Types and ACF as a CRUD Engine

WordPress's admin screens weren't originally designed as a general-purpose CRUD generator, but Custom Post Types plus Advanced Custom Fields (ACF) end up functioning as one, and it's a legitimate, fast way to give a client a management screen for something that isn't a blog post at all: team members, case studies, product listings.

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

That alone adds a full list screen, with search, bulk actions, and pagination, to the WordPress admin sidebar. ACF then adds structured custom fields to it through a visual field builder, no code required for common field types:

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

The result is a full create/edit/list/delete interface for "team members," built entirely from configuration, with `show_in_rest` also exposing it through [the WordPress REST API](ch06-03-wordpress-rest-api.md) for free.

## When to reach for this

Any WordPress site that needs to manage a second kind of structured content beyond posts and pages, and where the client is already comfortable in the WordPress admin.

## When it's the wrong fit

Complex relational data with many-to-many relationships and heavy business logic. WordPress's post-based data model bends a long way, but it's still fundamentally a content model, not a general relational database admin tool.

> **Under the hood:** Custom Post Types don't create new database tables. Every post type, `post`, `page`, or your own `team_member`, is stored as a row in the same `wp_posts` table, distinguished by a `post_type` column. That's why registering a new content type is a single function call instead of a migration.
