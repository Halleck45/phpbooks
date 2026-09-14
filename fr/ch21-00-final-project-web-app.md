# Projet final : construire une petite application web

Vous avez toutes les pièces. Classes et promotion de constructeur, espaces de noms et Composer, tableaux et collections, exceptions, interfaces : les chapitres précédents vous ont donné le vocabulaire courant du PHP moderne, un mot à la fois. **Ce chapitre assemble ces pièces en une seule chose, petite et cohérente : une application web construite avec rien d'autre que PHP.**

Pas de framework, et c'est voulu. Vous utiliserez sans doute Laravel ou Symfony au travail, et vous aurez raison. Mais s'en servir avant d'avoir construit quelque chose sans, c'est accepter leurs facilités sur parole. Routeur, contrôleur, vue : ce ne sont que des noms posés sur des motifs qui apparaissent d'eux-mêmes dès qu'on résout les petits problèmes que toute application web rencontre. Construisez-les une fois à la main, à cette échelle, et tout ce qu'un framework fera ensuite se lira comme « ah, c'est le truc que je connais déjà » plutôt que comme de la magie.

La construction se fait en trois temps. D'abord le plus petit routeur possible : un seul fichier, le serveur de développement fourni avec PHP, et quelques `if` qui décident quoi renvoyer. Ensuite ce fichier grandit jusqu'à prendre une forme MVC, avec de vraies classes de contrôleurs et le plus vieux talent de PHP, le templating, enfin utilisé comme il faut. Pour finir, un regard sur la façon dont la vie d'une requête se termine vraiment, et sur la manière d'exécuter du code de nettoyage à cet instant précis, ce qui ramène au modèle de requête du [chapitre 18](ch18-01-request-model.md).

Bien moins de deux cents lignes au total. Ce que vous en garderez dépasse le code : une image nette de ce qui se passe sous les frameworks que vous prendrez en main ensuite.
