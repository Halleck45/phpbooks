# Installation

## Ouvrir un terminal

**Un terminal, c'est une conversation avec votre ordinateur.** Vous tapez une phrase, vous appuyez sur Entrée, et il vous répond à la ligne suivante. Pas de boutons, pas de menus : des mots qui vont et viennent. Tous les exemples de ce livre se passent là. Première chose à faire : trouver le vôtre.

<img src="images/ch01-terminal-chat.png" alt="Un terminal dessiné comme une conversation : la personne tape une commande, l'ordinateur répond" width="520">

**macOS.** `Cmd+Espace`, tapez « Terminal », Entrée. C'est Terminal.app, et il suffit largement.

**Linux.** Chaque environnement de bureau en fournit un, généralement appelé Terminal, Konsole ou GNOME Terminal. Cherchez dans le menu des applications, ou essayez `Ctrl+Alt+T`.

**Windows.** Touche `Win`, tapez « Terminal », et ouvrez Windows Terminal. C'est celui de Windows 11 par défaut ; sur Windows 10, il s'installe depuis le Microsoft Store. À l'intérieur, Invite de commandes ou PowerShell, au choix : les deux conviennent pour ce livre.

## Avez-vous déjà PHP ?

Posez la question à votre ordinateur. Tapez ceci, puis Entrée :

```console
$ php -v
PHP 8.3.6 (cli) (built: ...) (NTS)
```

> [!TIP]
> Dans les exemples de terminal de ce livre, le `$` au début d'une ligne représente l'invite que le terminal affiche en attendant que vous tapiez. **Ne le tapez pas.** Tapez seulement ce qui vient après.

Regardez la réponse. Trois cas possibles :

- **Elle commence par `PHP 8`.** PHP est installé et assez récent. Filez directement à [Hello, World!](ch01-02-hello-world.md).
- **Elle commence par `PHP 7` ou moins.** Votre version est trop ancienne. Installez-en une nouvelle, juste en dessous.
- **Elle dit quelque chose comme `command not found`.** L'ordinateur ne connaît pas encore le mot `php`. Vous n'avez rien fait de travers : rien n'est installé, tout simplement. Lisez la suite.

## Installer PHP

**macOS.** Les versions récentes de macOS ne livrent plus PHP. Installez-le avec [Homebrew](https://brew.sh/) :

```console
$ brew install php
```

**Linux.** Le gestionnaire de paquets de votre distribution l'a. Sur Ubuntu ou Debian :

```console
$ sudo apt install php-cli
```

Les paquets des distributions ont parfois un an ou deux de retard. Si la version obtenue est trop vieille, le [dépôt d'Ondřej Surý](https://launchpad.net/~ondrej/+archive/ubuntu/php) suit les sorties de près.

**Windows.** Téléchargez l'archive « Non Thread Safe » sur [windows.php.net](https://windows.php.net/download/), décompressez-la dans un dossier simple comme `C:\php`, et ajoutez ce dossier à votre `PATH` pour que le terminal le trouve. Si vous préférez laisser un installeur s'en occuper, [Laragon](https://laragon.org/) ou [WampServer](https://www.wampserver.com/) livrent PHP avec une installation guidée.

**N'importe où, avec Docker.** Si vous ne voulez rien installer sur votre machine et que Docker est déjà là :

```console
$ docker run --rm -it php:8.3-cli bash
```

Vous obtenez un shell temporaire, PHP prêt à l'emploi, dans un petit environnement isolé. Tout ce que vous y tapez reste dans cette boîte, et la refermer laisse votre ordinateur exactement comme avant.

## Vérifier que ça marche

**Fermez votre terminal, ouvrez-en un nouveau**, et relancez `php -v`. Cette fois, un numéro de version doit s'afficher.

> [!TIP]
> Un terminal apprend la liste des programmes qu'il connaît au démarrage. Si vous venez d'installer PHP et qu'il répond encore `command not found`, neuf fois sur dix il suffit d'en ouvrir un nouveau.

## Bon à savoir : PHP a deux casquettes

En lisant sur PHP, vous croiserez des noms comme `php-cli`, `php-fpm` ou `mod_php`. **C'est le même langage, avec des casquettes différentes.**

<img src="images/ch01-two-hats.png" alt="PHP avec deux casquettes : une pour le terminal, où il exécute des scripts directement, une pour le serveur web, où il répond aux demandes de pages" width="520">

La première casquette, **`php-cli`**, c'est celle que vous venez d'installer. Elle exécute un script depuis votre terminal et affiche le résultat, comme le feraient Python ou Ruby.

La seconde, c'est **la version pour serveur web**. Elle se place derrière nginx ou Apache et répond aux demandes de pages.

Ce livre se contente de la première pendant longtemps. Quand le web arrivera, vous connaîtrez déjà le langage. Seule la casquette changera.
