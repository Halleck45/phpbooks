# Gouvernance et pérennité

Avant de miser une base de code sur quoi que ce soit, vous voulez savoir qui décide de ce qui y entre, qui est payé pour l'entretenir, et combien de temps une version reste maintenue. **PHP évolue par un processus de RFC public avec un vote aux deux tiers, livre une version mineure chaque année et maintient chacune pendant quatre ans, et dispose depuis 2021 d'une fondation qui contractualise treize ingénieurs et a signé 42 % des commits de l'interpréteur en 2025.** L'argent derrière cette fondation est inférieur à un million de dollars par an, et ce chiffre fait autant partie de la réponse que le reste.

## Comment un changement entre

Chaque changement du langage passe par une Request for Comments sur wiki.php.net. La proposition est écrite, discutée pendant au moins deux semaines sur la liste de diffusion internals, puis soumise à un vote ouvert pendant au moins deux semaines, et elle ne passe qu'avec les deux tiers des voix exprimées ; les votants sont les contributeurs qui disposent d'un compte php.net et un petit nombre de représentants de la communauté, et la règle des deux tiers est stricte depuis février 2019. Chaque étape est publique, jusqu'aux votes exprimés nominativement.

Les types intersection nullables ont été rejetés 12 à 26 en 2021. Les closures multi-instructions à capture automatique ont obtenu une majorité de 27 à 16 en 2022 et ont été refusées quand même, faute d'atteindre la barre des deux tiers. La visibilité asymétrique a été refusée 14 à 12 en janvier 2023, révisée, acceptée 24 à 7 en août 2024 et livrée dans PHP 8.4, et les classes imbriquées ont été refusées 2 à 20 en mai 2025. Cette liste de refus est la preuve que le processus est réel.

Le rythme se lit dans un index secondaire : 31 RFC pour PHP 8.4, 19 pour PHP 8.5, et déjà 29 listées pour PHP 8.6 en septembre 2026. Si vous venez d'un langage piloté par un seul éditeur ou par un dictateur bienveillant, pesez ce que cela signifie : rien n'entre dans PHP parce que quelqu'un d'important le veut, et des fonctionnalités qu'une majorité voulait ont été refusées. Le processus est lent, et il est public.

<img src="images/ch07-vote.png" alt="Une table ronde vue de dessus, avec une douzaine d'éléphants assis autour. Un document repose au centre. La plupart des éléphants lèvent une main ; quelques-uns gardent les deux sur la table. Au mur, une jauge horizontale avec un repère aux deux tiers de sa longueur, et le niveau de la jauge juste au-delà du repère" width="560">

## Le calendrier des versions

**Depuis décembre 2015, PHP livre une version mineure chaque année, onze d'affilée, chacune entre le 20 novembre et le 8 décembre**. Chaque branche reçoit ensuite deux ans de support actif, avec des corrections de bugs et de sécurité dans des versions correctives mensuelles, puis deux ans de corrections de sécurité seulement. Depuis une RFC votée en avril 2024, les deux fenêtres se terminent le 31 décembre de leur dernière année, ce qui vous permet de planifier vos mises à niveau par année civile.

