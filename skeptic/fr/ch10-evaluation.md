# Une évaluation en une semaine

Rien de ce que j'ai écrit ne devrait décider à votre place. La raison de votre décision devrait être une mesure faite sur votre propre charge de travail, et il ne faut pas longtemps pour en faire une. **Cinq jours ouvrés suffisent pour installer le langage, le lire, l'exécuter sous charge, construire une tranche de votre produit, et vérifier par vous-même l'écosystème et la gouvernance.** Il vous faut un ordinateur portable, une petite machine virtuelle et personne d'autre, et ce que vous tenez à la fin, c'est une page de chiffres que personne ne vous a tendue.

## Jour un : le langage

Installez PHP 8.5 depuis votre gestionnaire de paquets ou lancez l'image officielle, `php:8.5-cli`. Collez le premier exemple du chapitre [Le langage en 2026](ch05-the-language.md) dans un fichier, exécutez-le, puis cassez-le comme ce chapitre le suggère et lisez chaque message d'erreur. Clonez un projet PHP open source d'une taille qui vous parle et lancez sa suite de tests. Passez ensuite un analyseur statique, PHPStan ou Psalm, à son niveau le plus strict, et lisez les vingt premiers résultats :

```bash
composer require --dev phpstan/phpstan
vendor/bin/phpstan analyse --level=max src

composer require --dev vimeo/psalm
vendor/bin/psalm --init src 1 && vendor/bin/psalm
```

Ce que l'analyseur attrape et que le moteur laisse passer, c'est la réponse pratique à la question des génériques. Notez le temps qu'il vous a fallu pour lire la base de code, et si les résultats étaient des choses que vous auriez voulu voir attrapées.

## Jour deux : le runtime

Sur la machine virtuelle, installez PHP-FPM avec nginx, activez OPcache et servez un script hello-world. Servez ensuite le même script sous FrankenPHP en mode worker, et chargez les deux avec le même outil, à la même concurrence :

```bash
wrk -t4 -c64 -d30s --latency http://127.0.0.1/
```

Notez pour chaque exécution les requêtes par seconde, la latence médiane, le 99e centile et la mémoire par worker, lue sur la page de statut de FPM ou dans `ps`. Remplacez ensuite le hello-world par le squelette d'un framework full-stack, n'importe lequel parmi CakePHP, Laminas, Laravel, Symfony ou Yii, et recommencez. Le rapport entre les quatre exécutions est le coût du runtime pour votre future application sur votre matériel, le chiffre que [Débit et latence](ch03-throughput-and-latency.md) ne pouvait vous donner que pour le matériel de quelqu'un d'autre.

## Jour trois : une tranche du produit

Choisissez la fonctionnalité de votre produit qui le représente le mieux : un endpoint authentifié qui lit et écrit une base de données, rend ou sérialise quelque chose, et envoie un message dans une file. Construisez-la dans le framework choisi le deuxième jour, avec des tests, en n'utilisant que ce que le framework et Packagist fournissent, et n'optimisez pas. Notez le temps que cela a pris, la part que vous avez écrite et la part que vous avez configurée, le nombre de paquets tirés, et ce que `composer audit` en a dit.

<img src="images/ch10-week.png" alt="Une bande de cinq cases identiques dessinées sur un mur comme un planning hebdomadaire. Un éléphant debout sur un petit tabouret coche la troisième case avec un stylo ; les deux premières portent une coche, les deux dernières sont vides. Un ordinateur portable et un petit serveur sont posés au sol sous la bande" width="560">

## Jour quatre : la tranche sous charge

Chargez la tranche du troisième jour comme vous avez chargé le hello-world, à la concurrence que vous attendez en production, puis à dix fois cette valeur. Profilez une requête lente avec le profileur de Xdebug ou avec `hrtime()` autour des appels suspects, et regardez où passe le temps ; sur la plupart des tranches, il passe dans la base de données, et le langage n'est qu'une mince part à chaque bout. Notez le débit et le 99e centile aux deux concurrences, et la part d'une requête passée hors de PHP.

