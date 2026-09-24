# Dépôts de type path et monorepos

Publier suppose que votre paquet soit assez fini pour être confié à des inconnus. Une bonne partie du vrai travail se fait avant, dans la période où deux paquets liés grandissent ensemble et où un changement dans l'un doit apparaître dans l'autre immédiatement. **Composer a un type de dépôt conçu pour cette période : le dépôt path.**

## Le problème qu'il résout

Imaginons que vous coupiez `phpgrep` en deux : une bibliothèque cœur, `phpgrep/core`, et une enveloppe en ligne de commande, `phpgrep/cli`, qui en dépend. Tapez `composer require phpgrep/core` dans le paquet CLI, et Composer revient les mains vides. Packagist n'a jamais entendu parler du cœur, et aucun autre registre non plus. Vous pourriez publier une version à moitié finie juste pour vous débloquer, mais c'est prendre le problème à l'envers : vous publieriez du code dans le seul but de le tester sur votre propre machine.

## Pointer Composer vers un dossier local

Un dépôt path dit à Composer, pour un projet donné : **quand tu rencontres ce nom de paquet, ne cherche pas sur Packagist, cherche dans ce dossier sur le disque.**

```json
{
    "repositories": [
        {
            "type": "path",
            "url": "../phpgrep-core"
        }
    ],
    "require": {
        "phpgrep/core": "*"
    }
}
```

Avec une arborescence comme celle-ci :

```console
projects/
├── phpgrep-core/
│   └── composer.json     ("name": "phpgrep/core")
└── phpgrep-cli/
    └── composer.json     (the file above)
```

lancer `composer install` dans `phpgrep-cli` résout `phpgrep/core` vers `../phpgrep-core`. Par défaut, Composer ne copie pas le dossier. Il crée un *lien symbolique* dans `vendor/phpgrep/core`, qui renvoie au vrai dossier.

<img src="images/ch16-path-symlink.png" alt="Deux dossiers de projet côte à côte : dans phpgrep-cli, l'entrée vendor/phpgrep/core est une ficelle attachée au vrai dossier phpgrep-core d'à côté, si bien que les deux pointent vers les mêmes fichiers" width="560">

Modifiez un fichier dans `phpgrep-core`, et `phpgrep-cli` voit le changement à l'instant. Pas de réinstallation, pas de publication, rien à lancer entre les deux. Au quotidien, on dirait un seul paquet. Il en reste pourtant deux, chacun avec son `composer.json`, ses propres contraintes de version, et sa propre route vers Packagist le moment venu.

Essayez : dans `phpgrep-cli`, lancez `ls -l vendor/phpgrep` et lisez la flèche que `ls` dessine à côté de `core`. Cette flèche, c'est le lien symbolique.

## Où cela mène : les monorepos

Mettez plusieurs paquets liés dans un seul dépôt Git, chacun avec son `composer.json`, reliés par des dépôts path qui pointent vers les sous-dossiers les uns des autres, et vous obtenez la forme que prennent la plupart des monorepos PHP. **Il n'existe pas de mode monorepo dans Composer.** Un monorepo est une arborescence ordinaire de paquets qui partagent un dépôt et se désignent mutuellement pendant le développement.

Certaines équipes s'en tiennent là pour de bon et livrent le monorepo tel quel. D'autres y voient une commodité de développement et, quand un paquet se stabilise, le déplacent dans son propre dépôt pour le publier seul sur Packagist. Les deux se défendent. Le choix dépend de la façon dont votre équipe publie, pas de ce que Composer impose.
