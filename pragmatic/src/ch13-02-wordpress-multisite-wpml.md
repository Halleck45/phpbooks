# WordPress: Multisite and WPML

WordPress has two answers here, for two different questions. **Picking the wrong one is a common mistake, and an expensive one to undo.**

**"We have several distinct sites that should share users and plugins."** Several national subsidiaries with their own content and design, not a translation of the same pages. That is what WordPress Multisite solves: one install running a network of separate sites, sharing code and users but not content.

```bash
wp core multisite-convert
wp site create --slug=fr --title="Example France"
wp site create --slug=de --title="Example Germany"
```

**"We have one site that needs to exist in several languages."** The same pages, translated. Multisite is the wrong tool for it, since it would mean maintaining separate copies of every page by hand. A translation plugin such as WPML keeps one site with linked translations of each page:

```bash
wp plugin install sitepress-multilingual-cms --activate
wp wpml language add fr de
```

```php
// getting a translated post ID for the current language
$translated_id = apply_filters('wpml_object_id', $post_id, 'post', true);
```

## When to reach for each

Multisite when the sites differ beyond translation: different design, different content strategy, a different admin team per country. WPML when it is the same site and the same content in more than one language.

## When it's the wrong fit

Multisite as a translation tool, or WPML to run what are in fact separate, independently managed sites. Both mistakes are common, and both get expensive once a year of content has piled up on the wrong structure.

> **Under the hood:** Multisite works by adding a `blog_id` to WordPress's core tables and routing requests through a network-aware bootstrap, essentially running several logically separate installs against shared code. WPML instead adds its own linking table between translated posts, leaving WordPress's core single-site architecture untouched.
