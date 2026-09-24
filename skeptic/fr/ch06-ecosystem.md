# L'écosystème

Personne n'adopte un langage seul ; on adopte avec lui ses bibliothèques, ses outils et ses conventions, et votre question est de savoir si ceux de PHP tiennent la comparaison avec ce que npm, pip ou Maven vous donnent ailleurs. **PHP a un gestionnaire de paquets, un registre public, un organisme d'interopérabilité qui publie des standards plutôt que des produits, et au moins deux options mûres dans chaque catégorie d'outillage, dont aucune n'est cautionnée par le langage lui-même.** La taille et l'activité se mesurent, et les chiffres sont ici ; la qualité, je ne peux que vous la désigner du doigt.

## Composer et Packagist

Composer est le gestionnaire de dépendances, et il n'y en a pas de second. Il lit un `composer.json`, résout les versions selon des contraintes de versionnage sémantique, écrit un `composer.lock` qui fige chaque dépendance transitive, et génère l'autoloader qui fait correspondre les noms de classes aux fichiers selon le standard PSR-4. Packagist, son registre par défaut, listait 468 099 paquets et 5,8 millions de versions de paquets le 17 septembre 2026, et avait enregistré 199,6 milliards d'installations de paquets depuis avril 2012.

{{#include charts/ch06-packagist-installs.svg}}

Les installations via Composer sont passées de 2,0 milliards en 2016 à 36,0 milliards en 2025, et le seul mois d'août 2026 en a enregistré 4,9 milliards, 91 % de plus qu'en août 2025. C'est le signal d'activité, et sa définition appelle une réserve : une installation est un paquet installé par Composer et signalé au registre, si bien que les pipelines d'intégration continue et les builds d'images de conteneurs en représentent une part large et inconnue. La courbe dit que les projets PHP sont construits, testés et déployés en nombre croissant. Elle ne compte pas les projets, et vous ne pouvez pas non plus mettre le nombre de paquets d'un registre en face de celui d'un autre, parce que ce qu'on appelle un « paquet » diffère d'un écosystème à l'autre.

Depuis Composer 2.4, sorti en août 2022, `composer audit` confronte chaque paquet installé aux avis de sécurité que Packagist sert par son API, et fait échouer le build quand il trouve une vulnérabilité connue, un paquet abandonné ou un paquet signalé comme malveillant. Les avis viennent de la base partagée de l'écosystème, qui en contenait 1 649 en septembre 2026. Les extensions écrites en C, que Composer n'a jamais gérées, ont reçu leur propre installeur en 2025 et 2026 : PIE, le PHP Installer for Extensions, financé par une subvention publique et hébergé sous l'organisation php.

<img src="images/ch06-conveyor.png" alt="Un tapis roulant livre des caisses en bois étiquetées à un établi où un éléphant assemble une machine avec leur contenu. Au mur est accroché un porte-bloc qui liste chaque caisse, avec un petit cadenas dessiné à côté de la liste. Un second éléphant contrôle chaque caisse qui arrive contre le porte-bloc avant qu'elle n'atteigne l'établi" width="560">

## Frameworks et plateformes

Les frameworks full-stack en développement actif sont CakePHP, Laminas, Laravel, Symfony et Yii ; les micro-frameworks, Mezzio et Slim ; les plateformes de contenu, Drupal, Joomla, TYPO3 et WordPress ; les plateformes de commerce, Adobe Commerce avec son édition Magento Open Source, PrestaShop, Shopware, Sylius et WooCommerce. L'ordre est alphabétique d'un bout à l'autre, et je n'en recommande aucun.

Ce qu'ils sont les uns pour les autres, en revanche, se dit avec une source. Symfony publie la liste des projets construits sur ses composants, et elle compte Drupal, Joomla, TYPO3, Magento, PrestaShop, Shopware et Sylius, ainsi que Composer lui-même. Ces composants, et ceux de Laravel, sont ce que vous trouverez sous la plupart des plateformes du chapitre [Empreinte](ch01-footprint.md), WordPress excepté, et c'est pour cela que l'écosystème est moins fragmenté qu'une liste de noms ne le laisse croire. Les chiffres d'usage viennent d'une enquête : parmi les développeurs qui citent PHP comme langage principal, 64 % déclarent utiliser Laravel, 25 % WordPress et 23 % Symfony, plusieurs réponses étant permises. L'échantillon penche vers les clients de l'éditeur, alors lisez cela comme des réponses d'enquête, pas comme un classement que je cautionne.

## Outillage

Chaque catégorie a au moins deux options maintenues, et un après-midi avec chacune est la bonne façon de choisir. Pour les tests, Pest et PHPUnit. Pour l'analyse statique, PHPStan et Psalm, qui lisent tous deux une syntaxe de types en docblock plus riche que le langage et appliquent les génériques, les formes et les types conditionnels que le moteur ne connaît pas. Pour le style de code, PHP-CS-Fixer et PHP_CodeSniffer, tous deux capables d'appliquer le standard PER Coding Style. Pour l'édition, PhpStorm et VS Code avec une extension PHP, chacun avec un serveur de langage ; pour servir, FrankenPHP, PHP-FPM derrière un serveur web et RoadRunner. Deux outils sont seuls dans leur catégorie : Xdebug, le débogueur, qui profile aussi, et Rector, qui réécrit le code vers une syntaxe plus récente et qui est le moyen de faire passer une grande base de code d'une version de PHP à l'autre.

Quelle part de cet outillage est réellement utilisée est une autre affaire, et le chiffre d'enquête sur ce point est le moins flatteur de ce chapitre.

{{#include charts/ch06-tooling-adoption.svg}}

La moitié des développeurs PHP de l'échantillon JetBrains utilisent PHPUnit, un tiers utilisent PHPStan, et un tiers n'écrivent aucun test ; 42 % n'utilisent régulièrement aucun outil de qualité de code. Est-ce pire que dans d'autres écosystèmes, l'enquête ne le dit pas, et je ne le devinerai pas. L'outillage existe ; qu'il soit utilisé est une propriété de l'équipe, pas du langage.

## Standards

Une bibliothèque qui type son logger en `Psr\Log\LoggerInterface` fonctionne sous n'importe quel framework, et c'est à cela que sert le PHP Framework Interoperability Group, PHP-FIG. Il publie les standards qui permettent aux bibliothèques d'auteurs différents de s'emboîter : 14 PHP Standards Recommendations acceptées en septembre 2026, couvrant l'autoloading (PSR-4), la journalisation (PSR-3), les messages et gestionnaires HTTP (PSR-7, 15, 17), le cache (PSR-6, 16), les conteneurs (PSR-11), les événements (PSR-14) et les horloges (PSR-20), plus le PER Coding Style, en version 3.1, qui a remplacé PSR-12 comme standard de codage.

La distribution du langage lui-même est la dernière pièce. php.net publie des archives sources signées par les release managers depuis 2012, avec leurs sommes de contrôle ; les images Docker officielles `php:8.5-cli` et `php:8.5-fpm` suivent chaque version ; et les distributions Linux grand public empaquettent une version qu'elles corrigent elles-mêmes, qui n'est pas toujours une version que php.net maintient encore.

> La limite : l'écosystème est un écosystème web. Sa profondeur en HTTP, gabarits, ORM, files d'attente, paiement et contenu n'a pas d'équivalent en calcul numérique, apprentissage automatique, pipelines de données ou applications de bureau et mobiles, où les paquets sont rares et la communauté petite. Si votre produit en a besoin, vous utiliserez un autre langage pour cette partie, et [Là où PHP est le mauvais choix](ch09-wrong-choice.md) le dit en détail.

## Ce que vous pouvez vérifier vous-même

Lancez `composer create-project` avec le squelette du framework de votre choix, puis `composer audit`, et lisez le fichier lock produit ; toute la chaîne d'approvisionnement est devant vous en dix minutes. Cherchez ensuite sur Packagist les trois bibliothèques dont votre projet ne peut pas se passer, et regardez la date de leur dernière version et le nombre de leurs tickets ouverts. Cette vérification vous en apprend plus que le nombre de paquets.

Sous tout cela tourne un interpréteur, et qui l'entretient est une question à part entière.
