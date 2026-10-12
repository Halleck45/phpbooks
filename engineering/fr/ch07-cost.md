# Coût

**PHP est gratuit et publié sous une licence permissive, son écosystème de près d'un demi-million de paquets ne coûte rien à utiliser, et le coût réel d'une application PHP se loge presque entièrement dans l'hébergement, l'équipe et la discipline de maintenance, pas dans les licences.** La question utile pour vous n'est donc pas « combien coûte PHP », mais « qu'est-ce que l'architecture de PHP vous évite de payer », et c'est là que ce chapitre passe le plus de temps.

## La licence, précisément

PHP est distribué sous la PHP License, une licence permissive approuvée par l'OSI, qui ne vous oblige à publier aucune ligne de ce que vous construisez avec. PHP 8.4, la version plancher retenue dans ces pages, est publié sous la version 3.01 de cette licence. Une nouvelle licence, la version 4, reprend le texte BSD modifié (BSD-3-Clause) et s'applique à partir de PHP 8.6, qui n'était pas sorti au moment où j'écris ces lignes. Voyez-la comme un changement à suivre, pas comme le régime de la version que vous déploierez le plus probablement aujourd'hui. Aucune des deux licences n'exige de redevance, d'enregistrement ou de déclaration d'usage auprès de qui que ce soit.

## Ce que « gratuit » recouvre vraiment

Packagist, le registre public dans lequel Composer, le gestionnaire de dépendances de PHP, va chercher les paquets, recense près d'un demi-million de paquets publiés, environ 5,8 millions de versions à eux tous, et un total d'installations qui approche les 200 milliards depuis l'ouverture du registre en avril 2012.

| Indicateur | Ordre de grandeur |
|---|---|
| Paquets publiés | ~468 000 |
| Versions publiées | ~5,8 millions |
| Installations cumulées depuis avril 2012 | ~200 milliards |

Ces compteurs bougent en continu. Prenez les chiffres exacts comme un instantané, avec la même prudence que pour tous les autres chiffres mis à jour en permanence dans ce livre : c'est l'ordre de grandeur qui compte. La dépendance dont votre projet PHP a besoin a toutes les chances d'être déjà publiée, versionnée et installable en une commande, sans autre coût que le temps de vérifier ce que vous faites entrer dans votre code.

Publier sur Packagist est gratuit, et aucun contrôle n'a lieu au-delà de ce que Composer vérifie mécaniquement : chaque installation est comparée à une empreinte enregistrée dans le fichier de verrouillage du projet, si bien qu'une dépendance ne peut pas changer en silence entre la version que votre équipe a relue et celle qui s'installe réellement. La garantie est réelle et utile. Elle est aussi plus étroite qu'une traçabilité complète de la chaîne d'approvisionnement, car une empreinte confirme que le code n'a pas changé depuis son verrouillage, pas qu'il était sain le jour où il est entré dans le projet. Cette première relecture reste à la charge de l'équipe qui ajoute la dépendance, dans l'écosystème PHP comme dans celui de n'importe quel autre langage.

## Ce que vous ne payez pas : une orchestration propriétaire

<img src="images/ch07-cost.png" alt="Un éléphant qui porte la même petite valise franchit tour à tour trois portes, un garage en briques, une petite chambre louée et une cour de conteneurs, sans jamais l'ouvrir ; une étiquette de prix vierge pend à la poignée." width="560">

Le modèle de processus de PHP-FPM, décrit dans [Le runtime](ch02-runtime.md), ne demande qu'un système d'exploitation conforme POSIX, un serveur web et le runtime PHP pour servir des requêtes à grande échelle. Il n'exige aucune couche propriétaire d'orchestration serverless, et rien dans l'architecture ne vous pousse à en adopter une. C'est un fait d'architecture, réel et vérifiable, pas une affirmation sur tel ou tel hébergeur, et je le formule ainsi à dessein : la même application peut tourner sur une machine physique qui vous appartient, sur un serveur virtuel minimal ou dans un orchestrateur de conteneurs, sans être repensée pour aucun des trois.

