# Coût de possession

Un langage vous coûte trois choses : les gens qui l'écrivent, les machines qui l'exécutent et le calendrier que vous consacrez à le tenir à jour. PHP a un chiffre pour chacune, et chaque chiffre se lit de deux façons. **Les développeurs PHP sont nombreux et, d'après les médianes des enquêtes elles-mêmes, moins payés que ceux de la plupart des autres langages ; le runtime est celui qui compte le moins de pièces mobiles à héberger, des fichiers servis par un pool de processus ; et la cadence annuelle des versions impose un budget de mise à niveau annuel qu'une large part du parc installé n'a pas payé.** La lecture bon marché et la lecture chère sortent des mêmes sources, et vous aurez besoin des deux.

## Les personnes

Un développeur professionnel sur cinq a écrit du PHP dans l'année. Cela le place douzième parmi les langages de la plus grande enquête auprès des développeurs, à quelques points de Go et de C.

{{#include charts/ch08-developer-usage.svg}}

Une autre enquête confirme l'ordre de grandeur : 17 % des répondants de l'enquête JetBrains de 2025 ont utilisé PHP, et 9 % l'ont cité comme langage principal. Le marché du travail, lui, reste peu documenté publiquement. Un agrégateur d'offres d'emploi britanniques a compté 613 postes permanents citant PHP sur les six mois précédant septembre 2026, contre 404 un an plus tôt, pour un salaire médian annoncé de 48 676 livres, en hausse de 14,5 %. Je n'ai trouvé aucune série publique comparable pour d'autres pays, je n'en rapporte donc aucune.

Le chiffre de salaire qui existe est la médiane d'enquête, et elle est basse.

{{#include charts/ch08-salary.svg}}

Dans la dernière édition de l'enquête Stack Overflow à publier des salaires par langage, les développeurs utilisant PHP ont déclaré une médiane de 49 586 dollars par an, la deuxième plus basse de cinquante langages, contre 63 694 pour JavaScript, 67 723 pour Python et 90 221 pour Ruby. Le chiffre est mondial et auto-déclaré, et les répondants PHP vivent plus souvent qu'à leur tour dans des pays à bas salaires, si bien qu'il en dit moins sur votre ville qu'il n'y paraît. Lisez-le comme un coût, et recruter en PHP revient peu cher dans l'ensemble. Lisez-le comme un signal, et le marché valorise le poste PHP médian sous le poste médian des autres langages. Si vous montez une équipe, il vous faut les deux lectures.

{{#include charts/ch08-admired.svg}}

Le sentiment se chiffre moins bien que le salaire. Parmi les développeurs ayant utilisé un langage dans l'année, 38,9 % de ceux qui ont utilisé PHP veulent continuer, le taux le plus bas des langages grand public et loin derrière Rust à 72,4, TypeScript à 58,0 ou Python à 56,4. La même année, 58 % des développeurs dont le langage principal est PHP disaient ne pas prévoir de migrer vers un autre. Les deux chiffres décrivent des populations différentes, l'utilisateur occasionnel et le spécialiste, et mis côte à côte ils dessinent un langage auquel on est plus souvent affecté qu'attiré. Pour le recrutement, cela veut dire un vivier large et une question de rétention, et c'est à vous de les pondérer.

## Les machines

Une application PHP en production, ce sont des fichiers sur un disque, servis par un pool de processus. Pas de processus applicatif de longue durée à surveiller, redémarrer ou vider, pas de préchauffage, pas de tas mémoire à dimensionner : c'est le modèle shared-nothing décrit dans [Le runtime](ch02-runtime.md), et c'est lui qui donne à PHP le moins de pièces mobiles à héberger. Voilà pourquoi tous les hébergeurs mutualisés du monde le proposent, et pourquoi les plateformes du chapitre [Empreinte](ch01-footprint.md) peuvent être installées par des gens qui ne sont pas ingénieurs. Pour la plupart des applications, une image de conteneur du build officiel `php:8.5-fpm`, un serveur web devant et un répartiteur de charge forment toute l'architecture de production, et ajouter de la capacité, c'est ajouter une copie.

Cette simplicité se paie en efficacité par machine. Dans le benchmark de [Débit et latence](ch03-throughput-and-latency.md), un framework sous PHP-FPM sert quelques dizaines de milliers de requêtes par seconde sur un gros serveur ; un runtime en mode worker multiplie ce chiffre par trois à quatre, et apporte avec lui la discipline opérationnelle d'un processus de longue durée. Les progrès du moteur lui-même s'inscrivent dans le même registre. Badoo a rapporté en 2017 que le passage de ses centaines de serveurs applicatifs de PHP 5 à PHP 7 lui avait économisé environ un million de dollars de matériel, chiffre auto-déclaré sur le blog d'ingénierie de l'entreprise. Je ne dispose d'aucune mesure indépendante du coût d'hébergement par requête d'un langage à l'autre, et je n'affirme rien à ce sujet.

<img src="images/ch08-ledger.png" alt="Un livre de comptes ouvert sur un bureau, à trois colonnes surmontées de petites icônes : un groupe de personnes, une baie de serveurs, un calendrier. Un éléphant à lunettes de lecture écrit dans la deuxième colonne. À côté du registre, une petite pile de pièces et un calendrier mural avec un mois entouré" width="560">

## Le calendrier

L'historique des mises à niveau de Wikimedia est public : la production est passée de PHP 7.4 à 8.1 en mars 2025, à 8.3 en novembre 2025, et prévoyait 8.5 pour fin 2026. **Une version mineure sort chaque année fin novembre ou début décembre et reste supportée quatre ans, si bien que vous devez prévoir une mise à niveau par an pour rester en support actif, ou une tous les deux à trois ans pour rester en support de sécurité.** Le travail d'une mise à niveau est borné : le langage déprécie dans une version mineure et supprime à la majeure suivante, les analyseurs signalent les dépréciations, et Rector applique les réécritures mécaniques. Sur une base de code bien testée, une montée de version se compte en jours ; sur une base non testée, en semaines.

Le parc installé montre ce qui arrive quand ce budget n'est pas payé.

{{#include charts/ch08-php-versions-in-use.svg}}

Parmi les paquets installés via Composer, 94 % des installations d'août 2026 tournaient sur PHP 8 et 0,2 % sur PHP 5. Les sites WordPress qui se déclarent à wordpress.org en étaient à 77 % de PHP 8, 21 % de PHP 7 et 2 % de PHP 5. Le web tel que W3Techs le détecte tournait à 64 % sur PHP 8, 28 % sur PHP 7 et 8 % sur PHP 5, et ces deux dernières sont des versions qui n'ont reçu aucun correctif de sécurité depuis novembre 2022 et décembre 2018 respectivement. Ce sont trois populations : les développeurs qui construisent, les sites qui se mettent à jour eux-mêmes, et le web tel qu'il est. L'écart entre la première et la troisième, c'est la dette technique de l'écosystème, et si vous héritez d'une base de code PHP, demandez à quelle population elle appartient avant d'annoncer un prix.

> La limite : le recrutement PHP est bon marché selon les médianes et son hébergement a le moins de pièces mobiles, et chacun de ces faits traîne son ombre, une question de rétention et un parc installé dont plus d'un tiers tourne sur des versions non supportées. Budgétez la mise à niveau annuelle et recrutez le spécialiste plutôt que l'utilisateur occasionnel, et vous obtenez le bon côté de chaque fait ; sautez l'un ou l'autre, et vous obtenez l'autre côté.

## Ce que vous pouvez vérifier vous-même

Cherchez le langage sur les sites d'offres d'emploi de votre ville, puis les frameworks que vous utiliseriez, et comparez le nombre d'annonces et la fourchette affichée avec les langages que vous envisagez : cela vaut mieux que n'importe quelle médiane mondiale. Demandez à votre hébergeur ou à votre équipe plateforme quelle version de PHP ils font tourner aujourd'hui, et comment ils la mettraient à niveau. Prenez ensuite un projet PHP open source de la taille de votre base de code, en retard de deux versions, et passez-y le jeu de règles de mise à niveau de Rector : le diff qu'il produit, c'est le coût d'une version, sous vos yeux.

Les cas où cette arithmétique cesse de s'appliquer, parce que PHP est le mauvais outil et non un outil cher, sont rassemblés dans [Là où PHP est le mauvais choix](ch09-wrong-choice.md).
