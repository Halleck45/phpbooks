# TYPO3: Multilingual Content Trees Done Properly

TYPO3 has treated multiple languages as a first-class concept in its page tree since long before most competitors, and it shows in how cleanly the relationship between an original page and its translations is modeled: not a separate copy of the site, but connected records within the same structure.

```php
// config/sites/main/config.yaml
languages:
  - title: English
    languageId: 0
    locale: en_US.UTF-8
    base: /
  - title: French
    languageId: 1
    locale: fr_FR.UTF-8
    base: /fr/
    fallbackType: strict
```

Editors translate content directly from the backend's language view, page by page, with a clear indicator of which translations are complete, outdated (because the original changed since), or missing entirely:

```bash
./vendor/bin/typo3 language:update
```

`fallbackType: strict` means an untranslated page in French simply doesn't exist in that language rather than silently showing English content, an explicit, deliberate choice rather than a default that quietly ships half-translated pages to visitors.

## When to reach for this

Large institutional sites needing genuine multilingual content management, where editors in different regions manage their own language's content, and the relationship between an original and its translations needs to survive years of edits by different people.

## When it's the wrong fit

A small site needing only a couple of static translated pages, where [WPML on WordPress](ch13-02-wordpress-multisite-wpml.md) or a simpler translation plugin gets there with far less initial setup.

> **Under the hood:** TYPO3 stores translated content as separate database records connected by a shared identifier (`l10n_parent`), rather than one record with multiple language columns. That structural choice is what lets a page have three finished translations and two missing ones simultaneously, tracked cleanly rather than crammed into one row's worth of columns.
