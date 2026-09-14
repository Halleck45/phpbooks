# Étendre Composer avec des scripts et des plugins

`composer test` et `composer check` sont des scripts que vous lancez vous-même. Les scripts ont un second usage, plus discret. **Accrochez-en un à un moment du cycle de vie de Composer, et il s'exécute tout seul, au bon moment, sans que personne ait à y penser.**

## Les événements du cycle de vie

Composer émet un événement nommé à chaque étape de son travail : avant et après une installation, avant et après une mise à jour, et quelques autres. Utilisez l'un de ces noms comme clé de script, au lieu d'en inventer un, et Composer l'appelle quand le moment arrive :

```json
{
    "scripts": {
        "post-install-cmd": "@php artisan-like-thing:setup",
        "post-update-cmd": [
            "@php bin/generate-config.php"
        ]
    }
}
```

<img src="images/ch16-lifecycle-hook.png" alt="La frise d'un composer install : les paquets sont téléchargés, puis une cloche marquée post-install-cmd sonne et un script s'exécute tout seul, sans que personne tape de commande" width="600">

`post-install-cmd` s'exécute après chaque `composer install` : un clone frais qui récupère ses dépendances, un job d'intégration continue qui se prépare avant les tests, un nouveau collègue à son premier jour. Personne n'a à dénicher l'étape supplémentaire enfouie dans un README, parce que Composer s'en charge, dans le bon ordre, à chaque fois. `post-update-cmd` est le même hook pour `composer update`. D'autres événements existent pour des moments plus précis, avant l'installation ou la suppression d'un seul paquet par exemple, mais ces deux-là couvrent la plupart des besoins réels : régénérer un fichier de configuration, préchauffer un cache, afficher un rappel sur une variable d'environnement encore à définir.

> [!TIP]
> Le préfixe `@php` lance le script avec le binaire PHP sous lequel Composer tourne lui-même. Sur une machine où plusieurs versions de PHP sont installées, il lève tout doute sur le `php` utilisé.

## Où s'arrêtent les scripts, où commencent les plugins

Un script de cycle de vie est une commande que Composer lance à un point fixe. C'est utile, et ce n'est que cela. Parfois vous voulez davantage : une nouvelle commande Composer, une autre façon d'installer les paquets, une réaction à un événement écrite en vraie logique PHP plutôt qu'une ligne de shell lancée sans retour. **C'est à cela que servent les plugins : des paquets Composer ordinaires qui se branchent sur les entrailles de Composer, écrits en PHP, installés comme n'importe quelle dépendance.** Vous en avez sans doute déjà utilisé un sans le savoir ; la gestion automatique des fichiers `.env` dans certains frameworks est un plugin Composer sous le capot.

En écrire un est une démarche légitime, et c'est du vrai territoire interne à Composer : classes d'abonnés aux événements, API de plugins propre à Composer, bien au-delà de ce que ce livre couvre. Quand les scripts de cycle de vie ne suffisent plus, c'est la porte suivante, et la [documentation officielle de Composer](https://getcomposer.org/doc/articles/plugins.md) est l'endroit où commencer.
