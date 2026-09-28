# Framework, CMS ou headless : que construisez-vous, au juste ?

La plupart des cahiers des charges décrivent l'une de trois formes, que la personne qui les a rédigés le sache ou non.

## Il nous faut une application

Un système de réservation, un tableau de bord interne, une place de marché : quelque chose avec une logique propre, où le comportement est le produit. C'est le territoire du framework. Laravel ou Symfony vous fournit le routage, une couche d'accès aux données et un endroit où poser votre logique, sans aucun avis sur ce que fait votre application. Cette partie-là, vous l'écrivez.

**Choisissez un framework quand la valeur du produit est le comportement sur mesure lui-même**, et qu'aucun outil sur étagère ne fait déjà ce que décrit le cahier des charges.

## Il nous faut un site que les gens peuvent modifier

Un site vitrine, un blog, un portail de documentation, la plupart des sites de petites entreprises : la valeur, c'est le contenu, et des personnes non techniques vont l'ajouter, le corriger et le réorganiser après la mise en ligne. C'est le territoire du CMS. WordPress ou TYPO3 vous donne dès le premier jour une interface d'édition, une structure de contenu et un écosystème d'extensions, et vous n'écrivez jamais un panneau d'administration à partir de zéro.

Choisissez un CMS quand la vraie demande du client est « et ensuite, l'équipe marketing doit pouvoir mettre ça à jour toute seule ». C'est le cas de la plupart des briefs de contenu, qu'ils le disent ou non.

## Il nous faut une API pour autre chose

Une application mobile, un front séparé, le service d'une autre équipe : quelque chose qui alimente un consommateur, sans aucune page rendue côté serveur. C'est le territoire du headless. Un outil comme API Platform existe pour transformer un modèle de données en API documentée et versionnée, sans écrire chaque endpoint à la main.

Choisissez le headless quand vous savez déjà que le consommateur est un front JavaScript, une application mobile ou une autre équipe backend, et que toute page que vous rendriez finirait à la poubelle.

## Quand le brief est les deux à la fois

Beaucoup de projets réels cumulent deux formes : un site vitrine qui a aussi besoin d'un système de réservation, une application qui a aussi besoin d'une section de contenu éditable. Partez de la forme la plus proche de la valeur principale du projet, et greffez l'autre capacité ensuite. Un site WordPress avec une extension maison pour la logique de réservation se livre plus vite qu'une application Laravel qui réimplémente un éditeur de contenu. Une application Laravel avec une table `posts` et un écran d'administration simple se livre plus vite qu'une logique de réservation coincée dans des hooks WordPress.

> **Sous le capot :** rien de tout cela ne concerne PHP lui-même. Frameworks, CMS et outils d'API sont bâtis sur les mêmes briques du langage (un routeur qui fait correspondre une URL à du code, un ORM qui transforme des lignes en objets), emballées autour d'une hypothèse différente sur qui utilisera le résultat et sur la fréquence à laquelle le contenu change sans déploiement.
