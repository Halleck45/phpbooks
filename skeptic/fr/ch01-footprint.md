# Empreinte

Votre première question est de savoir qui tourne vraiment là-dessus, à quelle échelle, et si la réponse tient dans une liste de logos ou dans une liste de documents. **PHP est le langage côté serveur d'environ sept sites web sur dix parmi ceux dont le langage peut être détecté, et cette part baisse depuis dix ans**. Les deux moitiés de cette phrase comptent, et aucune ne vaut grand-chose tant que vous ne savez pas ce que l'enquête compte.

## Ce que mesure la part du web

{{#include charts/ch01-server-side-languages.svg}}

W3Techs, la société d'études derrière ce chiffre, inspecte chaque jour un échantillon de plus de vingt millions de sites web et détecte le langage côté serveur à partir des en-têtes de réponse, des cookies, des extensions de fichiers et d'autres traces du même genre. Le pourcentage est calculé sur les sites dont le langage a pu être détecté, si bien qu'un site derrière un framework qui ne laisse aucune trace n'est pas compté. Chaque site compte pour un, et l'ensemble de wordpress.com ou de wix.com pèse autant qu'un blog personnel. Un site peut aussi utiliser plusieurs langages, ce qui explique que les colonnes ne totalisent pas cent.

À la même date, JavaScript côté serveur est à 7,5 %, Ruby à 7,1, Java à 5,4, Scala à 5,0, ASP.NET à 4,2 et Python à 1,1. Dans ses limites, l'enquête est stable dans ce qu'elle dit : le gros du web adressable tourne sur PHP, surtout à travers WordPress, et les langages dont on parle davantage sont petits sur cette mesure. Scala devant ASP.NET rappelle que l'enquête compte ce que sa détection voit, et que quelques plateformes laissent une signature sans rapport avec leur usage.

{{#include charts/ch01-server-side-trend.svg}}

La part de PHP sur cette mesure était de 80,6 % au 1er janvier 2015, de 75,2 au 1er janvier 2025 et de 72,4 au 1er janvier 2026, puis de 69,9 en septembre 2026. **La tendance est à la baisse, et c'est la première chose à regarder.** Le déclin s'est accéléré en 2025 et 2026, et la part qui a quitté PHP est allée pour l'essentiel vers JavaScript côté serveur, dont W3Techs a noté en juillet 2026 qu'il avait dépassé Ruby à la deuxième place. Deux faits se tiennent côte à côte : une base installée sur le web public que rien d'autre n'égale, et une courbe qui ne va pas dans le sens de PHP.

## Les plateformes

L'essentiel de cette base installée, ce sont des produits, pas du code sur mesure. WordPress à lui seul fait tourner 40,2 % de tous les sites web, soit 58,8 % des sites qui utilisent un système de gestion de contenu détectable, et les systèmes PHP suivants, Joomla, Drupal, PrestaShop et TYPO3, sont chacun sous les deux pour cent. WooCommerce, l'extension de commerce de WordPress, équipe 8,0 % de tous les sites web et représente 47,7 % des systèmes de commerce en ligne détectés.

{{#include charts/ch01-cms.svg}}

Les plateformes publient aussi leurs propres décomptes, chacun avec son biais. Moodle, la plateforme d'apprentissage, déclare 146 634 sites enregistrés et 531 millions d'utilisateurs, en ne comptant que les sites qui ont choisi de s'enregistrer. Nextcloud annonce plus de 500 000 serveurs. Drupal compte 470 795 sites qui remontent leur version par son module de mise à jour, ce qui oublie ceux qui l'ont désactivé. PrestaShop revendique près de 250 000 sites et plus de 22 milliards d'euros de ventes passées par eux en 2024, un chiffre auto-déclaré. Shopware cite une étude EHI qui le place sur 115 des 1 000 plus grandes boutiques B2C allemandes en 2025, et Matomo, la plateforme d'analyse d'audience, annonce plus de 1,4 million de sites web. Adobe ne publie aucun décompte de marchands pour Adobe Commerce, donc je n'en donne aucun.

Aucun chiffre de cette liste ne compte autant que sa forme. La gestion de contenu, le commerce, l'apprentissage, le partage de fichiers et l'analyse d'audience sont les catégories où l'on installe un produit sur un serveur et où on le laisse tourner des années, et ce sont celles que les logiciels PHP dominent. C'est de là que vient la part de la section précédente.

<img src="images/ch01-backstage.png" alt="Un théâtre vu depuis les coulisses. Sur la scène, sous un projecteur, quelques petits animaux de formes différentes saluent. En coulisses, dans la pénombre, une rangée d'éléphants calmes manœuvrent les cordes, les contrepoids et le pupitre d'éclairage qui font tourner le spectacle" width="560">

## Les organisations qui le disent elles-mêmes

Une entreprise n'apparaît ici que si ses propres ingénieurs ou ses propres documents disent qu'elle fait tourner PHP, et la date de ce document fait partie de la preuve.

**Wikimedia Foundation.** Wikipédia et ses projets frères tournent sur MediaWiki, une application PHP servie par PHP-FPM. Les états financiers audités de la fondation font état de plus de 19,4 milliards de pages vues par mois sur l'ensemble de ses projets. Sa production est passée de PHP 8.1 à PHP 8.3 le 25 novembre 2025, et au moment où j'écris, la migration vers PHP 8.5 est prévue pour la fin 2026. La même infrastructure a tourné sur HHVM jusqu'en 2019, année où la fondation a achevé son retour à l'interpréteur PHP. La fondation rapporte aussi des pics de 800 000 requêtes par seconde sur ses sept centres de données, un chiffre compté en bordure, où la couche de cache sert la plupart des requêtes sans qu'elles atteignent jamais PHP ; ne le lisez donc pas comme un débit PHP.

**Automattic.** WordPress.com et Tumblr, selon Automattic, « tournent principalement sur PHP ». WordPress VIP, la branche d'hébergement pour grands comptes du groupe, publie 2 400 milliards de requêtes servies par an et 22 milliards de requêtes la nuit de l'élection américaine de 2024, des chiffres qui incluent son CDN.

**Etsy.** La page carrières de l'ingénierie de la place de marché indique que ses ingénieurs « codent principalement en PHP et en JavaScript », aux côtés de Java, Go et Swift. Etsy a fait passer sa production à PHP 7 en 2016 et a documenté le passage à l'époque, graphiques de production à l'appui.

**Mailchimp.** Le blog développeurs de l'entreprise décrit son exécuteur de tâches et son monolithe applicatif en PHP, et ses offres d'emploi en ingénierie de 2025 et 2026 demandent PHP aux côtés de React et de Go. Aucun chiffre d'échelle n'est publié.

**Bumble (Badoo).** Le blog d'ingénierie décrivait, en 2017, plus de trois millions de lignes de PHP et des centaines de serveurs applicatifs passés à PHP 7, avec une économie annoncée d'un million de dollars en matériel. Ce chiffre a neuf ans et vous devez le peser comme tel ; les offres d'emploi actuelles de l'entreprise listent toujours PHP à côté de Go.

**Secteur public.** Les sites web de la Commission européenne tournent sur Drupal, ce que leurs pages déclarent dans leurs métadonnées. Des agents de la Commission ont présenté la plateforme à Drupal4Gov EU en janvier 2026, avec 770 sites en ligne, un chiffre rapporté par des participants et que je n'ai pas pu confirmer dans une publication de la Commission. Le site de la Maison-Blanche tourne sur WordPress, hébergé chez WordPress VIP sous une autorisation FedRAMP Moderate. Le Government Site Builder fédéral allemand, le CMS standard des administrations fédérales, est bâti sur TYPO3 et sert plus de 80 administrations et 250 sites web. La plateforme australienne GovCMS déclare plus de 370 sites gouvernementaux sur Drupal, et 77 collectivités locales du Royaume-Uni partagent la distribution LocalGov Drupal.

## Qui est parti, et qui n'y a jamais été

La liste des entreprises qui ont abandonné PHP est aussi instructive que celle qui précède, et elle est plus courte que la réputation ne le laisse croire.

Meta et Slack sont les deux noms qu'on cite le plus souvent pour PHP à grande échelle, et ni l'un ni l'autre ne fait tourner PHP. Les deux font tourner Hack, un langage que Facebook a annoncé en 2014, sur HHVM, une machine virtuelle qu'il développait pour PHP depuis 2011 et qui a abandonné la compatibilité avec PHP en 2019. Slack a retiré son dernier code PHP lors du passage à HHVM 4 et maintient aujourd'hui environ cinq millions de lignes de Hack. Les deux entreprises montrent qu'une base de code commencée en PHP peut devenir très grande, et aucune des deux ne dit quoi que ce soit sur l'interpréteur PHP, donc je ne les compte jamais.

Zalando a réécrit sa boutique Magento en Java en 2010, d'après le témoignage d'un ancien ingénieur. Trivago a remplacé une grande base de code PHP par une application TypeScript entre 2020 et 2021. Dailymotion, qui servait son site avec PHP et Symfony depuis 2005, indique dans une offre d'emploi de 2026 qu'elle « réduit progressivement PHP » et que les nouveaux développements se font en Go, Java et Python. BlaBlaCar, une maison Symfony en 2015, décrit dans ses offres une migration « d'une pile PHP/Symfony vers une pile dominée par Java et JS ». Voilà les cas que j'ai trouvés avec une source primaire, et ils ont un motif commun : une entreprise dont le produit avait dépassé le cadre d'un monolithe web a déplacé ses services vers un langage compilé ou vers la JVM, comme le font au même stade les entreprises qui quittent Ruby ou Python.

## La population de développeurs

La part du web mesure des serveurs. Les enquêtes mesurent des personnes, et elles placent PHP plus bas.

| Mesure | Où se situe PHP | Source et date |
|---|---|---|
| Utilisé au cours de l'année écoulée, développeurs professionnels | 19,1 %, 12e langage | Enquête Stack Overflow, 2025 |
| Utilisé au cours de l'année écoulée, échantillon pondéré | 17 %, 13e langage | JetBrains Developer Ecosystem, 2025 |
| Langage principal | 9 %, 9e | JetBrains Developer Ecosystem, 2025 |
| Contributeurs mensuels sur GitHub | 6e langage, inchangé depuis 2023 | GitHub Octoverse, octobre 2025 |
| Pull requests et tags Stack Overflow | 4e, à égalité avec C# | RedMonk, janvier 2026 |
| Mentions dans les moteurs de recherche | 14e, 1,04 % | TIOBE, septembre 2026 |

Chacune de ces mesures porte sur autre chose, et chacune a un biais connu : l'échantillon de Stack Overflow est auto-sélectionné parmi ses utilisateurs, celui de JetBrains est pondéré vers ses clients, GitHub compte l'activité open source et TIOBE compte des résultats de recherche. Lues ensemble, elles disent qu'entre un développeur sur six et un sur cinq a écrit du PHP dans l'année, que PHP est un premier langage pour moins de gens qu'il n'est un second, et que son activité sur les dépôts publics ne bouge pas. JetBrains décrit PHP comme en « déclin de long terme » aux côtés de Ruby et d'Objective-C, tandis que l'enquête consacrée à PHP du même rapport a trouvé que 58 % des développeurs PHP ne prévoient pas de migrer vers un autre langage. Ce que cela veut dire pour le recrutement est une question pour [Coût de possession](ch08-cost.md).

> La limite : l'empreinte est large et vieille. Sa largeur vient des produits plus que des applications sur mesure, son âge se lit dans la part de la base installée encore sur des versions non maintenues, et la part du langage parmi les développeurs est plus petite que sa part des serveurs en service. Si vous choisissez un langage pour un nouveau service, donnez au second fait plus de poids qu'au premier.

## Ce que vous pouvez vérifier vous-même

Ouvrez les pages W3Techs des langages côté serveur et des systèmes de gestion de contenu ; elles sont mises à jour chaque jour et la vue historique est publique. Pour Wikimedia, les tâches Phabricator que je cite se lisent sans compte et montrent le travail de migration tel qu'il s'est déroulé, dates comprises. Pour toute entreprise nommée ici, allez fouiller vous-même son blog d'ingénierie et ses offres d'emploi, et traitez l'absence de PHP dans les offres récentes comme le signal qu'elle est.

L'échelle du déploiement ne dit rien de la façon dont une requête est servie. C'est là que le runtime entre en scène.
