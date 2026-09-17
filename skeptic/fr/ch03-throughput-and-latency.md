# Débit et latence

À quelle vitesse va-t-il, sur quelle mesure, et face à qui ? C'est votre deuxième question, et c'est celle où la hype fait le plus de dégâts. **Sur le plus grand benchmark public qui compare des frameworks web de tous langages, les entrées PHP s'étalent sur deux ordres de grandeur selon le runtime qui les fait tourner, des quarante premières places au dernier dixième. Le langage seul ne prédit rien ; le déploiement prédit presque tout.** Un écart pareil ne vous sert que si chaque chiffre vient avec son round, son matériel et son test, et ceux de ce chapitre les ont tous les trois.

## L'histoire du moteur

Sur du code qui occupe le processeur, l'interpréteur a fait un grand pas une fois, puis des petits pas depuis. Le grand pas, c'est PHP 7.0, en décembre 2015, qui a remplacé les structures de données internes du moteur. Son éditeur affirmait alors que le temps d'exécution était « souvent divisé par deux » par rapport à PHP 5.6, dans un livre blanc sans méthodologie publiée. Une mesure indépendante, faite sur une seule machine avec toutes les versions de l'interpréteur de 5.6 à une build de développement de PHP 8.0, retrouve la même forme. Le score PHPBench, une suite synthétique de micro-benchmarks de l'interpréteur, passe de 288 000 sur PHP 5.6 à 620 000 sur PHP 7.0, puis monte par petites marches, entre rien et treize pour cent par version, jusqu'à 876 000 sur la build 8.0.

