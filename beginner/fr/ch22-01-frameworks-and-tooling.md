# Les frameworks et l'outillage autour

## Les frameworks

Le [chapitre 21](ch21-00-final-project-web-app.md) vous a fait écrire un routeur, des contrôleurs et une couche de vues à la main, exprès, pour que rien de tout cela ne ressemble jamais à de la magie. **Un framework, c'est la même silhouette, déjà construite**, éprouvée par des milliers de projets, avec un écosystème de paquets assemblé autour. En choisir un n'est pas un aveu d'échec. C'est s'épargner un travail que d'autres ont déjà bien fait.

Deux frameworks dominent le monde PHP, et ils ne font pas le même pari.

**Laravel arrive avec tout inclus.** Un ORM (Eloquent), un moteur de templates (Blade), un outil en ligne de commande (Artisan), des files d'attente, une authentification prête à l'emploi, et bien d'autres choses, le tout conçu pour fonctionner ensemble dès l'installation. C'est aujourd'hui la porte d'entrée la plus courante pour un nouveau projet PHP.

**Symfony est construit composant par composant.** Ses briques (le routage, l'injection de dépendances, l'abstraction HTTP) s'utilisent chacune séparément, et il préfère l'explicite à la convention. C'est souvent le choix des bases de code plus grosses et plus durables, et certaines de ses briques font tourner discrètement d'autres projets, Laravel compris.

Des frameworks plus petits, comme Slim ou Mezzio, existent pour les cas où un framework complet est trop pour le projet, une API sans aucune vue, par exemple. Choisissez d'après ce dont le projet et l'équipe ont vraiment besoin, pas d'après le nom qui fait le plus de bruit en ligne. Comme vous avez construit les pièces vous-même, aucun ne devrait vous paraître opaque : ouvrez un contrôleur Laravel ou une route Symfony et vous en reconnaîtrez la forme.

> Un framework, c'est le chapitre 21, fait avant vous par mille personnes.

## L'outillage

L'[annexe D](appendix-04-useful-development-tools.md) a présenté les outils que vous lancez pendant que vous écrivez du PHP : Composer, PHPUnit, l'analyse statique, un débogueur. **La couche suivante s'occupe de ce qui se passe une fois le code écrit** : l'amener sans casse de votre machine jusqu'en production, et le garder en bonne santé une fois là-bas.

L'intégration continue (GitHub Actions, GitLab CI) lance votre suite de tests, PHPStan et votre vérificateur de style à chaque push, si bien qu'une modification cassée est repérée avant qu'un humain ait à s'en apercevoir. Les conteneurs (Docker) emballent PHP, ses extensions et ses dépendances dans quelque chose qui tourne à l'identique sur votre portable, en CI et en production, ce qui met fin à la conversation « ça marche sur ma machine ». Les outils de déploiement (Deployer, ou des plateformes gérées comme Laravel Forge et Platform.sh) automatisent « mettre le nouveau code sur le serveur correctement », une tâche qui, à la main, compte plus d'étapes qu'elle ne devrait.

Deux outils vont un cran plus loin. **Rector refactorise le code mécaniquement**, y compris pour faire monter toute une base de code d'une version de PHP à l'autre en bloc plutôt que fichier par fichier, ce qui compte dès que les questions de compatibilité de l'[annexe E](appendix-05-php-versions.md) cessent d'être théoriques. **Infection teste vos tests.** Il glisse volontairement de petits bugs dans votre code et vérifie si la suite du [chapitre 12](ch12-00-testing.md) s'en aperçoit, une question plus pointue que « est-ce que les tests passent ».

Aucune de ces idées n'est propre à PHP. Ce qui est propre à PHP, c'est à quel point elles s'y emboîtent bien : l'écosystème dispose d'un outillage mûr, ennuyeux et bien documenté pour chacune d'elles, et l'ennui est un vrai avantage face à des écosystèmes plus clinquants dont l'outillage est plus mince en dessous.
