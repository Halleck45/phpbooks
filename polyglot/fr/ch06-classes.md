# Les classes

**Une classe PHP moderne est courte, typée et presque entièrement immuable.** Le constructeur déclare les propriétés, les types sont vérifiés à l'exécution, et l'essentiel du code répétitif que vous connaissez de Java, ou de PHP 5, a disparu. L'exemple ci-dessous montre une classe complète :

```php
<?php
declare(strict_types=1);

namespace App\Billing;

final class Invoice
{
    private array $lines = [];

    public function __construct(
        public readonly string $number,
        public readonly \DateTimeImmutable $issuedAt,
    ) {
    }

    public function addLine(string $label, int $cents): static
    {
        $this->lines[] = ['label' => $label, 'cents' => $cents];

        return $this;
    }

    public function total(): int
    {
        return array_sum(array_column($this->lines, 'cents'));
    }
}

$invoice = new Invoice('2026-0042', new \DateTimeImmutable('2026-09-14'));
$invoice->addLine('Hosting', 1200)->addLine('Support', 800);

echo $invoice->number, ': ', $invoice->total(), PHP_EOL; // 2026-0042: 2000
```

En la lisant de haut en bas, vous rencontrez d'abord `namespace`, qui place la classe dans `App\Billing`, de sorte que son nom complet est `App\Billing\Invoice` (le chapitre [Namespaces, Composer et autoloading](ch09-composer-and-namespaces.md) explique comment ce nom correspond à un fichier). `final` interdit l'héritage, et le code PHP moderne rend les classes `final` par défaut pour ne les ouvrir qu'à dessein. Le constructeur n'a pas de corps, parce qu'**écrire `public readonly string $number` dans la liste des paramètres déclare la propriété, la type et l'affecte en une seule ligne**. Cette promotion de propriétés dans le constructeur (PHP 8.0) a retiré l'essentiel de la cérémonie des classes PHP. `readonly` (PHP 8.1) rend la propriété affectable une seule fois, dans le constructeur, et plus jamais ensuite. Enfin, `static` comme type de retour signifie « la classe de l'objet sur lequel la méthode a été appelée », ce qui est exactement ce qu'une méthode fluide veut promettre.

L'accès aux membres passe par deux symboles : `->` atteint un membre d'instance, `::` atteint un membre statique ou une constante. `$this` est l'objet courant, et vous l'écrivez toujours puisqu'il n'y a pas de `this` implicite.

## Les objets circulent par identifiant

Les tableaux se copient quand vous les affectez, comme le chapitre [Les tableaux](ch04-arrays.md) l'explique, mais les objets suivent la règle inverse. **Affecter ou passer un objet copie un identifiant qui désigne le même objet**, comme le font Java, Python et JavaScript :

```php
<?php
declare(strict_types=1);

final class Cart
{
    public array $items = [];
}

function addApple(Cart $cart): void
{
    $cart->items[] = 'apple';
}

$cart = new Cart();
addApple($cart);
echo count($cart->items), PHP_EOL; // 1, the caller sees the change
```

Ce comportement ne doit rien au `&` des paramètres par référence, qui sont un mécanisme différent, réservé aux variables, et dont vous n'avez presque jamais besoin avec des objets.

`clone $cart` fait une copie superficielle, c'est-à-dire un nouvel objet dont les propriétés contiennent les mêmes valeurs, de sorte qu'un objet rangé à l'intérieur est partagé entre les deux copies. Définissez `__clone()` si la copie a besoin de ses propres objets internes.

Pour comparer deux objets, `==` compare l'état propriété par propriété, tandis que `===` demande si les deux côtés sont le même objet, ce qui explique que `$a === clone $a` vaille `false`.

<img src="images/ch06-handle-vs-copy.png" alt="À gauche : deux variables qui tiennent deux boîtes séparées étiquetées array, chacune avec son propre contenu. À droite : deux variables qui tiennent des ficelles attachées à une seule boîte étiquetée object, de sorte que les deux tirent sur la même chose" width="560">

## L'immuabilité sans accesseurs

La classe PHP 5 classique avait une propriété privée, un getter, et parfois un setter. Ce motif a été remplacé par des fonctionnalités récentes que vous verrez dans toutes les bases de code écrites après 2024.

La première est `readonly`, que vous avez déjà rencontré. Quand toutes les propriétés d'une classe sont readonly, marquez plutôt la classe elle-même (PHP 8.2) :

