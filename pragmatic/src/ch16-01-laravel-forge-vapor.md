# Laravel: Forge and Vapor ($)

The Laravel team sells two deployment products, for two different ideas of what a server is.

**Forge** provisions and manages a traditional server on your own AWS, DigitalOcean or Hetzner account, with no manual administration. It configures Nginx, PHP-FPM, a database, SSL certificates and queue workers, then gives you a dashboard to deploy, monitor and scale.

```bash
# after connecting a server through Forge's dashboard, deployment is a git push
git push forge main
```

The deploy script runs whatever your project needs on each push, and you edit it per site:

```bash
cd /home/forge/example.com
git pull origin main
composer install --no-dev --optimize-autoloader
php artisan migrate --force
php artisan queue:restart
```

**Vapor** is a different model: serverless deployment onto AWS Lambda. There is no server to patch or scale. **The application runs only while it handles a request**, and scales on its own from zero to thousands of concurrent requests.

```bash
composer require laravel/vapor-cli --dev
vapor deploy production
```

## Pricing

Both are subscriptions on top of the infrastructure they provision. Forge charges per managed server; Vapor charges by usage plus the underlying AWS costs.

## When to reach for each

Forge for an app that benefits from a persistent server: background workers, WebSocket connections through [Reverb](ch07-01-laravel-reverb-livewire.md). Vapor for spiky or unpredictable traffic, where paying only for use, and never thinking about capacity, outweighs the constraints serverless imposes.

## When it's the wrong fit

A team with infrastructure expertise and existing cloud tooling may prefer [managing deployment directly](ch16-02-cloud-hosting-aws-gcp-azure.md) to paying for Forge's convenience layer on top of it.

> **Under the hood:** Vapor's serverless model works because Laravel's request lifecycle was stateless from the start. Nothing assumes the same process handles the next request, which is the assumption Lambda's "cold start per invocation" model needs in order to work at all.
