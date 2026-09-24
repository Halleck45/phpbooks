# Nextcloud : un drive prêt à l'emploi, pas un projet à bricoler

Quand la demande est « il nous faut notre propre Dropbox », la réponse pragmatique n'est presque jamais d'en construire un. **Nextcloud est une plateforme complète et auto-hébergée de synchronisation et de partage de fichiers, écrite en PHP, et elle se déploie aujourd'hui.** Clients de synchronisation pour ordinateur et mobile, liens de partage avec expiration et mot de passe, historique des versions, modèle de permissions complet : tout est déjà là.

```bash
docker run -d -p 8080:80 \
  -v nextcloud:/var/www/html \
  nextcloud
```

Pour une installation de production avec le reverse proxy, la base de données et le cache Redis déjà câblés, l'image Docker All-in-One (voir [Livrer en production](ch16-05-nextcloud-aio-docker.md)) est la voie officiellement recommandée.

Une fois la plateforme lancée, créer des utilisateurs et fixer des quotas se fait en ligne de commande, sans code :

```bash
php occ user:add jane.doe
php occ user:add-app-password jane.doe --group=editors
php occ files:external:create "shared-drive" local null::null -c datadir=/mnt/shared
```

Quand un client a besoin d'une chose que les fonctionnalités intégrées ne couvrent pas, vous écrivez une application dans le système d'extensions de Nextcloud, la même architecture que derrière [Nextcloud Talk](ch07-03-nextcloud-talk.md), au lieu de forker la plateforme.

## Quand le choisir

Une demande qui est vraiment « notre propre système de stockage et de partage de fichiers », et surtout un client dont les exigences de résidence des données ou de confidentialité écartent Google Drive et Dropbox d'emblée.

## Quand ce n'est pas le bon outil

Une fonctionnalité qui se résume à « laisser les utilisateurs envoyer une photo de profil » ou « joindre un PDF à cette commande ». C'est de l'envoi de fichiers ordinaire (voir [Laravel : abstraction de système de fichiers et stockage compatible S3](ch08-02-laravel-filesystem-s3.md)), pas une raison de monter une plateforme.

> **Sous le capot :** la synchronisation de Nextcloud repose sur des envois par morceaux et sur des ETags pour détecter ce qui a changé depuis la dernière synchronisation, si bien qu'un client ne transfère que les parties modifiées d'un gros fichier au lieu de le renvoyer en entier. Ce problème a été résolu une fois, en PHP, et aucune application bâtie par-dessus n'a à le résoudre à nouveau.
