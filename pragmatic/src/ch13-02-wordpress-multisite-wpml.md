# WordPress: Multisite and WPML

WordPress actually has two different answers here, for two different questions, and picking the wrong one is a common, expensive mistake.

**"We have several distinct sites that should share users and plugins"**, several national subsidiaries with genuinely different content and design, not just a translation of the same pages, is what WordPress Multisite solves: one WordPress install running a network of separate sites, sharing a codebase and user base but not content.

```bash
wp core multisite-convert
wp site create --slug=fr --title="Example France"
wp site create --slug=de --title="Example Germany"
```

**"We have one site that needs to exist in several languages"**, the same pages, translated, is a different problem, and Multisite is the wrong tool for it: it would mean maintaining separate copies of every page by hand. That's what a translation plugin like WPML solves instead, keeping one site with linked translations of each page:

```bash
wp plugin install sitepress-multilingual-cms --activate
wp wpml language add fr de
```

```php
// getting a translated post ID for the current language
$translated_id = apply_filters('wpml_object_id', $post_id, 'post', true);
```

## When to reach for each

Multisite when the sites genuinely differ beyond translation: different design, different content strategy, different admin teams per country. WPML when it's truly the same site, the same content, just needing to exist in more than one language.

## When it's the wrong fit

Using Multisite as a translation tool, or using WPML to try to run what are actually separate, independently-managed sites. Both mistakes are common, and both get expensive to unwind once a year of content has accumulated on the wrong structure.

> **Under the hood:** Multisite works by adding a `blog_id` to WordPress's core tables and routing requests through a network-aware bootstrap, essentially running several logically separate installs against shared code. WPML instead adds its own linking table between translated posts, leaving WordPress's core single-site architecture untouched.
