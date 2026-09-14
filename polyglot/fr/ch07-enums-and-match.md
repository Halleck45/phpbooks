# Énumérations et match

**Une énumération PHP est une classe dotée d'un ensemble fixe d'instances, et `match` est l'expression qui choisit une branche par instance.** Ensemble, ils remplacent le motif constantes-de-classe-plus-`switch` dont le vieux code PHP est rempli. Si vous connaissez les enums de Java, vous savez déjà presque tout ; si vous venez de l'`Enum` de Python ou des unions de littéraux de chaîne de TypeScript, la forme vous sera familière et les vérifications plus strictes.

```php
<?php
declare(strict_types=1);

enum Status: string
{
    case Draft = 'draft';
    case Published = 'published';
    case Archived = 'archived';

    public function label(): string
    {
        return match ($this) {
            self::Draft => 'Draft',
            self::Published => 'Live',
            self::Archived => 'Archived',
        };
    }

    public function canEdit(): bool
    {
        return $this !== self::Archived;
    }
}

$status = Status::from('published');   // Status::Published
echo $status->label(), PHP_EOL;         // Live
echo $status->value, PHP_EOL;           // published
var_dump($status->canEdit());           // bool(true)
var_dump(Status::tryFrom('deleted'));   // NULL
```

## Cas, valeurs et méthodes

Une énumération (PHP 8.1) déclare ses `case` et rien d'autre ne peut en être un. `Status::Draft` est un objet, le seul de son espèce, donc **deux références au même cas sont le même objet, et `===` est la comparaison à utiliser**. Les énumérations ne s'instancient pas avec `new`, ne s'étendent pas, et ne portent aucun état, ni propriétés ni données par instance. En revanche, elles peuvent avoir des méthodes, des constantes, des méthodes statiques et des interfaces à implémenter.

Le `: string` après le nom en fait une énumération adossée, dont chaque cas porte un scalaire (`string` ou `int`) accessible via `->value`. `from()` retransforme un scalaire en cas et lève une `ValueError` quand rien ne correspond, tandis que `tryFrom()` renvoie `null` à la place. C'est par ce duo qu'une énumération franchit une frontière, qu'il s'agisse d'une colonne en base, d'un champ JSON ou d'un paramètre d'URL. Une énumération pure, déclarée sans type adossé, a des cas mais pas de `->value`, et convient quand le choix ne quitte jamais votre code.

`cases()` renvoie tous les cas dans l'ordre de déclaration, ce que veulent une liste déroulante ou une règle de validation :

```php
$allowed = array_map(fn (Status $s) => $s->value, Status::cases());
// ['draft', 'published', 'archived']
```

Chaque cas a aussi un `->name` (`'Draft'`), utile pour les journaux.

Comme `$this` dans une méthode d'énumération est un cas, le comportement qui dépend du cas appartient à l'énumération plutôt qu'à des chaînes de `if` éparpillées dans le code. `label()` et `canEdit()` ci-dessus illustrent ce motif, où l'énumération sait ce que chacun de ses cas signifie.

Depuis PHP 8.2, les cas d'énumération sont autorisés dans les expressions constantes, donc comme valeurs par défaut de paramètres, constantes de classe et arguments d'attributs : `public function __construct(private Status $status = Status::Draft)`.

<img src="images/ch07-enum-boundary.png" alt="Une petite usine avec trois casiers étiquetés Draft, Published et Archived. Une chaîne 'published' arrive sur un tapis roulant par une porte marquée from et est dirigée vers le casier Published ; une chaîne 'deleted' arrive et est renvoyée avec un panneau null" width="560">

## match

`match` (PHP 8.0) ressemble à `switch` et se comporte comme une expression en Rust ou un `when` en Kotlin, avec un comportement qui se résume à ce qui suit.

**Il renvoie une valeur.** `$label = match ($status) { ... };` et `return match (...)` sont les usages normaux. Il n'y a pas de `break`, parce qu'il n'y a pas de passage à la branche suivante, et exactement une branche s'exécute.

**Il compare avec `===`.** `match ('1') { 1 => 'int', '1' => 'string' }` choisit la seconde branche, là où `switch` aurait choisi la première.

**Il doit être exhaustif.** Si aucune branche ne correspond et qu'il n'y a pas de `default`, PHP lève `UnhandledMatchError`. Si vous ajoutez un cas à une énumération et oubliez de mettre à jour un `match` qui la lit, la première fois que ce cas atteint le `match` vous obtenez une exception qui nomme la ligne exacte, plutôt qu'un `null` silencieux.

**Une branche peut lister plusieurs valeurs**, séparées par des virgules :

```php
<?php
declare(strict_types=1);

enum Status: string
{
    case Draft = 'draft';
    case Published = 'published';
    case Archived = 'archived';
}

function isVisible(Status $status): bool
{
    return match ($status) {
        Status::Published => true,
        Status::Draft, Status::Archived => false,
    };
}
```

