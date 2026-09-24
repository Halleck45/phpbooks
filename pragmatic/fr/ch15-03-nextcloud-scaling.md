# Nextcloud : faire grandir une plateforme auto-hébergée

Une plateforme auto-hébergée comme [Nextcloud](ch08-01-nextcloud-ready-made-drive.md) pose une question que la plupart des produits cloud n'exposent jamais à leurs clients : quelqu'un dans votre équipe doit gérer la courbe de croissance, et pas seulement payer un forfait plus gros.

**Chaque étape ci-dessous répond à un goulot d'étranglement mesuré**, dans l'ordre où une organisation les rencontre d'habitude après avoir dépassé un seul petit serveur :

```bash
# 1. Move sessions and caching to Redis instead of the filesystem
php occ config:system:set redis host --value=redis.internal
php occ config:system:set memcache.distributed --value='\OC\Memcache\Redis'

# 2. Move file storage to S3-compatible object storage instead of local disk
php occ config:system:set objectstore class --value='\OC\Files\ObjectStore\S3'

# 3. Add read replicas and split heavy background jobs onto dedicated workers
php occ background:cron
```

Redis entre en jeu quand les utilisateurs simultanés commencent à se disputer les verrous de session sur fichiers. Le stockage objet arrive quand le disque local se remplit, ou quand les entrées-sorties d'un seul serveur deviennent la limite. Les workers séparés viennent quand les tâches planifiées, comme les aperçus de fichiers que Nextcloud génère de lui-même, se mettent à concurrencer les utilisateurs en ligne pour le processeur.

Une organisation qui ne veut pas du tout porter cette courbe a deux voies prises en charge : l'image Docker All-in-One (voir [Nextcloud : déploiement Docker All-in-One](ch16-05-nextcloud-aio-docker.md)) ou l'offre hébergée de Nextcloud lui-même, qui échange la charge d'exploitation contre un abonnement.

## Quand le choisir

Une instance Nextcloud passée d'une équipe pilote à un déploiement pour toute l'organisation, où l'installation sur un seul serveur montre une tension mesurée.

## Quand ce n'est pas le bon outil

L'instance d'une petite équipe, confortablement dans les limites d'un serveur bien dimensionné. Redis et le stockage objet avant tout goulot, c'est de la complexité payée d'avance sans bénéfice mesuré.

> **Sous le capot :** L'abstraction de stockage de Nextcloud repose sur des adaptateurs à la Flysystem (voir [League/Flysystem](ch02-06-league-flysystem-standalone.md)). Le code qui lit et écrit les fichiers ne change pas quand le stockage passe du disque local à S3, parce qu'il n'a jamais été écrit contre « le système de fichiers » directement.
