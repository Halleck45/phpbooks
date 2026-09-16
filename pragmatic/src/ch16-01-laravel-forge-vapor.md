# Laravel: Forge and Vapor ($)

Laravel's own team offers two deployment products, aimed at different infrastructure preferences.

**Forge** provisions and manages a traditional server (on your own AWS, DigitalOcean, or Hetzner account) with zero manual server administration: it configures Nginx, PHP-FPM, a database, SSL certificates, and queue workers, and gives you a dashboard for deploying, monitoring, and scaling.

```bash
# after connecting a server through Forge's dashboard, deployment is a git push
git push forge main
```

Forge deploy scripts run whatever your project needs on each push, editable per site:

```bash
cd /home/forge/example.com
git pull origin main
composer install --no-dev --optimize-autoloader
php artisan migrate --force
php artisan queue:restart
```

**Vapor** is a different model entirely: serverless deployment onto AWS Lambda. There's no server to patch or scale manually; the application runs only while handling a request, and scales automatically to zero or to thousands of concurrent requests.

```bash
composer require laravel/vapor-cli --dev
vapor deploy production
```

## Pricing

Both are paid subscriptions on top of whatever infrastructure they provision (Forge charges per server managed; Vapor charges based on usage plus the underlying AWS costs), which is what earns them the `$`.

## When to reach for each

Forge for a traditional app that benefits from a persistent server (background workers, WebSocket connections via [Reverb](ch07-01-laravel-reverb-livewire.md)). Vapor for unpredictable or spiky traffic where paying only for actual usage, and never thinking about server capacity, outweighs the constraints serverless imposes.

## When it's the wrong fit

A team that already has infrastructure expertise and existing AWS/cloud tooling might prefer [managing deployment directly](ch16-02-cloud-hosting-aws-gcp-azure.md) rather than paying for Forge's convenience layer on top of it.

> **Under the hood:** Vapor's serverless model works because Laravel's request lifecycle was always stateless by design, nothing assumes the same process handles the next request, which is exactly the assumption Lambda's "cold start per invocation" model requires to work at all.