{{#include charts/ch07-support-timeline.svg}}

En septembre 2026, quatre branches sont maintenues : PHP 8.2 en support de sécurité jusqu'au 31 décembre 2026, 8.3 jusqu'à la fin 2027, 8.4 en support actif jusqu'à la fin 2026, et 8.5 en support actif jusqu'à la fin 2027. PHP 8.6 est prévu en disponibilité générale le 19 novembre 2026, avec son gel des fonctionnalités en août, des release candidates à partir du 24 septembre et trois release managers nommés. Aucune date n'existe pour un PHP 9.0, et je n'en donne aucune. [Les versions de PHP, 2015 à 2026](appendix-02-versions.md) liste chaque version avec ses dates.

Derrière le calendrier, le dépôt montre l'activité. Dans les douze mois jusqu'au 17 septembre 2026, la branche principale de php-src a reçu 5 316 commits de 171 auteurs distincts, et le dépôt compte 1 644 contributeurs sur un historique GitHub qui commence en 2011.

## Qui est payé

Jusqu'en 2021, l'interpréteur était entretenu par des bénévoles et par une poignée d'ingénieurs employés par des entreprises ayant un intérêt dans PHP. En novembre 2021, quand l'un des développeurs du cœur les plus actifs a annoncé qu'il s'éloignait de ce travail, dix entreprises ont créé The PHP Foundation pour financer directement le développement du cœur : Acquia, Automattic, Craft CMS, JetBrains, Laravel, PrestaShop, Private Packagist, Symfony, Tideways et Zend by Perforce. La fondation est hébergée fiscalement par Open Source Collective, liste chaque transaction sur sa page Open Collective et publie un rapport de transparence chaque année.

{{#include charts/ch07-foundation-funding.svg}}

Les contributions ont été de 712 000 dollars en 2022, 419 000 en 2023, 684 000 en 2024 et 731 000 en 2025. Les dépenses en ingénieurs sont passées de 275 000 dollars en 2023 à 635 000 en 2024 et 784 000 en 2025, une année que la fondation a close sur un déficit qu'elle décrit comme délibéré. Voilà l'échelle, et ce sont les rapports eux-mêmes qui la donnent.

Ce que cet argent achète, en septembre 2026, c'est treize ingénieurs à temps plein ou partiel sous contrat, un directeur exécutif et un conseil de dix membres non rémunérés ; ces ingénieurs ont signé 42 % des commits de php-src et 32 % des pull requests fusionnées en 2025. Deux subventions publiques s'ajoutent à l'argent des sponsors. La Sovereign Tech Agency allemande a financé 205 000 euros de travaux en 2023 et 2024 et 223 680 euros en 2025 et 2026, et une subvention d'Alpha-Omega, un projet de la Linux Foundation, finance une équipe de sécurité de l'écosystème depuis mai 2026.

La dépendance est dans les mêmes rapports. Deux sponsors, Automattic et JetBrains, représentent respectivement 762 500 et 476 670 dollars des 3,37 millions de dollars enregistrés sur la page Open Collective de la fondation depuis novembre 2021, soit environ 37 % à eux deux ; ce total cumulé et les rapports annuels n'ont pas le même périmètre, et je ne les ai pas réconciliés. Le nombre d'organisations et de particuliers sponsors est tombé de 658 en 2024 à 536 en 2025, ce que la fondation elle-même qualifie de « nettement moins ». Un budget inférieur à un million de dollars est petit pour un langage de l'empreinte décrite dans [Empreinte](ch01-footprint.md) : il paie une douzaine d'ingénieurs, pas un groupe de recherche. Chacun de ces chiffres, c'est la fondation qui le publie.

## Sécurité

Une vulnérabilité arrive au projet par le flux d'avis privés de GitHub sur le dépôt php-src ou par e-mail à l'équipe de sécurité. Une politique publiée la classe en sévérité haute, moyenne ou basse, et les deux classes supérieures sont corrigées dans un dépôt privé avant une publication coordonnée. Les tags de version sont signés par les release managers depuis avril 2012, et chaque archive est livrée avec une signature détachée et une somme de contrôle publiée. Je n'ai trouvé ni nomenclature logicielle ni attestation de build pour les archives de version, et je le rapporte comme « non trouvé » plutôt que comme « n'existe pas ».

{{#include charts/ch07-cves.svg}}

L'interpréteur a eu 8 vulnérabilités publiées en 2022, 7 en 2023, 18 en 2024, 13 en 2025 et 14 en 2026 jusqu'au 17 septembre. La hausse de 2024 coïncide avec un audit externe de l'interpréteur, commandé avec des fonds publics, qui a trouvé 27 problèmes dont 17 avaient des implications de sécurité, trois d'entre eux de sévérité haute, et qui a produit plusieurs des CVE de cette année-là. Le graphique se lit mal si l'on n'y prend garde. La politique de PHP n'attribue pas de CVE à la plupart des problèmes de sévérité basse, donc le décompte reflète la politique autant que le code. Un décompte de vulnérabilités ne se compare pas non plus d'un langage à l'autre : ce qui compte comme « le langage », un runtime, une bibliothèque standard, un registre de paquets, diffère dans chacun, et la politique de divulgation aussi.

> La limite : le langage est gouverné par ses contributeurs, financé par une fondation au budget inférieur à un million de dollars par an avec deux sponsors dominants, et sécurisé par une petite équipe et une politique qui attribue moins de CVE que d'autres ne le feraient. Ce sont les faits d'un projet communautaire, et ils sont publiés par le projet lui-même ; si vous les comparez avec un langage adossé à la masse salariale d'un grand éditeur, comparez les risques des deux côtés, y compris la liberté de l'éditeur de changer de cap.

## Ce que vous pouvez vérifier vous-même

Ouvrez wiki.php.net/rfc et lisez une RFC actuellement en vote, puis le fil de la liste internals qui l'accompagne ; une heure passée là vous montre comment les décisions se prennent, mieux que n'importe quelle description. Ouvrez la page Open Collective de la fondation, où chaque contribution et chaque dépense est listée par date. Ouvrez les avis de sécurité de php-src sur GitHub et lisez les trois plus récents, en notant le délai entre le signalement et le correctif.

Ce que tout cela vous coûte, en salaires, en hébergement et en mises à niveau, est la question suivante.