Faites ensuite la seule chose que les benchmarks ne font jamais. Tuez un worker en pleine requête, saturez la limite de mémoire, levez une exception non attrapée dans un job de file d'attente, et notez ce que l'utilisateur a vu, ce que les journaux ont dit, et ce qui s'est rétabli tout seul.

## Jour cinq : l'écosystème et la gouvernance

Cherchez sur Packagist les trois bibliothèques dont votre produit ne peut se passer, et notez pour chacune la date de sa dernière version et son nombre de tickets ouverts. Ouvrez wiki.php.net/rfc et lisez la RFC en cours de vote, puis le fil internals qui la porte. Ouvrez la page des versions maintenues de php.net et notez la date à laquelle la version que vous avez choisie cesse de recevoir des correctifs de sécurité. Ouvrez la page Open Collective de la fondation et lisez le dernier mois de transactions, puis les trois avis de sécurité les plus récents de php-src, avec leur délai entre signalement et correctif. Tout cela tient dans un après-midi, et c'est la matière première que [Gouvernance et pérennité](ch07-governance.md) a résumée pour vous.

## La décision

La semaine a produit des chiffres, et une décision demande des pondérations que vous seul pouvez fixer. Chaque question ci-dessous a ses preuves publiques dans un chapitre et votre propre réponse dans un jour de la semaine.

| Question | Preuves publiques | Votre résultat de la semaine |
|---|---|---|
| Aurai-je envie de lire et d'écrire ce langage pendant des années ? | [Le langage en 2026](ch05-the-language.md) | Jour un |
| Le débit du runtime suffit-il à mon trafic, sur mon matériel ? | [Débit et latence](ch03-throughput-and-latency.md) | Jour deux, jour quatre |
| Ma charge de travail tient-elle dans le modèle par requête, ou maintient-elle des connexions, ou consomme-t-elle du CPU ? | [Le runtime](ch02-runtime.md), [Concurrence](ch04-concurrency.md), [Là où PHP est le mauvais choix](ch09-wrong-choice.md) | Jour quatre |
| Les bibliothèques dont j'ai besoin existent-elles, et sont-elles maintenues ? | [L'écosystème](ch06-ecosystem.md) | Jour trois, jour cinq |
| Qui maintient le langage, et jusqu'à quand ma version est-elle prise en charge ? | [Gouvernance et pérennité](ch07-governance.md) | Jour cinq |
| Puis-je recruter pour lui, l'héberger, et me payer la mise à niveau annuelle ? | [Coût de possession](ch08-cost.md) | Vos sites d'offres d'emploi, votre équipe plateforme |
| Tourne-t-il, à l'échelle, dans des organisations dont je croirais qu'elles ont vérifié ? | [Empreinte](ch01-footprint.md) | Leurs documents publics |

Certaines issues reviennent souvent. Quand la charge de travail est en requête-réponse, que le débit du deuxième jour a dépassé votre besoin avec de la marge et que les bibliothèques du cinquième jour étaient vivantes, mes preuves et les vôtres concordent, et la décision porte sur votre équipe plus que sur le langage. Quand le quatrième jour a révélé un cœur limité par le CPU ou par les connexions, la conclusion honnête est un autre langage pour ce cœur, avec éventuellement PHP autour. Et quand la semaine a été agréable mais que les sites d'offres d'emploi de votre ville étaient vides, ou que les chiffres de rétention de [Coût de possession](ch08-cost.md) vous inquiètent plus que le runtime, c'est une raison légitime de décliner. Je ne la contesterai pas, même sous l'égide de la fondation du langage.

> La limite : une semaine mesure une tranche, pas un produit, et l'équipe qui fait tourner la tranche n'est pas celle qui fera tourner le produit pendant dix ans. La semaine retire la réputation de la décision, et laisse le jugement.

## Ce que vous pouvez vérifier vous-même

Tout ce qui précède. Si un chiffre de ces pages se révèle faux quand vous le vérifiez, l'annexe des sources donne l'URL où vit le bon, et le dépôt derrière ce livre accepte les corrections. C'est l'arrangement que vous devez attendre de tout document qui réclame votre temps.
