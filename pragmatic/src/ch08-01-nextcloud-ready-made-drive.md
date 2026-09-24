# Nextcloud: A Ready-Made Drive, Not a DIY Project

When the actual request is "we need our own Dropbox," the pragmatic answer is almost never to build one. Nextcloud is a complete, mature, self-hosted file sync and sharing platform: desktop and mobile sync clients, sharing links with expiration and passwords, version history, and a full permissions model, all written in PHP, all ready to deploy today.

```bash
docker run -d -p 8080:80 \
  -v nextcloud:/var/www/html \
  nextcloud
```

Or, for a production-ready setup with the reverse proxy, database, and Redis cache already wired together, the All-in-One Docker image (see [Shipping to Production](ch16-05-nextcloud-aio-docker.md)) is the officially recommended path.

Once running, provisioning users and setting quotas is a command-line job, no custom code required:

```bash
php occ user:add jane.doe
php occ user:add-app-password jane.doe --group=editors
php occ files:external:create "shared-drive" local null::null -c datadir=/mnt/shared
```

Extending it, if a client needs something the built-in feature set doesn't cover, means writing an app in Nextcloud's own plugin system, the same architecture that powers [Nextcloud Talk](ch07-03-nextcloud-talk.md), rather than forking the whole platform.

## When to reach for this

Any request that's genuinely "we need our own file storage and sharing system," particularly for clients with data residency or privacy requirements that rule out Google Drive or Dropbox outright.

## When it's the wrong fit

A feature that's really just "let users upload a profile picture" or "attach a PDF to this order." That's ordinary file upload handling (see [Laravel: Filesystem Abstraction and S3-Compatible Storage](ch08-02-laravel-filesystem-s3.md)), not a reason to stand up an entire platform.

> **Under the hood:** Nextcloud's file synchronization relies on chunked uploads and ETags to detect what changed since the last sync, letting a client transfer only the parts of a large file that actually changed rather than re-uploading the whole thing, a meaningful engineering problem solved once, in PHP, so no app built on top of it has to solve it again.
