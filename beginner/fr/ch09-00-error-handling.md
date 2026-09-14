# Gérer les erreurs

Un fichier manque. Un appel réseau ne répond plus. Quelqu'un passe une chaîne de caractères à une fonction qui attendait un nombre, et quelque part, une division tombe sur un zéro. **Aucun programme n'échappe aux ennuis ; ce qui distingue les langages, c'est ce qui se passe au moment où l'ennui arrive, et le mot que vous avez à dire dessus.** La réponse de PHP a beaucoup changé au fil des versions, et la réponse moderne vaut nettement mieux que sa réputation.

Le vieux PHP, et il en tourne encore beaucoup, échouait en silence. Un avertissement partait dans un journal que personne ne lisait, une fonction renvoyait `false` sans dire pourquoi, et le script continuait en boitant, avec des données à moitié construites, parce que rien ne l'avait arrêté. PHP 7 et 8 ont changé cela. La plupart des échecs produisent désormais un véritable objet que vous pouvez attraper et inspecter, et le langage trace une frontière nette entre deux sortes d'ennuis.

<img src="images/ch09-two-families.png" alt="Deux sortes d'ennuis côte à côte : un engrenage cassé étiqueté Error, le code est faux et doit être corrigé, et une route qui se sépare en deux étiquetée Exception, quelqu'un a une décision à prendre" width="560">

D'un côté, **quelque chose est cassé** : une méthode appelée sur `null`, un type qui ne correspond pas, une division par zéro. PHP lève une `Error`, et la seule réponse sensée est de corriger le code. De l'autre, **quelque chose demande une décision** : un fichier de configuration absent, un âge arrivé négatif, une API qui a refusé la requête. PHP, ou votre propre code, lève une exception, et quelqu'un, plus haut dans la pile d'appels, décide de la suite.

> Une `Error` dit « c'est cassé, corrigez ». Une exception dit « voilà un problème, décidez ».

Cette frontière traverse tout le chapitre. [Erreurs fatales et `Error`](ch09-01-fatal-errors.md) couvre la première sorte, et explique pourquoi il vaut mieux la laisser tranquille. [Les exceptions](ch09-02-exceptions.md) couvrent la seconde : `try`, `catch`, `finally`, lancer les vôtres, et la hiérarchie intégrée où se joue l'essentiel de votre gestion d'erreurs au quotidien. [Lancer ou ne pas lancer](ch09-03-to-throw-or-not-to-throw.md) parle de jugement : quand lancer, quand renvoyer `null` et laisser l'appelant décider, et quand la bonne réponse est de laisser le programme s'arrêter.

Rien de tout cela ne reste théorique. L'outil en ligne de commande du [chapitre 14](ch14-00-a-cli-project.md) s'appuie sur chacun de ces schémas, y compris une exception sur mesure écrite ici et retrouvée là-bas. La syntaxe s'apprend en un après-midi. L'instinct qui sépare « je gère » de « je laisse échouer » prend plus de temps, et il commence ici.
