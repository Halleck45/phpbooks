# PHP orienté objet

Ouvrez un framework, une bibliothèque, presque n'importe quel fichier PHP écrit par quelqu'un d'autre, et vous y trouverez des classes bâties sur d'autres classes. Le chapitre 5 vous a appris à écrire une classe. Le chapitre 11 vous a appris à faire promettre la même chose à des classes sans lien, grâce aux interfaces. **Ce chapitre est celui où ces pièces deviennent une conception.**

Un seul exemple traverse tout le chapitre : une boutique qui accepte plusieurs moyens de paiement. Une carte bancaire et un compte PayPal font le même travail de deux façons différentes, et c'est précisément la situation pour laquelle la programmation orientée objet a été inventée. Vous ferez reposer une classe sur une autre avec `extends`, vous remplacerez ce qui doit changer en gardant le reste grâce à `parent::`, puis vous toucherez la récompense. Un code écrit une seule fois contre l'idée générale de « moyen de paiement » fonctionne avec chaque moyen concret que vous lui confiez, y compris ceux que vous n'avez pas encore écrits. Cette propriété porte un nom, le polymorphisme, et c'est la raison d'être de l'héritage.

Les classes abstraites et les interfaces sont ensuite posées côte à côte. Elles résolvent des problèmes qui se recouvrent, et choisir entre les deux est une décision de conception, pas une affaire de goût.

La seconde moitié du chapitre se tourne vers les méthodes magiques de PHP, une poignée de méthodes au nom particulier que le langage appelle de lui-même quand un objet est affiché, utilisé comme une chaîne de caractères, ou interrogé sur une propriété qu'il n'a pas. Certaines sont des outils de tous les jours. D'autres rendent le code plus difficile à lire que le code répétitif qu'elles économisent, et le chapitre dit lesquelles.

L'exemple des paiements finit assemblé en un design pattern classique, Strategy, avec pour seuls ingrédients les interfaces et le polymorphisme que vous aurez déjà en main. Les patterns ont une réputation d'abstraction. Voir l'un d'eux se construire à partir de pièces familières, pour résoudre un problème que vous rencontrez vraiment, devrait régler son compte à cette réputation.
