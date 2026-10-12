# TYPO3: Multilingual Content Trees Done Properly

TYPO3 has treated languages as a first-class part of its page tree since long before most competitors. **A translation is not a separate copy of the site but a record connected to its original, inside the same structure.**

```yaml
# config/sites/main/config.yaml
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

Editors translate page by page from the backend's language view. It shows which translations are complete, which are outdated because the original changed since, and which are missing:

```bash
./vendor/bin/typo3 language:update
```

`fallbackType: strict` means an untranslated page does not exist in French, rather than silently showing English content. That is a deliberate choice, not a default that ships half-translated pages to visitors.

## When to reach for this

Large institutional sites with true multilingual content management: editors in each region manage their own language, and the link between an original and its translations has to survive years of edits by different people.

## When it's the wrong fit

A small site that needs a couple of static translated pages. [WPML on WordPress](ch13-02-wordpress-multisite-wpml.md), or a simpler translation plugin, gets there with far less setup.

> **Under the hood:** TYPO3 stores translated content as separate database records connected by a shared identifier (`l10n_parent`), rather than one record with multiple language columns. That structural choice is what lets a page have three finished translations and two missing ones at the same time, tracked cleanly rather than crammed into one row's worth of columns.
