# Hello, Composer!

`hello.php` n'a aucune dépendance, il n'a donc besoin de personne pour les gérer. Les vrais projets, si, et presque dès le premier jour : une bibliothèque de tests par ici, un client HTTP par là. **[Composer](https://getcomposer.org/) est le moyen, pour un projet PHP, de récupérer le code de quelqu'un d'autre sans le copier-coller dans le sien.** Si vous avez déjà utilisé `npm`, `pip` ou `cargo`, vous connaissez le métier. Sinon, vous le connaîtrez à la fin de cette page.

## Installer Composer

Sur macOS ou Linux, le plus rapide passe généralement par votre gestionnaire de paquets :

```console
$ brew install composer
```

Partout ailleurs, ou pour la méthode officielle, la [page de téléchargement](https://getcomposer.org/download/) propose un court script d'installation. Dans les deux cas, vérifiez qu'il répond :

```console
$ composer --version
Composer version 2.7.6 2024-...
```

## Démarrer un projet

Dans un répertoire vide, lancez :

```console
$ composer init
```

Composer pose une poignée de questions : nom du paquet, description, auteur, licence. Appuyez sur Entrée à peu près partout, rien de tout cela n'est définitif. Ce qui compte, c'est le fichier qu'il laisse derrière lui, `composer.json` :

```json
{
    "name": "you/hello-composer",
    "require": {}
}
```

**`composer.json` est la liste de courses de votre projet.** Elle nomme ce dont le projet a besoin, et elle va dans le gestionnaire de versions. Ce que Composer rapporte du magasin, lui, n'y va pas, comme vous allez le voir.

## Installer un premier paquet

Ajoutons quelque chose de réel. [`nunomaduro/termwind`](https://github.com/nunomaduro/termwind) est une petite bibliothèque pour mettre en forme la sortie du terminal. Rien d'indispensable, juste de quoi voir le mécanisme fonctionner :

```console
$ composer require nunomaduro/termwind
```

Deux choses apparaissent. Un répertoire `vendor/` contient le code téléchargé. Un fichier `composer.lock` note la version *exacte* qui a été installée, jusqu'au dernier commit, pour que vos collègues et votre serveur de production installent très précisément la même chose. **`composer.json` dit ce que vous acceptez ; `composer.lock` dit ce que vous avez réellement obtenu.** Committez aussi le fichier lock. `vendor/` reste hors du gestionnaire de versions, puisque n'importe qui peut le reconstruire à partir du lock avec `composer install`.

<img src="images/ch07-composer-shopping.png" alt="Composer comme une séance de courses : composer.json est la liste écrite à la main, vendor/ le sac de paquets rapporté à la maison, et composer.lock le ticket de caisse imprimé avec les versions exactes" width="600">

Utilisons-le maintenant :

```php
<?php

require 'vendor/autoload.php';

use function Termwind\render;

render('<div class="p-1 bg-green-400">Hello, Composer!</div>');
```

Lancez le fichier. Une bannière verte s'affiche dans votre terminal, dessinée par du code installé il y a trente secondes et que vous n'avez jamais lu.

La ligne du milieu est celle qui compte. `require 'vendor/autoload.php'` inclut un fichier généré par Composer : un autoloader, un bout de PHP qui sait trouver et charger n'importe quelle classe de n'importe quel paquet installé, à l'instant où votre code la mentionne pour la première fois. **Incluez ce fichier, une fois, en tête de votre point d'entrée, et chaque paquet que vous ajouterez ensuite fonctionnera sans rien de plus.** La ligne `use function`, qui vous permet d'appeler `render()` par son nom court, aura droit à sa propre explication plus loin dans ce chapitre.

Pour l'instant, l'autoloader n'a eu qu'un seul travail : charger Termwind. La suite du chapitre lui en confie un second. La même ligne, inchangée, trouvera aussi vos propres classes, une fois qu'elles seront réparties dans des fichiers comme les projets PHP s'y attendent.
