# Livrer du temps réel

Une notification qui apparaît d'elle-même, un point de présence, un widget de chat, un chiffre de tableau de bord qui se met à jour seul : la page sait qu'il s'est passé quelque chose, et personne n'a rechargé. Le modèle requête-réponse de PHP ne garde pas naturellement une connexion ouverte pour pousser des mises à jour. **L'écosystème a comblé ce vide de plusieurs côtés, et la question est de savoir si vous faites tourner le serveur de push vous-même ou si vous confiez ce travail à quelqu'un d'autre.**

<img src="images/ch07-switchboard.png" alt="Un petit éléphant assis à un standard téléphonique branche un câble. Des fils courent jusqu'à quatre fenêtres où quatre personnes regardent des écrans qui s'allument tous au même instant, sans que personne ne les touche" width="560">

- [Laravel : Reverb et Livewire, sans écrire de JavaScript](ch07-01-laravel-reverb-livewire.md) associe un serveur WebSocket officiel et auto-hébergé à un modèle de composants réactifs.
- [Symfony : UX Turbo et Mercure](ch07-02-symfony-ux-turbo-mercure.md) s'appuie sur un protocole temps réel ouvert plutôt que sur un serveur maison.
- [Nextcloud Talk : le temps réel au sein d'une plateforme](ch07-03-nextcloud-talk.md), ou comment une grosse application PHP gère le chat et les appels à grande échelle.
- [Pusher ($) : des WebSockets gérés, sans serveur à faire tourner](ch07-04-pusher-managed-websockets.md) échange l'infrastructure contre un abonnement.
