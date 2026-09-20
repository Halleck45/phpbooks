# Comment lire ce livre

On vous demande de prendre PHP au sérieux, et vous vous en passeriez bien. Le langage a trente ans, on l'associe au pire code qu'on vous ait jamais mis sous les yeux, et personne n'en parle dans les conférences que vous suivez. Il revient pourtant sans cesse : dans la pile technique d'une entreprise que vous respectez, dans les offres d'emploi, derrière un site qui encaisse plus de trafic que le vôtre. J'ai écrit ce livre pour régler cette contradiction avec des preuves plutôt qu'avec de l'enthousiasme.

**Chaque chiffre de ce livre a une source et une date, et l'annexe les recense pour que vous puissiez vérifier chacun d'eux.** Un nombre dans le texte est suivi de sa provenance et de sa date, entre parenthèses. Un chiffre de fournisseur, une étude de cas auto-déclarée ou un benchmark synthétique sont signalés comme tels dans la phrase même où ils apparaissent, et quand je ne sais pas, je le dis. Vous ne devriez jamais avoir à vous demander si une phrase énonce un fait ou un souhait.

## Pourquoi le doute est raisonnable

La réputation a été méritée. Pendant sa première décennie, PHP a été permissif jusqu'à la faute : les variables surgissaient de nulle part, `"abc" == 0` valait vrai, les erreurs s'imprimaient dans la page et l'exécution continuait, les requêtes vers la base de données se bricolaient par concaténation de chaînes, et la bibliothèque standard grossissait une fonction à la fois, sous le nom que son auteur préférait cette semaine-là. Une génération a appris à programmer sur ce PHP-là et en a écrit énormément, et une bonne partie de ce code tourne encore. L'essentiel de ce qu'on vous a montré sous l'étiquette « PHP » date de cette période.

Le langage que vous évalueriez aujourd'hui est un autre objet. PHP 7 (2015) a reconstruit le moteur et ajouté les déclarations de types scalaires. PHP 8 (2020) a apporté les types union, `match`, les arguments nommés, les attributs, les énumérations, les propriétés `readonly`, les callables de première classe et un compilateur JIT, et il a appris à l'interpréteur à lever une exception là où il devinait. Une version est sortie chaque année depuis, fin novembre ou début décembre. La PHP Foundation salarie des développeurs du cœur depuis 2021, le gestionnaire de paquets est universel, et deux analyseurs statiques vous donnent l'essentiel de ce qu'un compilateur vous donnerait. La syntaxe actuelle est dans [Le langage en 2026](ch05-the-language.md), et les gens qui la publient sont dans [Gouvernance et pérennité](ch07-governance.md).

Une partie de la réputation reste méritée. Les chaînes sont des suites d'octets, la bibliothèque standard garde ses noms historiques, il n'y a ni génériques ni threads en espace utilisateur, et le runtime est synchrone par défaut. Une grande part du PHP qui tourne sur le web public est vieille, parce que l'hébergement qui la fait tourner est vieux. Chacune de ces limites se trouve dans le chapitre où vous iriez la chercher, à côté de la pratique qui l'entoure aujourd'hui, et [Là où PHP est le mauvais choix](ch09-wrong-choice.md) rassemble les cas où le conseil honnête est de choisir autre chose.

<img src="images/ch00-two-columns.png" alt="Une feuille de papier divisée en deux colonnes par un trait vertical. La colonne de gauche est coiffée d'une coche et contient quelques barres bien nettes et un petit éléphant ; la colonne de droite est coiffée d'une croix et contient elle aussi quelques barres. Une main tient un stylo au-dessus de la feuille et remplit les deux colonnes" width="560">

## Les questions, dans l'ordre

Chaque chapitre répond à une question que vous poseriez, dans l'ordre d'une revue de due diligence, de l'extérieur vers l'intérieur.

[Empreinte](ch01-footprint.md) demande qui tourne sur PHP et à quelle échelle, et répond par les parts de marché du web, par les plateformes bâties dessus et par les organisations qui décrivent leur production PHP avec leurs propres mots. [Le runtime](ch02-runtime.md) explique le modèle d'exécution, parce que l'essentiel de ce que PHP fait bien et de ce qu'il ne sait pas faire en découle. [Débit et latence](ch03-throughput-and-latency.md) et [Concurrence](ch04-concurrency.md) donnent les chiffres de performance, avec le round du benchmark, le matériel et le test nommés, et avec, sur le même graphique, les langages qui battent PHP sur le même test.

[Le langage en 2026](ch05-the-language.md) est le tour de la syntaxe le plus court possible, pour ceux qui jugent un langage en le lisant. [L'écosystème](ch06-ecosystem.md) compte les paquets, les frameworks et les outils. [Gouvernance et pérennité](ch07-governance.md) couvre le processus des RFC, le calendrier des versions, le processus de sécurité et l'argent, et [Coût de possession](ch08-cost.md) regarde le recrutement, l'hébergement et les mises à niveau.

[Là où PHP est le mauvais choix](ch09-wrong-choice.md) est le chapitre qui rend les autres crédibles. [Une évaluation en une semaine](ch10-evaluation.md) est un protocole, quoi installer, quoi mesurer, quoi lire, pour que la décision que vous prendrez repose sur vos chiffres et non sur les miens.

## Les règles que je me suis fixées

**Les comparaisons sont symétriques.** Quand un graphique montre PHP devant un langage sur une mesure, le texte nomme une mesure où ce langage est devant, quand elle existe. Les options courantes que vous vous attendez à voir, Node.js, Python, Java, C#, Go, Ruby, ne sont jamais écartées d'un graphique parce qu'elles y feraient bonne figure.

**Les noms viennent avec des preuves.** Une entreprise n'apparaît ici que si ses propres ingénieurs, dans un billet de blog, une conférence, un dépôt ou un rapport, disent qu'elle fait tourner PHP en production, et l'annexe renvoie à ce document avec sa date. Les entreprises qui font tourner Hack sur HHVM, un langage issu d'un fork de PHP, ne sont pas présentées comme des utilisatrices de PHP, si tentant que fût le logo.

**Les frameworks et les outils sont listés, pas recommandés.** Ils apparaissent par ordre alphabétique. La PHP Foundation, sous l'égide de laquelle ce livre paraît, promeut le langage et ses standards plutôt qu'un fournisseur, et je fais de même.

## Comment le vérifier

Chaque chapitre se termine par quelque chose que vous pouvez vérifier en un après-midi : un tableau de bord public à ouvrir, un benchmark à relancer sur votre matériel, une commande à taper. Prenez-les au sérieux. Un chiffre que j'ai mal relevé, ou qui a vieilli depuis que je l'ai écrit, est exactement ce que vous devriez trouver, et [Sources](appendix-01-sources.md) vous donne l'URL pour le trouver.

Votre première question est sans doute celle par laquelle j'ai commencé moi aussi : qui tourne vraiment là-dessus ?
