# Nextcloud: Scaling a Self-Hosted Platform

A self-hosted platform like [Nextcloud](ch08-01-nextcloud-ready-made-drive.md) asks a question most cloud products never expose to their customers: someone on your team has to operate the growth curve, not just pay for a bigger plan.

**Each step below answers one measured bottleneck**, in the order an organization usually meets them after outgrowing a single small server:

```bash
# 1. Move sessions and caching to Redis instead of the filesystem
php occ config:system:set redis host --value=redis.internal
php occ config:system:set memcache.distributed --value='\OC\Memcache\Redis'

# 2. Move file storage to S3-compatible object storage instead of local disk
php occ config:system:set objectstore class --value='\OC\Files\ObjectStore\S3'

# 3. Add read replicas and split heavy background jobs onto dedicated workers
php occ background:cron
```

Redis comes in when concurrent users start contending on file-based session locks. Object storage comes in when the local disk fills up, or when one server's I/O becomes the limit. Separate workers come in when scheduled tasks, such as the file previews Nextcloud generates on its own, start competing with live users for CPU.

An organization that does not want to own this curve at all has two supported routes: the All-in-One Docker image (see [Nextcloud: All-in-One Docker Deployment](ch16-05-nextcloud-aio-docker.md)) or Nextcloud's own hosted offering, trading operational ownership for a subscription.

## When to reach for this

A Nextcloud instance that has grown from a pilot team to an organization-wide rollout, where the single-server setup shows measured strain.

## When it's the wrong fit

A small team's instance, comfortably within the range of one well-specced server. Redis and object storage ahead of a bottleneck are complexity paid early for no measured benefit.

> **Under the hood:** Nextcloud's storage abstraction is built on Flysystem-style adapters (see [League/Flysystem](ch02-06-league-flysystem-standalone.md)). The code that reads and writes files does not change when the backend moves from local disk to S3, because it was never written against "the filesystem" in the first place.
