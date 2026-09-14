# Sécurité et performance

## La sécurité

Le [chapitre 10](ch10-02-validation-and-xss.md) a traité le XSS et l'injection SQL correctement, et a nommé le CSRF sans s'en défendre. **C'est le début de la sécurité d'une application web, pas le tout.** Quelques directions de plus méritent qu'on sache qu'elles existent.

L'authentification et l'autorisation répondent à deux questions distinctes : qui fait cette requête, et qu'a-t-il le droit de faire. `password_hash()` et `password_verify()` sont la façon intégrée à PHP, et correctement salée, de stocker des mots de passe. Les sessions suivent un utilisateur connecté d'une requête à l'autre, malgré le modèle sans état partagé du [chapitre 18](ch18-01-request-model.md). OAuth couvre le « se connecter avec un compte d'ailleurs ».

**Une base de code n'est jamais plus sûre que les paquets qu'elle embarque**, et le [chapitre 16](ch16-00-more-about-composer.md) vous a appris à en embarquer beaucoup. `composer audit` compare les paquets installés à une base de vulnérabilités connues, et Roave Security Advisories empêche carrément d'installer une version de paquet avec une faille connue.

Le Top 10 de l'OWASP est une liste standard, régulièrement mise à jour, des vulnérabilités les plus courantes des applications web, XSS et injection SQL comprises. Lisez-le une fois, comme une carte de ce contre quoi se défendre au-delà de ce que ce livre a couvert.

Les secrets sont la dernière direction : ne jamais commiter un identifiant dans un dépôt. Les variables d'environnement, le mécanisme du [chapitre 14](ch14-05-working-with-environment-variables.md), sont le plancher. Un coffre à secrets dédié (Vault, ou le gestionnaire de secrets d'un fournisseur de cloud) est le plafond pour tout ce qui manipule de vraies données d'utilisateurs.

## Performance et observabilité

Par défaut, PHP compile votre code source en bytecode à chaque requête, puis jette le résultat. **Opcache conserve ce bytecode compilé d'une requête à l'autre.** L'activer en production n'est pas tant une option qu'une évidence.

Les couches de cache comme Redis et Memcached vous donnent un endroit où ranger des données coûteuses à recalculer ou à aller rechercher. Le modèle sans état partagé du [chapitre 18](ch18-01-request-model.md) signifie que rien ne survit entre deux requêtes si vous ne le déposez pas quelque part exprès, la raison même pour laquelle le [chapitre 10](ch10-03-talking-to-a-database.md) a eu besoin d'une base de données.

Profiler en production demande d'autres outils. Le profileur de Xdebug du [chapitre 13](ch13-02-xdebug.md) est fait pour le développement, bien trop lent pour rester actif sous du vrai trafic. La production s'appuie sur des instruments plus légers : Blackfire, ou des produits généralistes de supervision applicative comme Datadog et New Relic.

**Savoir après coup ce qu'une requête a fait compte davantage en PHP que dans un serveur qui tourne en continu**, précisément parce que l'état de chaque requête disparaît dès qu'elle se termine. Les logs structurés, les métriques par requête et le traçage distribué sont ce qui vous permet de reconstituer les faits une fois que « j'ajoute un `var_dump()` et je relance » n'est plus une option.

Les deux directions partagent un même fil. Le livre d'or du chapitre 10 et le projet final du chapitre 21 ont été construits pour enseigner correctement le modèle sous-jacent. Aucun des deux n'a été bâti pour survivre à un internet hostile ou à un trafic sérieux, et c'est très bien ainsi. C'est à cela que sert cette section.
