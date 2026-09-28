# Nextcloud Talk : le temps réel au sein d'une plateforme

Nextcloud Talk est un système de chat et de visioconférence en production à grande échelle, construit comme une application à l'intérieur d'une application PHP plutôt que comme un produit parti de zéro. Vous ne toucherez peut-être jamais au code de Nextcloud, et il a quand même quelque chose à vous apprendre. **« PHP ne sait pas faire de temps réel » n'a jamais été vrai ; tout l'art est de savoir ce qu'on garde dans PHP et ce qu'on délègue.**

Talk s'installe comme une application dans n'importe quelle instance Nextcloud :

```bash
php occ app:install spreed
php occ app:enable spreed
```

Pour le chat, Talk s'appuie sur les mêmes techniques de polling et de Server-Sent Events que le reste de ce chapitre. Pour les appels audio et vidéo à grande échelle, il passe la main à un High-Performance Backend, un serveur de signalisation séparé, au lieu de forcer les flux média dans le cycle de requête de PHP :

```bash
php occ talk:signaling:add wss://signaling.example.com "shared-secret-here"
```

Ce découpage est le modèle à emprunter. PHP possède les comptes, les permissions et l'historique des conversations. Un service spécialisé possède le flux média.

## Quand le choisir

Pas comme un paquet à installer dans votre propre projet, mais comme une architecture de référence le jour où votre fonctionnalité temps réel se met à vouloir de la vidéo ou de l'audio, et plus seulement des données : gardez PHP comme source de vérité pour les comptes et les permissions, et déléguez le transport média à un service conçu pour ça.

## Quand ce n'est pas le bon outil

Si la question est d'auto-héberger Nextcloud pour votre organisation (voir [Livrer du stockage de fichiers et de la collaboration](ch08-01-nextcloud-ready-made-drive.md)), Talk est l'une des applications livrées avec, pas une décision à part.

> **Sous le capot :** le système d'applications de Nextcloud permet d'installer, de mettre à jour et de désactiver une fonctionnalité comme Talk indépendamment du cœur, en s'appuyant sur les conventions de paquets et d'autoloading propres à PHP. C'est la même intuition que les extensions WordPress ou les bundles Symfony : un cœur stable, et des fonctionnalités posées par-dessus en unités distinctes et interchangeables.
