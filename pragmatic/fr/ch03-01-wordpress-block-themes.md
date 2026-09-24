# WordPress : thèmes de blocs et éditeur de site

WordPress fait toujours tourner une large part du web de contenu, et le WordPress d'aujourd'hui n'est plus l'outil sur lequel sa réputation est restée figée. **Avec les thèmes de blocs et l'éditeur de site, un client construit et réorganise visuellement des mises en page entières, en-têtes et pieds de page compris**, dans le même éditeur de blocs qu'il utilise déjà pour ses articles. Les modifications de mise en page courantes ne demandent plus aucun fichier de template PHP.

```bash
wp core download --path=my-site
cd my-site
wp config create --dbname=my_site --dbuser=root --dbpass=
wp core install --url=localhost:8080 --title="My Site" --admin_user=admin --admin_password=admin --admin_email=you@example.com
wp theme install twentytwentyfive --activate
```

Votre travail, dans un thème de blocs, tient surtout dans `theme.json` : la palette de couleurs, l'échelle d'espacements et la typographie parmi lesquelles le client peut choisir. Quoi qu'il réorganise, le site reste dans la charte.

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

Quand un client a besoin d'une chose que les blocs par défaut ne couvrent pas, un bloc sur mesure s'enregistre en PHP et peut tenir dans une seule fonction.

## Quand le choisir

Sites vitrines, blogs et sites de petites entreprises, quand le client veut modifier le site lui-même après la mise en ligne, et quand l'écosystème d'extensions (formulaires, SEO, cache) résout les problèmes plus vite que vous ne les coderiez.

## Quand ce n'est pas le bon outil

Un site qui est surtout de la logique applicative sur mesure, habillée d'une mince couche de contenu. Forcer cela dans le modèle de contenu de WordPress coûte en général plus de temps qu'il n'en fait gagner.

> **Sous le capot :** un thème de blocs stocke sa mise en page sous forme de HTML structuré avec des commentaires de bloc (`<!-- wp:heading -->`), pas de balises de template PHP. Le PHP de WordPress rend ces blocs à chaque requête, mais le format d'écriture reste volontairement proche du balisage brut, et c'est ce qui permet à l'éditeur visuel de le relire sans se tromper.
