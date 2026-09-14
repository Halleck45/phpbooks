# Pour aller plus loin

Le livre s'arrête ici, mais le langage continue d'évoluer, et le projet qu'on vous a confié aussi. **Quelques sources vous permettent de rester à jour, et aucune n'appartient à un éditeur commercial.**

## Le manuel

[php.net](https://www.php.net/) est la référence, et une bonne référence : chaque fonction a sa page, avec sa signature, son historique par version, et des exemples qui tournent. Les notes contribuées par les utilisateurs sous chaque page sont inégales, alors que le texte officiel au-dessus est fiable. Mettez en favori les guides de migration, un par version ([php.net/manual/fr/migration85.php](https://www.php.net/manual/fr/migration85.php) et ses voisins) : ils listent chaque dépréciation et chaque nouveauté, et lire celui de la prochaine version de votre projet est la préparation de montée de version la moins chère que vous ferez.

## Le wiki des RFC

Chaque changement du langage passe par une proposition publique, une discussion sur la liste de diffusion internals, et un vote des développeurs du cœur. Les propositions vivent sur [wiki.php.net/rfc](https://wiki.php.net/rfc), acceptées, refusées et en cours. **Lire les RFC acceptées d'une version vous dit non seulement ce qui a changé, mais pourquoi**, avec les alternatives écartées et les arguments contre. Quand une fonctionnalité paraît étrange, sa RFC explique en général la contrainte qui l'a rendue ainsi.

## La Fondation et le FIG

La [PHP Foundation](https://thephp.foundation/) finance les développeurs du cœur qui maintiennent l'interpréteur et accompagne la direction du langage. Son blog rend compte des versions et des chantiers en cours. Le [PHP-FIG](https://www.php-fig.org/) (Framework Interoperability Group) publie les PSR et le PER Coding Style, les interfaces et conventions qui permettent à des bibliothèques d'auteurs différents de fonctionner ensemble. Quand une base de code mentionne PSR-quelque chose, le site du FIG a la spécification en deux pages.

## Le framework de votre projet

La plupart des projets PHP reposent sur un framework, et la documentation du framework est l'endroit où l'apprendre. Frameworks complets : CakePHP, Laminas, Laravel, Symfony, Yii. Micro-frameworks bâtis autour des middlewares PSR-15 : Mezzio, Slim. Plateformes de contenu avec leurs propres conventions : Drupal, Joomla, TYPO3, WordPress.

Une habitude paie dès le premier jour : **quand vous lisez du code de framework, triez ce que vous voyez entre ce qui relève du langage et ce qui relève du framework.** Un constructeur promu `readonly`, une énumération dans un `match` ou une chaîne de `?->` sont du PHP, et ils veulent dire la même chose partout. Une façade, une liaison dans un conteneur de services ou un `__call` magique qui redirige vers un constructeur de requêtes appartiennent au framework, et c'est sa documentation qui les explique. Ceux qui confondent les deux finissent par croire que PHP est ce à quoi leur premier framework l'a fait ressembler.

## Un chemin plus long

Ce livre a sauté les bases volontairement. Si vous voulez la version qui part de zéro, avec un petit jeu, un outil en ligne de commande et une application web construite sans framework, le volume compagnon, [*The PHP Book*](https://thephpbook.readthedocs.io/), prend ce chemin à un rythme plus lent, et il est publié depuis le même dépôt que celui-ci.

Au-delà de l'écrit, PHP a des groupes d'utilisateurs dans la plupart des grandes villes et des conférences sur la plupart des continents, et une salle pleine de gens qui ont déjà résolu le problème que vous allez rencontrer vaut largement l'après-midi qu'on y passe.

## Ce que vous savez maintenant

Il y a deux ou trois heures, vous avez ouvert une base de code et vu des `$this->`, des `::` et un modèle d'exécution que vous ne reconnaissiez pas. **Vous savez maintenant comment PHP s'exécute, comment il type, comment il organise le code en paquets, et où il va vous surprendre**, et l'ancienne réputation du langage a retrouvé sa place, dans le chapitre consacré au passé. Cette base de code est devenue lisible, et vous pouvez retourner la lire.
