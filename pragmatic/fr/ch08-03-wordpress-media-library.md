# WordPress : la médiathèque quand elle grossit

La médiathèque gère les envois, la génération des vignettes et une grille avec recherche, sans extension. **Pour la plupart des sites de contenu, c'est toute la fonctionnalité, déjà faite.**

```php
$attachment_id = media_handle_upload('file', $post_id);
$url = wp_get_attachment_url($attachment_id);
$thumb = wp_get_attachment_image_url($attachment_id, 'medium');
```

Le premier problème d'échelle est presque toujours l'espace disque local et la bande passante, une fois que le site compte des milliers d'images. Le remède standard déporte le stockage vers un stockage objet compatible S3 par une extension, et les rédacteurs gardent la même interface :

```bash
wp plugin install amazon-s3-and-cloudfront --activate
wp media-offload run
```

À partir de là, les envois passent par le même écran, et les fichiers sont stockés et servis depuis le stockage objet plutôt que depuis le disque du serveur.

Le second problème est le traitement des images lui-même. Générer plusieurs tailles de vignette pour chaque envoi pèse lourd sur le processeur à grand volume, et la réponse habituelle consiste à laisser un CDN redimensionner à la volée au lieu de pré-générer chaque taille à l'envoi.

## Quand le choisir

Tout site WordPress avec plus d'une poignée d'images, autrement dit presque tous. Même un petit site vitrine reçoit gratuitement les tailles de vignette automatiques et la grille avec recherche.

## Quand ce n'est pas le bon outil

L'hébergement de vidéos, ou une application lourde en médias à grande échelle. Une plateforme média spécialisée, intégrée par son API, sert mieux ce besoin qu'une médiathèque étirée bien au-delà de ce pour quoi elle a été conçue.

> **Sous le capot :** WordPress génère les tailles de vignette au moment de l'envoi avec l'extension GD ou Imagick de PHP, selon ce que le serveur possède. Redimensionner d'avance plutôt qu'à la demande explique pourquoi les grosses médiathèques finissent par avoir besoin du déport décrit plus haut : le coût est payé une seule fois par envoi, mais payé par chaque envoi.
