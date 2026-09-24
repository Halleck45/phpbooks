# Installer des outils globaux avec Composer

Tout ce que vous installez avec Composer n'appartient pas à un projet. Un analyseur statique comme PHPStan ou un formateur comme PHP-CS-Fixer est un outil que vous emportez avec vous, pour le lancer sur le projet dans lequel vous vous trouvez. **Composer a une commande à part pour ce genre d'outils.**

## `require --dev` ou `global require`

Vous connaissez déjà `require-dev` : une dépendance nécessaire seulement pendant le développement, comme PHPUnit, listée dans le `composer.json` du projet et installée dans son dossier `vendor/` :

```console
$ composer require --dev phpunit/phpunit
```

C'est le bon choix pour tout ce dont les tests ou la construction du projet dépendent. Quiconque clone le dépôt et lance `composer install` obtient la même version, et cette reproductibilité compte. C'est le mauvais choix pour un outil que vous aimez lancer partout, quoi qu'un projet déclare. Dix projets, dix copies de PHPStan dans dix dossiers `vendor/`, en dix versions potentiellement différentes : beaucoup de doublons pour quelque chose qui n'appartient à aucun d'eux.

<img src="images/ch16-global-vs-project.png" alt="Avant et après : une rangée de dossiers de projet portant chacun sa propre copie du même outil, puis les mêmes dossiers partageant un seul outil rangé sur une étagère en dehors de tous" width="600">

`composer global require` l'installe une seule fois :

```console
$ composer global require phpstan/phpstan
```

PHPStan atterrit dans un répertoire Composer global, à l'écart de tout projet : `~/.config/composer` sous Linux, `~/.composer` sous macOS par défaut, et le chemin exact mérite d'être vérifié avec `composer global config home`. À partir de là, il n'y a plus qu'une seule installation partagée, quel que soit le répertoire où vous vous trouvez.

## Le mettre dans votre `PATH`

Installer globalement ne fait pas, à lui seul, de `phpstan` une commande que votre shell connaît. Le binaire se trouve dans un dossier `vendor/bin` à l'intérieur de ce répertoire global, et **votre shell ne regarde que dans les dossiers listés dans `PATH`** :

```console
$ export PATH="$HOME/.composer/vendor/bin:$PATH"
```

Placez cette ligne dans le fichier de démarrage de votre shell (`~/.zshrc`, `~/.bashrc` ou l'équivalent) pour que chaque nouveau terminal en profite, puis vérifiez :

```console
$ phpstan --version
PHPStan - PHP Static Analysis Tool 1.11.5
```

Si la commande est introuvable, la ligne `PATH` est presque toujours la coupable. Elle manque, elle pointe vers le mauvais répertoire pour votre plateforme, ou vous avez modifié le fichier de démarrage sans jamais le recharger (`source ~/.zshrc`, ou ouvrez un nouveau terminal).

## Choisir entre les deux

**Un outil qui doit tourner à l'identique pour tout le monde, intégration continue comprise, à une version figée dans le gestionnaire de versions, va dans `require-dev`. Un outil personnel que vous lancez sur tous vos projets, et dont la version peut différer d'un cran de celle d'un collègue sans que personne s'en émeuve, va dans `composer global require`.** Beaucoup de configurations utilisent les deux : PHPStan figé par projet pour que l'intégration continue soit reproductible, et PHP-CS-Fixer installé globalement pour un formatage rapide en cours d'édition.
