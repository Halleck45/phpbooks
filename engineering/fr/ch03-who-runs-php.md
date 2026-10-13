# Qui fait tourner PHP

**PHP fait tourner la majorité du web si l'on compte les serveurs et une minorité si l'on compte les développeurs, et ces deux chiffres sont vrais en même temps parce qu'ils ne mesurent pas la même chose.** Si vous n'avez entendu que l'un des deux, vous n'avez vu que la moitié du tableau, et la moitié que vous connaissez dépend sans doute de la personne qui vous l'a racontée.

Côté serveurs, W3Techs, qui explore les sites en ligne au lieu d'interroger des gens, place PHP à **69,9 % des sites web dont il parvient à détecter le langage côté serveur**, au 17 septembre 2026. Ce chiffre bouge en continu au fil de l'exploration. Prenez-le donc pour un instantané et non pour une constante, avec la même réserve que celle posée dans [La réputation](ch01-introduction.md). Côté développeurs, le tableau change. Le Stack Overflow Developer Survey 2025, fondé sur 24 759 répondants qui se déclarent développeurs professionnels, trouve 19,1 % d'utilisateurs de PHP, contre 68,8 % pour JavaScript, 54,8 % pour Python, 48,8 % pour TypeScript, 29,9 % pour C# et 29,6 % pour Java.

<div class="chart">

