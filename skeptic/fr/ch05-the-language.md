# Le langage en 2026

Est-ce un langage que vous auriez envie d'écrire pendant quelques années ? Aucun benchmark ne répond à cela ; vous y répondez en lisant du code. **PHP est aujourd'hui un langage orienté objet, avec ramasse-miettes, aux types déclarés et appliqués à l'exécution aux frontières des fonctions et des propriétés, doté d'énumérations, d'immutabilité, de closures, d'attributs et d'un gestionnaire de paquets.** Un exemple suffit pour le juger, et chaque construction plus jeune que 2022 porte la version qui l'a introduite, pour que vous sachiez ce qu'un projet donné peut utiliser.

## Un exemple complet

```php
<?php
declare(strict_types=1);

enum Status: string
{
    case Draft = 'draft';
    case Published = 'published';
    case Archived = 'archived';

    public function isVisible(): bool
    {
        return $this === self::Published;
    }
}

final readonly class Article
{
    public function __construct(
        public string $title,
        public Status $status,
        public ?\DateTimeImmutable $publishedAt = null,
    ) {
    }

    public function publish(\DateTimeImmutable $at): static
    {
        return new static($this->title, Status::Published, $at);
    }
}

function summary(Article ...$articles): string
{
    $visible = array_filter($articles, fn (Article $a): bool => $a->status->isVisible());
    $titles = array_map(fn (Article $a): string => $a->title, $visible);

    return match (count($titles)) {
        0 => 'nothing published',
        1 => $titles[array_key_first($titles)],
        default => implode(', ', $titles),
    };
}

$draft = new Article(title: 'Benchmarks', status: Status::Draft);
$live = $draft->publish(new \DateTimeImmutable('2026-09-01'));

echo summary($draft, $live), PHP_EOL;   // Benchmarks
echo $draft->status->value, PHP_EOL;    // draft
```

Lisez-le comme vous liriez une pull request. `declare(strict_types=1)` passe le fichier en typage strict : une chaîne passée là où un `int` est déclaré lève une `TypeError` au lieu d'être convertie. L'interrupteur agit fichier par fichier, et un projet l'active dans chacun. L'`enum` est une vraie énumération, un ensemble fermé d'objets singletons qui peuvent porter des méthodes et une valeur sous-jacente. La classe `readonly` (PHP 8.2) rend chaque propriété immuable après construction, et son constructeur déclare et affecte ces propriétés en un seul endroit.

Le reste de la syntaxe, vous le connaissez déjà d'ailleurs : les arguments nommés à l'appel, `?` pour les types nullables, `static` comme type de retour, `fn` pour les closures d'une ligne, et un `match` qui compare strictement, ne tombe jamais dans la branche suivante et lève une exception quand aucune branche ne correspond.

Ce que l'exemple ne montre pas compte tout autant. Chaque frontière y est typée, alors que le langage ne l'exige pas ; la lecture d'une variable non définie est un avertissement en PHP 8, et les analyseurs statiques en font une erreur. Le sigle `$` sur les variables et la flèche `->` pour l'accès aux membres sont les deux morceaux de syntaxe qui paraissent étrangers à tout le monde, et au bout d'une heure on ne les voit plus.

## Les ajouts récents

Les deux dernières versions ont changé la façon d'écrire le code, et un projet sur PHP 8.4 ou plus récent utilisera ce qu'elles ont apporté.

```php
// PHP 8.4
final class Money
{
    public function __construct(
        public private(set) int $cents,
        public string $currency,
    ) {
    }

    public string $formatted {
        get => number_format($this->cents / 100, 2) . ' ' . $this->currency;
    }
}

$price = new Money(1999, 'EUR');
echo $price->formatted, PHP_EOL;     // 19.99 EUR
$price->cents = 5;                   // Error: Cannot modify private(set) property Money::$cents
```

`public private(set)` est la visibilité asymétrique (PHP 8.4) : la propriété se lit de partout et ne s'écrit que depuis l'intérieur de la classe, ce qui supprime la plupart des getters qu'un développeur Java ou C# s'attend à écrire. Le bloc `get` sous `$formatted` est un hook de propriété (PHP 8.4), une logique attachée à une propriété sans changer ses sites d'appel, et cela supprime la plupart des autres. L'opérateur pipe (PHP 8.5) enchaîne les fonctions de gauche à droite :

```php
// PHP 8.5
$slug = '  Hello, World  '
    |> trim(...)
    |> strtolower(...)
    |> (fn (string $s): string => preg_replace('/[^a-z0-9]+/', '-', $s))
    |> (fn (string $s): string => trim($s, '-'));

echo $slug, PHP_EOL;   // hello-world
```