Cette propriété prend un relief particulier pour les organisations soumises à des obligations de localisation des données ou à une exigence de cloud souverain, où le calcul doit rester sur une infrastructure conforme aux règles de résidence d'une juridiction plutôt que sur la plateforme la plus commode. Un runtime qui n'a besoin de l'orchestration managée d'aucun fournisseur pour fonctionner se déplace plus facilement vers une infrastructure conforme, parce que la contrainte porte sur l'endroit où se trouve la machine, pas sur le service propriétaire pour lequel l'application a été écrite.

> **La limite.** Cette portabilité concerne le runtime PHP, pas l'ensemble de votre exploitation. Une équipe qui a aussi adopté une base de données managée propre à un cloud, une file de messages managée propre à un cloud ou un outillage d'observabilité construit autour de l'agent d'un seul fournisseur a déjà réintroduit la même dépendance à ces étages-là, quel que soit le langage placé devant. Formulez l'argument ainsi : « le runtime n'impose pas de dépendance à un cloud », et non « une application PHP est portable », car la seconde affirmation va plus loin que ce que les faits établissent.

## Ce que PHP vous donne pour la sécurité, d'emblée

La réputation de PHP, traitée une fois pour toutes dans [La réputation](ch01-introduction.md), comprend l'idée que le langage serait peu sûr par nature. Le langage actuel fournit des briques précises et vérifiables qui interdisent de tenir cette idée pour encore vraie par défaut. `password_hash` et `password_verify` offrent une API de hachage de mots de passe maintenue et indépendante de l'algorithme, si bien qu'une application n'a pas à bricoler la sienne. Les bindings Libsodium sont livrés avec PHP depuis la version 7.2 et donnent un accès direct à des primitives cryptographiques auditées, sans extension tierce. Les requêtes préparées de PDO séparent la structure d'une requête de ses données au niveau du pilote, ce qui constitue la défense standard et efficace contre l'injection SQL, à condition de s'en servir. Aucun de ces faits ne rend une application sûre à lui seul, et une équipe qui les ignore peut écrire une application vulnérable dans n'importe quel langage. Ils signifient en revanche que les bons outils sont déjà dans la bibliothèque standard, et non un achat supplémentaire ou une dépendance tierce qu'il faudrait d'abord trouver puis évaluer.

## Ce que ce chapitre ne sait pas chiffrer

J'aimerais répondre à deux questions de coût par un chiffre, et je ne le peux pas. Je préfère le dire ici plutôt que de deviner. Une comparaison propre et sourcée du coût d'hébergement de PHP face à d'autres langages n'existe pas sans s'appuyer sur les chiffres marketing d'un hébergeur, que les règles de sourçage de ce livre excluent ; l'argument d'architecture ci-dessus tient lieu de chiffre précisément parce que ce chiffre n'existe pas sans ce compromis. Le manque de données sur les salaires et la demande d'emploi, déjà signalé dans [Qui fait vivre PHP](ch06-who-maintains-it.md), vaut ici aussi : je ne peux pas vous dire, source défendable à l'appui, si un développeur PHP coûte plus ou moins cher à recruter qu'un développeur d'un autre langage sur votre marché, et un chiffre inventé pour combler ce vide vaudrait moins que pas de chiffre du tout.

**À vérifier vous-même.** Consultez directement [packagist.org/statistics](https://packagist.org/statistics) pour connaître le nombre actuel de paquets, de versions et d'installations, et comparez-le aux chiffres imprimés ici : l'écart montre en direct à quelle vitesse l'écosystème grandit encore. Lisez ensuite [php.net/license](https://php.net/license) en regard de la version de PHP que vous comptez réellement faire tourner, car la licence applicable dépend de cette version précise, pas de celle que ce livre considère comme actuelle.

Licences et hébergement sont les parts du coût total de possession que vous pouvez chiffrer directement. Les parts plus difficiles à chiffrer, la façon dont le langage est gouverné, le rythme de ses changements et ce qui arrive quand une version atteint sa date de fin de support, sont précisément le sujet de [Gouvernance et versions](ch08-governance-and-versions.md).
