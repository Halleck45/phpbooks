# Craft CMS ($) : un CMS sous licence, pensé pour les rédactions

Craft part d'une hypothèse différente de celle de WordPress : il n'y a aucun modèle de contenu par défaut. **Chaque projet définit ses propres champs, types d'entrées et structure à partir de zéro**, avec l'éditeur de Craft comme couche visuelle. La première heure est plus lente qu'avec WordPress. L'année qui suit est plus rapide, pour les clients dont le contenu ne rentre pas dans un « article » générique.

```bash
composer create-project craftcms/craft my-site
cd my-site
php craft setup
php craft serve
```

Vous définissez la structure du contenu dans l'interface d'administration de Craft (champs, sections, types d'entrées), puis vous l'interrogez dans des templates Twig :

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

## Licence

Le cœur de Craft est à sources ouvertes : vous pouvez lire et modifier le code. L'exploiter commercialement exige une licence payante par projet. Un palier gratuit existe pour l'évaluer sur un site mono-utilisateur et non commercial.

## Quand le choisir

Les agences qui construisent des sites éditoriaux sur mesure pour des clients aux besoins précis et au budget prévu pour la licence, qui préfèrent un modèle de contenu taillé pour eux à un modèle générique étiré.

## Quand ce n'est pas le bon outil

Un budget serré, un brief en forme de blog générique, ou un client qui veut la place de marché d'extensions de WordPress. L'écosystème d'extensions de Craft existe, mais il est bien plus petit.

> **Sous le capot :** le système de champs souple de Craft repose sur un schéma relationnel classique. L'accès dynamique aux propriétés de PHP et le constructeur de requêtes de Craft font que des structures de contenu très différentes se manipulent dans Twig comme des données typées, pas comme des tableaux.
