# Livrer sans framework : les composants autonomes

Un script d'import ponctuel n'a pas besoin de Laravel. Une tâche cron qui interroge trois API et rédige un rapport n'a pas besoin de Symfony. **Parfois, le moyen le plus rapide de livrer, c'est un seul `composer require` pour la bibliothèque faite pour ce travail, et quarante lignes autour.**

<img src="images/ch02-single-tool.png" alt="Un atelier où une grosse machine dort sous une housse. Un petit éléphant décroche une seule clé à molette d'un panneau d'outils et la tend à une personne installée à un petit établi où attend une pièce unique" width="560">

Chaque paquet de ce chapitre tient debout tout seul : aucun framework dessous, rien à configurer au-delà de la seule chose qu'il fait. Plusieurs sont aussi les moteurs qui tournent à l'intérieur des frameworks des chapitres suivants. Une fois que vous les avez utilisés seuls, les encadrés « Sous le capot » de la suite du livre n'ont plus grand-chose à vous apprendre.

- [Outils en ligne de commande : Symfony/Console](ch02-01-symfony-console-standalone.md)
- [Parler à d'autres API : Guzzle](ch02-02-guzzle-http-client.md)
- [Des templates sans framework : League/Plates](ch02-03-league-plates-standalone.md)
- [Des logs qui marchent tout de suite : Monolog](ch02-04-monolog-standalone.md)
- [Valider les entrées : Respect/Validation](ch02-05-respect-validation.md)
- [Stocker des fichiers sans adopter un framework : League/Flysystem](ch02-06-league-flysystem-standalone.md)
