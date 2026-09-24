# Les méthodes magiques

Glissez un objet dans une chaîne de caractères, et PHP a une décision à prendre. Lisez une propriété que la classe n'a jamais déclarée, et il en a une autre. **Les méthodes magiques sont les crochets que PHP cherche à ces moments-là** : des méthodes au nom particulier, toujours précédé de deux tirets bas, que le langage appelle de lui-même quand une situation précise se présente. Vous en connaissez déjà deux.

## `__construct` et `__destruct`, en bref

`__construct()` tourne sous chaque `new` que vous avez écrit depuis le chapitre 5. PHP l'appelle à la création de l'objet, et c'est là que la promotion de constructeur fait son travail. `__destruct()` est son reflet : PHP l'appelle quand l'objet est sur le point de disparaître, en général quand la dernière variable qui le désigne sort de sa portée. Vous l'écrirez rarement. Le ramasse-miettes de PHP, vu au [chapitre 4](ch04-03-scope-and-gc.md), libère la mémoire tout seul, donc `__destruct()` sert aux cas où autre chose doit être relâché sans délai, un descripteur de fichier ou une connexion réseau, plutôt qu'à la fin du processus.

## `__toString()` : laisser un objet se comporter comme une chaîne

C'est celle que vous utiliserez le plus. Définissez-la, et PHP l'appelle partout où votre objet atterrit dans un contexte de chaîne : concaténation, interpolation, un simple `echo`.

```php
<?php
declare(strict_types=1);

final class Money
{
    public function __construct(
        private int $cents,
        private string $currency,
    ) {
    }

    public function __toString(): string
    {
        return sprintf('%.2f %s', $this->cents / 100, $this->currency);
    }
}

$price = new Money(4999, 'USD');

echo "Total: {$price}\n";
echo 'Total: ' . $price . "\n";
```

```console
$ php money.php
Total: 49.99 USD
Total: 49.99 USD
```

Aucun des deux `echo` ne nomme de méthode. PHP voit `$price` tomber dans une chaîne et appelle `__toString()` de lui-même. **Toute classe qui a une forme textuelle évidente (une somme d'argent, un nom, un identifiant) est une bonne candidate.** Le type de retour doit être `string` ; renvoyer autre chose est une erreur fatale.

<img src="images/ch17-magic-buttons.png" alt="Un objet dessiné comme une boîte avec trois boutons sur le côté, __toString, __get et __call, et l'éléphant PHP qui appuie lui-même sur le bouton __toString au moment où l'objet est déposé dans une ligne de texte" width="520">

> Vous écrivez ce que fait le bouton. PHP décide quand appuyer dessus.

## `__get` et `__set` : des propriétés dynamiques

Ces deux-là se déclenchent quand le code lit ou écrit une propriété que la classe ne déclare pas :

```php
<?php
declare(strict_types=1);

final class Config
{
    private array $values = [];

    public function __get(string $name): mixed
    {
        return $this->values[$name] ?? null;
    }

    public function __set(string $name, mixed $value): void
    {
        $this->values[$name] = $value;
    }
}

$config = new Config();
$config->debug = true;

var_dump($config->debug);      // true
var_dump($config->unset_key);  // null
```

`$config->debug = true` ressemble à une écriture de propriété ordinaire. `Config` n'a pas de propriété `$debug`, alors PHP appelle `__set('debug', true)` à la place, et la valeur atterrit dans le tableau privé `$values`. Lire `$config->debug` déclenche `__get('debug')` de la même manière. **L'objet se comporte comme un sac dans lequel on peut tout déposer.**

Voyons le prix. Lisez `$config->debug` quelque part dans le code : rien ne vous dit d'où vient la valeur, ni même si elle existe. Votre éditeur ne peut pas la compléter. Un outil d'analyse statique comme PHPStan, vu au [chapitre 11](ch11-03-generic-style-code.md), ne peut pas la vérifier comme il vérifie une propriété déclarée. **Chaque accesseur magique échange un peu de code répétitif contre un code que les humains et les outils suivent moins bien.** Réservez-les aux cas où la forme dynamique est tout l'intérêt, un sac de configuration, une enveloppe autour de données externes à la forme imprévisible, et déclarez de vraies propriétés partout ailleurs.

## `__call` : intercepter les appels de méthode

`__call()` fait pour les méthodes ce que `__get` fait pour les propriétés : elle se déclenche quand le code appelle une méthode que l'objet n'a pas.

```php
<?php
declare(strict_types=1);

final class Logger
{
    public function __call(string $name, array $arguments): void
    {
        $level = strtoupper($name);
        echo "[{$level}] {$arguments[0]}\n";
    }
}

$logger = new Logger();
$logger->warning('Disk space is low.');
$logger->error('Connection refused.');
```

```console
$ php logger.php
[WARNING] Disk space is low.
[ERROR] Connection refused.
```

`Logger` n'a ni `warning()` ni `error()`. Chaque appel à une méthode absente atterrit dans `__call()`, avec le nom sous forme de `string` et les arguments sous forme d'`array`, et la méthode transforme ce nom en niveau de log. C'est une vraie technique ; certaines bibliothèques bâtissent là-dessus leurs API à l'allure fluide. Elle porte aussi la réserve de `__get`, en double : la définition de la classe ne dit rien des méthodes qui existent ni de ce qu'elles acceptent.

Essayez : déclarez une vraie méthode `warning()` dans `Logger`. Le premier appel va maintenant vers elle, et seul `error()` atteint encore `__call()`. PHP cherche d'abord une méthode déclarée, et ne se rabat sur la magie que s'il n'en trouve aucune.

Prenez `__call` quand cette souplesse vaut son prix. Sinon, une poignée de méthodes déclarées noir sur blanc rendra un meilleur service à votre lecteur, et à vos outils.
