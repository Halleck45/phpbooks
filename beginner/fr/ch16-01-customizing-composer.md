# Personnaliser l'autoload et les scripts

Jusqu'ici, votre `composer.json` faisait deux choses : lister les dépendances, et associer un espace de noms à un dossier. Deux entrées de plus, quelques lignes chacune, méritent d'entrer tout de suite dans vos habitudes.

## Les scripts : des raccourcis pour les commandes de tous les jours

Pensez aux commandes que vous tapez dix fois par jour dans un projet : la suite de tests, le linter, un vidage de cache. Chacune a son nom, ses options, et un collègue qui la tape légèrement autrement. **Composer vous laisse donner à chacune un nom court, dans la section `"scripts"` de `composer.json` :**

```json
{
    "name": "you/phpgrep",
    "require": {},
    "require-dev": {
        "phpunit/phpunit": "^11.0"
    },
    "scripts": {
        "test": "phpunit",
        "check": "phpstan analyse src"
    }
}
```

Lancez l'une ou l'autre avec `composer run`, ou, quand le nom n'entre pas en collision avec une commande intégrée de Composer, avec `composer` suivi directement du nom :

```console
$ composer test
$ composer check
```

Économiser quelques frappes, c'est le petit gain. Le grand se voit en équipe. Tout le monde lance `composer test`, que l'outil dessous soit PHPUnit, Pest ou autre chose, et quelles que soient les options dont il a besoin. Changez d'outil ou modifiez une option, et chaque développeur, chaque pipeline d'intégration continue récupère le changement à sa prochaine exécution, sans rien toucher de son côté. **Le nom du script est le contrat ; la commande derrière est un détail.**

<img src="images/ch16-script-signpost.png" alt="Un panneau indicateur marqué composer test, et derrière lui un rideau qui cache la vraie commande avec son outil et ses options : l'équipe ne voit que le panneau, la commande derrière peut changer" width="520">

Quand une tâche a vraiment besoin de plusieurs étapes, une entrée peut être une liste de commandes, exécutées dans l'ordre :

```json
{
    "scripts": {
        "check": [
            "phpstan analyse src",
            "phpunit"
        ]
    }
}
```

Essayez : `composer run --list` affiche tous les scripts qu'un projet définit. C'est le moyen le plus rapide de prendre ses repères dans un dépôt que l'on vient de cloner.

## L'autoload `"files"` : pour le code qui n'est pas une classe

PSR-4, vu au [chapitre 7](ch07-06-psr4.md), fonctionne comme une bibliothèque bien rangée : demandez une classe par son nom, et Composer sait quelle étagère et quel fichier. Un fichier rempli de simples fonctions n'a pas de nom de classe à demander, alors PSR-4 passe devant sans s'arrêter. **Pour ce cas, `composer.json` a un second mécanisme, `"files"` : une liste de fichiers chargés chaque fois que l'autoloader démarre, sans poser de question :**

```json
{
    "autoload": {
        "psr-4": {
            "PhpGrep\\": "src/"
        },
        "files": [
            "src/helpers.php"
        ]
    }
}
```

Tout ce qui est défini au premier niveau de `src/helpers.php`, fonctions et constantes, devient disponible partout dans le projet dès que `vendor/autoload.php` est inclus. Pas de `use`, exactement comme une fonction native telle que `strtolower()` n'en demande pas.

<img src="images/ch16-psr4-vs-files.png" alt="Deux façons de charger du code : à gauche, un bibliothécaire va chercher un fichier de classe sur une étagère seulement quand on le lui demande, à droite, une pile de fichiers d'aide reste ouverte sur le bureau en permanence" width="560">

Cette commodité a un prix. Une classe PSR-4 n'est chargée que lorsque quelque chose y fait référence. Une entrée `"files"` est chargée à chaque requête, que la requête s'en serve ou non. Réservez la liste à une poignée de petites fonctions vraiment globales, et laissez PSR-4 gérer tout ce qui a raisonnablement sa place dans une classe.

> PSR-4 charge une classe quand on la demande. `"files"` charge un fichier à chaque fois.

Après avoir modifié l'une ou l'autre section à la main, il reste une étape : `composer dump-autoload`, pour que Composer régénère l'autoloader en accord avec ce que vous venez d'écrire. `composer install` et `composer require` le font pour vous ; une modification manuelle, non, tant que vous ne le demandez pas.
