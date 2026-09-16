# Cloud Hosting: AWS, GCP, and Azure the Pragmatic Way

Sometimes the deployment decision isn't yours to make: the client already has an AWS, Google Cloud, or Azure contract, often for compliance, procurement, or existing-infrastructure reasons that have nothing to do with what's easiest for you. In that situation, the pragmatic move is picking the option on that specific cloud that costs the least operational effort, not hand-rolling infrastructure you don't need.

**AWS**: App Runner takes a container and runs it with automatic scaling and load balancing, with far less configuration than a hand-built EC2/ECS setup.

```bash
aws apprunner create-service \
  --service-name my-app \
  --source-configuration file://apprunner-config.json
```

**Google Cloud**: Cloud Run does the same job for a container on GCP, scaling to zero when idle, which suits a modest-traffic app well on a usage-based bill.

```bash
gcloud run deploy my-app --source . --platform managed --region us-central1
```

**Azure**: App Service supports PHP directly, without needing to containerize first, closer in spirit to traditional managed hosting than the container-first AWS and GCP options above.

```bash
az webapp up --runtime "PHP:8.3" --name my-app
```

A `Dockerfile` written once, using a standard `php:8.3-fpm` or FrankenPHP-based image, generally works across App Runner and Cloud Run with little to no change, since both just want a container that listens on a port.

## When to reach for this

The client already has, or specifically requires, infrastructure on a particular cloud provider, and a framework-specific platform like [Forge](ch16-01-laravel-forge-vapor.md) or a third-party PaaS like [Platform.sh](ch16-03-platform-sh.md) isn't an option for procurement or compliance reasons.

## When it's the wrong fit

No existing cloud relationship, and no compliance requirement pointing at one. In that case, a framework-native option or a dedicated PaaS usually reaches production faster with less infrastructure knowledge required.

> **Under the hood:** All three platforms ultimately run the same PHP-FPM or FrankenPHP process your local development environment does; a container is a container. The differences between them are entirely in deployment mechanics and billing, not in how PHP itself executes your code once it's running.
