# Comment lire ce livre

« Ajoutez un écran de connexion. » « Il nous faut un blog. » « La recherche doit répondre instantanément. » **Chaque chapitre après le premier est une demande de ce genre, une phrase qu'un client ou un product manager pourrait prononcer**, jamais un morceau de syntaxe. Ouvrez le chapitre qu'on vous a commandé et sautez le reste. Personne n'attend de vous que vous lisiez ce livre d'une traite.

<img src="images/ch00-menu.png" alt="Une personne attablée à un café lit un menu dont les lignes sont des icônes plutôt que des mots : un cadenas, un panier, une loupe, une enveloppe. Un petit éléphant en tablier de serveur attend, carnet à la main. Le doigt de la personne s'arrête sur la ligne du cadenas" width="560">

## La forme d'un chapitre

Un chapitre s'ouvre sur une courte page qui pose la décision : ce que la fonctionnalité implique vraiment, et les deux à quatre écosystèmes capables de la livrer proprement. Chaque écosystème a ensuite sa propre page, toujours en trois parties :

- Ce que l'outil ou la plateforme fait pour vous, en un paragraphe.
- Un exemple minimal qui fonctionne : la commande à lancer ou le code à écrire.
- Quand choisir cette option, et quand ce n'est pas le bon outil.

Les écosystèmes viennent à peu près dans l'ordre, du « plus rapide vers une démo » au « meilleur choix pour quelque chose qui doit durer ». Prenez cet ordre comme un repère, pas comme un classement. Le bon choix dépend du budget de votre client, de la stack que votre équipe fait déjà tourner, et du temps que la chose devra survivre une fois livrée.

## Le marqueur `$`

L'essentiel de ce livre est du logiciel libre et gratuit. Quelques noms portent un **`$`** dans leur titre : des produits payants ou des services en ligne, pas de l'open source. Ils sont là parce qu'ils sont souvent le chemin le plus rapide ou le plus fiable vers une fonctionnalité précise, pas parce que quelqu'un a payé pour figurer dans ces pages. Chaque option `$` côtoie au moins une alternative libre dans le même chapitre, pour que vous puissiez peser un abonnement contre votre propre temps.

## Les encadrés « Sous le capot »

La plupart des pages se terminent par un court aparté de cette forme :

> **Sous le capot :** une note d'un ou deux paragraphes sur la fonctionnalité du langage ou le comportement du moteur qui rend possible la facilité décrite juste au-dessus. Toujours facultative. Toujours sautable.

Vous livrerez tout ce que contient ce livre sans en ouvrir un seul. Ils existent pour le moment où la curiosité prendra le dessus, et pour ce moment-là, l'[annexe C](appendix-03-under-the-hood-index.md) les indexe tous, chapitre par chapitre.

## Si le vocabulaire vous bloque

L'[annexe B](appendix-02-glossary.md) définit les termes récurrents de l'écosystème (ORM, conteneur de services, hook, bundle, ressource) par ce qu'ils font pour vous, pas par leur définition de manuel. Un terme inconnu est une raison d'y jeter un œil, pas d'arrêter de lire.

La première décision vient avant toute fonctionnalité : que construisez-vous, au juste ?
