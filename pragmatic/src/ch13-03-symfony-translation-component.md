# Symfony: The Translation Component

Everything else in this chapter translates content, what an editor wrote. **Symfony's Translation component solves a narrower problem: the application's own interface**, the labels, buttons and error messages that live in the code.

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

The active locale is set per request, from a URL prefix, a user preference or the `Accept-Language` header. Everything wrapped in `trans()` follows it.

## When to reach for this

Any Symfony application whose interface must speak several languages: labels, validation messages, email templates, navigation. For a Symfony app with international users this is standard practice, not an advanced feature.

## When it's the wrong fit

Editorial content such as blog posts or product descriptions. That is the problem [TYPO3's multilingual content trees](ch13-01-typo3-multilingual-trees.md) or [WPML](ch13-02-wordpress-multisite-wpml.md) solve. This component has no concept of content, only of message keys.

> **Under the hood:** Translation files are loaded once and cached as compiled PHP arrays in Symfony's cache directory, so looking up a translated string in production is an array lookup, not a file read or a database query, even with hundreds of keys across a dozen languages.
