# Au-delà de PHP : autres langages, autres technologies, et le moteur lui-même

## Parler à d'autres langages

Les vrais systèmes sont rarement écrits dans un seul langage, et **la façon courante de les mélanger n'est pas de les lier ensemble mais de les faire dialoguer par une API.** Chaque côté expose une interface neutre, en HTTP ou en gRPC, que n'importe quel langage peut appeler. Un backend PHP et un service écrit en Go ou en Rust se parlent ainsi à longueur de journée, sans qu'aucun des deux sache dans quoi l'autre est écrit.

Deux routes plus directes existent. FFI (Foreign Function Interface, depuis PHP 7.4) appelle directement une bibliothèque C compilée depuis PHP, sans écrire une extension complète. C'est étroit, utile quand ça s'applique, et bon à connaître. À l'autre bout de l'échelle d'effort, `proc_open()` du [chapitre 18](ch18-02-queues-and-processes.md) lance tout simplement un programme écrit dans autre chose et relit ce qu'il affiche.

## Parler à d'autres technologies

Le [chapitre 10](ch10-03-talking-to-a-database.md) a utilisé SQLite parce qu'il ne demandait aucun serveur à part. **La plupart du PHP en production parle plutôt à MySQL, MariaDB ou PostgreSQL**, par la même interface PDO et un DSN différent, chacun avec les particularités de son dialecte SQL, qu'il vaut mieux connaître.

La file d'attente du [chapitre 18](ch18-02-queues-and-processes.md) grandit en logiciel dédié, comme RabbitMQ ou Amazon SQS, pour le travail en arrière-plan qui doit survivre à un plantage ou se répartir sur plusieurs workers de manière fiable. Les moteurs de recherche (Elasticsearch, Meilisearch) prennent le relais le jour où une requête `LIKE '%...%'` ne suffit plus : la recherche plein texte et à facettes réclame une infrastructure faite pour cela. Les services cloud (le stockage d'objets comme S3 et ses nombreux équivalents compatibles, les bases de données gérées, les files gérées) sont en grande partie les mêmes idées, exploitées et dimensionnées par quelqu'un d'autre.

## Étendre le moteur lui-même

Les pilotes PDO et Xdebug que vous avez déjà utilisés sont des extensions PHP : du code écrit en C sur l'API du Zend Engine, installé via PECL. Zephir est un langage de plus haut niveau qui se compile en une vraie extension, pour les équipes qui veulent ce niveau de performance sans écrire du C brut à la main.

**Cette couche mérite d'être connue et mérite rarement d'être utilisée.** Presque tout ce dont une application a besoin se fait en PHP ordinaire, côté utilisateur. Écrire une extension, c'est une décision pour le jour où c'est PHP lui-même qui bloque, pas l'application posée dessus, et on se retrouve rarement là.
