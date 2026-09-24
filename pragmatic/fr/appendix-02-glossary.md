# B - Glossaire de l'écosystème

Chaque terme est défini par ce qu'il fait pour vous, pas par sa définition formelle.

**Adaptateur**
Un petit morceau de code qui fait parler une chose (un stockage, un moteur de recherche) dans l'interface qu'attend votre application, pour qu'échanger le service en dessous n'oblige pas à réécrire l'application. Voir [League/Flysystem](ch02-06-league-flysystem-standalone.md).

**Attribut**
Une métadonnée écrite juste au-dessus d'une classe ou d'une méthode PHP (`#[ApiResource]`, `#[IsGranted('ROLE_ADMIN')]`), qu'un framework lit à l'exécution pour décider comment la traiter. Il remplace ce qui demandait autrefois des fichiers de configuration séparés.

**Bundle**
Le mot de Symfony pour un paquet installable qui ajoute une fonctionnalité à une application : le Security Bundle, l'AI Bundle. En gros, un paquet Laravel ou une extension WordPress.

**Façade**
Une convention Laravel : un appel court, d'apparence statique (`Storage::get(...)`), adossé à un vrai objet interchangeable en dessous. Vous gagnez une syntaxe mémorisable sans perdre la souplesse de l'injection de dépendances.

**Fiber**
Une fonctionnalité de PHP 8.1 qui permet à un seul processus de suspendre et de reprendre son exécution à volonté, en gardant de nombreuses choses en vol à la fois sans un thread par tâche. C'est ce qui rend possible [le serveur WebSocket de Reverb](ch07-01-laravel-reverb-livewire.md).

**Hook / Filtre**
Le mécanisme d'extension de WordPress : un point nommé dans le code de base où une extension exécute sa propre fonction (`add_action`) ou modifie une valeur au passage (`add_filter`), sans toucher à WordPress lui-même.

**Migration**
Un changement de schéma de base de données, incrémental et versionné, écrit en code plutôt qu'appliqué à la main. Chaque développeur et chaque environnement aboutit à la même structure en exécutant les mêmes fichiers de migration.

**ORM (Object-Relational Mapper)**
La couche qui transforme les lignes de la base en objets PHP et inversement (Eloquent chez Laravel, Doctrine chez Symfony), pour que le code de tous les jours s'écrive `$product->price` au lieu de SQL à la main.

**Provider (Service Provider / conteneur de services)**
La partie d'un framework qui construit les objets et les remet à qui en a besoin. Une classe déclare « il me faut un logger » dans son constructeur et ne saura jamais comment ce logger a été construit ni configuré.

**PSR**
Une PHP Standards Recommendation : une interface convenue (PSR-3 pour les logs, PSR-7 pour les messages HTTP) qui permet à des paquets d'éditeurs différents de fonctionner ensemble sans connaître leurs entrailles respectives.

**Ressource**
Dans une API, un type de chose que l'API expose (un `Product`, un `Order`) avec les opérations disponibles dessus. Laravel emploie aussi le mot, plus étroitement, pour la classe qui met un modèle en forme JSON.

**Webhook**
Un rappel. Au lieu que votre application demande sans arrêt à un service « il s'est passé quelque chose ? », le service envoie une requête HTTP à votre application dès que c'est le cas. C'est ainsi que [Stripe](ch09-03-laravel-cashier-stripe.md) prévient votre application qu'un paiement a abouti.

**Worker**
Un processus de longue durée qui prend les tâches dans une file d'attente et les exécute, à part du processus qui sert les requêtes web, pour qu'un travail lent ne bloque jamais un utilisateur qui attend une page. Voir [Livrer du travail en arrière-plan](ch11-00-shipping-background-work.md).
