# Comment PHP s'exécute

**PHP n'exécute pas votre application : il exécute votre script, une fois, pour une requête, puis il s'arrête.** Il n'y a pas d'objet serveur à instancier, pas d'appel à `listen()`, pas de boucle d'événements. Quelque chose d'extérieur à PHP (un serveur web, ou vous dans un terminal) lance l'interpréteur, l'interpréteur exécute un fichier de haut en bas, et tout ce qu'il a alloué est libéré quand le fichier se termine.

Tous les autres chapitres de ce livre sont plus faciles une fois celui-ci assimilé.

## Deux portes d'entrée

Depuis un terminal, PHP se comporte comme Python ou Ruby :

```bash
php hello.php
php -r 'echo PHP_VERSION, PHP_EOL;'
php -a          # interactive shell
php -l file.php # syntax check only
php -S localhost:8000   # development web server, current folder as document root
```

Sur le web, PHP n'est pas le serveur. **Le serveur web reçoit la requête HTTP et la transmet à PHP**, le plus souvent via PHP-FPM, un pool de processus PHP en attente derrière nginx, Apache ou Caddy. Un processus prend la requête, exécute le script auquel l'URL correspond, écrit la réponse, nettoie, et retourne attendre la suivante. Le pool compte autant de processus que vous en configurez, et c'est ainsi que PHP utilise tous vos cœurs, avec des processus plutôt qu'avec des threads.

<img src="images/ch01-request-lifecycle.png" alt="Une boucle en quatre étapes : un navigateur envoie une requête, un éléphant tout neuf se réveille dans une pièce vide, il construit la réponse sur un établi, puis la remet et la pièce est nettoyée pour la requête suivante" width="560">

La couche qui relie l'interpréteur au monde extérieur s'appelle une SAPI (server API). La ligne de commande, FPM et le `mod_php` d'Apache sont trois SAPI différentes posées sur le même moteur ; seule la plomberie change de l'une à l'autre.

## Rien de partagé

C'est la partie qui change votre façon d'écrire du code. **Rien ne survit d'une requête à la suivante à l'intérieur de PHP.** Une propriété statique que vous affectez, une globale, une connexion ouverte, un objet mis en cache dans un tableau : tout cela existe le temps d'une requête, puis disparaît.

```php
<?php
declare(strict_types=1);

final class Counter
{
    public static int $hits = 0;
}

Counter::$hits++;
echo Counter::$hits; // 1, on every single request, forever
```

Exécutez ce code sous un serveur web, rechargez la page cent fois, et il affiche 1 cent fois, là où le même code en Node ou en Java compterait jusqu'à 100. Aucun des deux comportements n'est un bug, ce sont simplement deux modèles différents.

Les conséquences s'enchaînent :

- **Un bug n'affecte qu'une requête.** Fuite mémoire, boucle infinie, exception non rattrapée : le processus qui traitait cette requête meurt ou est recyclé, et la requête suivante en reçoit un neuf.
- **La montée en charge est horizontale par construction.** Plus de trafic demande plus de processus FPM ou plus de machines, et rien dans l'application n'a besoin d'être thread-safe, puisque rien n'est partagé.
- **L'état vit hors de PHP.** Les sessions vont dans des fichiers, une base de données ou un stockage clé-valeur. Les caches vont dans OPcache et APCu (mémoire partagée entre les processus d'une machine) ou dans un stockage externe comme Redis ou Memcached. La connexion à la base s'ouvre au début de la requête et se ferme à la fin ; le pooling, si vous en avez besoin, se fait dans un pooler devant la base, pas dans PHP.
- **Le coût de démarrage se paie à chaque requête.** C'est ce qui explique que PHP démarre vite, et que l'écosystème accorde autant d'attention à l'autoloading, à OPcache et au préchargement.

> Si vous vous surprenez à concevoir un singleton pour « garder la connexion ouverte entre les requêtes », arrêtez-vous : dans ce modèle, il n'existe aucun moment entre deux requêtes.

## Le cache de bytecode

Lire et compiler chaque fichier à chaque requête serait lent, alors PHP ne le fait pas. **OPcache conserve la forme compilée de chaque fichier en mémoire partagée**, et la requête suivante la réutilise. Il est livré avec PHP et activé par défaut dans toute installation sérieuse.

