# Nextcloud: All-in-One Docker Deployment

Standing up [Nextcloud](ch08-01-nextcloud-ready-made-drive.md) correctly by hand means configuring a web server, PHP-FPM, a database, Redis, a reverse proxy with valid TLS, and a background cron job, each a separate opportunity to misconfigure something security-sensitive. The All-in-One (AIO) Docker image is Nextcloud's own officially maintained answer: all of that, pre-wired, running as a coordinated set of containers.

```bash
docker run \
  --name nextcloud-aio-mastercontainer \
  --restart always \
  -p 8080:8080 \
  -v nextcloud_aio_mastercontainer:/mnt/docker-aio-config \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  nextcloud/all-in-one:latest
```

Visiting the container's web interface afterward walks through TLS certificate setup, choosing which optional apps to enable (Talk's high-performance backend, covered in [Real-Time Features](ch07-03-nextcloud-talk.md), included), and backup configuration, all managed through one dashboard rather than a dozen separate config files.

Updates, including of Nextcloud itself and each enabled app, are handled through the same interface:

```bash
# update the mastercontainer image, then trigger an update from its UI
docker pull nextcloud/all-in-one:latest
docker stop nextcloud-aio-mastercontainer
docker rm nextcloud-aio-mastercontainer
# re-run the original docker run command to restart it on the new image
```

## When to reach for this

Self-hosting Nextcloud for real, ongoing use, whether for a small team or a full organization. The AIO image encodes a lot of hard-won operational knowledge about correctly securing and maintaining a Nextcloud instance that's easy to get subtly wrong by hand.

## When it's the wrong fit

A quick local evaluation where the plain Docker image (see [Nextcloud: A Ready-Made Drive](ch08-01-nextcloud-ready-made-drive.md)) is faster to throw away, or an environment where Docker itself isn't an option.

> **Under the hood:** The mastercontainer pattern, one container that manages the lifecycle of several others via the Docker socket, is a form of orchestration lighter than Kubernetes but heavier than a single `docker run`, chosen specifically so updates to interdependent services (the app, the database, the proxy) happen in the right order automatically.
