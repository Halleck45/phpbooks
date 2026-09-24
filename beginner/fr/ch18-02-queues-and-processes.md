# Le travail en arrière-plan : files d'attente et processus

Une requête arrive, PHP la traite, et le processus disparaît une fois la réponse envoyée. Très bien pour « retrouve cet utilisateur et affiche son profil ». Beaucoup moins pour « redimensionne cette photo, fabrique trois miniatures et envoie un e-mail de confirmation ». Personne ne veut regarder une roue tourner pendant huit secondes parce que votre code traite des images avant de pouvoir dire « Upload successful ».

L'utilisateur n'a pas besoin d'attendre ce travail. Il a seulement besoin de savoir qu'il a été pris en compte. **La réponse standard en PHP tient en une ligne : ne le faites pas maintenant. Faites-le plus tard, dans un autre processus.**

## Les files d'attente de tâches

Pensez à un pressing. Vous déposez le manteau, on vous donne un ticket, vous repartez. Le nettoyage se fait dans l'arrière-boutique, une fois que vous êtes parti, et vous n'êtes pas planté au comptoir à regarder.

Une file d'attente de tâches (job queue), c'est ce comptoir. **Au lieu de faire le travail lent dans la requête, le code qui la traite note ce qu'il y a à faire, « redimensionner l'image #482 pour l'utilisateur #17 », sous la forme d'un petit message, et pousse ce message dans une file.** Puis il répond tout de suite à l'utilisateur : « Upload received, processing ». Pendant ce temps, un ou plusieurs processus PHP séparés, appelés **workers**, tournent en boucle en surveillant la file. Dès qu'un message apparaît, un worker le prend et fait le vrai travail, sans plus aucun lien avec la requête d'origine.

<img src="images/ch18-job-queue.png" alt="Un comptoir de pressing : la requête remet un ticket au visiteur et dépose l'enveloppe de la tâche sur un tapis roulant marqué queue, qui l'emporte vers les workers de l'arrière-boutique" width="600">

La file elle-même repose en général sur un outil fait pour ça. Redis est un choix courant et léger ; RabbitMQ et Amazon SQS apparaissent dans les systèmes plus gros. Des frameworks comme Laravel et Symfony fournissent des abstractions de file par-dessus, pour que vous n'ayez pas à bricoler la tuyauterie. L'idée est pourtant assez simple pour que vous puissiez en construire une version rudimentaire vous-même, avec rien de plus qu'une table en base de données et un `SELECT ... WHERE processed = false`.

Les workers sont du PHP ordinaire, lancé en ligne de commande, en général maintenu en vie par un superviseur de processus :

```console
$ php worker.php
Waiting for jobs...
Processing job: resize-image #482
Done.
Waiting for jobs...
```

Ce script de worker boucle sans fin : regarder la file, traiter ce qui s'y trouve, recommencer. **C'est un processus PHP de longue durée, exactement le genre de chose qui sort du modèle shared-nothing** de la [section précédente](ch18-01-request-model.md). Il garde un état d'une tâche à l'autre, une connexion à la base, peut-être une configuration en cache, comme un serveur Node.js le fait d'une requête à l'autre.

> La requête donne le ticket. Le worker fait le nettoyage. Personne n'attend au comptoir.

La prochaine fois que vous envoyez une photo sur un gros site, observez : la page dit « reçu » presque instantanément, et les miniatures apparaissent quelques secondes plus tard. C'est une file d'attente au travail.

## Lancer un processus séparé directement

Les files d'attente sont le bon outil quand beaucoup de petites unités de travail arrivent au fil du temps. Parfois, vous voulez plus simple : lancer cet autre programme tout de suite, et soit ne pas l'attendre, soit le laisser tourner pendant que vous faites autre chose. Pour cela, **PHP peut lancer directement des processus du système d'exploitation.**

`proc_open()` est l'outil généraliste. Il démarre une commande externe (qui peut très bien être un autre script PHP) et vous donne des poignées sur son entrée, sa sortie et son flux d'erreur, pour dialoguer avec elle pendant qu'elle tourne. Composer s'en sert pour sa propre gestion des processus.

Il y a aussi l'extension `pcntl`, qui permet à un script PHP de se dupliquer en plusieurs copies avec `pcntl_fork()` : du PHP réellement parallèle, sous forme de processus séparés, chacun avec sa propre mémoire. Honnêtement, c'est un peu rude. Le fork n'existe que sur les systèmes de type Unix, pas sous Windows, et raisonner juste sur plusieurs processus à la fois demande une vraie attention. On le croise dans les outils en ligne de commande et les démons bien plus que dans les applications web.

Les deux méritent d'être connus. **Aucun des deux n'est à choisir avant une file d'attente**, qui résout le même problème, « fais-le plus tard, pas maintenant », avec bien moins d'occasions de se tromper.
