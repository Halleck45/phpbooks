# L'architecture et le processus de développement

## L'architecture

Passé une poignée de fichiers, « où vit ce bout de code, et pourquoi là » cesse d'être évident. Cela devient une discipline à part entière. Vous en avez déjà pratiqué la plus petite forme : le patron Stratégie du [chapitre 17](ch17-04-oop-design-patterns.md) a sorti un comportement variable derrière une interface, si bien que la classe qui s'en servait n'avait jamais besoin de savoir quelle version elle recevait. **L'architecture, c'est ce même réflexe, appliqué à toute une base de code au lieu d'une seule classe.**

Quelques noms valent la peine d'être reconnus.

**L'architecture en couches** sépare les responsabilités comme l'ont fait le routeur, les contrôleurs et les vues du [chapitre 21](ch21-02-mvc-structure.md), en plus formel : des couches explicites (présentation, logique métier, persistance), et des règles sur qui a le droit de dépendre de qui.

**Le Domain-Driven Design**, DDD pour les intimes, nomme les classes et les méthodes d'après les concepts que le métier emploie vraiment, plutôt que d'après l'arborescence du framework, pour que le code se lise comme le problème qu'il résout.

**L'architecture hexagonale**, aussi appelée ports et adaptateurs, garde votre logique centrale dans l'ignorance de la base de données et du framework qui l'entourent, de sorte qu'on peut la tester et raisonner dessus sans que ni l'un ni l'autre ne soit dans la pièce.

**Monolithe contre microservices** est le débat que vous entendrez le plus souvent. Un monolithe bien organisé reste le bon choix bien plus longtemps que la sagesse d'internet ne le suggère. Découper un système en services résout des problèmes d'organisation (beaucoup d'équipes qui livrent indépendamment), pas des problèmes techniques, et cela en apporte de nouveaux, bien réels : coordonner à travers un réseau au lieu d'un seul processus, le modèle sans état partagé du [chapitre 18](ch18-01-request-model.md) répété à une tout autre échelle.

Aucun de ces noms n'est une règle à appliquer partout. C'est du vocabulaire. Le jour où la structure d'une base de code commence à faire mal, vous aurez un mot à chercher.

> Les noms d'architecture sont du vocabulaire, pas des ordres.

## Le cycle de vie du logiciel

L'architecture organise le code. **Le reste des pratiques autour d'un projet organise les gens qui modifient ce code**, et le chemin qu'une modification parcourt depuis l'idée jusqu'à quelque chose qui tourne en production sans danger.

Les branches et la revue de code donnent à une équipe une façon commune de proposer un changement et de le faire regarder par quelqu'un d'autre avant qu'il ne soit fusionné, ce qui attrape les problèmes qu'une suite de tests ne voit pas. Le versionnage donne un sens aux publications : le même schéma MAJEUR.MINEUR.CORRECTIF que l'[annexe E](appendix-05-php-versions.md) a utilisé pour les promesses de compatibilité de PHP s'applique à tout paquet que vous publiez selon le [chapitre 16](ch16-02-publishing-to-packagist.md). Les environnements gardent le local, la préproduction et la production raisonnablement semblables, bâtis sur les variables d'environnement du [chapitre 14](ch14-05-working-with-environment-variables.md) plutôt que sur des différences codées en dur. Le suivi des tickets et les changelogs conservent une trace de ce qui a changé et pourquoi, en marge de l'historique des commits, qu'un collègue (ou vous, dans six mois) pourra vraiment lire.

Rien de tout cela n'est propre à PHP non plus. Ce qui mérite d'être dit, c'est que PHP rend cette discipline particulièrement facile à sauter. Pas de compilation, pas d'attente de build : on modifie, on recharge, c'est bon. On peut vivre longtemps sans elle et ne rien sentir de travers, jusqu'au jour où le projet a assez d'historique et assez de contributeurs pour que l'avoir sautée finisse par coûter quelque chose.
