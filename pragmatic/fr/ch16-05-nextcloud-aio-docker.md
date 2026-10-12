# Nextcloud : déploiement Docker All-in-One

Monter [Nextcloud](ch08-01-nextcloud-ready-made-drive.md) à la main, c'est configurer un serveur web, PHP-FPM, une base de données, Redis, un proxy inverse avec un TLS valide et une tâche cron en arrière-plan. Chacun est une occasion de mal régler quelque chose de sensible pour la sécurité. **L'image Docker All-in-One (AIO) est la réponse de Nextcloud lui-même : tout cela, précâblé, sous la forme d'un ensemble coordonné de conteneurs.**

```bash
docker run \
  --name nextcloud-aio-mastercontainer \
  --restart always \
  -p 8080:8080 \
  -v nextcloud_aio_mastercontainer:/mnt/docker-aio-config \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  nextcloud/all-in-one:latest
```

L'interface web du conteneur vous guide ensuite pour les certificats TLS, le choix des applications optionnelles à activer (dont le backend haute performance de Talk, vu dans [le temps réel](ch07-03-nextcloud-talk.md)) et la configuration des sauvegardes. Un seul tableau de bord, au lieu d'une douzaine de fichiers de configuration.

Les mises à jour de Nextcloud et de chaque application activée passent par la même interface :

```bash
# update the mastercontainer image, then trigger an update from its UI
docker pull nextcloud/all-in-one:latest
docker stop nextcloud-aio-mastercontainer
docker rm nextcloud-aio-mastercontainer
# re-run the original docker run command to restart it on the new image
```

## Quand le choisir

Auto-héberger Nextcloud pour un usage durable, pour une petite équipe ou toute une organisation. L'image AIO condense un savoir d'exploitation durement acquis sur la sécurisation et l'entretien d'une instance, le genre de chose qu'on rate facilement, et subtilement, à la main.

## Quand ce n'est pas le bon outil

Une évaluation locale rapide, où l'image Docker simple (voir [Nextcloud : un drive prêt à l'emploi](ch08-01-nextcloud-ready-made-drive.md)) se jette plus vite. Ou un environnement où Docker lui-même n'est pas une option.

> **Sous le capot :** Le motif du « mastercontainer », un conteneur qui gère le cycle de vie de plusieurs autres à travers la socket Docker, est une orchestration plus légère que Kubernetes et plus lourde qu'un simple `docker run`. Il existe pour que les mises à jour de services interdépendants (l'application, la base, le proxy) se fassent dans le bon ordre, toutes seules.
