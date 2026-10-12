# Livrer du travail en arrière-plan

Envoyer l'e-mail de confirmation plus tard. Redimensionner l'image envoyée plus tard. Générer le rapport mensuel à deux heures du matin, sans personne devant l'écran. Tout ce qui ne doit pas bloquer la requête de l'utilisateur, ou qui tourne à heure fixe plutôt qu'en réponse à un clic, est du travail en arrière-plan. **Le faire proprement demande une file d'attente et un processus worker, pas un `sleep()` et un peu d'espoir.**

<img src="images/ch11-kitchen-rail.png" alt="Un restaurant vu en coupe. Au comptoir, un petit éléphant tend aussitôt un ticket à un client. Dans la cuisine derrière, un rail de bons de commande et deux éléphants en toque qui les traitent un par un" width="560">

- [Laravel : files d'attente et Horizon](ch11-01-laravel-queues-horizon.md) : des jobs dans une file, un worker pour les exécuter, un tableau de bord pour les surveiller.
- [Symfony : le composant Messenger](ch11-02-symfony-messenger.md) : un seul bus de messages pour les tâches de fond et pour le dialogue entre services.
- [WordPress : WP-Cron et l'Action Scheduler](ch11-03-wordpress-wp-cron-action-scheduler.md) : ce que WordPress utilise pour ses tâches planifiées, son défaut bien connu, et le remède.
