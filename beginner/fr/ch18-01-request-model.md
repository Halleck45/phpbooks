# Le modèle de requête PHP : pourquoi PHP est (presque toujours) monothread

Un serveur Node.js ou Java démarre une fois et reste debout. Il traite toutes les requêtes qui arrivent tant qu'il est en vie, et sa mémoire persiste de l'une à l'autre. Une variable posée en servant un utilisateur peut, si vous n'y prenez pas garde, être encore là quand le suivant se présente.

PHP, dans sa forme classique et toujours la plus répandue, ne fonctionne pas ainsi. **Chaque requête HTTP repart de zéro.** Le processus PHP (ou le thread, selon la configuration de votre serveur web) charge votre script, l'exécute depuis le haut, envoie une réponse, puis jette tout. Chaque variable, chaque objet, chaque propriété statique : disparus. La requête suivante repart d'une page blanche. Rien ne survit, sauf ce que vous avez volontairement rangé en dehors de PHP : une base de données, un fichier, un cache comme Redis ou Memcached.

<img src="images/ch18-always-on-vs-fresh-start.png" alt="À gauche, un serveur toujours allumé dont le bureau accumule les notes d'un visiteur à l'autre ; à droite, une requête PHP à un bureau nettoyé avant chaque visiteur" width="600">

On appelle cela une architecture **shared-nothing** (« rien de partagé »), et c'est la plus grande différence de structure entre PHP et les langages bâtis autour d'un processus serveur qui tourne en continu. Vous l'avez déjà vue en miniature au [chapitre 1](ch01-02-hello-world.md) : `php hello.php` lance l'interpréteur, exécute le script de haut en bas, et s'arrête. La production, c'est le même cycle derrière un serveur web. Avec PHP-FPM (le FastCGI Process Manager, la façon standard de faire tourner PHP derrière nginx ou Apache), un groupe de processus PHP attend, prêt à servir, et chaque requête entrante est confiée à l'un d'eux pour exactement le temps qu'il faut pour produire la réponse.

> Une requête PHP naît, travaille, répond, et oublie. La suivante repart propre.

## Pourquoi les threads sont devenus inutiles

Les threads existent pour qu'un même programme fasse plusieurs choses à la fois, en partageant sa mémoire. Mais si votre programme ne traite jamais qu'une requête du début à la fin avant de disparaître, il n'y a presque rien à faire tourner en parallèle *à l'intérieur*. **La concurrence dont une application PHP a besoin, des milliers d'utilisateurs en même temps, se gère un étage au-dessus**, en faisant tourner beaucoup de processus PHP côte à côte, pas en apprenant à un seul processus à jongler. Pensez à un bureau de poste : plutôt qu'un guichetier très rapide qui servirait dix clients à la fois, dix guichets servent chacun un client. Ce sont votre serveur web et votre gestionnaire de processus qui ouvrent les guichets, et ils font déjà le plus dur.

<img src="images/ch18-worker-pool.png" alt="Un bureau de poste avec une rangée de guichets, chacun tenu par un éléphant PHP servant un seul visiteur, les nouveaux arrivants étant dirigés vers le prochain guichet libre par PHP-FPM" width="600">

L'avantage pratique est considérable. Vous ne raisonnez jamais sur des accès concurrents (race conditions) à l'intérieur d'une requête, comme vous le feriez dans une servlet Java multithread. Deux utilisateurs ne peuvent pas corrompre mutuellement leurs données de `$_SESSION` en écrivant au même moment dans la même variable, parce qu'il n'y a pas de variable commune : chacun a sa propre exécution. **Des catégories entières de bugs qui empoisonnent les serveurs à mémoire partagée ne peuvent tout simplement pas se produire en PHP classique.** Le modèle les exclut dès le départ, au lieu de vous demander de les éviter à force de discipline.

## Là où ça cesse d'être toute l'histoire

PHP *peut* partager de l'état et exécuter des choses en parallèle. Par défaut, il ne le fait pas, et les applications PHP traditionnelles ont été conçues avec cette contrainte plutôt que contre elle. Trois exceptions méritent d'être connues.

Le travail qui doit se faire mais ne doit pas retarder la réponse, envoyer un e-mail, redimensionner une image reçue, est confié à un processus séparé plutôt qu'exécuté dans la requête. La [section suivante](ch18-02-queues-and-processes.md) parle exactement de cela.

Les processus PHP de longue durée existent bel et bien. Les démons en ligne de commande, les workers de file d'attente et des outils plus récents comme les serveurs Swoole gardent un même processus en vie pendant de nombreuses unités de travail, et *là*, la garantie du shared-nothing ne s'applique plus automatiquement. Elle redevient votre affaire.

Opcache, le cache de bytecode de PHP, partage bien le code compilé entre les requêtes pour gagner du temps. Mais c'est du code compilé, pas l'état de votre application : vos variables, elles, meurent toujours avec la requête.

**Dès qu'un processus PHP survit à une requête, la garantie de la page blanche disparaît, et vous voilà à réfléchir à l'état partagé comme tout le monde.** Comment les applications PHP font-elles leur travail « en parallèle » en pratique, sans un seul thread ? C'est la prochaine étape.
