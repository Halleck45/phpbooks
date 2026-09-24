# Symfony : le composant Translation

Tout le reste de ce chapitre traduit du contenu, ce qu'un rédacteur a écrit. **Le composant Translation de Symfony résout un problème plus étroit : l'interface de l'application elle-même**, les libellés, les boutons et les messages d'erreur qui vivent dans le code.

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

La locale active se fixe à chaque requête, d'après un préfixe d'URL, une préférence de l'utilisateur ou l'en-tête `Accept-Language`. Tout ce qui passe par `trans()` la suit.

## Quand le choisir

Toute application Symfony dont l'interface doit parler plusieurs langues : libellés, messages de validation, modèles d'e-mail, navigation. Pour une application Symfony avec des utilisateurs à l'international, c'est la pratique normale, pas une fonctionnalité avancée.

## Quand ce n'est pas le bon outil

Le contenu éditorial, articles de blog ou fiches produit. C'est le problème que résolvent [les arbres de contenu multilingues de TYPO3](ch13-01-typo3-multilingual-trees.md) ou [WPML](ch13-02-wordpress-multisite-wpml.md). Ce composant n'a aucune notion de contenu, seulement de clés de message.

> **Sous le capot :** les fichiers de traduction sont chargés une fois et mis en cache sous forme de tableaux PHP compilés dans le répertoire de cache de Symfony. En production, retrouver une chaîne traduite est une lecture dans un tableau, pas une lecture de fichier ni une requête en base, même avec des centaines de clés dans une douzaine de langues.
