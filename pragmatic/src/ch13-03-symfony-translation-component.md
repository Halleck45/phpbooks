# Symfony: The Translation Component

There's a distinction worth being precise about: everything else in this chapter is about translating *content*, what an editor wrote. Symfony's Translation component solves a different, narrower problem: translating an application's own interface, the labels, buttons, and error messages that are part of the code, not the content.

```bash
composer require symfony/translation
```

```yaml
# translations/messages.en.yaml
welcome_message: "Welcome back, %name%!"
cart.empty: "Your cart is empty."
```

```yaml
# translations/messages.fr.yaml
welcome_message: "Content de vous revoir, %name% !"
cart.empty: "Votre panier est vide."
```

```twig
<h1>{{ 'welcome_message'|trans({'%name%': user.firstName}) }}</h1>
```

```php
$message = $translator->trans('cart.empty');
```

The active locale is typically set per request, from a URL prefix, a user preference, or the `Accept-Language` header, and everything wrapped in `trans()` follows it automatically.

## When to reach for this

Any Symfony application whose interface itself needs to support multiple languages: labels, validation error messages, email templates, navigation. This is standard practice for any Symfony app with international users, not an advanced feature.

## When it's the wrong fit

Translating editorial content (blog posts, product descriptions) rather than interface strings. That's the problem [TYPO3's multilingual content trees](ch13-01-typo3-multilingual-trees.md) or [WPML](ch13-02-wordpress-multisite-wpml.md) solve; this component has no concept of "content," only of message keys.

> **Under the hood:** Translation files are loaded once and cached as compiled PHP arrays in Symfony's cache directory, so looking up a translated string in production is an array lookup, not a file read or a database query, even with hundreds of keys across a dozen languages.
