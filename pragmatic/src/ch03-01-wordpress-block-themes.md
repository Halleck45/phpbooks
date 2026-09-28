# WordPress: Block Themes and the Site Editor

WordPress still runs a large share of the content web, and the WordPress of today is a different tool from the one its reputation is stuck on. **With block themes and the Site Editor, a client builds and rearranges whole page layouts, headers, and footers visually**, in the same block editor they already use for posts. Common layout changes need no PHP template file at all.

```bash
wp core download --path=my-site
cd my-site
wp config create --dbname=my_site --dbuser=root --dbpass=
wp core install --url=localhost:8080 --title="My Site" --admin_user=admin --admin_password=admin --admin_email=you@example.com
wp theme install twentytwentyfive --activate
```

Your job in a block theme is mostly `theme.json`: the color palette, the spacing scale, and the typography the client may choose from. Whatever they rearrange, the site stays on brand.

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

When a client needs something the default blocks don't cover, a custom block is registered in PHP and can be as small as a single function.

## When to reach for this

Marketing sites, blogs, and small business sites where the client wants to edit the site themselves after launch, and where the plugin ecosystem (forms, SEO, caching) solves problems faster than you could build them.

## When it's the wrong fit

A site that is mostly custom application logic wearing a thin content layer. Forcing that into WordPress's content model usually costs more time than it saves.

> **Under the hood:** Block themes store their layout as structured HTML with block comments (`<!-- wp:heading -->`), not PHP template tags. WordPress's own PHP renders those blocks at request time, but the authoring format stays deliberately close to plain markup, which is what lets the visual editor read it back reliably.
