# WordPress: AI Plugins and When to Call an API Instead

The fastest AI feature you'll ever ship on WordPress is one you don't write at all. Plugins already exist for the common requests: an AI writing assistant in the block editor, automatic alt-text generation for images, an on-site chatbot trained on the site's own content.

```bash
wp plugin install ai-engine --activate
```

Most of these plugins work by holding your own API key for a provider (OpenAI, Anthropic) and wrapping it in a WordPress-friendly settings screen and editor integration, rather than reinventing the underlying model access.

For something a plugin doesn't cover, calling a provider's API directly from a small custom plugin is often only a few lines, using WordPress's own HTTP API rather than a separate library:

```php
add_action('save_post_product', function ($post_id) {
    $description = get_post_field('post_content', $post_id);

    $response = wp_remote_post('https://api.anthropic.com/v1/messages', [
        'headers' => [
            'x-api-key' => get_option('anthropic_api_key'),
            'content-type' => 'application/json',
        ],
        'body' => wp_json_encode([
            'model' => 'claude-sonnet',
            'max_tokens' => 100,
            'messages' => [['role' => 'user', 'content' => "Write a one-line SEO summary for: {$description}"]],
        ]),
    ]);

    $data = json_decode(wp_remote_retrieve_body($response), true);
    update_post_meta($post_id, 'ai_seo_summary', $data['content'][0]['text']);
});
```

## When to reach for this

An existing plugin for common, well-trodden requests like writing assistance or alt-text. A small custom plugin using `wp_remote_post()` for anything specific to the site's own content model.

## When it's the wrong fit

A feature that's really a full custom application (a recommendation engine, a complex multi-step AI workflow) wearing a thin WordPress skin. At that point, a proper framework's tooling, like [Prism](ch12-01-laravel-prism-llm-clients.md) or [Symfony's AI Bundle](ch12-02-symfony-ai-bundle.md), gives you far more structure than hooking raw API calls into WordPress actions.

> **Under the hood:** `wp_remote_post()` is WordPress core's own HTTP client, built to work consistently across different server environments (some hosts restrict which PHP HTTP functions are available), which is why WordPress code conventionally avoids calling `curl` or `file_get_contents()` directly for outbound requests.