```php
<?php
declare(strict_types=1);

final readonly class Money
{
    public function __construct(
        public int $amount,
        public string $currency,
    ) {
    }

    public function add(Money $other): self
    {
        return new self($this->amount + $other->amount, $this->currency);
    }
}
```

Chaque propriété est publique et personne ne peut la modifier, ce qui vous donne un objet valeur sans le moindre getter.

**La visibilité asymétrique (PHP 8.4) laisse l'extérieur lire une propriété que seule la classe peut écrire :**

```php
// PHP 8.4
final class Counter
{
    public private(set) int $count = 0;

    public function increment(): void
    {
        $this->count++;
    }
}

$c = new Counter();
$c->increment();
echo $c->count; // 1
$c->count = 5;  // Error: Cannot modify private(set) property Counter::$count
```

Le getter n'a plus de raison d'être. Là où il vous faut de la logique à la lecture ou à l'écriture, les hooks de propriété (PHP 8.4) l'attachent à la propriété elle-même, comme une propriété C# ou le `@property` de Python :

```php
// PHP 8.4
final class User
{
    public string $email {
        set(string $value) {
            if (!filter_var($value, FILTER_VALIDATE_EMAIL)) {
                throw new \InvalidArgumentException("Invalid email: $value");
            }
            $this->email = strtolower($value);
        }
    }

    public string $domain {
        get => substr($this->email, strpos($this->email, '@') + 1);
    }
}

$u = new User();
$u->email = 'Ada@Example.org';
echo $u->domain; // example.org
```

Pour l'appelant, ce sont des propriétés ordinaires, alors qu'à l'intérieur `set` valide et normalise pendant que `get` calcule. Une propriété avec un seul hook `get` et sans stockage est simplement une propriété calculée.

## Interfaces, classes abstraites, traits

Les interfaces et les classes abstraites fonctionnent comme en Java et en C# : une interface liste des signatures de méthodes et des constantes, une classe abstraite peut porter de l'implémentation, une classe implémente plusieurs interfaces et étend un seul parent. `#[\Override]` (PHP 8.3) sur une méthode fait vérifier à PHP que le parent la possède vraiment, ce qui attrape les fautes de frappe dans les redéfinitions.

Les traits, eux, n'ont pas d'équivalent exact dans la plupart des langages. **Un trait est un bloc de méthodes et de propriétés que le compilateur copie dans chaque classe qui l'utilise avec `use`.** Les mixins de Ruby en sont le repère le plus proche, alors que les traits de Rust, malgré le nom, décrivent tout autre chose.

```php
<?php
declare(strict_types=1);

trait HasTimestamps
{
    private ?\DateTimeImmutable $createdAt = null;

    public function touch(): void
    {
        $this->createdAt ??= new \DateTimeImmutable();
    }
}

final class Article
{
    use HasTimestamps;
}

$a = new Article();
$a->touch();
```

Les traits sont pratiques pour les utilitaires transversaux et faciles à surutiliser, parce qu'une classe qui en utilise cinq vous impose cinq fichiers à lire pour savoir ce qu'elle fait. Préférez la composition quand vous le pouvez.

La différence entre `static` et `self` tient en quelques lignes : `self` nomme la classe où le code est écrit, tandis que `static` nomme la classe de l'objet à l'exécution. Dans une fabrique statique définie dans une classe parente, `new static()` construit donc la sous-classe réellement appelée, alors que `new self()` construit toujours le parent.

## Construction

PHP n'a qu'un constructeur par classe et ne connaît pas la surcharge de méthodes. Le manque est comblé par les arguments nommés (PHP 8.0) pour les paramètres optionnels, et par les fabriques statiques pour les autres façons de construire :

```php
<?php
declare(strict_types=1);

final readonly class Period
{
    private function __construct(
        public \DateTimeImmutable $start,
        public \DateTimeImmutable $end,
    ) {
    }

    public static function fromStrings(string $start, string $end): self
    {
        return new self(new \DateTimeImmutable($start), new \DateTimeImmutable($end));
    }

    public static function year(int $year): self
    {
        return self::fromStrings("$year-01-01", "$year-12-31");
    }
}

$fy = Period::year(2026);
echo $fy->end->format('Y-m-d'), PHP_EOL; // 2026-12-31
```

Un constructeur privé plus des fabriques publiques se lit aussi bien qu'un jeu de constructeurs surchargés, et chaque variante porte un nom.

