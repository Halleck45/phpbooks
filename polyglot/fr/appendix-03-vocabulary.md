# C - Vocabulaire

Cette annexe définit, en une ou deux phrases chacun, les mots qui reviennent dans les conversations PHP et rarement ailleurs.

**SAPI.** Server API : la couche qui relie l'interpréteur à ce qui l'exécute. La ligne de commande, PHP-FPM, `mod_php` et les runtimes embarqués sont tous des SAPI au-dessus du même moteur.

**CLI.** La SAPI en ligne de commande, invoquée par `php file.php`. Elle n'a par défaut ni limite de temps d'exécution ni limite de mémoire, contrairement aux SAPI web.

**FPM.** FastCGI Process Manager : un pool de processus PHP qui attendent les requêtes derrière un serveur web. La façon standard de servir PHP.

**FastCGI.** Le protocole par lequel le serveur web transmet une requête à FPM et relit la réponse.

**mod_php.** Le module Apache qui embarque PHP dans le processus du serveur web lui-même. Plus ancien que FPM, et toujours présent.

**OPcache.** Le cache de bytecode. Les fichiers compilés restent en mémoire partagée, et la requête suivante s'épargne l'analyse. Activé dans toute installation sérieuse.

**JIT.** Compilation à la volée du code chaud en code machine, à l'intérieur d'OPcache, depuis 8.0. Aide les scripts gourmands en CPU ; change peu de chose pour le trafic web ordinaire.

**Preloading** (préchargement). Une option d'OPcache qui compile et lie un ensemble de fichiers une fois au démarrage du serveur, pour que chaque requête commence avec eux déjà chargés.

**APCu.** Un cache mémoire partagé entre les processus PHP d'une même machine. Pour les valeurs calculées une fois et lues souvent, quand un stockage externe serait disproportionné.

**Extension.** Un module C compilé qui ajoute des fonctions ou des classes à PHP : `pdo_mysql`, `intl`, `mbstring`, `xdebug`. `php -m` liste celles qui sont chargées.

**PECL.** Le dépôt historique des extensions non livrées avec PHP, avec son propre installeur.

**PIE.** L'installeur d'extensions plus récent, dans l'esprit de Composer, appelé à succéder au circuit PECL.

**ZTS et NTS.** Les builds thread-safe et non-thread-safe de l'interpréteur. NTS est le défaut et celui qu'utilise FPM ; ZTS existe pour les rares SAPI multithreadées et l'extension `parallel`.

**php.ini.** Le fichier de configuration. La CLI et FPM en lisent des différents, ce qui explique la plupart des mystères du type « ça marche dans le terminal ».

**Composer.** Le gestionnaire de paquets. Lit `composer.json`, écrit `composer.lock`, remplit `vendor/`, génère l'autoloader.

**Packagist.** Le registre public de paquets où Composer s'approvisionne.

**vendor.** Le dossier où Composer installe les paquets, qu'on ne modifie jamais à la main et qu'on ne commite pas.

**Autoload.** Le mécanisme qui charge le fichier d'une classe à sa première utilisation, si bien qu'on n'écrit plus jamais une ligne `require` à la main.

**PSR-4.** La correspondance standard entre espace de noms et dossier que suivent les autoloaders : `App\Billing\Invoice` vit dans `src/Billing/Invoice.php`.

**PHP-FIG.** Framework Interoperability Group : l'organisme qui publie les PSR et le style de code.

**PSR.** PHP Standards Recommendation : une interface ou une convention numérotée (PSR-3 pour les logs, PSR-7 pour les messages HTTP, PSR-15 pour les middlewares) sur laquelle les bibliothèques s'accordent afin d'être interchangeables.

**PER Coding Style.** Le standard de style de code actuel du FIG, successeur de PSR-12. Ce que les formateurs font respecter.

**RFC.** Request for Comments : la proposition publique par laquelle passe tout changement du langage avant un vote des développeurs du cœur.

**PHP Foundation.** L'organisation à but non lucratif qui, depuis 2021, salarie des développeurs du cœur pour maintenir et faire avancer l'interpréteur.

