# Craft CMS ($): A Licensed CMS Built for Editorial Control

Craft starts from a different assumption than WordPress: there is no default content model at all. **Every project defines its own fields, entry types, and structure from scratch**, with Craft's editor as the visual layer. The first hour is slower than with WordPress. The following year is faster, for clients whose content does not fit a generic "post."

```bash
composer create-project craftcms/craft my-site
cd my-site
php craft setup
php craft serve
```

You define the content structure in Craft's admin UI (fields, sections, entry types), then query it in Twig templates:

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

Craft's core is source-available: you can read and modify the code. Running it commercially requires a paid license per project. A free tier exists for evaluating it on a single-user, non-commercial site.

## When to reach for this

Agencies building custom, editorial-heavy sites for clients with specific content needs and a budget for licensing, who would rather have a content model that fits them than one stretched to fit.

## When it's the wrong fit

A tight budget, a generic blog-shaped brief, or a client who wants WordPress's plugin marketplace. Craft's plugin ecosystem is real but far smaller.

> **Under the hood:** Craft's flexible field system sits on a fairly conventional relational schema. PHP's dynamic property access and Craft's own query builder make wildly different content structures feel like first-class, typed data in Twig templates rather than loosely typed arrays.
