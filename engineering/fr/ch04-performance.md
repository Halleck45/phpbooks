# Performances

**La vitesse de PHP dépend entièrement de ce que vous mesurez : sur une requête web ordinaire, il est rapide, parce que la requête passe l'essentiel de son temps à attendre une base de données ou le réseau, pas à exécuter du PHP ; sur du calcul pur, il est plus rapide que Python et plus lent que les langages compilés ou dotés d'un JIT mûr, comme Go, Rust, Java et C#.** Les deux moitiés de cette phrase portent le raisonnement, et un benchmark qui ne vous en montre qu'une vous cache la moitié du tableau.

Dans la plupart des discussions sur la performance, le mot « rapide » recouvre trois choses qu'il faut séparer avant de regarder le moindre chiffre. Le débit, c'est le nombre de requêtes qu'un matériel donné sert par seconde, et c'est lui qui compte quand vous dimensionnez une infrastructure. La latence, c'est le temps que met une requête précise à obtenir sa réponse, et c'est elle que ressent l'utilisateur qui attend sa page. La vitesse de calcul brute, enfin, c'est le temps que prend un morceau d'arithmétique donné, et elle intéresse la tâche de fond qui fait du calcul numérique lourd. Avec le modèle de PHP, un processus par requête et rien de partagé, décrit dans [Le runtime](ch02-runtime.md), les deux premières dépendent surtout de la quantité d'entrées-sorties de la requête et du réglage de la couche qui sert l'application, pas de la vitesse arithmétique du langage. La troisième est le seul cas où le langage lui-même fait goulot. C'est elle qui demande le plus de soin dans ce chapitre, parce que c'est aussi celle qu'on mesure le plus souvent avec un micro-benchmark synthétique avant d'en tirer, en douce, une conclusion sur la performance web. Ce glissement, j'essaie de ne pas le commettre.

## Le benchmark que je ne peux pas utiliser

Le benchmark de référence pour comparer les frameworks web entre langages, TechEmpower Framework Benchmarks, a été arrêté le 24 mars 2026, et son dépôt GitHub est désormais archivé. Le dernier tour complet, le Round 23, publié le 17 mars 2025, couvrait plus de 330 implémentations de frameworks dans de nombreux langages. Je préfère vous donner la date de cet arrêt que citer un tour périmé comme s'il était encore d'actualité : si vous cherchez un tour plus récent, vous ne trouverez que l'avis d'archivage, et mieux vaut expliquer ce trou que faire comme s'il n'existait pas. C'est aussi pour cela que ce chapitre s'appuie davantage sur deux autres sources : un benchmark livré avec la proposition qui a introduit le JIT de PHP, et une suite de benchmarks multilangages maintenue de façon indépendante et toujours active.

## Ce que le JIT vous apporte vraiment sur une requête web

[Le runtime](ch02-runtime.md) a déjà présenté le compilateur à la volée (JIT) de PHP, et l'aveu de sa propre RFC : il aide bien plus le code de calcul que le code web ordinaire. Ce même benchmark est la preuve de performance la plus nette de tout ce guide, justement parce qu'il vient des personnes qui ont construit la fonctionnalité et qui avaient tout intérêt à la montrer sous son meilleur jour.

<div class="chart">

