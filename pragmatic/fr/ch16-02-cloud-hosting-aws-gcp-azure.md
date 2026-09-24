# Cloud : AWS, GCP et Azure sans se compliquer la vie

Parfois, la décision de déploiement ne vous appartient pas. Le client a déjà un contrat AWS, Google Cloud ou Azure, pour des raisons de conformité, d'achats ou d'infrastructure existante qui n'ont rien à voir avec ce qui vous arrange. **Le choix pragmatique, c'est l'option de ce cloud qui coûte le moins d'effort d'exploitation**, pas une infrastructure montée à la main dont vous n'avez pas besoin.

**AWS** : App Runner prend un conteneur et le fait tourner avec mise à l'échelle et répartition de charge automatiques, avec bien moins de configuration qu'un montage EC2/ECS à la main.

```bash
aws apprunner create-service \
  --service-name my-app \
  --source-configuration file://apprunner-config.json
```

**Google Cloud** : Cloud Run fait le même travail pour un conteneur sur GCP. Il descend à zéro instance quand il est inactif, ce qui convient à une application à trafic modeste facturée à l'usage.

```bash
gcloud run deploy my-app --source . --platform managed --region us-central1
```

**Azure** : App Service exécute PHP directement, sans conteneur. Il est plus proche, dans l'esprit, d'un hébergement infogéré classique que des options ci-dessus, pensées d'abord pour les conteneurs.

```bash
az webapp up --runtime "PHP:8.3" --name my-app
```

Un `Dockerfile` écrit une fois, sur une image standard `php:8.3-fpm` ou FrankenPHP, tourne sur App Runner comme sur Cloud Run avec peu ou pas de changement. Les deux ne demandent qu'un conteneur qui écoute sur un port.

## Quand le choisir

Le client a déjà, ou exige, une infrastructure sur un cloud donné, et une plateforme liée au framework comme [Forge](ch16-01-laravel-forge-vapor.md) ou un PaaS tiers comme [Platform.sh](ch16-03-platform-sh.md) est exclu par les achats ou la conformité.

## Quand ce n'est pas le bon outil

Aucune relation cloud existante et aucune exigence de conformité qui en désigne un. Une option native du framework ou un PaaS spécialisé atteint la production plus vite, avec moins de connaissances d'infrastructure.

> **Sous le capot :** Les trois plateformes exécutent le même processus PHP-FPM ou FrankenPHP que votre portable ; un conteneur est un conteneur. Les différences tiennent à la mécanique de déploiement et à la facturation, pas à la façon dont PHP exécute votre code une fois lancé.
