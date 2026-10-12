# Livrer des comptes utilisateurs

Inscription, connexion, « mot de passe oublié », et savoir qui regarde l'écran en ce moment : presque toute application en a besoin, et presque aucune ne devrait l'écrire à partir de zéro. **Le hachage des mots de passe, les sessions et la douzaine de petits détails de sécurité qui les entourent sont du code que vous voulez hériter d'un paquet bien entretenu**, pas réinventer sous pression. Attaques temporelles, fixation de session, limitation de débit : tout cela a été résolu avant que vous ne commenciez.

<img src="images/ch04-front-desk.png" alt="Un comptoir d'accueil où un petit éléphant coiffé d'une casquette contrôle le badge de la première personne d'une courte file. Derrière le comptoir, un tableau de clés et une porte marquée d'un cadenas" width="560">

- [Laravel : Breeze, Fortify et Jetstream](ch04-01-laravel-breeze-fortify.md) : trois kits de démarrage officiels, des « seules vues » jusqu'au squelette complet d'un SaaS avec équipes.
- [Symfony : le Security Bundle](ch04-02-symfony-security-bundle.md) : authentification et autorisation pilotées par la configuration.
- [WordPress : rôles, capacités et mots de passe d'application](ch04-03-wordpress-roles-capabilities.md) : ce que le cœur de WordPress livre déjà, et quand cela suffit.
