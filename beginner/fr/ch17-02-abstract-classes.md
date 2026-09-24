# Classes abstraites et interfaces, deuxième passage

Rien ne vous empêche d'écrire `new PaymentMethod()` et de lui débiter quarante-deux dollars. La classe de base de la section précédente a un `charge()` qui fonctionne, alors PHP obéit, et l'argent est « débité » sur un moyen de paiement qui n'est rattaché à aucune carte, aucun compte, rien du tout. `PaymentMethod` n'a jamais été conçue que comme une fondation pour ses sous-classes, mais un commentaire qui le dit n'est pas une règle. **`abstract` transforme cette intention en quelque chose que PHP fait respecter.**

## Rendre le contrat explicite

```php
<?php
declare(strict_types=1);

abstract class PaymentMethod
{
    abstract public function charge(float $amount): string;

    protected function receipt(float $amount): string
    {
        return sprintf('$%.2f processed on %s', $amount, date('Y-m-d'));
    }
}

class CreditCard extends PaymentMethod
{
    public function __construct(private string $last4)
    {
    }

    public function charge(float $amount): string
    {
        return $this->receipt($amount) . " (card ending {$this->last4})";
    }
}
```

Deux choses ont changé. `abstract class PaymentMethod` signifie que PHP refuse `new PaymentMethod()` tout net : une erreur fatale, imposée par le langage plutôt que laissée à une convention que vous espérez voir respectée. Et `charge()` est devenue `abstract public function charge(float $amount): string;`, une signature sans corps, exactement comme une méthode d'interface. **Toute sous-classe non abstraite doit désormais implémenter `charge()`, sinon PHP refuse aussi de charger cette sous-classe.**

Ce que la classe de base a gardé, c'est `receipt()` : une vraie méthode, qui fonctionne, dont chaque sous-classe hérite gratuitement. Ce couple est tout l'intérêt d'une classe abstraite. **Un contrat que le langage fait respecter, livré avec du code partagé écrit une seule fois.** Une simple interface ne peut vous donner que la première moitié.

<img src="images/ch17-blueprint-vs-badge.png" alt="À gauche, une classe abstraite dessinée comme une maison en chantier : une fondation solide étiquetée receipt() et des murs en pointillés étiquetés charge(), laissés à la sous-classe. À droite, une interface dessinée comme un petit badge Formattable épinglé sur trois objets qui n'ont rien d'autre en commun" width="600">

> [!TIP]
> `receipt()` est `protected` : visible depuis `PaymentMethod` et ses sous-classes, invisible pour tout le reste. C'est la visibilité habituelle d'une méthode utilitaire qu'une classe de base offre à ses enfants et à personne d'autre.

## Comparez avec `Formattable`

Revenez à l'interface `Formattable` du [chapitre 11](ch11-01-interfaces.md) :

```php
<?php
interface Formattable
{
    public function format(): string;
}
```

Une interface n'est rien d'autre qu'un contrat. **Aucun corps de méthode, pas même un corps facultatif dont une classe pourrait hériter.** Chaque classe qui implémente `Formattable` écrit son propre `format()` de zéro, parce qu'il n'y a rien à hériter.

Ce n'est pas un défaut, c'est sa fonction. Une interface nomme une capacité que des classes sans rien d'autre en commun peuvent toutes revendiquer. Un `Product`, une `LogEntry` et une `HttpResponse` n'ont aucun ancêtre commun et n'en auront jamais, et pourtant chacun peut promettre `format()`. Une classe peut implémenter autant d'interfaces qu'elle veut, et c'est ainsi que PHP se passe d'héritage multiple. Une classe abstraite, elle, est un véritable ancêtre : une classe ne peut en étendre qu'une seule, et tout ce que le parent porte vient avec, propriétés, méthodes concrètes, logique de constructeur.

> Une interface est un badge que la classe porte. Une classe abstraite est un parent dont elle descend. Vous avez droit à un seul parent, et à autant de badges que vous voulez.

## Laquelle choisir

Prenez une **classe abstraite** quand vous avez du vrai code que toutes les sous-classes doivent partager, et que vous voulez en plus forcer chacune à remplir les parties qui doivent différer. `receipt()` partagée, `charge()` obligatoire mais propre à chaque sous-classe : l'exemple ci-dessus est le cas d'école.

Prenez une **interface** quand tout ce qu'il vous faut est la garantie qu'une méthode existe, sans supposer que les classes soient apparentées. C'est aussi la seule option quand une classe étend déjà quelque chose et doit encore promettre une seconde capacité sans rapport.

Les deux ne sont pas rivales, et PHP ne vous oblige pas à choisir :

```php
<?php
declare(strict_types=1);

interface Formattable
{
    public function format(): string;
}

abstract class PaymentMethod implements Formattable
{
    abstract public function charge(float $amount): string;

    public function format(): string
    {
        return static::class;
    }
}
```

`PaymentMethod` a les deux. La structure imposée d'une classe abstraite pour sa propre famille de sous-classes, et un badge `Formattable` à part, qui permet à n'importe quel code du système d'appeler `format()` dessus sans savoir, ni se soucier, qu'il s'agit de paiements. `static::class` est le nom de la classe concrète à l'exécution, donc une `CreditCard` se formate en `CreditCard`, et le parent n'a jamais eu besoin de connaître ses enfants par leur nom.
