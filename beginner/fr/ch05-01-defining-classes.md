# Définir et instancier une classe

Une classe est un plan. Elle dit quelles données un objet de ce type contient et, plus tard, ce qu'il sait faire. Un plan ne construit rien tout seul. **C'est avec `new` que vous demandez à PHP de bâtir un objet à partir du plan.**

## Définir une classe

```php
<?php
declare(strict_types=1);

class Rectangle
{
    public float $width;
    public float $height;
}
```

`class Rectangle { ... }` déclare le plan. À l'intérieur, `public float $width;` déclare une **propriété typée** : une case nommée que chaque `Rectangle` possédera, avec un type que PHP fait respecter à chaque affectation. C'est la même déclaration de type que vous posez sur les paramètres de fonction depuis le [chapitre 3](ch03-02-data-types.md), appliquée à une donnée qui vit sur un objet plutôt que dans un appel de fonction.

## Instancier une classe

**`new` construit un vrai objet à partir du plan. Cet objet s'appelle une instance :**

```php
<?php

$rect = new Rectangle();
$rect->width = 10.0;
$rect->height = 4.0;

echo $rect->width;  // 10
echo $rect->height; // 4
```

`new Rectangle()` vous remet un `Rectangle` bien réel, avec ses propres `$width` et `$height`, et `$rect` le tient. **La flèche `->` entre dans un objet pour lire ou écrire l'une de ses propriétés.** C'est l'équivalent, pour un objet, des crochets `[]` sur un tableau, sauf qu'un objet est beaucoup plus regardant sur ce qu'on y met, comme vous le verrez bientôt.

<img src="images/ch05-blueprint-instances.png" alt="Un plan intitulé Rectangle avec deux cases vides, width et height, et deux flèches marquées new qui mènent à deux rectangles séparés, un large avec les valeurs 10 et 4, un carré avec les valeurs 3 et 3" width="560">

Construisez un second `Rectangle`, et vous obtenez un objet vraiment distinct, avec son propre espace :

```php
<?php

$rect2 = new Rectangle();
$rect2->width = 3.0;
$rect2->height = 3.0;

echo $rect->width;  // 10, untouched by $rect2
echo $rect2->width; // 3
```

Un instant, parce que le [chapitre 4](ch04-02-references.md) vous a peut-être rendu méfiant envers les objets qui partagent une poignée. `$rect` et `$rect2` ne sont pas deux noms pour un même objet. Ils viennent de deux appels à `new` distincts, donc ce sont deux instances distinctes. **La règle « les objets s'aliasent, ils ne se copient pas » concerne l'affectation d'un objet existant à une autre variable, `$a = $b`. Chaque `new` construit un objet neuf.**

> Un plan, autant d'objets que vous en demandez. Chaque `new` en fait un nouveau.

## Construire avec `__construct`

Remplir chaque propriété à la main après `new` fonctionne, mais on en oublie facilement une, et pendant un instant un `Rectangle` à moitié bâti existe, avec des propriétés encore vides. PHP a une méthode spéciale pour ça. **`__construct()` s'exécute automatiquement à l'instant où l'objet est créé**, si bien que l'objet est complet dès son premier souffle :

```php
<?php
declare(strict_types=1);

class Rectangle
{
    public float $width;
    public float $height;

    public function __construct(float $width, float $height)
    {
        $this->width = $width;
        $this->height = $height;
    }
}

$rect = new Rectangle(10.0, 4.0);

echo $rect->width;  // 10
echo $rect->height; // 4
```

Tout ce que vous passez à `new Rectangle(...)` file directement à `__construct()`. À l'intérieur, `$this` est l'objet en cours de construction : `$this->width = $width` prend le paramètre reçu et le range dans la case `$width` de l'objet. `$this` aura droit à un examen plus attentif, avec une façon bien plus courte d'écrire exactement ce constructeur, dans [Méthodes et promotion des propriétés](ch05-03-methods.md).

## Visibilité : `public`, `private`, `protected`

Chaque propriété et chaque méthode a une **visibilité**, et jusqu'ici tout était `public` : accessible de partout, y compris depuis du code qui n'a rien à voir avec la classe. C'est souvent plus que vous ne voulez. **Marquez une propriété `private`, et seul le code à l'intérieur de la classe peut y toucher :**

```php
<?php
declare(strict_types=1);

class Rectangle
{
    private float $width;
    private float $height;

    public function __construct(float $width, float $height)
    {
        $this->width = $width;
        $this->height = $height;
    }
}

$rect = new Rectangle(10.0, 4.0);
echo $rect->width; // Error: Cannot access private property Rectangle::$width
```

<img src="images/ch05-visibility.png" alt="Une maison étiquetée Rectangle avec deux coffres verrouillés à l'intérieur, width et height, une porte fermée marquée private, et un guichet ouvert marqué public par lequel la valeur 10 est remise à un visiteur" width="360">

C'est une restriction voulue, pas un bug à contourner. Une fois `$width` privée, le seul moyen pour l'extérieur d'en connaître ou d'en changer la valeur passe par les méthodes que `Rectangle` choisit d'offrir. C'est donc `Rectangle` qui décide de ce qu'est une largeur valide, au lieu de faire confiance à tous ses appelants. Essayez : ajoutez `public function width(): float { return $this->width; }` à la classe et appelez `$rect->width()`. La valeur redevient lisible, aux conditions de la classe.

`protected` se place entre les deux : invisible de l'extérieur, visible depuis toute classe qui viendra plus tard étendre celle-ci. La distinction prendra son sens avec l'héritage, au [chapitre 17](ch17-00-object-oriented-php.md).

> [!TIP]
> Partez sur `private`. Ne passez une propriété en `public` que pour une raison précise, et offrez une méthode au code extérieur quand il a vraiment besoin d'y accéder.
