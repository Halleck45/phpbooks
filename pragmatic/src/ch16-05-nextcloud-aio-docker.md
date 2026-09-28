# Nextcloud: All-in-One Docker Deployment

Standing up [Nextcloud](ch08-01-nextcloud-ready-made-drive.md) by hand means configuring a web server, PHP-FPM, a database, Redis, a reverse proxy with valid TLS and a background cron job. Each is a separate chance to misconfigure something security-sensitive. **The All-in-One (AIO) Docker image is Nextcloud's own answer: all of that, pre-wired, as a coordinated set of containers.**

```bash
docker run \
  --name nextcloud-aio-mastercontainer \
  --restart always \
  -p 8080:8080 \
  -v nextcloud_aio_mastercontainer:/mnt/docker-aio-config \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  nextcloud/all-in-one:latest
```

The container's web interface then walks you through TLS certificates, the optional apps to enable (including Talk's high-performance backend, covered in [Real-Time Features](ch07-03-nextcloud-talk.md)) and backup configuration. One dashboard, instead of a dozen config files.

Updates to Nextcloud and to each enabled app go through the same interface:

```bash
# update the mastercontainer image, then trigger an update from its UI
docker pull nextcloud/all-in-one:latest
docker stop nextcloud-aio-mastercontainer
docker rm nextcloud-aio-mastercontainer
# re-run the original docker run command to restart it on the new image
```

## When to reach for this

Self-hosting Nextcloud for ongoing use, for a small team or a whole organization. The AIO image encodes hard-won operational knowledge about securing and maintaining an instance, the kind that is easy to get subtly wrong by hand.

## When it's the wrong fit

A quick local evaluation, where the plain Docker image (see [Nextcloud: A Ready-Made Drive](ch08-01-nextcloud-ready-made-drive.md)) is faster to throw away. Or an environment where Docker itself is not an option.

> **Under the hood:** The mastercontainer pattern, one container managing the lifecycle of several others through the Docker socket, is orchestration lighter than Kubernetes and heavier than a single `docker run`. It exists so that updates to interdependent services (the app, the database, the proxy) happen in the right order on their own.
