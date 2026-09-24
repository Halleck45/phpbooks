# WordPress : l'hébergement infogéré bien fait (Kinsta, WP Engine $)

Un hébergement générique traite WordPress comme n'importe quelle application PHP. L'hébergement WordPress infogéré, chez des fournisseurs comme Kinsta ou WP Engine, est bâti autour de ce dont WordPress a besoin, et on le sait : un cache objet et un cache de pages réglés sur ses schémas de requêtes, un environnement de préproduction en un clic, des mises à jour du cœur et des extensions selon un calendrier que vous contrôlez, et une recherche de logiciels malveillants ciblée sur les failles connues des extensions.

```bash
# a typical managed-host workflow: staging, then push to production
wp @staging plugin update --all
wp @staging cache flush
# after review in the staging environment
wp @production deploy
```

**La différence avec un hébergement que vous gérez vous-même apparaît pendant un incident.** Les hébergeurs infogérés incluent des sauvegardes automatiques avec restauration en un clic, et un support qui sait déjà comment WordPress tombe en panne, plutôt qu'un support serveur généraliste qui découvre la plateforme en lisant votre ticket.

## Tarif

Kinsta et WP Engine sont payants, par paliers de trafic et de nombre de sites, sans offre gratuite. Le coût se situe bien au-dessus d'un hébergement mutualisé générique et bien en dessous d'une équipe interne qui ferait à la main le même travail de fiabilité et de performance.

## Quand le choisir

Tout site WordPress exposé aux clients, générateur de revenus ou important pour une autre raison, où une panne ou une page lente a un coût, et où personne en interne ne veut prendre en charge le réglage serveur et la surveillance de sécurité propres à WordPress.

## Quand ce n'est pas le bon outil

Un blog personnel sans enjeu, ou un outil interne. Un hébergement générique moins cher suffit, et l'outillage spécialisé resterait inutilisé.

> **Sous le capot :** Une grande part de ce que vendent ces hébergeurs est du cache objet : les résultats des requêtes WordPress coûteuses gardés en mémoire, via Redis ou Memcached, pour qu'une page populaire ne relance pas les mêmes requêtes à chaque visiteur. C'est le réflexe de cache derrière [le framework de cache de TYPO3](ch15-02-typo3-caching-framework.md), préconfiguré pour les schémas de requêtes habituels de WordPress.