La forme `trim(...)` est un callable de première classe (PHP 8.1), une référence à une fonction sous forme de valeur, avec l'arité vérifiée par le moteur. Ajoutez les attributs, des métadonnées structurées lues par réflexion et utilisées par tous les frameworks pour le routage, la validation et le mapping, et vous avez les constructions que vous croiserez le plus dans une base de code démarrée après 2024.

<img src="images/ch05-two-listings.png" alt="Deux listings de code côte à côte sur un bureau, vus de dessus. Celui de gauche est sur du papier jauni, dense, avec quelques taches de café et des soulignements ondulés. Celui de droite est sur une feuille blanche propre, plus court, avec une indentation nette et quelques annotations de type surlignées. Un petit éléphant lit la feuille de droite, un stylo à la main" width="560">

## Ce que le système de types fait et ne fait pas

**Les types sont déclarés sur les paramètres, les valeurs de retour, les propriétés et les constantes de classe, et le moteur les applique à l'exécution.** Les types union (`int|string`), les types intersection (`Countable&Traversable`), les types nullables, `never`, `mixed` et les énumérations font tous partie du langage. Une erreur de type est une exception, pas un avertissement, et en mode strict il n'y a aucune coercition implicite entre scalaires, à l'exception de l'élargissement d'un `int` en `float`.

Ce qui manque, autant l'entendre de moi maintenant que le découvrir la troisième semaine. **Il n'y a pas de génériques dans le langage.** Un `list<Order>` ne peut pas s'exprimer dans une signature ; le paramètre est `array`. L'écosystème répond par une syntaxe de docblock que les deux analyseurs statiques, PHPStan et Psalm, comprennent et appliquent. `@param list<Order> $orders` est vérifié au moment de l'analyse, dans l'éditeur et en intégration continue, avec les types template, les types conditionnels et les types de forme, plus riches que tout ce que le langage lui-même sait exprimer ; un projet PHP typé exécute donc un analyseur à son niveau le plus strict à chaque build et traite sa sortie comme des erreurs de compilation. Que ce soit un substitut acceptable à des génériques dans le langage, c'est à vous d'en juger, selon vos propres habitudes. C'est un substitut, et vous devriez le peser comme tel.

L'autre absence vient du runtime plutôt que du langage : pas de threads en userland ni de boucle d'événements intégrée. [Concurrence](ch04-concurrency.md) décrit ce qui existe à la place.

## La bibliothèque standard

`strpos` voisine avec `str_replace`, `array_key_exists` avec `in_array`, et certaines fonctions prennent l'aiguille en premier quand d'autres prennent la botte de foin. Cette incohérence est historique, elle est réelle, et elle ne disparaîtra pas. Depuis PHP 8.0, les nouvelles fonctions suivent un seul schéma de nommage (`str_contains`, `array_is_list`, `array_find`), les fonctions internes lèvent `TypeError` et `ValueError` sur une entrée invalide au lieu de retourner `false`, et tout éditeur doté d'un serveur de langage PHP complète les noms ; c'est ainsi qu'une équipe vit avec le reste. La seconde verrue, ce sont les chaînes, qui sont des suites d'octets : `strlen('é')` vaut 2, et le traitement du texte passe par la famille `mb_`. Voilà les deux que vous rencontrerez en premier.

> La limite : le système de types de PHP est appliqué à l'exécution et aux frontières des fonctions et des propriétés, pas à l'intérieur des expressions ni à travers les conteneurs génériques. Une équipe qui veut des garanties à la compilation sur ses collections les obtient d'un analyseur statique, pas du langage.

## Ce que vous pouvez vérifier vous-même

Installez PHP 8.5 (votre gestionnaire de paquets, ou l'image Docker officielle `php:8.5-cli`), collez le premier exemple dans un fichier et lancez-le avec `php file.php`. Puis cassez-le : passez une chaîne là où l'énumération `Status` est attendue, retirez `strict_types`, écrivez un `match` sur l'énumération en oubliant un cas, puis appelez-le avec ce cas. Les messages d'erreur sont la partie d'un langage avec laquelle on vit, et cinq minutes suffisent pour les juger. Pour le système de types, lancez PHPStan ou Psalm à son niveau le plus strict sur n'importe quel projet PHP open source d'une taille qui vous parle, et lisez les vingt premiers résultats ; ils vous montrent ce que l'analyseur attrape et que le moteur laisse passer.
