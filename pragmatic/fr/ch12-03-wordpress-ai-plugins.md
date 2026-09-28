# WordPress : extensions IA, et quand appeler une API à la place

**La fonctionnalité IA la plus rapide que vous livrerez jamais sur WordPress est celle que vous n'écrivez pas.** Des extensions existent déjà pour les demandes courantes : un assistant de rédaction dans l'éditeur de blocs, des textes alternatifs générés pour les images, un chatbot entraîné sur le contenu du site.

```bash
wp plugin install ai-engine --activate
```

La plupart de ces extensions gardent votre propre clé d'API chez un fournisseur (OpenAI, Anthropic) et l'habillent d'un écran de réglages et d'une intégration à l'éditeur. Elles ne réinventent pas l'accès au modèle.

Pour ce qu'aucune extension ne couvre, une petite extension maison peut appeler l'API du fournisseur directement. L'API HTTP de WordPress fait le travail en quelques lignes, sans bibliothèque à part :

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

## Quand le choisir

Une extension existante pour les demandes déjà balisées, l'aide à la rédaction ou les textes alternatifs. Une petite extension maison avec `wp_remote_post()` pour tout ce qui tient au modèle de contenu du site.

## Quand ce n'est pas le bon outil

Une fonctionnalité qui est en réalité une application complète (un moteur de recommandation, un enchaînement d'étapes IA) déguisée en extension WordPress. À ce stade, [Prism](ch12-01-laravel-prism-llm-clients.md) ou [l'AI Bundle de Symfony](ch12-02-symfony-ai-bundle.md) vous donnent bien plus de structure que des appels d'API bruts accrochés à des actions WordPress.

> **Sous le capot :** `wp_remote_post()` est le client HTTP du cœur de WordPress, conçu pour se comporter de la même façon d'un hébergeur à l'autre (certains restreignent les fonctions HTTP de PHP disponibles). C'est pour cela que le code WordPress évite par convention d'appeler `curl` ou `file_get_contents()` directement pour les requêtes sortantes.
