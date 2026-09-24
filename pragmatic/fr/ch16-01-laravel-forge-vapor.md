# Laravel : Forge et Vapor ($)

L'équipe Laravel vend deux produits de déploiement, pour deux idées différentes de ce qu'est un serveur.

**Forge** provisionne et administre un serveur classique sur votre propre compte AWS, DigitalOcean ou Hetzner, sans administration manuelle. Il configure Nginx, PHP-FPM, une base de données, les certificats SSL et les workers de file d'attente, puis vous donne un tableau de bord pour déployer, surveiller et faire grandir.

```bash
# after connecting a server through Forge's dashboard, deployment is a git push
git push forge main
```

Le script de déploiement exécute ce dont votre projet a besoin à chaque push, et vous le modifiez site par site :

```bash
cd /home/forge/example.com
git pull origin main
composer install --no-dev --optimize-autoloader
php artisan migrate --force
php artisan queue:restart
```

**Vapor** est un autre modèle : un déploiement serverless sur AWS Lambda. Il n'y a aucun serveur à mettre à jour ni à dimensionner. **L'application ne tourne que pendant qu'elle traite une requête**, et s'adapte toute seule, de zéro à des milliers de requêtes simultanées.

```bash
composer require laravel/vapor-cli --dev
vapor deploy production
```

## Tarif

Les deux sont des abonnements qui s'ajoutent à l'infrastructure qu'ils provisionnent. Forge facture par serveur administré ; Vapor facture à l'usage, plus les coûts AWS sous-jacents.

## Lequel choisir

Forge pour une application qui profite d'un serveur persistant : workers en arrière-plan, connexions WebSocket via [Reverb](ch07-01-laravel-reverb-livewire.md). Vapor pour un trafic irrégulier ou imprévisible, où ne payer que l'usage, et ne plus jamais penser à la capacité, l'emporte sur les contraintes du serverless.

## Quand ce n'est pas le bon outil

Une équipe qui a déjà l'expertise infrastructure et son outillage cloud préférera peut-être [gérer le déploiement directement](ch16-02-cloud-hosting-aws-gcp-azure.md) plutôt que payer la couche de confort de Forge par-dessus.

> **Sous le capot :** Le modèle serverless de Vapor fonctionne parce que le cycle de vie d'une requête Laravel a toujours été sans état. Rien ne suppose que le même processus traitera la requête suivante, et c'est précisément l'hypothèse dont le modèle « démarrage à froid à chaque invocation » de Lambda a besoin pour marcher.
