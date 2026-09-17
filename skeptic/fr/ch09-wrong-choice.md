# Là où PHP est le mauvais choix

Une évaluation incapable de nommer les cas où son sujet perd n'est pas une évaluation, et PHP perd dans plusieurs. **PHP est le mauvais choix pour le calcul limité par le CPU, pour les services dont le métier est de maintenir de nombreuses connexions de longue durée, pour tout ce qui s'exécute hors d'un serveur, et pour les équipes dont les compétences, la plateforme et l'échelle les ont déjà menées ailleurs.** Dans chacun de ces cas, le conseil honnête est rarement « tout réécrire » et bien plus souvent « pas cette partie », avec un autre outil pour la partie en question.

## Le calcul

Le programme n-body prend 204 secondes en PHP avec le JIT désactivé, contre 8,6 pour Node.js, et le JIT resserre cet écart sans le combler, comme [Débit et latence](ch03-throughput-and-latency.md) l'a montré. Sur du code qui occupe un cœur, l'interpréteur joue dans la catégorie de Python et de Ruby, un ordre de grandeur derrière V8, la JVM, .NET, Go et Rust. Autour de lui, aucune pile numérique digne de ce nom : pas de bibliothèque de tableaux de la portée de NumPy, pas de bibliothèque de dataframes de la portée de pandas, pas de framework d'apprentissage automatique qu'une équipe de recherche reconnaîtrait. Les paquets qui existent sont rares et maintenus par de petits groupes, et je n'ai trouvé aucun chiffre d'échelle à citer pour aucun d'entre eux.

Si votre produit est un modèle, une simulation, un pipeline de traitement du signal ou un gros calcul par lots, prenez Python pour l'écosystème ou un langage compilé pour la vitesse. Si ce produit a aussi une façade web, c'est là que PHP peut encore trouver sa place.

## Les connexions de longue durée

Dix mille connexions inactives coûtent dix mille processus dans le modèle par défaut de PHP, et un processus coûte trop cher pour le dépenser sur une socket qui dort. Les runtimes asynchrones de [Concurrence](ch04-concurrency.md) existent et tiennent la charge, l'entrée Swoole servant 3,5 millions de requêtes pipelinées par seconde sur le test plaintext. Mais ce sont des bibliothèques avec leurs propres clients d'entrées-sorties, pas une propriété du langage, et la plupart des paquets de l'écosystème ont été écrits pour le modèle bloquant. Un backend de chat, un serveur de jeu multijoueur, une passerelle de trading, un pipeline de streaming ou un service de notifications push, c'est le cas ordinaire pour Node.js, Go, Elixir et Erlang, Java ou C#, et ces écosystèmes ont les bibliothèques qui vont avec.

Les budgets de latence sous la milliseconde tombent du même côté. Le plancher d'une requête PHP-FPM est sous la milliseconde sur une machine au repos, et rien de ce qui se construit dessus n'y reste sous charge, donc un système avec ce budget s'écrit dans un langage compilé.

## Hors du serveur

PHP est un langage pour serveurs. Il a un interpréteur en ligne de commande, et une bonne partie de l'outillage est écrite avec, mais pour les applications de bureau, les applications mobiles, les navigateurs, les appareils embarqués ou la distribution d'un binaire autonome aux utilisateurs finaux, il n'a rien sur quoi une équipe devrait bâtir. Si vos utilisateurs n'exécutent pas d'interpréteur PHP, écrivez l'outil que vous leur donnez dans autre chose.

<img src="images/ch09-toolbox.png" alt="Un mur d'atelier où les outils sont suspendus dans leurs silhouettes. Un éléphant se tient devant, remettant une clé à molette dans sa silhouette et tendant la main vers un autre outil. Sur l'établi en dessous, un objet à moitié terminé qui a manifestement besoin du second outil" width="560">

## Les garanties au niveau du langage

Un `match` auquel il manque une branche lève une exception à l'exécution. Ce seul fait décrit le système de types du chapitre [Le langage en 2026](ch05-the-language.md) : il est appliqué à l'exécution, aux frontières des fonctions et des propriétés, sans génériques dans le langage, sans étape de compilation, sans modèle de propriété ni de durée de vie, et sans vérification d'exhaustivité. La réponse de l'écosystème est un analyseur statique lancé à son niveau le plus strict à chaque build, ce qui donne à un projet typé l'essentiel de ce qu'un compilateur donnerait, et beaucoup de grandes bases de code PHP vivent avec cette réponse. Si « le compilateur le garantit » est pour vous une exigence et non une préférence, à cause du domaine, du régulateur ou de la taille de la base de code, TypeScript, Java, C#, Kotlin, Go ou Rust vous serviront mieux, et je ne plaiderai pas le contraire.

## Les équipes et l'échelle

Un développeur professionnel sur cinq a écrit du PHP l'an dernier, un sur onze le cite comme langage principal, et sa part du web est passée de 80 à 70 % en dix ans. La part des développeurs est plus petite que la part des serveurs en production. [Empreinte](ch01-footprint.md) documente aussi les entreprises qui ont quitté PHP, et elles sont parties vers Java, Go ou TypeScript quand un monolithe web s'était mué en un ensemble de services : Zalando en 2010, Trivago en 2021, Dailymotion et BlaBlaCar en 2025 et 2026. Leurs documents publics donnent l'architecture pour raison, pas le coût du runtime.

Si vos ingénieurs travaillent déjà dans un autre langage, sur une plateforme construite pour lui, ajouter PHP pour un nouveau service vous rapporte peu. Les avantages du runtime, décrits tout au long de ce livre, sont des avantages de simplicité, et une seconde pile les efface. Et si votre entreprise a atteint l'échelle où elle réécrit son monolithe en services compilés et typés, vous suivez un schéma dans lequel PHP est ce que l'on quitte, comme Ruby et Python le sont ailleurs au même stade.

## Là où le doute ne s'applique pas

Les mêmes preuves soutiennent le verdict inverse, et sans adjectifs. Les applications web en requête-réponse, à toute échelle que vous avez des chances d'atteindre : contenu, commerce, back-offices, API, les plateformes du chapitre [Empreinte](ch01-footprint.md) et les applications sur mesure bâties à côté. Les équipes qui tiennent à un runtime sans processus à materner et à un déploiement qui se résume à une copie de fichiers. Les organisations qui doivent faire tourner un logiciel pendant dix ans sur un hébergement qu'elles ne contrôlent pas, où le parc installé et la fenêtre de support de quatre ans pèsent plus que le débit. Et les produits dont la partie difficile est le domaine et non la machine, c'est-à-dire la plupart des produits.

> La limite de ce chapitre : il nomme les cas que les preuves couvrent. Un domaine que je n'ai pas mesuré, je ne l'ai pas jugé, et si le vôtre en fait partie, déroulez la semaine qui suit avant de croire la réputation, ou moi.

## Ce que vous pouvez vérifier vous-même

Écrivez la charge de travail de votre produit qui vous inquiète le plus, et cherchez-la ci-dessus. Si elle y est, le conseil tient, sauf si votre propre mesure le contredit. Si elle n'y est pas, [Une évaluation en une semaine](ch10-evaluation.md) existe pour elle.