Depuis PHP 8.4, vous pouvez chaîner un appel sur un objet fraîchement créé sans l'entourer de parenthèses : `new Period(...)->start` exigeait auparavant `(new Period(...))->start`.

Pour les objets immuables, « modifier » signifie « fabriquer une copie modifiée ». PHP 8.5 lui donne sa propre syntaxe : `clone($money, ['amount' => 500])` renvoie une copie avec les propriétés listées remplacées. Les règles de visibilité habituelles s'appliquent, et une propriété `readonly` ne s'écrit que depuis l'intérieur de sa classe, donc l'appel vit dans une méthode `withAmount()` plutôt que chez l'appelant. Avant 8.5, cette même méthode clonait puis affectait dans `__clone()`, ce que PHP 8.3 a autorisé pour les propriétés readonly.

## Chaînes, magie et métadonnées

Tout objet peut s'afficher lui-même en implémentant `__toString()`. Le déclarer fait automatiquement implémenter `Stringable` (PHP 8.0) à la classe, de sorte que vous pouvez typer un paramètre `string|Stringable` et accepter les deux.

Les autres méthodes à double tiret bas sont des crochets que le moteur appelle : `__get` et `__set` s'exécutent quand le code touche une propriété qui n'existe pas, `__call` quand il appelle une méthode qui n'existe pas. Les frameworks et les ORM s'en servent pour construire des API fluides et des modèles paresseux, et il suffit de savoir les reconnaître, sans les utiliser dans le code applicatif. Dans le même esprit, créer une propriété jamais déclarée (`$obj->foo = 1` sans `$foo` dans la classe) est déprécié depuis PHP 8.2 et doit devenir une erreur dans la prochaine version majeure, ce qui est une raison de plus de déclarer toutes vos propriétés.

**Les attributs (PHP 8.0) sont des métadonnées structurées sur une classe, une méthode, une propriété ou un paramètre, lues par réflexion.** Les annotations Java et les attributs C# sont le repère direct :

```php
<?php
declare(strict_types=1);

#[\Attribute(\Attribute::TARGET_METHOD)]
final readonly class Route
{
    public function __construct(public string $path) {}
}

final class HomeController
{
    #[Route('/')]
    public function index(): string
    {
        return 'Hello';
    }
}

$method = new \ReflectionMethod(HomeController::class, 'index');
foreach ($method->getAttributes(Route::class) as $attribute) {
    echo $attribute->newInstance()->path, PHP_EOL; // /
}
```

Un attribut est lui-même une classe marquée `#[\Attribute]`, et rien ne se passe à l'exécution tant que personne n'appelle `getAttributes()`, la métadonnée restant inerte jusqu'à sa lecture. Le routage, la validation, la sérialisation et les frameworks de test reposent tous sur ce mécanisme.

`Invoice::class` donne le nom pleinement qualifié sous forme de chaîne, ce que vous faites circuler au lieu d'écrire `'App\Billing\Invoice'` en dur. `$x instanceof Invoice` vérifie le type à l'exécution et vaut `false`, sans erreur, quand `$x` n'est pas un objet. Les objets paresseux (PHP 8.4) permettent d'instancier une classe sans exécuter son constructeur tant qu'une propriété n'est pas touchée, un outil pour les conteneurs d'injection de dépendances et les ORM plutôt que pour le code de tous les jours.

Le langage n'a pas de génériques, et une classe `Collection` contient du `mixed` aux yeux du moteur ; les docblocks `@template` décrits dans [Le système de types](ch03-types.md) donnent à PHPStan et Psalm ce qui manque au moteur.

## Le piège

Une fonction qui reçoit un objet et « l'ajuste juste un peu » ajuste aussi l'objet de l'appelant. Si vous vouliez une modification locale, faites d'abord un `clone`, ou concevez la classe en readonly et renvoyez une nouvelle instance.

Gardez aussi en tête que `readonly` est superficiel : il gèle la case de la propriété, pas ce vers quoi elle pointe. Un `readonly array $items` ne peut pas être réaffecté, mais un `readonly Cart $cart` laisse quiconque tient `$cart` y pousser des articles. L'immuabilité de tout le graphe reste une décision de conception, que le mot-clé ne prend pas à votre place.

Une fois les classes en main, reste à voir comment PHP représente un ensemble fermé de choix, ce qui est le sujet du chapitre [Énumérations et match](ch07-enums-and-match.md).
