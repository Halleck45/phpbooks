# Déboguer du PHP

Tôt ou tard, un de vos programmes s'exécutera sans la moindre erreur et donnera quand même une mauvaise réponse. Pas d'exception, pas d'avertissement, juste un total décalé de un ou une page qui salue la mauvaise personne. Relire le code aide rarement, parce que le code dit exactement ce que vous vouliez dire. **Déboguer, c'est découvrir ce que le programme fait vraiment, par opposition à ce que vous vouliez qu'il fasse.** C'est une compétence à part entière, qui mérite d'être apprise exprès.

Jusqu'ici, chaque programme de ce livre était assez court pour se lire de haut en bas et repérer le bug à l'œil nu. Le jeu de devinette et le livre d'or ont déjà dépassé ce stade.

Il existe deux façons de regarder à l'intérieur d'un programme qui tourne, et vous aurez besoin des deux.

<img src="images/ch13-two-ways.png" alt="Deux façons de déboguer : à gauche, une lampe torche éclaire un point dans un couloir de code sombre ; à droite, un bouton pause fige le programme en pleine course pour lire toutes ses variables" width="600">

La première est le **débogage par affichage**, la plus vieille astuce du métier. Vous glissez au milieu de votre code quelque chose qui vous montre une valeur, vous relancez le programme, vous lisez la sortie. C'est une lampe torche : vous voyez le seul endroit où vous la pointez. Il ne faut rien d'autre que PHP, et `var_dump()` et `print_r()` sont les outils du genre.

La seconde est le **débogage pas à pas**. Vous mettez le programme en pause sur une ligne précise, vous regardez chaque variable telle qu'elle était à cet instant, et vous avancez une ligne à la fois. Un bouton pause plutôt qu'une lampe torche : plus besoin de deviner où regarder. Il faut un outil, **Xdebug**, et quelques minutes d'installation, remboursées dès le premier bug qui ne vous laisse aucune valeur évidente à afficher.

Aucune des deux ne remplace la gestion des erreurs du [chapitre 9](ch09-00-error-handling.md). Une exception bien placée vous dit *que* quelque chose a mal tourné. Le débogage sert à découvrir *pourquoi*, surtout quand rien n'a été levé et que le programme a simplement produit, sans bruit, une mauvaise réponse. L'outil en ligne de commande du [chapitre 14](ch14-00-a-cli-project.md) est exactement le genre de programme en plusieurs fichiers où les deux outils gagnent leur place.
