# C - Glossaire

Les termes que j'emploie et que vous pouvez ne pas connaître si vous venez d'un autre écosystème, dans l'ordre alphabétique des termes anglais.

**Active support (support actif).** Les deux premières années d'une branche de PHP, pendant lesquelles les bugs et les failles de sécurité sont corrigés dans des versions de correction mensuelles. Suivent deux années de support de sécurité, avec des correctifs de sécurité seulement. Voir [Gouvernance et pérennité](ch07-governance.md).

**Composer.** Le gestionnaire de dépendances de l'écosystème PHP, comparable à npm, pip ou Maven. Il lit `composer.json`, résout les versions, écrit `composer.lock` et génère l'autoloader qui fait correspondre les noms de classes aux fichiers.

**Fiber.** Une coroutine à pile, ajoutée dans PHP 8.1 : une fonction qui peut se suspendre elle-même et être reprise plus tard par qui la détient. Le langage fournit le mécanisme, rien de plus, et l'ordonnancement revient aux bibliothèques. Voir [Concurrence](ch04-concurrency.md).

**FrankenPHP.** Un serveur d'application pour PHP, écrit en Go au-dessus du serveur web Caddy. Il exécute PHP soit dans le mode classique d'un processus par requête, soit dans un mode worker qui garde l'application démarrée entre les requêtes. Voir [Le runtime](ch02-runtime.md).

**Hack et HHVM.** Hack est un langage qui a divergé de PHP chez Facebook en 2014, et HHVM est sa machine virtuelle. HHVM a abandonné la prise en charge de PHP lui-même en 2019. Les organisations qui font tourner Hack ne font pas tourner PHP, et je ne les compte pas comme utilisatrices de PHP.

**JIT.** Le compilateur à la volée livré à l'intérieur d'OPcache depuis PHP 8.0, qui compile les chemins de code chauds en code machine. Il profite bien plus au code limité par le CPU qu'aux requêtes web ordinaires, et je le rappelle partout où un chiffre JIT apparaît.

**NTS et ZTS.** Les builds non-thread-safe et Zend-thread-safe de l'interpréteur. Le build standard est NTS, parce que le modèle par processus n'a jamais eu besoin de threads. Les builds ZTS existent pour l'usage embarqué et pour l'extension `parallel`.

**OPcache.** L'extension qui garde la forme compilée de chaque fichier PHP en mémoire partagée, si bien qu'un fichier est analysé et compilé une fois plutôt qu'à chaque requête. Elle est standard en production depuis PHP 5.5.

**p50, p95, p99.** Les centiles d'une distribution de latence : le temps de réponse sous lequel 50, 95 ou 99 % des requêtes se terminent. Un benchmark qui ne rapporte que la moyenne cache la queue de distribution, et c'est pourquoi je préfère les sources qui publient des centiles.

**Packagist.** Le registre public de paquets que Composer utilise par défaut, comparable à npmjs.com ou PyPI.

**PER Coding Style.** Le standard de style de code maintenu par le PHP-FIG, successeur de PSR-12. Des outils tels que PHP-CS-Fixer et PHP_CodeSniffer le font respecter.

**PHP-FIG.** Le PHP Framework Interoperability Group, qui publie les standards PSR pour que les bibliothèques d'auteurs différents s'emboîtent.

**PHP-FPM.** Le FastCGI Process Manager, la façon standard d'exécuter PHP derrière un serveur web. Il entretient un pool de processus worker, chacun traitant une requête à la fois.

**Preloading (préchargement).** Une fonctionnalité d'OPcache (PHP 7.4) qui compile une liste de fichiers une fois au démarrage et les garde liés en mémoire, si bien qu'aucune classe n'a besoin d'autoloading pendant une requête.

**PSR.** PHP Standards Recommendation, un standard d'interopérabilité numéroté publié par le PHP-FIG : PSR-4 pour l'autoloading, PSR-3 pour la journalisation, PSR-7 pour les messages HTTP, et ainsi de suite.

**Rector.** Un outil qui réécrit le code PHP automatiquement : il fait monter la syntaxe d'une version à la suivante, applique des refactorings et supprime les appels dépréciés. Les équipes s'en servent pour les montées de version à grande échelle.

**RFC.** Request for Comments, le document par lequel tout changement du langage est proposé, discuté sur la liste de diffusion internals et soumis au vote. Un changement du langage requiert une majorité des deux tiers. Voir [Gouvernance et pérennité](ch07-governance.md).

**RoadRunner.** Un serveur d'application pour PHP écrit en Go. Il garde des processus worker en vie et leur transmet les requêtes par un protocole, si bien que l'application est démarrée une fois plutôt qu'à chaque requête.

**Shared-nothing.** Le modèle d'exécution dans lequel chaque requête démarre avec une mémoire vierge, s'exécute, répond et est jetée, sans rien partager avec la requête précédente ni la suivante. La plupart des propriétés opérationnelles de PHP en découlent. Voir [Le runtime](ch02-runtime.md).

**Static analysis (analyse statique).** Lire le code sans l'exécuter, pour y trouver les erreurs de type et d'autres défauts. PHPStan et Psalm sont les deux analyseurs de l'écosystème PHP, et tous deux comprennent une syntaxe de types en docblock plus riche que celle du langage lui-même.

**Swoole et OpenSwoole.** Une extension en C et son fork. Chacune donne à PHP une boucle d'événements, des coroutines et un serveur HTTP intégré, pour les charges de travail qui ont besoin de nombreuses connexions concurrentes dans un seul processus.

**TechEmpower Framework Benchmarks.** Une suite de benchmarks publique, exécutée en continu, qui compare des centaines de frameworks web de tous langages sur un jeu de tests fixe (sérialisation JSON, requêtes de base de données simples et multiples, rendu HTML « fortunes », plaintext). Je la cite avec son numéro de round, son matériel et le test, et je dis ce que chaque test mesure.

**W3Techs.** Une société d'enquêtes sur le web qui publie l'usage des technologies côté serveur sur un échantillon de plus de vingt millions de sites. Ses chiffres ne comptent que les sites dont le langage peut être détecté, ce qui les biaise d'une manière que je précise quand je les utilise.

**Worker mode (mode worker).** Une façon d'exécuter PHP dans laquelle l'application est démarrée une fois et gardée en mémoire, chaque processus worker traitant de nombreuses requêtes à la suite. FrankenPHP et RoadRunner le proposent, entre autres. Il supprime le coût de démarrage par requête, au prix de la garantie shared-nothing.
