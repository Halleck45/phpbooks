# Introduction

En ce moment même, quelque part, quelqu'un ouvre une page web. Une boutique en ligne, un blog, une encyclopédie. Derrière une bonne partie de ces pages, un petit programme vient de se réveiller, a fait son travail en quelques millisecondes, a envoyé sa réponse, puis a disparu. Il y a de fortes chances qu'il ait été écrit en PHP.

Ce rythme, **se réveiller, travailler, disparaître**, c'est le cœur de PHP sur le web. Autant le comprendre tout de suite : il explique une bonne partie du caractère du langage.

Imaginez un serveur de restaurant sans aucune mémoire. Un client arrive, il prend la commande, la prépare, l'apporte, et oublie tout aussitôt. Le client suivant est accueilli exactement comme s'il était le premier de la journée. Rien ne traîne de la commande précédente : ni miettes, ni assiette sale, ni conversation en suspens.

<img src="images/ch00-request-cycle.png" alt="La vie d'une requête PHP : un visiteur demande une page, PHP se réveille, fait le travail, envoie la réponse et oublie tout" width="560">

Une page PHP fonctionne exactement ainsi. **À chaque visite, le programme démarre de zéro, s'exécute de haut en bas, puis tout est jeté.** Dit comme ça, on dirait du gaspillage. En réalité, c'est l'une des façons les plus solides qu'on ait trouvées pour servir des millions de personnes par jour : un bug ne gâche qu'une visite au lieu de contaminer tout le serveur, et s'il faut absorber plus de monde, on ajoute des serveurs de salle.

> Un programme PHP naît pour un visiteur, lui répond, puis oublie. Le suivant repart d'une page blanche.

Le web est la maison de PHP, mais PHP ne s'arrête pas là. C'est aussi un très bon langage pour **les petits outils qu'on lance depuis un terminal** : renommer mille fichiers, lire un export de tableur, envoyer une série de courriels, faire le ménage dans un dossier. Pas de navigateur, pas de serveur web. Un script, et son résultat.

C'est par là que ce livre commence, et ce n'est pas un hasard. Dans un terminal, vous tapez une commande et la réponse s'affiche juste en dessous. **Ce retour immédiat est la façon la plus rapide d'apprendre un langage.** Le web, avec ses requêtes, ses pages et ses formulaires, viendra ensuite, quand le langage vous sera devenu familier.

Pour commencer, une seule compétence est nécessaire : **savoir ouvrir un terminal et y taper une commande**. Si vous savez entrer dans un dossier avec `cd` et lancer un programme, vous avez tout ce qu'il faut.

Inutile d'avoir déjà programmé. Si vous n'avez jamais écrit une ligne de code, les premiers chapitres construisent chaque idée depuis le début, et la suite ne suppose jamais que vous avez sauté des pages. Si vous connaissez déjà un autre langage, vous reconnaîtrez les grandes formes (variables, boucles, fonctions) et vous irez plus vite, en guettant les endroits où PHP fait les choses à sa façon.

Apprendre un langage, c'est un peu comme apprendre à faire du vélo. Personne ne commence par la physique de l'équilibre. On monte, on vacille, on fait quelques mètres. Les explications deviennent lumineuses une fois qu'on a senti la machine bouger. Ce livre suit le même ordre.

> D'abord on roule. Ensuite on comprend pourquoi le vélo tient debout.

<img src="images/ch00-roadmap.png" alt="Le chemin à travers le livre : un premier programme, un petit jeu, les fondamentaux, un outil en ligne de commande, puis une application web" width="620">

1. **Un premier programme.** Installer PHP et lui faire afficher une phrase.
2. **Un petit jeu.** Un jeu de devinette en trente lignes, écrit avant même de connaître le sens de la plupart des mots.
3. **Les fondamentaux.** Chaque pièce de ce jeu (variables, types, décisions, boucles, fonctions), expliquée pour de bon, maintenant que vous l'avez vue fonctionner.
4. **Un vrai outil.** Un programme en ligne de commande qui lit des fichiers et gère les erreurs comme un logiciel qu'on utilise vraiment.
5. **Une application web.** Un petit site construit à partir de rien, sans framework pour cacher ce qui se passe.

Chaque projet est plus ambitieux que le précédent, et aucun n'utilise autre chose que ce que vous avez déjà vu.

Il y a deux façons de lire ce livre.

**Si PHP est votre premier langage**, lisez-le dans l'ordre. Chaque chapitre s'appuie sur les précédents, et les projets de la fin sont bien plus faciles quand les bonnes habitudes sont prises tôt.

**Si vous programmez déjà** et voulez seulement savoir comment PHP s'y prend (comment se comportent ses types, ce qui distingue ses objets de ses tableaux, à quoi ressemble sa syntaxe moderne), utilisez-le comme une référence et allez directement au chapitre qui vous intéresse. Les chapitres se suffisent à eux-mêmes autant que possible, et renvoient aux pages précédentes quand ils s'appuient dessus.

Une dernière chose avant de commencer : **installez PHP**. Le [chapitre 1](ch01-00-getting-started.md) explique comment, en quelques minutes. Ensuite, gardez un terminal ouvert à côté du livre et exécutez chaque exemple au moment où vous le rencontrez.

> Lire un livre sur la natation n'a jamais appris à nager. Lire un livre sur PHP n'apprend pas PHP. Le taper, si.
