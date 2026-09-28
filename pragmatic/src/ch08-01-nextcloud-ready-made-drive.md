# Nextcloud: A Ready-Made Drive, Not a DIY Project

When the request is "we need our own Dropbox," the pragmatic answer is almost never to build one. **Nextcloud is a complete self-hosted file sync and sharing platform, written in PHP, and it deploys today.** Desktop and mobile sync clients, sharing links with expiration and passwords, version history, a full permissions model: all of it is already there.

```bash
docker run -d -p 8080:80 \
  -v nextcloud:/var/www/html \
  nextcloud
```

For a production setup with the reverse proxy, database, and Redis cache already wired, the All-in-One Docker image (see [Shipping to Production](ch16-05-nextcloud-aio-docker.md)) is the officially recommended path.

Once it runs, provisioning users and setting quotas is a command-line job, with no custom code:

```bash
php occ user:add jane.doe
php occ user:add-app-password jane.doe --group=editors
php occ files:external:create "shared-drive" local null::null -c datadir=/mnt/shared
```

When a client needs something the built-in feature set does not cover, you write an app in Nextcloud's plugin system, the same architecture behind [Nextcloud Talk](ch07-03-nextcloud-talk.md), instead of forking the platform.

## When to reach for this

A request that is truly "our own file storage and sharing system," and especially a client whose data residency or privacy requirements rule out Google Drive and Dropbox.

## When it's the wrong fit

A feature that amounts to "let users upload a profile picture" or "attach a PDF to this order." That is ordinary upload handling (see [Laravel: Filesystem Abstraction and S3-Compatible Storage](ch08-02-laravel-filesystem-s3.md)), not a reason to stand up a platform.

> **Under the hood:** Nextcloud's sync relies on chunked uploads and ETags to detect what changed since the last sync, so a client transfers only the parts of a large file that changed rather than the whole file again. That problem was solved once, in PHP, and no app built on top has to solve it again.
