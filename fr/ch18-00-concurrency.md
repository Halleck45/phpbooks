# La concurrence en PHP : un bref tour d'horizon

Vous pouvez sauter ce chapitre, y revenir dans un an, et n'avoir rien perdu.

C'est une phrase inhabituelle dans un livre de programmation, alors voici pourquoi elle est vraie. La plupart des développeurs PHP écrivent pendant des années du code de production, du vrai code qui sert un vrai trafic, sans jamais toucher un thread, une fibre ou un fork de processus. Ce n'est pas une lacune. **PHP a été conçu pour que les applications ordinaires n'aient jamais à gérer la concurrence elles-mêmes**, et pour l'immense majorité du travail en PHP, du site d'une petite entreprise à une grande boutique en ligne, c'est toujours la bonne façon de faire.

Ce chapitre est donc différent des autres. Partout ailleurs, le livre vous dit « vous vous en servirez tout le temps, apprenez-le bien ». Ici, c'est l'inverse : une courte visite, facultative. Rien de ce qu'elle contient n'est nécessaire pour écrire du PHP au quotidien.

Pourquoi l'inclure, alors ? Parce que tôt ou tard, deux questions arrivent. Pourquoi PHP n'a-t-il pas de threads comme Java ou C# ? Et comment envoyer un e-mail de bienvenue sans faire attendre l'utilisateur ? Les deux questions ont la même réponse, et il faut deux courtes sections pour la donner : d'abord [le modèle de requête](ch18-01-request-model.md), qui a rendu la concurrence explicite largement inutile en PHP, puis [les files d'attente et les processus en arrière-plan](ch18-02-queues-and-processes.md), les outils de tous les jours vers lesquels se tournent les développeurs PHP quand un travail doit se faire en dehors de la requête.

> Rien ici n'est obligatoire. Lisez-le par curiosité, ou gardez-le pour le jour où vous en aurez besoin.

Dans les deux cas, vous en sortirez en sachant pourquoi PHP se comporte ainsi, quelles sont vos options quand le modèle de requête ne suffit plus, et quoi chercher le jour où il vous faudra davantage.
