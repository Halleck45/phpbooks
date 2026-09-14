# Publier un paquet sur Packagist

Chaque `composer require` que vous avez tapé s'est appuyé sur un service que vous n'avez jamais eu à nommer : [Packagist](https://packagist.org/), le registre public que Composer consulte par défaut. C'est pour cela que `composer require nunomaduro/termwind`, au [chapitre 7](ch07-01-hello-composer.md), n'a demandé ni URL ni serveur. Packagist savait déjà où vivait ce paquet. **Y déposer votre propre paquet est plus simple qu'il n'y paraît, et le mécanisme mérite d'être compris, parce qu'il explique ce que « publier un paquet PHP » veut vraiment dire.**

## Ce qu'il faut à un `composer.json` publiable

Quatre choses, au minimum :

```json
{
    "name": "yourname/phpgrep",
    "description": "A small line-searching CLI tool, built as a learning project.",
    "license": "MIT",
    "require": {
        "php": ">=8.1"
    },
    "autoload": {
        "psr-4": {
            "PhpGrep\\": "src/"
        }
    }
}
```

`"name"` a une forme fixe, `vendor/package`, tout en minuscules, les mots séparés par des tirets. La partie vendor est en général votre nom d'utilisateur ou votre organisation GitHub, pas une raison sociale ; beaucoup de paquets publiés appartiennent à une seule personne. `"description"` et `"license"` sont ce que les visiteurs lisent sur votre page Packagist. **La licence compte pour une raison très concrète : sans elle, personne ne sait à quelles conditions il a légalement le droit d'utiliser votre code**, et ce genre de doute fait fuir les utilisateurs sans bruit. `"MIT"` est le choix permissif courant quand vous n'avez pas de raison d'en préférer un autre.

## Vous ne téléversez rien

C'est la partie qui surprend ceux qui viennent d'écosystèmes dotés d'une commande `publish`. **Packagist n'héberge pas votre code. Il héberge des informations sur votre code, et lit la source directement dans votre dépôt Git**, GitHub compris.

<img src="images/ch16-packagist-directory.png" alt="Packagist dessiné comme un annuaire : une page liste un nom de paquet et pointe vers un dépôt Git ailleurs, et le terminal d'un développeur qui lance composer require suit ce pointeur jusqu'au dépôt" width="560">

Publier tient en trois gestes. Poussez un `composer.json` comme celui ci-dessus dans un dépôt Git public. Connectez-vous sur [packagist.org](https://packagist.org/), cliquez sur « Submit » et collez l'URL de votre dépôt. Packagist lit alors votre `composer.json`, indexe le paquet sous le `"name"` que vous lui avez donné et, c'est le point important, installe un webhook pour être prévenu de chacun de vos push à partir de là.

Pas d'étape de publication, pas d'archive à remettre. Packagist surveille votre dépôt.

> Packagist est un annuaire, pas un entrepôt. Il sait où vit votre code et y envoie Composer.

## Les versions viennent des tags Git

Si Packagist lit votre dépôt, d'où sort une version comme `1.2.0` ? D'un tag Git ordinaire, nommé selon le [versionnage sémantique](https://semver.org/) : `MAJOR.MINOR.PATCH`.

```console
$ git tag v1.0.0
$ git push origin v1.0.0
```

Poussez le tag, le webhook se déclenche, et `1.0.0` apparaît comme version installable quelques instants plus tard. **Le tag, c'est la release.** Il n'y a rien d'autre à faire.

<img src="images/ch16-semver-tags.png" alt="Un historique Git dessiné comme une ligne de commits avec trois drapeaux plantés dessus, v1.0.0, v1.0.1 et v1.1.0, et la liste des versions de Packagist qui reflète les drapeaux" width="560">

Les trois nombres portent une promesse. Incrémentez le patch pour un correctif qui ne casse rien, le mineur pour une fonctionnalité qui ne casse rien, et le majeur dès que vous cassez quelque chose sur lequel un utilisateur pourrait compter. Cette dernière règle est celle qui compte pour quiconque dépend de vous : c'est elle qui lui permet d'écrire `^1.0` dans son propre `composer.json` et de faire confiance à tout ce qui y correspond pour ne pas casser son code.
