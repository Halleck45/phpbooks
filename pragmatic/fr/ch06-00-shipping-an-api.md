# Livrer une API que d'autres équipes peuvent utiliser

« L'équipe mobile doit pouvoir lire nos données d'ici le prochain sprint. » Quelqu'un finit toujours par vouloir parler à vos données : une application mobile, le système d'un partenaire, un front construit par une autre équipe. Cela veut dire des endpoints, de la validation des requêtes, des réponses d'erreur cohérentes et une documentation qui ne se périme pas à la première modification du code. **Écrire tout cela à la main pour chaque ressource, c'est précisément le travail répétitif que l'outillage PHP existe pour supprimer.**

<img src="images/ch06-service-hatch.png" alt="Un guichet percé dans un mur. Derrière, un petit éléphant devant des étagères de boîtes étiquetées tend un colis. Dans la file d'attente, un smartphone, un ordinateur portable et un petit robot. Un panneau avec une liste d'icônes est punaisé à côté du guichet" width="560">

La décision porte sur ce que vous voulez voir généré pour vous, et ce que vous préférez garder explicite.

- [API Platform : une API complète à partir d'une classe PHP](ch06-01-api-platform-from-one-class.md) génère REST, GraphQL et la documentation OpenAPI depuis une seule classe annotée.
- [Laravel : Sanctum, Resources et versions d'API](ch06-02-laravel-sanctum-resources.md), l'approche plus légère, plus manuelle et plus répandue.
- [WordPress : l'API REST intégrée](ch06-03-wordpress-rest-api.md), ce qu'un site WordPress expose déjà avant que vous n'installiez quoi que ce soit.
