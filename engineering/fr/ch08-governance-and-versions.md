# Gouvernance et versions

**Les évolutions du langage passent par un processus public de proposition et de vote qui exige une majorité des deux tiers pour toute modification du langage lui-même, les versions sortent selon un calendrier annuel fixe avec quatre ans de support, et la maintenance du cœur est financée par une fondation indépendante de la feuille de route produit de toute entreprise.** Cette combinaison, un processus prévisible, un rythme prévisible et un financement qui ne dépend pas de l'intérêt durable d'un seul fournisseur, est au fond ce que vous voulez savoir quand vous demandez « qui décide, pour ce langage ».

## Le rythme de publication, et ce à quoi il engage

PHP publie une nouvelle version par an, fin novembre. Chaque branche reçoit ensuite deux ans de support actif, c'est-à-dire des corrections de bugs comme de sécurité, puis deux ans de correctifs de sécurité seulement : quatre ans de support au total avant que la branche n'arrive en fin de vie.

| Version | Sortie | Fin du support actif | Fin du support de sécurité |
|---|---|---|---|
| PHP 8.2 | 8 déc. 2022 | 31 déc. 2024 | 31 déc. 2026 |
| PHP 8.3 | 23 nov. 2023 | 31 déc. 2025 | 31 déc. 2027 |
| PHP 8.4 | 21 nov. 2024 | 31 déc. 2026 | 31 déc. 2028 |
| PHP 8.5 | 20 nov. 2025 | 31 déc. 2027 | 31 déc. 2029 |

Ce tableau est la pièce la plus utile de ce chapitre, parce qu'il transforme la question « PHP est-il bien maintenu ? » en une date vérifiable, propre à la version que vous faites réellement tourner. Une branche dont la fin du support de sécurité est passée ne reçoit plus de correctif pour les vulnérabilités nouvellement découvertes, de la part de personne, et c'est un fait sur votre déploiement, pas une opinion sur le langage.

<div class="chart">

