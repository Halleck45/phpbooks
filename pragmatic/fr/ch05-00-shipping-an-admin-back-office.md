# Livrer un back-office

« On pourrait avoir un écran pour modifier les produits nous-mêmes ? » Tôt ou tard, chaque application a besoin de cet écran : un endroit où quelqu'un qui n'est pas développeur corrige une fiche, valide une commande ou répare une coquille dans une table de paramètres. Le construire formulaire par formulaire est l'une des façons les moins rentables de dépenser un sprint. **Le modèle de données que vous avez déjà décrit suffit à un outil pour générer cet écran.**

<img src="images/ch05-generated-desk.png" alt="Un petit éléphant glisse une seule feuille de papier dans une machine en forme de boîte munie d'une manivelle. De l'autre côté sort, sur un tapis roulant, un bureau complet avec ses tiroirs, un classeur, un formulaire et un tableau de lignes. Une personne, tasse de café à la main, le regarde arriver" width="560">

Le choix dépend de ce qui décrit déjà vos données : un modèle Eloquent, une entité Doctrine, une ressource d'API ou un type de contenu WordPress.

- [Laravel : Filament en un après-midi](ch05-01-laravel-filament.md) génère une administration complète à partir des modèles Eloquent, presque sans code répétitif.
- [Symfony : EasyAdmin et Sonata](ch05-02-symfony-easyadmin.md), l'option légère et l'option lourde pour un projet Doctrine.
- [API Platform : une administration générée depuis votre API](ch05-03-api-platform-auto-admin.md) transforme l'API que vous exposez déjà en panneau d'administration, gratuitement.
- [WordPress : types de contenu personnalisés et ACF comme moteur CRUD](ch05-04-wordpress-cpt-as-crud.md) montre jusqu'où l'administration de WordPress s'étire avant qu'il faille autre chose.
- [Laravel Nova ($) : l'alternative officielle à Filament](ch05-05-laravel-nova.md) échange un panneau open source contre un support éditeur et une feuille de route.
