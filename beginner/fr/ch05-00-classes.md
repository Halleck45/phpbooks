# Structurer des données avec des classes

Quelque part dans votre code, il y a un tableau `$product`. Ailleurs, une fonction `calculateTotal($product)`. Les deux ne fonctionnent ensemble que tant qu'ils sont d'accord sur les clés que contient le tableau, et rien dans PHP ne vérifie qu'ils le sont.

Vous regroupez des valeurs liées dans des tableaux depuis le [chapitre 3](ch03-00-common-programming-concepts.md) : les articles d'un panier, des prix indexés par nom. Ça marche, jusqu'au jour où ça ne marche plus. **Un tableau associatif n'a pas de forme fixe.** Rien ne vous empêche de mal orthographier une clé, rien ne dit quelles clés sont censées exister, et rien ne rattache aux données les opérations que vous faites dessus.

<img src="images/ch05-array-vs-class.png" alt="À gauche, un sac qui déverse des post-it avec des noms de clés, dont un mal orthographié ; à droite, un formulaire imprimé avec trois champs fixes et un outil totalPrice accroché dessous" width="600">

**Une classe donne une forme à une donnée** : des propriétés nommées et typées, qui existent toujours, avec les opérations qui ont un sens sur ces données rangées juste à côté, sous forme de méthodes. Pensez à la différence entre une pile de post-it et un formulaire imprimé. Le formulaire a des champs fixes, chaque exemplaire a les mêmes, et le mode d'emploi est imprimé sur le formulaire lui-même.

Vous avez déjà croisé les objets deux fois : en passant dans [Types de données](ch03-02-data-types.md), puis plus sérieusement au [chapitre 4](ch04-00-variables-and-references.md), où vous avez appris la chose la plus importante à leur sujet. Contrairement aux tableaux, les objets ne sont pas copiés quand on les affecte ou qu'on les passe à une fonction : toute variable qui en tient un tient une poignée vers la même instance. À partir d'ici, les objets cessent d'être un décor d'arrière-plan. C'est vous qui les construisez.

La mécanique d'abord : le mot-clé `class`, les propriétés typées, la visibilité, et `new`, qui fait naître une instance. Puis un petit exemple, mené du début à la fin, comme une classe apparaît dans du vrai code : non pas parce qu'un livre vous l'a dit, mais parce que la version à base de tableaux du même problème était devenue une dette. Les méthodes ferment le chapitre, avec `$this` et le raccourci moderne de PHP pour les constructeurs, qui fait disparaître une quantité surprenante du code répétitif dont le vieux PHP est plein.

> Un sac de tableaux tenus par une convention, ou une forme que le langage lui-même fait respecter. C'est le choix dont parle ce chapitre.
