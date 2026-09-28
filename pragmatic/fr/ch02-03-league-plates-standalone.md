# Des templates sans framework : League/Plates

Dès qu'un script doit produire du HTML plutôt qu'un bloc JSON ou une ligne de log, les `echo` mélangés à la logique deviennent illisibles à toute vitesse. **Plates est un moteur de templates écrit en PHP pur : aucune syntaxe nouvelle**, seulement des fichiers PHP avec des layouts, des sections et un échappement automatique, utilisables depuis n'importe quel script.

```bash
composer require league/plates
```

```php
<?php
require 'vendor/autoload.php';

use League\Plates\Engine;

$templates = new Engine(__DIR__ . '/templates');

echo $templates->render('profile', ['name' => 'Ada']);
```

```php
<?php // templates/layout.php ?>
<!doctype html>
<html>
<head><title><?= $this->e($title ?? 'My Site') ?></title></head>
<body>
    <?= $this->section('content') ?>
</body>
</html>
```

```php
<?php // templates/profile.php ?>
<?php $this->layout('layout', ['title' => 'Profile']) ?>

<?php $this->start('content') ?>
    <h1>Hello, <?= $this->e($name) ?></h1>
<?php $this->stop() ?>
```

`$this->e()` échappe la sortie. C'est la même protection que vous offrent Twig ou Blade, écrite en toutes lettres au lieu d'être cachée derrière une autre syntaxe.

## Quand le choisir

Un petit outil interne, un générateur de rapports, ou un script qui rend une poignée de pages HTML et ne justifie pas toute la couche de templates d'un framework.

## Quand ce n'est pas le bon outil

Dès qu'un projet accumule des composants, des inclusions et plus d'une poignée de pages. Le moteur du framework (Blade chez Laravel, Twig chez Symfony) gagne alors sa place avec la réutilisation de composants et la compilation des assets, des fonctionnalités que Plates laisse volontairement de côté pour rester petit.

> **Sous le capot :** les templates Plates sont des fichiers PHP, donc pas d'étape de compilation ni de cache de templates à comprendre. Cette simplicité est toute la raison d'être de la bibliothèque, et c'est précisément ce que le moteur de templates d'un framework abandonne en échange de fonctionnalités supplémentaires.
