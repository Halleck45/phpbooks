# L'évaluation

**Chaque chiffre de ce livre était vérifiable le jour où je l'ai écrit, et chacun aura bougé le jour où vous le lirez ; ce chapitre vous donne donc les vérifications elles-mêmes, pas un chiffre de plus à croire sur parole.** Une revue de due diligence ne s'achève pas sur la lecture des conclusions d'un autre. Elle s'achève quand vous refaites vous-même les mesures dont dépend votre décision, et ce chapitre ne contient rien d'autre que les moments où les neuf chapitres précédents vous demandaient déjà de le faire.

<img src="images/ch10-evaluation.png" alt="À une table de cuisine, une personne tape sur un ordinateur portable pendant qu'un éléphant à côté d'elle tient une liste imprimée et coche la troisième case, en comparant la feuille avec l'écran." width="560">

## Ce que votre propre machine sait déjà

Avant de vérifier quoi que ce soit sur l'écosystème, regardez l'installation de PHP sur laquelle vous déploieriez vraiment. Le script ci-dessous, volontairement court, rapporte les faits que [Le runtime](ch02-runtime.md) a passé un chapitre à expliquer : la version qui tourne, si opcache est réellement chargé et pas seulement disponible en théorie, et si le JIT est activé.

```php
<?php

declare(strict_types=1);

function reportRuntimeStatus(): array
{
    return [
        'php_version' => PHP_VERSION,
        'sapi' => PHP_SAPI,
        'opcache_loaded' => extension_loaded('Zend OPcache'),
        'jit_enabled' => function_exists('opcache_get_status')
            && (opcache_get_status(false)['jit']['on'] ?? false),
    ];
}

foreach (reportRuntimeStatus() as $fact => $value) {
    printf("%-15s %s\n", $fact, var_export($value, true));
}
```

Lancez-le avec `php status.php` sur chaque environnement que vous évaluez, y compris celui qu'un fournisseur vous livre avec ses garanties. Quand un fournisseur affirme qu'« opcache et le JIT sont activés », c'est une phrase. La sortie de ce script est un fait établi sur cette machine précise, et les deux ne pèsent pas le même poids comme preuve.

## Toutes les vérifications du livre, au même endroit

Chaque chapitre se terminait sur une chose à vérifier en un après-midi. En les refaisant ensemble, dans l'ordre, vous reconstruisez toute la base de preuves du livre à partir des sources vivantes, et non de la photographie qu'en a imprimée cette édition.

```bash
# Chapter 1 and 8: current adoption and version fragmentation
# https://w3techs.com/technologies/details/pl-php

# Chapter 2: your own install's runtime state
php -v
php -i | grep -i opcache

# Chapter 3: professional developer adoption by language
# https://survey.stackoverflow.co (current year's technology results)

# Chapter 4: CPU-bound benchmarks, still actively maintained
# https://benchmarksgame-team.pages.debian.net/benchmarksgame/

# Chapter 6: the PHP core's own contributor activity
# https://github.com/php/php-src

# Chapter 7: live package, version, and install counts
# https://packagist.org/statistics

# Chapter 8: the current support window for your PHP version
# https://php.net/supported-versions.php
```

Aucune de ces vérifications ne demande d'accès particulier, de compte payant ou de contact bien placé. C'est voulu. Vous demander de croire un chiffre que vous ne pourriez pas atteindre seul, ce serait vous demander la même confiance que la réputation décrite dans [La réputation](ch01-introduction.md) : croire des impressions de seconde main sur PHP plutôt que regarder le langage tel qu'il est aujourd'hui. J'ai passé neuf chapitres à combattre cette habitude.

## Lire les affirmations d'un fournisseur comme j'ai lu les miennes

La méthode compte plus que la liste, parce que la liste vieillira et que la méthode ne devrait pas. Quand un fournisseur, la documentation d'un framework ou un collègue vous tend un chiffre de performance, une promesse de sécurité ou une statistique d'adoption, posez-lui les trois questions que je me suis posées avant d'imprimer quoi que ce soit. D'où vient le chiffre, dans les mots mêmes de la source et non dans un résumé ? Qu'a-t-on mesuré exactement, et cela correspond-il à ce qui vous importe ? [Performances](ch04-performance.md) a dû séparer un micro-benchmark du JIT d'un benchmark de requêtes web avant que l'un ou l'autre veuille dire quelque chose. Enfin, que dit la source elle-même de ce qu'elle ignore ? Une source qui énonce ses propres limites mérite plus de confiance qu'une source qui n'en a aucune.

## Un exemple concret, avec mes citations les plus fragiles

Le meilleur test de cette méthode consiste à la retourner contre ce livre. [Qui fait vivre PHP](ch06-who-maintains-it.md) cite une enquête de JetBrains qui annonce elle-même sa faiblesse : ses résultats penchent sans doute vers les utilisateurs des produits JetBrains. Cette source passe le test. Elle n'est pas impartiale, aucune enquête auprès de répondants volontaires ne l'est, mais elle vous dit de quel côté elle penche avant que vous ayez à le deviner. [Performances](ch04-performance.md) fait un autre travail honnête : il nomme une série de benchmarks, TechEmpower, qui a cessé de paraître, avec la date exacte, au lieu de citer sa dernière édition comme si rien n'avait changé. [Gouvernance et versions](ch08-governance-and-versions.md), lui, écarte de ses affirmations fermes quelques chiffres, dont les montants exacts du financement de la PHP Foundation, parce qu'au moment de l'écriture je ne les avais confirmés que par un récit de seconde main et non sur la page de la Foundation. [Sources](appendix-01-sources.md) marque chacun d'eux comme en attente de vérification directe, plutôt que d'imprimer un chiffre que je ne peux pas défendre. Une source qui vous dit ce qu'elle ignore, dans ses propres mots, fait le travail que j'ai essayé de faire tout au long de ces pages, et c'est le signal le plus net à chercher dans tout ce qu'on vous remettra pendant votre propre évaluation.

> **La limite.** Une liste de vérifications ne vaut que pour le jour où on l'a passée. Chaque commande et chaque URL ci-dessus renverra un autre chiffre au trimestre prochain, de la même façon que chaque chiffre imprimé plus haut aura bougé quand vous le lirez. Ce chapitre ne peut pas vous donner une réponse à jour pour toujours. Il vous donne une façon reproductible d'en obtenir une, et c'est ce qui durera le plus longtemps.

**À vérifier vous-même, une dernière fois.** Choisissez le chiffre du livre dont votre décision dépend le plus, quel que soit le chapitre d'où il vient, et retournez à sa source avant d'agir. S'il dit toujours ce que j'ai écrit qu'il disait, vous tenez une confirmation indépendante. Sinon, vous avez pris ce livre en flagrant délit de péremption avant qu'il vous coûte quoi que ce soit, et c'est exactement pour cela que toute la démarche a été construite.

J'ai ouvert ce livre en séparant la réputation de PHP du langage que vous avez aujourd'hui sous les yeux. Je le referme en vous rendant cette séparation sous forme de méthode, pas de conclusion. Le modèle d'exécution, les chiffres d'adoption, les comparaisons de performances, la structure des coûts, le processus de gouvernance et les limites dites sans détour ne valent que ce que vaut votre volonté de les vérifier à nouveau. [Sources](appendix-01-sources.md) donne l'origine exacte de chaque chiffre, chapitre par chapitre, pour que la vérification ne soit jamais à plus d'un lien.
