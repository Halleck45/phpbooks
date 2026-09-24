# Concurrence et performance

**PHP est synchrone : un processus exécute une requête, bloque à chaque appel d'entrée-sortie, et ce comportement est voulu.** Il n'y a pas de boucle d'événements à alimenter, pas de mot-clé `async` à écrire, pas de goroutine à lancer, parce que la concurrence vient de l'extérieur du processus : le pool FPM fait tourner autant de copies de votre script que vous en avez configurées, chacune seule dans sa mémoire, et le système d'exploitation les répartit sur les cœurs.

Si vous venez de Node, cela ressemble à un retour en arrière, mais la comparaison ne tient pas. Node a besoin d'une boucle d'événements parce qu'un seul processus sert toutes les connexions, si bien qu'un seul appel bloquant les figerait toutes. PHP a donné à chaque requête son propre processus, donc un appel bloquant ne coûte rien que quiconque puisse voir : une requête en base qui prend 40 millisecondes occupe un worker pendant 40 millisecondes, et les autres workers ne s'en aperçoivent pas.

<img src="images/ch13-processes-vs-loop.png" alt="Panneau de gauche : un éléphant jongleur qui maintient de nombreuses balles en l'air, étiqueté boucle d'événements. Panneau de droite : une rangée d'éléphants qui tiennent chacun calmement une balle, étiquetée pool de processus. Les deux panneaux ont le même nombre de balles" width="620">

## Ce que vous n'avez pas

Il n'y a pas de threads côté utilisateur. Une extension `parallel` existe pour les builds thread-safe (ZTS), et presque personne ne s'en sert. Le build standard est NTS, non thread-safe, parce que le modèle sans état partagé n'a jamais eu besoin de threads.

Il n'y a pas non plus d'ordonnanceur intégré. **Les Fibers (PHP 8.1) sont des coroutines à pile : une fonction peut se suspendre, et celui qui détient la fiber peut la reprendre plus tard, sans que rien dans le langage ne décide du moment de la reprise ni ne multiplexe les sockets.** Une fiber est une brique de base, et les bibliothèques asynchrones s'en servent pour qu'un code d'apparence ordinaire puisse céder la main au milieu d'un appel bloquant.

```php
<?php
declare(strict_types=1);

$fiber = new Fiber(function (string $greeting): string {
    $name = Fiber::suspend('who is there?');

    return "$greeting, $name";
});

$question = $fiber->start('Hello');   // runs until suspend()
echo $question, PHP_EOL;              // who is there?

$fiber->resume('Ada');                // runs to the return
echo $fiber->getReturn(), PHP_EOL;    // Hello, Ada
```

Vous lirez du code comme celui-ci dans une bibliothèque, mais vous ne l'écrirez pas dans une application. L'équivalent Python serait une coroutine à base de générateurs comme on en écrivait avant `asyncio`, c'est-à-dire le mécanisme sans le runtime.

## Quand vous avez vraiment besoin d'asynchrone

Certaines charges ne rentrent pas dans le modèle « une requête, un processus » : un serveur websocket qui tient dix mille connexions inactives, du long polling, un crawler qui fait cent appels HTTP sortants à la fois. **Pour celles-là, PHP a des runtimes asynchrones, et ce sont des bibliothèques, pas des fonctionnalités du langage.** Par ordre alphabétique : AMPHP, ReactPHP, et Swoole ou son fork OpenSwoole, qui est une extension. Les deux premiers sont du PHP pur bâti sur les fibers et la sélection de flux ; Swoole apporte sa propre boucle d'événements en C.

