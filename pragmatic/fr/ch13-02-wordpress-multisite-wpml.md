# WordPress : Multisite et WPML

WordPress a deux réponses ici, à deux questions différentes. **Se tromper de réponse est une erreur courante, et coûteuse à défaire.**

**« Nous avons plusieurs sites distincts qui doivent partager leurs utilisateurs et leurs extensions. »** Plusieurs filiales nationales avec leur propre contenu et leur propre design, pas une traduction des mêmes pages. C'est ce que résout WordPress Multisite : une seule installation qui fait tourner un réseau de sites séparés, avec le code et les utilisateurs en commun, mais pas le contenu.

```bash
wp core multisite-convert
wp site create --slug=fr --title="Example France"
wp site create --slug=de --title="Example Germany"
```

**« Nous avons un site qui doit exister en plusieurs langues. »** Les mêmes pages, traduites. Multisite est le mauvais outil pour ça, puisqu'il faudrait entretenir à la main une copie de chaque page. Une extension de traduction comme WPML garde un seul site, avec pour chaque page ses traductions reliées :

```bash
wp plugin install sitepress-multilingual-cms --activate
wp wpml language add fr de
```

```php
// getting a translated post ID for the current language
$translated_id = apply_filters('wpml_object_id', $post_id, 'post', true);
```

## Lequel choisir

Multisite quand les sites diffèrent au-delà de la traduction : autre design, autre stratégie de contenu, une équipe d'administration par pays. WPML quand c'est le même site et le même contenu, dans plus d'une langue.

## Quand ce n'est pas le bon outil

Multisite comme outil de traduction, ou WPML pour faire tourner des sites qui sont en réalité séparés et gérés indépendamment. Les deux erreurs sont fréquentes, et les deux coûtent cher une fois qu'un an de contenu s'est accumulé sur la mauvaise structure.

> **Sous le capot :** Multisite ajoute un `blog_id` aux tables du cœur de WordPress et fait passer les requêtes par un amorçage conscient du réseau, ce qui revient à faire tourner plusieurs installations logiquement séparées sur un même code. WPML ajoute au contraire sa propre table de liaison entre articles traduits, et laisse intacte l'architecture monosite du cœur.
