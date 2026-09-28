# Valider les entrées : Respect/Validation

Chaque formulaire, chaque charge utile d'API, chaque envoi de CSV pose la même question : ces données sont-elles utilisables ? **Respect/Validation y répond avec des règles lisibles et chaînables**, sans avoir besoin du cycle de requête d'un framework autour.

```bash
composer require respect/validation
```

```php
<?php
require 'vendor/autoload.php';

use Respect\Validation\Validator as v;

$validator = v::key('email', v::email())
    ->key('age', v::intVal()->between(18, 120))
    ->key('username', v::alnum()->length(3, 20));

try {
    $validator->assert([
        'email' => 'ada@example.com',
        'age' => 34,
        'username' => 'ada_l',
    ]);
    echo "Valid.\n";
} catch (\Respect\Validation\Exceptions\NestedValidationException $e) {
    foreach ($e->getMessages() as $message) {
        echo "- {$message}\n";
    }
}
```

Les règles se lisent presque comme de l'anglais et se combinent librement. `v::stringType()->notEmpty()->length(1, 255)` ou `v::arrayType()->each(v::stringType())` couvrent l'essentiel des besoins d'un formulaire ou d'une API, sans règle sur mesure.

## Quand le choisir

Un script ou un petit service qui reçoit des données de l'extérieur : un import CSV, un récepteur de webhooks, une API légère. Tout un framework pour sa seule couche de validation serait disproportionné.

## Quand ce n'est pas le bon outil

Dès que vous êtes dans Laravel ou Symfony. `$request->validate()` et le composant Validator de Symfony sont câblés aux formulaires et à l'affichage des erreurs de leur framework, et sont là le meilleur choix par défaut.

> **Sous le capot :** les bibliothèques de validation s'appuient sur le système de types de PHP bien plus qu'autrefois. Sous les appels fluides comme `v::intVal()`, les versions récentes décrivent « valide » avec les types union et les enums de PHP plutôt qu'en réinventant les vérifications de type.
