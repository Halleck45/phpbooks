# C - Interfaces natives et méthodes magiques

Deux tables de référence : les interfaces SPL qui branchent vos objets sur les mécanismes intégrés du langage, et les méthodes magiques qui permettent à vos objets de s'insérer dans un comportement que PHP gérerait sinon tout seul.

## Interfaces natives

| Interface | Ce que son implémentation vous apporte |
|---|---|
| `Countable` | Vos objets fonctionnent avec `count()` |
| `ArrayAccess` | Vos objets acceptent la syntaxe `$obj[$key]` : lecture, écriture, isset et unset |
| `Iterator` | Vos objets se parcourent directement dans `foreach`, avec un contrôle total sur l'itération |
| `IteratorAggregate` | Vos objets se parcourent dans `foreach` en déléguant à un autre itérateur, souvent un `Generator` |
| `Stringable` | Vos objets s'utilisent partout où une chaîne de caractères est attendue |

`Stringable` fait bande à part : ajoutée en PHP 8, vous avez rarement besoin de l'implémenter vous-même, car toute classe qui définit `__toString()` est automatiquement considérée comme l'implémentant. Elle existe surtout pour qu'une déclaration de type puisse dire « n'importe quoi d'affichable » sans énumérer toutes les classes qui se trouvent avoir une méthode `__toString()`.

Des exemples complets des cinq, y compris ce qu'`Iterator` exige de vous et qu'`IteratorAggregate` ne demande pas, sont au [chapitre 20](ch20-02-built-in-interfaces.md).

## Méthodes magiques

| Méthode | Appelée quand |
|---|---|
| `__construct` | Un objet est créé |
| `__destruct` | Un objet est sur le point d'être détruit |
| `__get` | On lit une propriété inaccessible ou non définie |
| `__set` | On écrit dans une propriété inaccessible ou non définie |
| `__call` | On appelle une méthode d'instance inaccessible ou non définie |
| `__callStatic` | On appelle une méthode statique inaccessible ou non définie |
| `__toString` | L'objet est utilisé dans un contexte de chaîne de caractères |
| `__invoke` | L'objet est appelé comme s'il était une fonction |
| `__clone` | L'objet est dupliqué avec `clone` |

« Magique » est le mot de PHP pour les méthodes que le langage appelle à votre place, par convention de nommage, plutôt que vous directement. Utiles pour construire des propriétés chargées à la demande ou des proxys fluides, elles glissent facilement vers un code que personne ne peut suivre en le lisant. Le [chapitre 17](ch17-03-magic-methods.md) les traite en entier, compromis compris.