{{#include charts/ch04-jit.svg}}

</div>

Sur une requête WordPress, on mesure trois cent vingt-six requêtes par seconde avec le JIT, trois cent quinze sans. L'écart est d'environ 3 %, sur une vraie application, d'après la RFC qui a introduit la fonctionnalité. La raison tient à l'architecture, pas à un mauvais réglage : une requête WordPress passe la plupart de son temps en requêtes SQL et en entrées-sorties, pas dans le calcul numérique que le JIT accélère. Si votre grille d'évaluation contient la question « activer le JIT rendra-t-il mon application web nettement plus rapide ? », la réponse honnête, tirée des propres chiffres de PHP, est : en général, pas beaucoup. Un benchmark qui affirme le contraire sur une charge web mérite qu'on regarde de près ce qu'il a réellement mesuré.

Le JIT n'est pas inutile pour autant. Il vise simplement une cible plus étroite que « PHP » en général. Un script en ligne de commande qui traite des images dans une boucle serrée, un worker qui fait tourner une simulation numérique, un consommateur de file qui transforme massivement des chaînes ou des tableaux sans appel réseau au milieu : voilà les charges où le compilateur montre ses gains, parce qu'elles sont limitées par le CPU, ce que n'est pas une requête WordPress. Pour décider d'activer ou non le JIT, demandez-vous quelle part de votre charge réelle calcule et quelle part attend, plutôt que de vous demander si le JIT existe.

## La comparaison que PHP perd d'ordinaire sur le mauvais axe

La critique la plus courante compare PHP à Python et le déclare lent. Le Computer Language Benchmarks Game, une suite multilangages maintenue de façon indépendante et mise à jour régulièrement, raconte autre chose sur les tâches de calcul. Dans ses tests de PHP 8.4.1 face à Python 3.13, sur des tâches comme fannkuch-redux, n-body et spectral-norm, trois benchmarks classiques de calcul pur sans entrées-sorties derrière lesquelles se cacher, PHP est **plus rapide que Python sur la plupart d'entre elles, d'un facteur d'environ une fois et demie à deux**.

| Tâche | Ce qu'elle sollicite | Langage le plus rapide |
|---|---|---|
| fannkuch-redux | Génération de permutations, boucles serrées | PHP |
| n-body | Arithmétique flottante, simulation | PHP |
| spectral-norm | Calcul matriciel et vectoriel | PHP |

Ce résultat change la façon de formuler la limite, et pas seulement le chiffre. **« PHP est lent » n'est pas vrai par rapport à Python ; c'est vrai par rapport aux langages compilés et à ceux dont le JIT est mûr.** Une comparaison qui s'arrête à Python et tient le résultat pour acquis compare PHP à la mauvaise catégorie, et si vous relancez ce benchmark vous-même dans le cadre d'un audit, vous retrouverez le classement imprimé ici. C'est aussi le résultat qui a le plus de chances de vous surprendre si vous arrivez avec la réputation décrite dans [La réputation](ch01-introduction.md) en tête : un langage dont on garde le souvenir d'une lenteur bat l'un des langages les plus associés au travail sur les données et aux scripts, sur l'axe précis où l'on mesure les deux.

<img src="images/ch04-performance.png" alt="Une piste à deux couloirs : en haut, un lièvre mène, un éléphant court deuxième et une tortue ferme la marche ; en bas, les trois mêmes coureurs font la queue à un guichet pendant qu'un employé fouille des classeurs. Une personne avec un chronomètre regarde tour à tour les deux couloirs." width="560">

> **La limite.** Sur un débit de calcul soutenu, PHP reste derrière les langages compilés et ceux dont le JIT est mûr, Go, Rust, Java et C#, et je n'ai pas de coefficient unique, propre et tiré d'une source primaire pour chiffrer cet écart comme je peux le faire pour Python. C'est une vraie limite des données disponibles, pas une façon de dire que l'écart est faible : une charge réellement limitée par le CPU, qui fait du calcul numérique lourd avec peu d'entrées-sorties pour masquer ce temps, est une charge pour laquelle PHP n'est pas, par construction, l'outil le plus rapide. [Là où PHP est le mauvais choix](ch09-wrong-choice.md) traite ce cas de front.

**À vérifier vous-même.** Le Computer Language Benchmarks Game publie l'intégralité de ses résultats à jour sur son propre site, et sa page de méthodologie précise le matériel et la version de chaque langage utilisés. Relancez une tâche qui ressemble à votre propre charge plutôt que de croire le tableau récapitulatif. Si vous voulez voir le débit de PHP sur des requêtes sans faire confiance à l'un ou l'autre benchmark, le test le plus honnête est celui que décrit [L'évaluation](ch10-the-evaluation.md) : faites tourner une charge représentative de la vôtre sur votre propre version de PHP, avec opcache et le JIT dans l'état où vous les déploieriez vraiment.

La vitesse brute sur une seule machine n'est qu'une partie de la question de capacité. En production, ce qui compte le plus est en général ce qui se passe quand la charge grandit et que vous ajoutez des machines, et c'est là que reprend [Montée en charge](ch05-scale.md).
