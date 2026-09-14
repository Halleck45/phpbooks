# Composer et Packagist, plus en profondeur

Depuis le [chapitre 7](ch07-01-hello-composer.md), Composer fait un seul travail pour vous : lire `composer.json`, télécharger les paquets qui y sont listés, et retrouver vos classes par leur nom grâce à une ligne PSR-4. Cela couvre l'essentiel d'une journée de travail. **Ce n'est pourtant pas tout ce que Composer sait faire, et le reste devient utile le jour où votre projet cesse d'être « un paquet, un dépôt ».**

Les deux premiers ajouts tiennent dans le `composer.json` que vous avez déjà. Une section `"scripts"` transforme les commandes que vous tapez à longueur de journée en sous-commandes Composer courtes, et une seconde forme d'autoload, `"files"`, se charge des fichiers de fonctions que PSR-4 n'a aucun moyen de trouver.

Puis le champ s'élargit. Packagist est le registre public derrière chaque `composer require`, et il vaut la peine de savoir comment un paquet y arrive. Petit spoiler : personne ne téléverse quoi que ce soit. Viennent ensuite les dépôts de type path, le mécanisme qui permet de développer deux paquets locaux côte à côte avant d'en publier un seul, et la forme sur laquelle reposent la plupart des monorepos PHP.

Deux dernières étapes se situent un peu en dehors de tout projet : installer des outils en ligne de commande une seule fois, globalement, plutôt qu'une copie par projet, et un regard court et honnête sur les hooks que Composer déclenche autour de son propre cycle de vie, avec la porte qu'il laisse ouverte aux plugins.
