# Nextcloud: Scaling a Self-Hosted Platform

A self-hosted platform like [Nextcloud](ch08-01-nextcloud-ready-made-drive.md) faces a scaling question most cloud SaaS products never expose to their customers: someone on your team has to actually operate the growth curve, not just pay for a bigger plan.

The standard path, in order, as an organization grows past a single small server:

```bash
# 1. Move sessions and caching to Redis instead of the filesystem
php occ config:system:set redis host --value=redis.internal
php occ config:system:set memcache.distributed --value='\OC\Memcache\Redis'

# 2. Move file storage to S3-compatible object storage instead of local disk
php occ config:system:set objectstore class --value='\OC\Files\ObjectStore\S3'

# 3. Add read replicas and split heavy background jobs onto dedicated workers
php occ background:cron
```

Each step addresses a specific, identifiable bottleneck rather than being applied preemptively: Redis when concurrent users start contending on file-based session locks, object storage when local disk fills up or a single server's I/O becomes the limit, background job separation when scheduled tasks (like the file preview generation Nextcloud does automatically) start competing with live user requests for CPU.

For organizations that don't want to own this operational curve at all, the officially supported route is the All-in-One Docker image (see [Nextcloud: All-in-One Docker Deployment](ch16-05-nextcloud-aio-docker.md)) or Nextcloud's own hosted offering, trading operational ownership for a subscription.

## When to reach for this

Any self-hosted Nextcloud instance that's grown from a pilot team to an organization-wide rollout, where the default single-server setup starts showing real, measured strain rather than hypothetical concern.

## When it's the wrong fit

A small team's instance well within the comfortable range of a single well-specced server. Adding Redis and object storage ahead of an actual bottleneck is operational complexity paid for early, for no measured benefit.

> **Under the hood:** Nextcloud's storage abstraction is, again, built on Flysystem-style adapters (see [League/Flysystem](ch02-06-league-flysystem-standalone.md)): the application code that reads and writes files doesn't change when the backend switches from local disk to S3, because it was never written against "the filesystem" directly in the first place.