{{#include charts/ch03-engine-progression.svg}}

Depuis PHP 8.0, la vitesse de l'interpréteur sur une application web ne bouge plus, et ceux qui la mesurent le disent eux-mêmes. Un hébergeur qui publie des benchmarks chaque année a mesuré WordPress à 146 requêtes par seconde sur PHP 8.2 et à 148 sur PHP 8.5, sur la même machine, et il écrit que « les versions incrémentales produisent rarement de grands sauts de vitesse à elles seules ». C'est sa propre mesure, lancée à quinze requêtes simultanées sur une machine de trente cœurs ; elle dit donc le temps de réponse, pas la capacité. Retenez ceci : une version actuelle de PHP est à peu près deux fois plus rapide que PHP 5 sur le travail propre de l'interpréteur, et une montée de version mineure ne vous apportera rien d'autre que des corrections et des fonctionnalités.

## Le benchmark multi-langages

Le Framework Benchmarks de TechEmpower est une suite publique qui a fait passer des centaines de frameworks web, dans des dizaines de langages, par les six mêmes tests sur le même matériel, chaque implémentation étant contribuée et entretenue par des volontaires dans un dépôt public. Son dernier round achevé est le Round 23, daté du 24 février 2025, exécuté sur un serveur à processeur Xeon Gold 6330, 28 cœurs et 56 threads, avec un réseau à 40 gigabits. Le dépôt du projet a été archivé le 24 mars 2026 : le Round 23 est donc le dernier, et ses chiffres sont les derniers de leur espèce. Rien d'autre ne compare autant de frameworks sous un même protocole, c'est pourquoi je les garde. Et comme les tests ne mesurent pas la même chose, chaque chiffre nomme le sien.

Le test Fortunes est celui qui ressemble le plus à une page web : une requête en base qui renvoie une douzaine de lignes, un gabarit HTML rendu avec échappement. Sur ce test, 510 entrées ont terminé le Round 23. Le graphique en retient seize, les leaders toutes catégories, le framework grand public de chaque langage majeur et les entrées PHP de chaque type de runtime. Le tableau brut avec toutes les entrées est rangé à côté des données de graphiques du livre, pour que vous puissiez faire votre propre sélection.

{{#include charts/ch03-techempower-fortunes.svg}}

Lisez les barres PHP de haut en bas. Les entrées PHP les plus rapides, sur les runtimes workerman et Swoole, en SQL brut et sans framework, occupent les rangs 31 à 38 sur 510, au-dessus de 730 000 requêtes par seconde, devant l'entrée ASP.NET Core de base, les entrées Go et Spring. Un framework PHP complet avec un ORM complet sur un runtime worker, l'entrée Ubiquity, atteint 428 000 au rang 92. PHP nu sous PHP-FPM et nginx, le déploiement standard, atteint 146 000 au rang 248, environ un tiers devant Gin et FastAPI. Les deux frameworks PHP les plus utilisés, sous PHP-FPM, sont près du bas : Symfony à 26 000 et Laravel à 16 000, derrière Rails à 43 000 et Django à 32 000. Un même benchmark soutient donc à la fois que PHP peut compter parmi les runtimes web les plus rapides et qu'une application PHP typique compte parmi les plus lentes. Quand on ne vous dit que l'un des deux, on vous vend quelque chose.

Une partie de l'écart tient au runtime. Une entrée qui garde l'application chargée entre deux requêtes supprime le coût de démarrage, et c'est lui qui domine le temps de requête d'un framework.

{{#include charts/ch03-runtime-effect.svg}}

Le même code Symfony passe de 26 000 requêtes par seconde sous PHP-FPM à 74 000 sous FrankenPHP et 111 000 sous Swoole, et le même code Laravel de 16 000 à 50 000 sous workerman. Le reste de l'écart tient à l'entrée elle-même. Chez TechEmpower, une entrée est entretenue par qui veut bien s'en occuper, et une entrée lente peut refléter une configuration datée autant que le framework. L'entrée Laravel sous RoadRunner, à 8 000, est plus lente que sous PHP-FPM ; je n'ai pas d'explication et je la rapporte telle qu'elle a été mesurée.

Les autres tests déplacent les rangs, pas l'histoire. Sur le test de sérialisation JSON, qui n'a pas de base de données, l'entrée Swoole atteint 2,5 millions de requêtes par seconde au rang 73, PHP-FPM nu 428 000 et Laravel sous PHP-FPM 27 000, tandis qu'ASP.NET Core est à 1,4 million, Node.js à 1,1 million, Spring à 328 000 et Django à 167 000. Sur le test à vingt requêtes SQL, que le pilote de base de données bride, les leaders de tous les langages se rejoignent sous 90 000, et les entrées PHP les plus rapides sont à 56 000, devant FastAPI à 37 000 et Spring à 32 000.

## La latence

Le débit dit combien de requêtes une machine peut absorber. La latence dit combien de temps un utilisateur attend, et ce qui la domine, c'est ce que la requête attend, pas l'interpréteur. Tideways, un éditeur de profileur et membre fondateur de The PHP Foundation, a mesuré un hello-world PHP-FPM derrière nginx sur une machine virtuelle à huit cœurs, et relevé un 99e centile de 0,9 milliseconde à 18 000 requêtes par seconde. C'est le plancher : l'interpréteur et le gestionnaire de processus coûtent ensemble moins d'une milliseconde quand il n'y a rien d'autre à faire, et tout ce qui vient au-dessus, c'est l'application et ses dépendances.

Les chiffres de latence publics les plus utiles viennent d'une organisation qui publie ses propres objectifs et ses propres tableaux de bord. Les règles d'ingénierie de Wikimedia exigent qu'une requête GET s'achève en 50 millisecondes à la médiane et en 200 millisecondes au 99e centile du temps passé dans PHP, et en 500 millisecondes au 99e centile pour un POST. Son instance Grafana est publique et montre la distribution mesurée pour les requêtes qui atteignent les serveurs applicatifs, c'est-à-dire les défauts de cache et les utilisateurs connectés, autrement dit les requêtes chères. Le jour où j'ai vérifié, la médiane était d'environ 170 millisecondes et la queue de distribution bien au-dessus de l'objectif, pour des pages qui incluent le rendu du wikitexte depuis un cache d'analyse froid. Je vous donne le tableau de bord plutôt que l'instantané, parce qu'une semaine vous en dira plus qu'une heure.

## Là où PHP perd

**Sur du calcul pur, sans entrées-sorties, PHP est un interpréteur avec un JIT en option, et il est un ordre de grandeur plus lent qu'un runtime compilé à la volée comme V8.** Le Computer Language Benchmarks Game, qui compare des programmes contribués sur les mêmes petites tâches, place le programme n-body mono-thread le plus rapide à 2,2 secondes en Rust, 3,1 en C#, 6,0 en Java, 6,4 en Go, 8,6 en Node.js, 167 en Ruby avec YJIT, 204 en PHP 8.4 et 360 en Python 3.13.

{{#include charts/ch03-cpu-bound.svg}}

Le graphique a ses réserves. Les programmes PHP tournent avec un tampon JIT configuré mais `opcache.jit` laissé à sa valeur par défaut de PHP 8.4, c'est-à-dire désactivé : ils mesurent donc l'interpréteur seul. La RFC du JIT rapporte un gain de quatre fois sur Mandelbrot une fois le JIT activé, ce qui resserrerait l'écart sans le combler. Les programmes sont aussi contribués, donc ils mesurent le meilleur programme que quelqu'un a pris la peine d'écrire. Avec ces deux réserves, l'ordre tient. Pour du calcul numérique, de la simulation, l'analyse de gros fichiers en boucle ou tout ce qui occupe un cœur, PHP est dans la classe de Python et de Ruby, pas dans celle de Node.js, et trente à cent fois derrière Go, Java, C# et Rust sur ce programme. [Là où PHP est le mauvais choix](ch09-wrong-choice.md) en tire la conséquence.

> La limite : les bons chiffres de débit de PHP viennent des runtimes worker et de l'accès brut à la base, ce qu'une équipe ordinaire ne fait pas tourner dès le premier jour. Ses chiffres typiques, un framework complet sous PHP-FPM, sont ceux de Rails et de Django, quelques dizaines de milliers de requêtes par seconde sur une grosse machine, ce qui reste plus que ce que la plupart des applications recevront jamais. Et sur du calcul pur, l'interpréteur est un ordre de grandeur derrière V8.

## Ce que vous pouvez vérifier vous-même

L'outillage TechEmpower tourne encore depuis son dépôt archivé, avec Docker, et les tableaux bruts du Round 23 pour six tests sont rangés en CSV dans le dossier `charts/raw/` du livre : vous pouvez vérifier ma sélection et en faire une autre. Plus près de chez vous, prenez l'application que vous construiriez, ou un équivalent open source, faites-la tourner sous PHP-FPM puis sous un runtime worker sur la même machine, et mesurez avec `wrk` à la concurrence que vous attendez en production. Le rapport que vous obtiendrez est le seul qui compte. Pour la latence, ouvrez le tableau de bord public « Backend Pageview Timing » de Wikimedia et lisez-en une semaine.

Le débit suppose des requêtes indépendantes. Que se passe-t-il quand elles ne le sont pas ? C'est la question suivante.
