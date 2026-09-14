# Fonctionnalités avancées

Tout atelier a un tiroir pour les outils qui servent deux fois par an. Le ciseau à bois, la clé à tube, le jeu de tarauds. On ne les emporte pas partout, mais le jour où le bon travail se présente, savoir qu'ils existent sauve l'après-midi. **Ce chapitre, c'est ce tiroir.**

<img src="images/ch20-tool-drawer.png" alt="Un tiroir d'atelier ouvert contenant quatre outils spécialisés, chacun étiqueté du nom d'une section du chapitre : reflection, interfaces, callables, attributs" width="560">

Les quatre sections qui suivent ne s'appuient pas les unes sur les autres, et aucune n'est nécessaire pour finir ce livre. **Sautez ce chapitre si vous voulez, et revenez-y le jour où un framework fait quelque chose que vous n'arrivez pas à expliquer.** Tout ce qu'il contient est courant dans l'écosystème PHP, dans les bibliothèques que vous installez avec Composer, dans Symfony et Laravel, dans le code écrit par des gens qui pratiquent depuis longtemps. Rien de tout cela n'est du code que vous écrirez chaque jour, et c'est précisément pour ça qu'il se trouve ici, vers la fin, plutôt que disséminé dans les chapitres précédents.

Voici ce qu'il y a dans le tiroir. Les constantes magiques et la Reflection permettent au code de se regarder lui-même, et de regarder d'autre code, pendant qu'il s'exécute ; vous les appellerez rarement, parce que les frameworks et les outils de test le font pour vous. Quelques interfaces natives branchent vos propres objets sur la syntaxe de PHP, si bien que `count()`, les crochets et `foreach` fonctionnent dessus comme sur des tableaux. Les closures ont droit à un second regard, avec la syntaxe des callables de première classe apportée par PHP 8.1. Et les attributs mettent des métadonnées directement dans le code, là où un commentaire faisait le travail autrefois.

Choisissez la section qui correspond au casse-tête que vous avez sous les yeux. Chacune tient debout toute seule.
