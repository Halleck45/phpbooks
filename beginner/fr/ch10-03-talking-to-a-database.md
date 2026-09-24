# Parler à une base de données avec PDO

Signez le livre d'or, rechargez la page, et votre message a disparu. Ce n'est pas un bug. PHP, dans sa forme classique et toujours la plus répandue, offre à chaque requête un départ à neuf : il exécute le script depuis le haut et jette tout une fois la réponse envoyée, variables comprises. Rien ne survit d'une requête à la suivante, sauf ce qu'on a pris soin de ranger quelque part, et jusqu'ici, rien ne l'a été. **Pour qu'un message survive à la requête qui l'a envoyé, il doit vivre quelque part où PHP pourra le relire plus tard : une base de données.** (Le [chapitre 18](ch18-01-request-model.md) revient posément sur ce modèle de requête sans mémoire partagée, et sur les raisons qui font que PHP a rarement besoin de threads.)

<img src="images/ch00-request-cycle.png" alt="La vie d'une requête PHP : un visiteur demande une page, PHP se réveille, fait le travail, envoie la réponse, et oublie tout" width="560">

## PDO et SQLite

PHP parle aux bases de données par plusieurs extensions. **PDO, pour PHP Data Objects, est celle vers laquelle se tourner en premier** : elle offre une seule interface pour de nombreux moteurs, si bien que le même code fonctionne que les données soient dans MySQL, PostgreSQL ou, comme ici, SQLite. SQLite range une base de données entière dans un seul fichier ordinaire. Aucun serveur à installer, rien à configurer, ce qui garde la technologie autour de ce chapitre aussi simple que le PHP qu'il contient.

Ouvrez une connexion en tête de `guestbook.php` :

```php
<?php

$pdo = new PDO('sqlite:' . __DIR__ . '/guestbook.db');
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$pdo->exec('
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        message TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
');
```

La chaîne `'sqlite:' . __DIR__ . '/guestbook.db'` est un DSN, un data source name : quel pilote utiliser, et où se trouve la base. Le fichier est créé à la première exécution s'il n'existe pas encore. `CREATE TABLE IF NOT EXISTS` peut rester dans le script et tourner à chaque requête sans risque, puisqu'il ne fait rien une fois la table en place.

La deuxième ligne mérite de devenir un réflexe. **Mettez `PDO::ATTR_ERRMODE` à `PDO::ERRMODE_EXCEPTION` chaque fois que vous ouvrez une connexion.** Sans cela, PDO peut échouer en silence et vous rendre un simple `false`, exactement le genre d'échec discret contre lequel le [chapitre 9](ch09-00-error-handling.md) vous a mis en garde. Avec, une mauvaise requête lève une `PDOException`, à attraper comme n'importe quelle autre.

## La mauvaise façon de construire une requête

Avant d'écrire l'insertion, regardez la version à éviter :

```php
// Don't do this.
$pdo->exec("INSERT INTO entries (name, message, created_at) VALUES ('$name', '$message', '" . date('c') . "')");
```

Lisez la requête comme la base de données la lira. Si `$message` contient une apostrophe suivie du SQL de son choix, cette apostrophe ferme la chaîne avant l'heure et la suite fait partie de ce qui s'exécute vraiment. **C'est l'injection SQL**, de la même famille que le XSS de la section précédente, mais dirigée contre votre base de données plutôt que contre le navigateur d'un visiteur. Construire une requête en collant du texte non fiable dans une chaîne n'est jamais sûr, si soigneusement assemblée qu'elle paraisse.

## Les requêtes préparées

La réponse de PDO, c'est la **requête préparée**. La requête part d'abord vers la base, avec des marqueurs à la place des valeurs, et les valeurs voyagent séparément ensuite. **La base ne lit jamais une valeur comme un morceau de la syntaxe de la requête**, donc il n'y a aucune chaîne d'où s'échapper, et l'injection est fermée pour de bon :

<img src="images/ch10-prepared-statement.png" alt="Une requête préparée en deux temps : d'abord le squelette de la requête avec ses cases :name et :message vides est remis à la base, puis les valeurs arrivent séparément dans des enveloppes scellées et sont déposées dans les cases sans jamais être lues comme du SQL" width="600">

```php
if ($submitted && !$errors) {
    $statement = $pdo->prepare(
        'INSERT INTO entries (name, message, created_at) VALUES (:name, :message, :created_at)'
    );
    $statement->execute([
        'name' => $name,
        'message' => $message,
        'created_at' => date('c'),
    ]);
}
```

`:name`, `:message` et `:created_at` sont des marqueurs nommés. `prepare()` envoie la forme de la requête une fois ; `execute()` l'exécute avec un jeu de valeurs, donné sous forme de tableau associatif avec une clé par marqueur. PDO s'occupe des guillemets pour le moteur qui se trouve dessous, et c'est précisément la partie qu'on rate facilement à la main.

> La requête, c'est la phrase. Les valeurs sont remplies après coup, et ne peuvent jamais changer la phrase.

## Relire ce qui a été écrit

Relire les entrées suit la même forme `prepare()` puis `execute()`, ou, pour une requête sans valeur à insérer, le plus simple `query()` :

```php
$entries = $pdo->query('SELECT name, message, created_at FROM entries ORDER BY id DESC')
    ->fetchAll(PDO::FETCH_ASSOC);
```

`fetchAll(PDO::FETCH_ASSOC)` renvoie chaque ligne sous forme de tableau associatif indexé par nom de colonne, le tout dans un tableau ordinaire : la même forme de données que le [chapitre 8](ch08-03-associative-arrays.md) vous a appris à manipuler. Parcourez-le dans le HTML, en échappant chaque valeur exactement comme avant :

```php
<h2>Previous entries</h2>
<ul>
    <?php foreach ($entries as $entry) { ?>
        <li>
            <strong><?= htmlspecialchars($entry['name']) ?></strong>:
            <?= htmlspecialchars($entry['message']) ?>
            <em>(<?= htmlspecialchars($entry['created_at']) ?>)</em>
        </li>
    <?php } ?>
</ul>
```

L'échappement s'applique toujours, pour la même raison qu'avant. Ces valeurs viennent d'un visiteur, en passant par la base, et la base ne sait pas, et ne cherche pas à savoir, si elles peuvent s'afficher en HTML sans danger. **Ranger une valeur sans risque et l'afficher sans risque sont deux travaux distincts**, et en sauter un rouvre la brèche que la section précédente a refermée.

## Ce que vous avez construit

Rechargez le livre d'or, signez-le plusieurs fois, puis arrêtez `php -S` et relancez-le. Les entrées sont toujours là. Elles n'ont jamais vécu en mémoire ; elles vivent dans `guestbook.db`, sur le disque, indépendantes de toute requête. C'est la silhouette complète d'une vraie application web, si petite soit-elle : recevoir les données par les superglobales, les valider, les échapper à la sortie, les ranger par des requêtes préparées. Le projet final du livre construit quelque chose de plus grand sur la même fondation, avec plus de routes, des classes contrôleur et une vraie couche de vues, et rien ne change dans les idées de fond. Vous avez déjà fait la partie qui compte.