{{#include charts/ch08-versions.svg}}

</div>

## Ce que le processus RFC exige vraiment

Les modifications du langage sont proposées et votées publiquement, sur un wiki consacré à ce processus, et la règle de PHP exige une majorité des deux tiers pour qu'une modification du langage lui-même soit adoptée, une barre plus haute qu'une majorité simple. Ce seuil existe justement pour freiner les changements qui casseraient du code existant ou fragmenteraient la cohérence du langage, au prix d'une progression plus lente que sous un modèle de dictateur bienveillant. Aucun des deux côtés de cet arbitrage n'est gratuit, et je le présente dans les deux sens plutôt que de faire de cette barre haute un bien sans mélange : la majorité des deux tiers protège la stabilité, et elle signifie aussi qu'une proposition soutenue par une nette majorité, mais pas écrasante, peut quand même échouer.

<img src="images/ch08-governance.png" alt="Une salle des fêtes où un éléphant à un pupitre se tient près d'une urne et où la plupart des éléphants de l'assistance lèvent la main ; au mur, un calendrier annuel avec un mois entouré, au-dessus de quatre étagères de boîtes dont la plus basse est poussiéreuse." width="560">

## Qui finance le travail

La PHP Foundation a été créée en novembre 2021, face à une inquiétude précise : la maintenance du cœur du langage dépendait du temps rémunéré qu'une poignée de contributeurs obtenaient de leurs employeurs, plutôt que d'une base de financement assez large pour survivre à la décision d'un employeur de réduire ce temps. La Fondation publie son financement sur un registre public, qui montre des contributions régulières d'un éventail d'entreprises technologiques et d'organisations open source ayant intérêt à ce que PHP reste maintenu. Le mécanisme compte davantage que le nom de tel ou tel contributeur. Un financement réparti entre plusieurs organisations indépendantes, visible sur un registre public plutôt qu'annoncé dans un communiqué de presse, est un arrangement différent, et plus durable, qu'une maintenance suspendue à la bonne volonté d'une seule entreprise.

Ce financement paie un travail précis et sans éclat : relire et intégrer les RFC, trier et traiter les signalements de sécurité visant le moteur du langage, et assurer l'ingénierie de publication qui fait que le rythme annuel du tableau ci-dessus tombe bien fin novembre au lieu de glisser. PHP dispose d'un processus spécifique pour les signalements de sécurité visant le cœur du langage, distinct du processus RFC utilisé pour les nouvelles fonctionnalités, précisément parce qu'une vulnérabilité demande un circuit plus rapide et mieux contrôlé qu'un débat public sur une fonctionnalité. Je n'ai pas de décompte daté et de première main du nombre de vulnérabilités du cœur traitées par ce processus sur une période récente, et je préfère laisser ce chiffre de côté plutôt que d'en emprunter un à un agrégateur tiers qui ne serait pas le compte rendu du processus lui-même.

Comparez avec l'autre modèle que vous avez sans doute en tête : un langage ou un framework dont la direction est fixée entièrement par une entreprise, où une modification sort parce que cette entreprise l'a décidé, pas parce qu'elle a survécu à un vote public. Ce modèle peut aller plus vite à court terme. Il rend aussi l'avenir du langage exactement aussi stable que l'intérêt de cette entreprise, un risque que le financement multi-sponsors de PHP et son processus RFC public sont tous deux conçus pour éviter, même au prix de la barre des deux tiers et de la lenteur qu'elle impose.

## Là où le calendrier bien rangé rencontre une réalité plus désordonnée

Le tableau des versions décrit ce que PHP publie. Il ne dit rien de ce qui tourne vraiment. L'exploration par W3Techs des sites web en service qui utilisent PHP, au 17 septembre 2026, en trouvait 64,1 % sur la branche 8.x, 28,1 % encore sur la 7.x, dont la dernière branche est arrivée en fin de vie en novembre 2022, et 7,8 % encore sur PHP 5.x, hors support depuis 2018 ou 2019. Un reliquat de 0,1 % tournait encore, de façon détectable, sur PHP 4.

C'est une réserve sur la réalité du marché, pas une affirmation sur le langage actuel, et la distinction mérite d'être tenue fermement : le support de PHP 8.x, tel que le décrit le tableau, est exactement aussi prévisible que ce chapitre le dit. Ce qu'une part non négligeable du parc installé fait de cette prévisibilité est une autre question, qui relève de la discipline d'exploitation de certaines organisations, pas de la gouvernance. Ce chiffre va de pair avec la répartition déclarée des versions dans [Qui fait vivre PHP](ch06-who-maintains-it.md), mais ne doit jamais s'y mélanger. L'un décrit des serveurs qui tournent réellement sur Internet, l'autre ce que les développeurs disent utiliser eux-mêmes, et un graphique qui mêlerait les deux comparerait des choses qui ne se comparent pas.

> **La limite.** Un processus de gouvernance aussi prévisible ne vous protège que si votre propre organisation suit le rythme. Le tableau de support est une promesse sur ce que les mainteneurs soutenus par la PHP Foundation feront selon un calendrier fixe ; ce n'est pas une promesse que votre déploiement sera mis à jour avant la fin du support de sécurité de sa branche. Environ un tiers du web qui tourne sous PHP ne suit pas ce rythme aujourd'hui, et [Là où PHP est le mauvais choix](ch09-wrong-choice.md) traite de front le risque d'hériter de l'un de ces déploiements.

**À vérifier vous-même.** Confrontez [php.net/supported-versions.php](https://php.net/supported-versions.php) à la version que vous faites tourner ou que vous évaluez, car les dates du tableau seront tôt ou tard remplacées par un nouveau cycle. Consultez ensuite [w3techs.com/technologies/details/pl-php](https://w3techs.com/technologies/details/pl-php) pour la répartition actuelle des versions, et comparez-la à celle imprimée ici pour voir de combien le parc installé a rattrapé son retard, s'il l'a rattrapé.

La gouvernance et le support des versions décrivent la maintenance de PHP quand tout se passe comme prévu. [Là où PHP est le mauvais choix](ch09-wrong-choice.md) regarde le cas où c'est le langage lui-même, et non la négligence d'un déploiement, qui est le mauvais outil, et le dit aussi franchement que tout le reste.
