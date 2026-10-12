# Cloud Hosting: AWS, GCP, and Azure the Pragmatic Way

Sometimes the deployment decision is not yours. The client already has an AWS, Google Cloud or Azure contract, for compliance, procurement or existing-infrastructure reasons that have nothing to do with what is easiest for you. **The pragmatic move is the option on that cloud that costs the least operational effort**, not infrastructure you hand-roll and do not need.

**AWS**: App Runner takes a container and runs it with automatic scaling and load balancing, with far less configuration than a hand-built EC2/ECS setup.

```bash
aws apprunner create-service \
  --service-name my-app \
  --source-configuration file://apprunner-config.json
```

**Google Cloud**: Cloud Run does the same job for a container on GCP. It scales to zero when idle, which suits a modest-traffic app on a usage-based bill.

```bash
gcloud run deploy my-app --source . --platform managed --region us-central1
```

**Azure**: App Service runs PHP directly, no container required. It is closer in spirit to traditional managed hosting than the container-first options above.

```bash
az webapp up --runtime "PHP:8.3" --name my-app
```

A `Dockerfile` written once, on a standard `php:8.3-fpm` or FrankenPHP image, works on App Runner and Cloud Run with little or no change. Both only want a container that listens on a port.

## When to reach for this

The client already has, or requires, infrastructure on one cloud, and a framework platform like [Forge](ch16-01-laravel-forge-vapor.md) or a third-party PaaS like [Platform.sh](ch16-03-platform-sh.md) is ruled out by procurement or compliance.

## When it's the wrong fit

No existing cloud relationship and no compliance requirement pointing at one. A framework-native option or a dedicated PaaS usually reaches production faster, with less infrastructure knowledge required.

> **Under the hood:** All three platforms run the same PHP-FPM or FrankenPHP process your laptop does; a container is a container. The differences are in deployment mechanics and billing, not in how PHP executes your code once it is running.
