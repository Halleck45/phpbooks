# Énumérations et filtrage par motif

Une commande est en attente, expédiée ou annulée. Jamais autre chose. Une carte à jouer appartient à l'une des quatre couleurs, point. Un feu tricolore est rouge, orange ou vert. Les programmes regorgent de valeurs de ce genre, et PHP a longtemps manqué d'un moyen propre de le dire.

Avant PHP 8.1, on prenait une chaîne de caractères, `'shipped'`, ou une constante entière, et on croisait les doigts. Rien n'empêchait un collègue d'écrire `'shiped'` quelque part. Rien ne disait, à un endroit unique, quelle était la liste complète des valeurs permises. La règle vivait dans votre tête, et les têtes oublient.

<img src="images/ch06-fixed-set.png" alt="Un champ de texte libre où quelqu'un a écrit shiped avec une faute, à côté d'un bouton rotatif qui ne peut pointer que sur l'une de trois positions gravées : pending, shipped, cancelled" width="560">

**Une énumération transforme cette liste en un vrai type, vérifié par le moteur, qui ne peut contenir qu'un des cas que vous avez déclarés.** C'est la différence entre un champ de texte où chacun tape ce qu'il veut et un bouton à trois positions gravées dans le métal.

Vous avez croisé `match` au passage au [chapitre 3](ch03-05-control-flow.md), pour jauger un code de statut HTTP, et les classes donnent forme à vos données depuis le [chapitre 5](ch05-00-classes.md). Les énumérations se logent exactement entre les deux : elles ressemblent à une petite classe, et `match` a été conçu pour les lire. Le chapitre se termine sur l'opérateur nullsafe, `?->`, un cousin de la même famille. Il traite un ensemble d'exactement deux possibilités, quelque chose ou rien, sans un `if` défensif devant chaque accès.
