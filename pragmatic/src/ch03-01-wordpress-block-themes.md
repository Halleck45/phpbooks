# WordPress: Block Themes and the Site Editor

WordPress still powers a large share of the content web, and modern WordPress is a genuinely different tool from the one its reputation is often stuck on. Block themes and the Site Editor let a client build and rearrange full page layouts, headers, and footers visually, using the same block editor they already use for posts, with no PHP template files required for common layout changes.

```bash
wp core download --path=my-site
cd my-site
wp config create --dbname=my_site --dbuser=root --dbpass=
wp core install --url=localhost:8080 --title="My Site" --admin_user=admin --admin_password=admin --admin_email=you@example.com
wp theme install twentytwentyfive --activate
```

A developer's job in a block theme is mostly `theme.json`: defining the color palette, spacing scale, and typography the client is allowed to choose from, so the site stays on-brand no matter what the client rearranges.

```json
{
  "version": 2,
  "settings": {
    "color": {
      "palette": [
        { "slug": "brand-primary", "color": "#1d4ed8", "name": "Brand Primary" },
        { "slug": "brand-ink", "color": "#111827", "name": "Ink" }
      ]
    },
    "typography": {
      "fontSizes": [
        { "slug": "small", "size": "0.875rem", "name": "Small" },
        { "slug": "large", "size": "1.5rem", "name": "Large" }
      ]
    }
  }
}
```

Custom blocks, when a client needs something the default set doesn't cover, are registered in PHP and can be as small as a single function.

## When to reach for this

Marketing sites, blogs, and small business sites where the client explicitly wants to edit the site themselves after launch, and where the enormous plugin ecosystem (forms, SEO, caching) solves problems faster than building them.

## When it's the wrong fit

A site that's mostly custom application logic wearing a thin content layer. Forcing that into WordPress's content model usually costs more time than it saves.

> **Under the hood:** Block themes store their layout as structured HTML with block comments (`<!-- wp:heading -->`), not PHP template tags. WordPress's own PHP renders those blocks at request time, but the *authoring* format is deliberately close to plain markup, which is what lets the visual editor read it back reliably.
