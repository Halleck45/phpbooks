# Annexe B : Calendrier des versions

PHP publie une version porteuse de nouvelles fonctionnalités par an, fin novembre. Chaque branche reçoit ensuite deux ans de support actif, corrections de bugs et de sécurité comprises, puis deux ans de correctifs de sécurité seulement : quatre ans de support au total, de la sortie à la fin de vie. Le tableau ci-dessous est celui de [Gouvernance et versions](ch08-governance-and-versions.md), reproduit seul pour s'y reporter vite.

| Version | Sortie | Fin du support actif | Fin du support de sécurité |
|---|---|---|---|
| PHP 8.2 | 8 décembre 2022 | 31 décembre 2024 | 31 décembre 2026 |
| PHP 8.3 | 23 novembre 2023 | 31 décembre 2025 | 31 décembre 2027 |
| PHP 8.4 | 21 novembre 2024 | 31 décembre 2026 | 31 décembre 2028 |
| PHP 8.5 | 20 novembre 2025 | 31 décembre 2027 | 31 décembre 2029 |

Source : [php.net/supported-versions.php](https://php.net/supported-versions.php), vérifié le 17 septembre 2026. La page change à chaque nouvelle version et à chaque branche retirée ; prenez ce tableau pour ce qu'il est, une photographie prise ce jour-là, et consultez la page en ligne avant toute décision qui dépend d'une date précise.

## Ce que veulent dire « actif » et « sécurité seulement »

Pendant le support actif, une branche reçoit à la fois les corrections de bugs et les correctifs de sécurité, et c'est la version que le projet PHP recommande lui-même. À la fin du support actif, elle passe aux correctifs de sécurité seulement : une vulnérabilité découverte sera encore corrigée, un bug ordinaire ne le sera plus. À la fin du support de sécurité, la branche ne reçoit plus rien du projet, quoi qu'on y trouve ensuite. Un déploiement en production qui tourne encore sur une branche arrivée en fin de vie n'a pas seulement des fonctionnalités en retard ; il n'a plus aucun chemin vers un correctif pour la prochaine faille qu'on y découvrira.

## Ce tableau face à ce qui tourne réellement

[Gouvernance et versions](ch08-governance-and-versions.md) et [Là où PHP est le mauvais choix](ch09-wrong-choice.md) s'appuient tous deux sur un autre chiffre pour donner le contexte. Le 17 septembre 2026, W3Techs comptait 64,1 % des sites sous PHP sur la ligne 8.x que couvre ce tableau, 28,1 % encore sur la ligne 7.x, dont la dernière branche a quitté le support de sécurité en novembre 2022, et 7,8 % encore sur PHP 5.x, sans support depuis 2018 ou 2019. Le tableau décrit ce que le projet PHP s'engage à publier et à maintenir. Il ne dit rien de ce que votre organisation, ou celle d'un fournisseur, fait réellement tourner : seul un contrôle direct du déploiement concerné peut l'établir.

## En septembre 2026

PHP 8.6 n'était pas sorti au moment où j'écris. Je ne lui prête pas de date de sortie, par la même discipline que pour tous les autres chiffres : un calendrier annoncé est décrit comme annoncé, et ne devient un fait qu'une fois la version publiée. Le seul détail confirmé qui s'y rattache est traité dans [Coût](ch07-cost.md) : la licence PHP version 4 s'applique à partir de PHP 8.6 et remplace la licence 3.01, qui régit les versions que ce tableau donne aujourd'hui comme supportées.