{{#include charts/ch03-adoption.svg}}

</div>

Lisez ce graphique tel qu'il doit être lu, et non comme l'un ou l'autre camp d'un débat le préférerait. PHP se place derrière JavaScript, Python, TypeScript, C# et Java, et devant Go et Ruby, à 17,4 % et 6,9 %. Ce n'est pas le langage dominant chez les développeurs professionnels, et ce n'est pas non plus un langage de niche. Il occupe une position précise, au milieu du classement et bien peuplée, et un lecteur hostile qui consulte l'enquête lui-même trouvera exactement ce graphique, pas une version plus flatteuse ou plus arrondie.

Les deux chiffres ne se contredisent pas. Ils comptent des populations différentes. Celui de W3Techs compte des sites en service, dont la plupart ont été construits une fois puis peu entretenus, voire pas du tout. Une énorme part du web est faite de petits sites marchands, de blogs et de plateformes de contenu bâtis sur un CMS, et les CMS, parmi lesquels Drupal, Joomla, TYPO3 et WordPress, tournent sur PHP. Celui de Stack Overflow compte les développeurs qui ont choisi de répondre à une enquête destinée aux professionnels qui écrivent du code au quotidien, une population plus petite, plus autosélectionnée et différente de « tous ceux qui ont un jour mis un site en ligne ». Les deux chiffres sont honnêtes. Aucun, à lui seul, ne répond à « les développeurs que mon nouveau projet vise connaissent-ils déjà PHP ? », plus proche de la question des effectifs, ni à « mon application va-t-elle côtoyer beaucoup d'autres infrastructures PHP ? », plus proche de la question des serveurs.

<img src="images/ch03-who-runs.png" alt="Une rue où presque chaque devanture porte une petite enseigne à l'éléphant, alors que seules trois personnes dans la foule du trottoir portent un badge à l'éléphant ; au coin de la rue, un éléphant compte les deux sur un bloc-notes." width="560">

Pour une décision de recrutement, le chiffre des développeurs est en général le plus utile, parce qu'il se rapproche de la question « combien de personnes connaissant déjà ce langage pourrais-je raisonnablement embaucher ? ». Le chiffre des serveurs se rapproche plutôt de « quelle part de l'infrastructure environnante, des panneaux de contrôle d'hébergement aux extensions de CMS en passant par les outils internes d'autres entreprises, supposera que PHP est de la partie ? ». Les deux questions ont leur place dans une revue de due diligence, et les fondre en une seule phrase du type « PHP est populaire » efface précisément la distinction dont vous avez besoin.

## Un cas à grande échelle, documenté par l'organisation elle-même

Les chiffres agrégés sur le web sont utiles, mais vous voulez aussi savoir à quoi ressemble PHP sous une charge réelle et soutenue, pas seulement à quelle fréquence il apparaît. Wikimedia est l'une des rares organisations à le documenter en détail, avec ses propres mots, sur son propre wiki technique et non par l'intermédiaire d'un tiers. MediaWiki, le logiciel qui fait tourner Wikipédia et ses projets frères, est écrit à environ 70 % en PHP selon Wikimedia, soit près de deux millions de lignes de code PHP maintenues par la fondation. Il tourne dans sept centres de données, trois aux États-Unis, deux en Europe, un en Asie et un en Amérique du Sud, derrière plusieurs étages de cache (Varnish et Apache Traffic Server devant, APCu et Memcached derrière l'application) qui maintiennent réactif un site du top dix mondial sous un trafic continu venu du monde entier.

<div class="chart">

{{#include charts/ch05-datacenters.svg}}

</div>

Cette répartition géographique compte pour une raison qui dépasse la redondance : elle montre que le modèle de requête *shared-nothing* de PHP, décrit dans [Le runtime](ch02-runtime.md), n'est pas une limite réservée aux petits sites. Dans chacun de ces sept emplacements, une requête démarre, s'exécute et se démonte de façon indépendante, sans mémoire partagée par construction, et l'ensemble sert pourtant l'un des sites les plus visités d'internet. Le trafic y est routé selon la géographie, si bien qu'un visiteur obtient sa réponse du centre de données le plus proche plutôt que d'un centre unique. La documentation de Wikimedia est une page de wiki vivante et non un rapport daté, je la cite donc avec sa date de consultation, le 17 septembre 2026, et je la traite comme toute source qui évolue : exacte au jour de la lecture, pas figée pour toujours.

Ce cas ne remplace pas une enquête. Une organisation, si grande soit-elle, prouve qu'une chose est possible ; elle ne décrit pas une distribution. Elle vous apprend que PHP peut être exploité à cette échelle par une organisation prête à investir dans les couches de cache et de routage qui l'entourent. Elle ne vous dit pas quelle part des déploiements PHP atteint réellement cette échelle, et je ne laisserai pas entendre le contraire en présentant un exemple unique comme représentatif.

## Ceux qu'il faut écarter

Deux noms reviennent par réflexe dès qu'on parle de PHP à grande échelle, et tous deux appartiennent à l'autre colonne. On suppose souvent que Meta et Slack font tourner PHP, à cause du lien historique entre PHP et les débuts de l'ingénierie chez Meta. En réalité, tous deux utilisent Hack, un langage apparenté mais distinct, sur HHVM, un runtime qui a rompu la compatibilité avec PHP il y a des années. Les compter comme preuves en faveur de PHP serait exactement le genre de tri sélectif que la règle de neutralité de ce livre doit empêcher. Je les nomme donc ici pour les écarter, pas pour les revendiquer.

> **La limite.** En dehors de Wikimedia, les études de cas PHP à grande échelle, vérifiables et documentées à la source, sont plus difficiles à trouver que la réputation ne le laisse croire. Plusieurs des chiffres qu'on répète volontiers sur d'autres grandes plateformes PHP remontent à des billets de blog sponsorisés, à des conférences résumées de seconde main ou à des documents commerciaux vieux de plusieurs années, plutôt qu'à une déclaration actuelle et datée de l'entreprise elle-même. Je préfère publier une seule étude de cas que je peux défendre entièrement plutôt que plusieurs que je ne peux pas défendre, et je le dis ici au lieu de remplir le chapitre en douce.

**À vérifier vous-même.** Ouvrez [w3techs.com/technologies/details/pl-php](https://w3techs.com/technologies/details/pl-php) et comparez le pourcentage en ligne à celui imprimé plus haut. Ouvrez ensuite les résultats technologiques du Stack Overflow Developer Survey de l'année en cours et regardez où se situe réellement PHP face aux langages que votre équipe connaît déjà : pour une décision de recrutement, c'est en général cette comparaison qui compte, et non la part agrégée du web.

L'adoption vous dit qui fait tourner PHP et sur quelle surface. Elle ne vous dit pas à quelle vitesse tout cela tourne, une question distincte, souvent confondue avec la première, et que [Performances](ch04-performance.md) aborde de front.
