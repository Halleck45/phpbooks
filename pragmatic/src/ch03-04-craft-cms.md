# Craft CMS ($): A Licensed CMS Built for Editorial Control

Craft CMS starts from a different assumption than WordPress: there's no default content model at all. Every project defines its own custom fields, entry types, and structure from scratch, using Craft's editor as the visual layer. That makes the first hour slower than WordPress, and the following year faster for clients whose content genuinely doesn't fit a generic "post" model.

```bash
composer create-project craftcms/craft my-site
cd my-site
php craft setup
php craft serve
```

Content structure is defined through Craft's own admin UI (fields, sections, entry types), then queried in templates with Twig:

```twig
{% for entry in craft.entries()
    .section('caseStudies')
    .client(currentClient)
    .all() %}
    <article>
        <h2>{{ entry.title }}</h2>
        {{ entry.summary }}
    </article>
{% endfor %}
```

## Licensing

Craft's core CMS is source-available (you can read and modify the code), but running it commercially requires a paid license per project, which is what earns it the `$`. There's a free tier for a single-user, non-commercial site to evaluate it.

## When to reach for this

Agencies building custom, editorial-heavy sites for clients who have specific, non-generic content needs and a budget for licensing, and who value a content model that fits the client exactly rather than one that's stretched to fit.

## When it's the wrong fit

A tight budget, a generic blog-shaped brief, or a client who wants access to WordPress's enormous plugin marketplace. Craft's plugin ecosystem is real but far smaller.

> **Under the hood:** Craft's flexible field system is built on top of a fairly conventional relational database schema, using PHP's dynamic property access and its own query builder to make wildly different content structures feel like first-class, typed data in Twig templates rather than loosely-typed arrays.