Les analyseurs statiques comprennent cette règle, et PHPStan comme Psalm signalent un `match` sur une énumération qui laisse un cas non traité, avant même qu'il s'exécute.

Le sujet d'un `match` n'est pas forcément une énumération. Toute valeur convient, et l'idiome `match (true)` en fait une échelle de conditions qui produit une valeur :

```php
$size = match (true) {
    $bytes < 1024 => 'small',
    $bytes < 1024 * 1024 => 'medium',
    default => 'large',
};
```

Chaque branche est comparée avec `===` à `true`, donc chaque branche est une expression booléenne, ce qui se lit mieux qu'un ternaire imbriqué et ne peut pas passer à la branche suivante.

`switch` existe toujours, avec sa comparaison lâche, son passage à la branche suivante et ses `break`, et vous le croiserez dans du code plus ancien. Dans du code neuf, `match` est le bon choix par défaut, et `switch` sert au cas rare où vous voulez vraiment que plusieurs étiquettes partagent un bloc d'instructions.

## Null et throw comme expressions

Deux opérateurs se marient naturellement avec `match` et les énumérations. L'opérateur nullsafe `?->` (PHP 8.0) court-circuite une chaîne quand le côté gauche vaut `null`, de sorte que `$order?->customer?->email` vaut `null` si un maillon est `null`, au lieu de provoquer une erreur. Combiné à `??`, il donne une valeur par défaut en une ligne : `$email = $order?->customer?->email ?? 'nobody@example.org';`.

`throw` est une expression (PHP 8.0), donc il peut se placer à droite d'un `??`, dans un ternaire ou dans une branche de `match` :

```php
$status = Status::tryFrom($input) ?? throw new \InvalidArgumentException("Unknown status: $input");

$handler = match ($status) {
    Status::Draft => $this->saveDraft(...),
    Status::Published => $this->publish(...),
    Status::Archived => throw new \LogicException('Archived items are read-only'),
};
```

Le second exemple montre aussi le motif du dispatch, un `match` qui renvoie un callable, suivi de `$handler($item)`.

## Persistance et comportement au même endroit

Dans une application, les trois idées se retrouvent dans une même déclaration : une énumération adossée pour le stockage, des méthodes pour le comportement, et `match` là où vivent les branches.

```php
<?php
declare(strict_types=1);

interface HasColor
{
    public function color(): string;
}

enum Priority: int implements HasColor
{
    case Low = 1;
    case Normal = 2;
    case High = 3;

    public const DEFAULT = self::Normal;

    public static function fromLabel(string $label): self
    {
        return match (strtolower($label)) {
            'low' => self::Low,
            'normal', 'medium' => self::Normal,
            'high', 'urgent' => self::High,
            default => throw new \ValueError("Unknown priority: $label"),
        };
    }

    public function color(): string
    {
        return match ($this) {
            self::Low => 'grey',
            self::Normal => 'blue',
            self::High => 'red',
        };
    }

    public function escalate(): self
    {
        return match ($this) {
            self::Low => self::Normal,
            self::Normal, self::High => self::High,
        };
    }
}

$p = Priority::fromLabel('medium');
echo $p->color(), PHP_EOL;              // blue
echo $p->escalate()->name, PHP_EOL;     // High
echo Priority::DEFAULT->value, PHP_EOL; // 2
```

L'entier part en base et l'énumération circule partout ailleurs. Il n'y a pas de constante `PRIORITY_HIGH = 3` à garder synchronisée avec une table de couleurs quelque part, parce que le cas et son comportement vivent dans un seul fichier.

Face au motif ancien, constantes de classe plus drapeaux de chaîne plus `switch`, une énumération vous donne un vrai type à mettre dans une signature (`function assign(Priority $p)`), vérifié par le moteur, et un ensemble fermé sur lequel l'analyseur peut raisonner.

## Le piège

Deux habitudes venues d'autres langages, et du vieux PHP, provoquent le même bug.

La première consiste à reprendre `switch`, qui compare de façon lâche : `switch (Status::Draft)` avec `case 'draft':` ne correspond jamais, puisqu'une énumération n'est pas égale à sa valeur quelle que soit la comparaison, et avec un sujet de type chaîne un `case 0:` correspond à plus de choses que vous ne l'imaginez.

La seconde consiste à comparer une énumération à sa valeur adossée, alors que `$status == 'published'` vaut toujours `false`, l'énumération étant un objet et la chaîne ce qu'elle stocke. Comparez des cas à des cas (`$status === Status::Published`), ou convertissez d'abord (`$status->value === 'published'`).

La question suivante, pour un développeur venu d'ailleurs, est ce qui se passe quand quelque chose tourne mal, et le chapitre [Erreurs et exceptions](ch08-errors-and-exceptions.md) décrit un modèle qui mêle deux mécanismes.