Les runtimes worker de [Comment PHP s'exécute](ch01-how-php-runs.md), FrankenPHP et RoadRunner, sont une autre réponse à une autre question : ils gardent votre application amorcée entre les requêtes, toujours une requête à la fois par worker. Ils suppriment le coût de démarrage, mais ils ne rendent pas votre code concurrent.

Avant de vous tourner vers l'un d'eux, demandez-vous si le problème est vraiment la concurrence, parce qu'une application web classique n'en a jamais besoin et que dix workers FPM de plus ne coûtent qu'une ligne de configuration.

## Le travail en arrière-plan

Une requête dispose de trente secondes et doit envoyer une réponse, donc tout ce qui prend plus longtemps, ou tout ce que l'utilisateur n'attend pas, doit sortir de la requête.

**L'idiome consiste à associer une file d'attente et un worker.** La requête dépose un travail (une ligne dans une table, un message dans un broker) et rend la main. Un script CLI, lancé par un superviseur de processus, boucle indéfiniment en tirant les travaux et en les exécutant. Il n'a ni limite de temps ni limite de mémoire à moins que vous ne les fixiez, donc fixez-les : `memory_limit` dans l'ini, et un compteur qui sort proprement après quelques milliers de travaux pour que le superviseur relance un processus neuf. Une fuite mémoire dans une boucle sans fin est le seul cas où le nettoyage par requête de PHP ne vous sauve pas.

Cron couvre le cas planifié. La CLI a le reste de la boîte à outils : `proc_open()` lance un sous-processus avec des tubes, `pcntl_fork()` duplique le processus courant (CLI seulement, jamais sous FPM), et `curl_multi_exec()` effectue des requêtes HTTP en parallèle sans la moindre bibliothèque :

```php
<?php
declare(strict_types=1);

$urls = ['https://example.com/a', 'https://example.com/b', 'https://example.com/c'];
$multi = curl_multi_init();
$handles = [];

foreach ($urls as $url) {
    $handle = curl_init($url);
    curl_setopt($handle, CURLOPT_RETURNTRANSFER, true);
    curl_multi_add_handle($multi, $handle);
    $handles[$url] = $handle;
}

do {
    $status = curl_multi_exec($multi, $running);
    if ($running) {
        curl_multi_select($multi);
    }
} while ($running && $status === CURLM_OK);

foreach ($handles as $url => $handle) {
    echo $url, ': ', strlen((string) curl_multi_getcontent($handle)), " bytes\n";
    curl_multi_remove_handle($multi, $handle);
}
```

Trois requêtes partent en même temps pour une seule attente, et c'est tout le parallélisme dont la plupart des scripts auront jamais besoin.

## Où passe le temps

**L'interpréteur est rarement le goulot d'étranglement.** Une requête passe son temps à attendre la base de données, le cache, le système de fichiers et d'autres services. Optimiser une boucle qui tourne en deux millisecondes pendant qu'une requête SQL en prend quatre-vingts est l'erreur classique, et elle ne dépend pas du langage.

Le seul réglage qui compte est OPcache, décrit dans [Comment PHP s'exécute](ch01-how-php-runs.md). Assurez-vous qu'il est actif et que `opcache.memory_consumption` est assez grand pour toute la base de code (`opcache_get_status()` vous le dit). Deux raffinements viennent par-dessus :

- **Le préchargement** (`opcache.preload=preload.php`) compile une liste de fichiers une fois au démarrage de FPM et les garde liés en mémoire, si bien que les classes n'ont plus besoin d'autoloading du tout. Il faut un redémarrage pour prendre en compte les changements, et c'est pourquoi c'est un réglage de production.
- **Le JIT** compile les chemins chauds en code machine. Il accélère le travail gourmand en CPU, parfois beaucoup, et accélère très peu une requête web ordinaire. Activez-le (`opcache.jit=tracing`, `opcache.jit_buffer_size=64M`), mesurez, gardez-le s'il a aidé.

L'autoloading a un coût, et Composer peut en supprimer l'essentiel. `composer dump-autoload -o` génère une carte de classes pour qu'aucune recherche sur le système de fichiers n'ait lieu par classe ; `--classmap-authoritative` va plus loin et ne touche jamais au système de fichiers pour une classe absente de la carte. Les deux ont leur place dans le script de déploiement. `realpath_cache_size` dans l'ini, quelques mégaoctets, évite à PHP de résoudre à nouveau les chemins à chaque requête.

## Mesurer

Rien de ce qui précède ne vaut la peine avant une mesure. Le langage fournit les deux primitives :

```php
<?php
declare(strict_types=1);

$numbers = range(1, 1_000_000);

$start = hrtime(true);
$doubled = array_map(fn (int $n): int => $n * 2, $numbers);
$mapTime = hrtime(true) - $start;

$start = hrtime(true);
$doubled = [];
foreach ($numbers as $n) {
    $doubled[] = $n * 2;
}
$loopTime = hrtime(true) - $start;

printf("array_map: %.1f ms\n", $mapTime / 1e6);
printf("foreach:   %.1f ms\n", $loopTime / 1e6);
printf("peak memory: %.1f MB\n", memory_get_peak_usage() / 1e6);
```

Les deux mesures tombent dans les dizaines de millisecondes pour un million d'éléments, avec un écart faible qui dépend de la version de PHP. La leçon n'est pas de savoir lequel gagne, mais qu'un million d'itérations coûte moins qu'une seule requête SQL lente, ce qui vous laisse libre d'écrire la version la plus lisible.

Pour un vrai profil, Xdebug a un mode profileur (`xdebug.mode=profile`) qui écrit des graphes d'appels que votre éditeur peut ouvrir, et des profileurs par échantillonnage existent sous forme d'extensions pour la production, où le surcoût de Xdebug est inacceptable. Pointez l'un ou l'autre sur une requête lente et lisez le haut de la liste.

La mémoire suit la même règle. Une requête qui construit un tableau de cent mille lignes et meurt sur `memory_limit` a besoin d'un générateur, comme l'a montré [Fonctions et closures](ch05-functions-and-closures.md), pas d'une limite plus haute. `unset()` libère une variable, et le ramasse-miettes gère seul les cycles de références ; `gc_collect_cycles()` force une passe, qu'un worker de longue durée peut appeler entre deux travaux.

<img src="images/ch13-where-time-goes.png" alt="Une barre horizontale qui montre une requête web comme une frise chronologique. Une fine tranche à gauche est étiquetée PHP, puis un long segment étiqueté base de données, puis un segment moyen étiqueté appel HTTP, puis une fine tranche étiquetée PHP à nouveau. Un petit éléphant pointe le long segment base de données avec une loupe" width="560">

## Le piège

La première erreur consiste à importer un modèle de concurrence parce que le langage précédent en avait besoin. Un runtime asynchrone sous une application CRUD ajoute une couche, un jeu de bibliothèques qui doivent être compatibles avec les fibers, et une classe de bugs (l'état partagé entre les requêtes) que FPM rendait impossibles. Le gain est nul, parce que les requêtes ne s'attendaient jamais les unes les autres.

La seconde consiste à optimiser sans chiffre. L'option JIT, la carte de classes ou la boucle réécrite sont autant d'hypothèses, et seule une mesure avec `hrtime()` sur le chemin lent, avant et après, en fait des résultats.

Le runtime, le langage et les outils sont maintenant couverts, et il reste un lecteur à servir : [Revenir à PHP après des années](ch14-returning-developer.md) s'adresse au développeur dont le dernier PHP contenait encore `mysql_query`.