**php-src.** Le dépôt source de l'interpréteur lui-même, écrit en C.

**Zend Engine.** Le cœur de l'interpréteur : le compilateur et l'exécuteur. Le nom survit dans quelques réglages et messages d'erreur.

**Superglobal** (superglobale). Un tableau intégré au langage, visible dans toutes les portées : `$_GET`, `$_POST`, `$_SERVER`, `$_COOKIE`, `$_FILES`, `$_SESSION`, `$_ENV`.

**Docblock.** Un commentaire `/** ... */` au-dessus d'un symbole, portant des annotations `@param` et `@return` que lisent les éditeurs et les analyseurs statiques. C'est là que vivent les génériques.

**Attribute** (attribut). Des métadonnées structurées attachées à une classe, une méthode, une propriété ou un paramètre avec `#[...]`, lues par réflexion. Ce que les annotations étaient en Java.

**Trait.** Un bloc de méthodes et de propriétés copié dans toute classe qui le `use`. De la réutilisation horizontale sans héritage.

**Enum** (énumération). Un type avec un ensemble fixe de cas nommés, éventuellement adossés à un entier ou une chaîne, avec méthodes et interfaces. Depuis 8.1.

**Fiber.** Une coroutine à pile qui peut se suspendre et reprendre depuis n'importe quel point de sa pile d'appels. La primitive sur laquelle bâtissent les bibliothèques asynchrones ; pas quelque chose que le code applicatif pilote directement.

**Generator** (générateur). Une fonction qui produit des valeurs une à une avec `yield` et conserve son état entre les appels. De l'itération paresseuse sans construire de tableau.

**SPL.** Standard PHP Library : l'ensemble intégré de structures de données, d'itérateurs, d'exceptions et d'interfaces tels que `ArrayIterator`, `SplQueue`, `Countable`, `RuntimeException`.

**PDO.** PHP Data Objects : l'abstraction de base de données avec une seule API pour tous les pilotes, requêtes préparées comprises.

**mbstring.** L'extension de chaînes multi-octets. `mb_strlen`, `mb_substr` et leurs semblables comptent des caractères là où les fonctions ordinaires comptent des octets.

**intl.** L'extension d'internationalisation : collation, formatage des nombres et des dates, normalisation Unicode, au-dessus de la bibliothèque ICU.

**Xdebug.** Le débogueur pas à pas et profileur, réservé au développement.

**PHPUnit.** Le framework de test de style xUnit avec lequel la plupart des tests PHP sont écrits.

**Pest.** Un framework de test à la syntaxe describe et expect, qui tourne sur le moteur de PHPUnit.

**PHPStan.** Un analyseur statique qui trouve les erreurs de type et le code impossible sans l'exécuter, avec des niveaux de 0 à 10.

**Psalm.** L'autre analyseur statique, avec des niveaux de 8 à 1 et un accent sur la solidité des types et l'analyse de souillure (taint analysis).

**Rector.** Un outil de refactoring automatisé qui réécrit le code vers une version plus récente de PHP ou une API de bibliothèque plus récente.

**phpt.** Le format des fichiers de test de l'interpréteur lui-même, dans `php-src`. Vous le croisez si vous contribuez à PHP ou lisez ses rapports de bug.

**strict_types.** La déclaration par fichier `declare(strict_types=1);` qui fait lever une exception, au lieu de convertir, sur les incompatibilités de types scalaires dans les appels faits depuis ce fichier.

**Copy-on-write** (copie à l'écriture). L'astuce du moteur qui rend l'affectation de tableaux bon marché : la copie partage la mémoire de l'original jusqu'à ce que l'un des deux soit modifié.

**Late static binding** (liaison statique tardive). `static::` qui se résout vers la classe sur laquelle l'appel a été fait, pas celle où la méthode est écrite. `self::` est l'autre.

**Magic method** (méthode magique). Une méthode au nom réservé à double tiret bas que le moteur appelle de lui-même : `__construct`, `__toString`, `__get`, `__call`, `__clone`, `__invoke`.
