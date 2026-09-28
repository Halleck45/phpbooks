# WordPress: AI Plugins and When to Call an API Instead

**The fastest AI feature you will ever ship on WordPress is one you do not write.** Plugins already exist for the common requests: a writing assistant in the block editor, automatic alt text for images, an on-site chatbot trained on the site's own content.

```bash
wp plugin install ai-engine --activate
```

Most of these plugins hold your own API key for a provider (OpenAI, Anthropic) and wrap it in a settings screen and an editor integration. They do not reinvent the model access.

For something no plugin covers, a small custom plugin can call the provider's API directly. WordPress's own HTTP API does the job in a few lines, no separate library:

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

An existing plugin for the well-trodden requests, writing assistance or alt text. A small custom plugin with `wp_remote_post()` for anything specific to the site's own content model.

## When it's the wrong fit

A feature that is a full custom application (a recommendation engine, a multi-step AI workflow) wearing a thin WordPress skin. At that point [Prism](ch12-01-laravel-prism-llm-clients.md) or [Symfony's AI Bundle](ch12-02-symfony-ai-bundle.md) gives you far more structure than raw API calls hooked into WordPress actions.

> **Under the hood:** `wp_remote_post()` is WordPress core's own HTTP client, built to work consistently across server environments (some hosts restrict which PHP HTTP functions are available), which is why WordPress code conventionally avoids calling `curl` or `file_get_contents()` directly for outbound requests.
