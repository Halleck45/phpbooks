# Interfaces, traits et code de style générique

Une classe, c'est facile. Les ennuis commencent avec la deuxième.

Deux classes qui n'ont rien à voir l'une avec l'autre doivent quand même se mettre d'accord sur certaines choses. Votre ligne de facture et vos frais de port ont tous deux un résumé à afficher. Votre processeur de paiement et votre générateur de rapports veulent tous deux écrire une ligne dans un journal. **Comment des classes sans lien s'entendent-elles pour travailler ensemble, et comment partager une méthode entre elles sans la retaper cinq fois ?** PHP répond avec deux outils, et chacun règle une moitié opposée de la question.

Une interface est un contrat. Elle dit « toute classe qui se réclame de ce nom promet d'avoir ces méthodes », et ne dit rien du tout sur la façon dont ces méthodes sont écrites. Un trait, c'est l'inverse : un vrai morceau d'implémentation, copié dans toutes les classes qui le demandent, sans aucune promesse sur ce que sont ces classes ni sur leurs liens de parenté. **L'un est une forme dans laquelle vous acceptez de rentrer. L'autre est un bout de code que vous empruntez.** Les débutants les confondent, et bon nombre de développeurs aguerris venus d'autres langages aussi, d'où cette distinction posée aussi crûment, aussi tôt.

<img src="images/ch11-shape-vs-borrow.png" alt="À gauche, plusieurs objets différents passent tous par la même découpe, étiquetée interface. À droite, la même page de code est photocopiée et collée dans deux classeurs sans rapport, étiquetée trait" width="600">

Il y a un troisième sujet dans ce chapitre, et il demande un peu de franchise. PHP n'a pas de génériques. Vous ne pouvez pas écrire `Collection<Product>` et compter sur le langage pour refuser qu'une `Banana` s'y glisse. Ce que PHP a à la place, c'est une convention bien rodée, des docblocks lus par un outil d'analyse statique, qui vous offre l'essentiel de la même sécurité. La vérification est faite par un programme à part, que vous lancez avant de livrer, et non par PHP lui-même.

Les interfaces d'abord, parce que vous les utiliserez bien plus souvent que les deux autres.