En développement, OPcache vérifie les dates des fichiers et recompile ce qui a changé, donc la boucle éditer-recharger fonctionne telle quelle, sans étape de build ni watcher. En production, la vérification des dates est en général désactivée pour gagner du temps, ce qui signifie qu'**un déploiement doit réinitialiser le cache**, en redémarrant FPM ou en appelant `opcache_reset()`. Quand on l'oublie, on obtient le classique « j'ai déployé et rien n'a changé ».

OPcache héberge aussi le compilateur JIT (PHP 8.0). Il aide surtout les scripts gourmands en CPU, et ce n'est pas lui qui rend une application web rapide, donc voyez-le comme une option à essayer plutôt que comme une fondation.

## PHP persistant

Le modèle sans état partagé est le comportement par défaut, pas une loi. **Plusieurs runtimes gardent votre application en mémoire entre les requêtes**, comme le ferait un serveur Node ou Java : FrankenPHP en mode worker, RoadRunner, et Swoole ou OpenSwoole. Votre amorçage s'exécute une fois, puis une boucle vous tend les requêtes l'une après l'autre.

<img src="images/ch01-two-runtime-modes.png" alt="À gauche : une rangée de petites pièces identiques, chacune avec un éléphant neuf, une requête qui entre et une réponse qui sort, puis la pièce vidée. À droite : une grande pièce avec un seul éléphant qui reste à son bureau pendant qu'une file de requêtes défile" width="620">

Le gain est réel, puisque le coût d'amorçage disparaît et que les connexions peuvent vraiment rester ouvertes. Le coût est celui que vous connaissez déjà des autres langages : l'état fuit si vous ne le nettoyez pas, une fuite mémoire grossit, et un compteur statique compte pour de bon. Les frameworks qui supportent ces runtimes réinitialisent leur conteneur entre deux requêtes précisément pour cela. Commencez avec FPM, et passez à un runtime worker quand vous aurez mesuré une raison de le faire.

## Ce qu'il y a dans la boîte

L'interpréteur est un cœur en C plus des extensions, certaines intégrées et toujours actives, d'autres compilées au build, d'autres installées à part. `php -m` liste ce que contient votre build. Celles dont vous remarquerez l'absence sur une installation fraîche sont en général `pdo_mysql` ou `pdo_pgsql` (pilotes de base de données), `intl` (collation Unicode, formatage), `mbstring` (chaînes multi-octets), `curl`, `gd` ou `imagick` (images), et `xdebug` (débogueur, développement seulement).

Votre gestionnaire de paquets les fournit sous forme de paquets séparés (`php-intl`, `php-mbstring`, etc.), et l'image Docker officielle fournit `docker-php-ext-install`. Les extensions non livrées avec PHP viennent de PECL, ou de PIE, l'installeur d'extensions plus récent, dans l'esprit de Composer.

La configuration vit dans `php.ini`. **La ligne de commande et FPM lisent des fichiers ini différents**, ce qui explique qu'un script se comporte d'une façon dans un terminal et d'une autre sous le serveur web. `php --ini` montre les fichiers que charge la CLI, et `phpinfo()` dans une page montre ceux que charge FPM. Deux réglages comptent dès le premier jour : `memory_limit` (128 Mo par défaut sous FPM, illimité en CLI) et `max_execution_time` (30 secondes sous FPM, illimité en CLI).

## Le piège

En venant d'un runtime persistant, la première erreur est d'attendre que la mémoire persiste, avec un cache dans un tableau statique, une classe « pool de connexions » ou un compteur pour limiter le débit. Sous FPM, tout cela ne sert silencieusement à rien. La seconde erreur est le miroir de la première : après le passage à un runtime worker, une valeur propre à une requête rangée dans une statique se retrouve partagée entre les utilisateurs.

Posez une seule question sur tout état : doit-il survivre à cette requête ? Si oui, sa place n'est pas dans la mémoire de PHP, mais dans la base, dans un cache ou dans la session.

Une fois ce modèle en place, la syntaxe est la partie facile, et c'est l'objet du chapitre [La syntaxe](ch02-syntax.md).
