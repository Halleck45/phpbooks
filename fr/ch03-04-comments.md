# Les commentaires

Le jeu de devinette n'a aucun commentaire, et à trente lignes il n'en a pas besoin. Mais les programmes grandissent, et tôt ou tard une ligne réclame une note à côté d'elle : pourquoi cette vérification est là, ce que signifie ce nombre, quel bug elle contourne. **Un commentaire est un texte que PHP ignore entièrement et qu'un humain lit.** PHP vous donne trois façons d'en écrire un, un héritage de ses débuts comme langage de gabarits.

```php
<?php

// A single-line comment.

# Also a single-line comment, same effect, different heritage
// (this style is borrowed from shell scripts; you'll see it far less often).

/*
 * A multi-line comment,
 * for when one line isn't enough.
 */
```

En pratique `//` domine pour les notes de tous les jours, et `/* ... */` sert pour la variété plus longue et plus structurée, le plus souvent sous la forme d'un *docblock* posé juste au-dessus d'une fonction ou d'une classe :

```php
<?php

/**
 * Calculates compound interest.
 *
 * @param float $principal Starting amount
 * @param float $rate Annual interest rate, as a decimal (e.g. 0.05 for 5%)
 * @param int $years Number of years to compound
 * @return float The final amount after compounding
 */
function compoundInterest(float $principal, float $rate, int $years): float {
    return $principal * (1 + $rate) ** $years;
}
```

**L'ouverture `/**`, deux astérisques et non un, marque un docblock.** C'est une convention, pas une fonctionnalité du langage, mais votre éditeur, PHPStan et les générateurs de documentation y lisent tous les balises `@param` et `@return`. Les docblocks prennent toute leur valeur au [chapitre 11](ch11-00-interfaces-and-traits.md), où le système de types de PHP a besoin d'un coup de main des commentaires pour dire ce que le langage ne sait pas encore exprimer.

## Ce qui mérite un commentaire

Moins que vous ne le pensez. Une fonction bien nommée, avec des paramètres bien typés, s'explique toute seule. Un commentaire qui répète ce que dit déjà le code vous donne deux endroits à garder synchronisés, et PHP n'en vérifie qu'un.

```php
<?php

// Bad: says what, which the code already says
// Increment the counter by one
$counter++;

// Good: says why, which the code can't say on its own
// Retry once more here: the upstream API is flaky on cold start
$retries++;
```

<img src="images/ch03-comment-why.png" alt="Deux post-it sur la même ligne de code : l'un répète ce que fait la ligne et est barré, l'autre explique pourquoi la ligne existe et est conservé" width="360">

**Commentez le pourquoi, pas le quoi.** Un commentaire qui explique un contournement, une contrainte peu évidente ou une décision qui paraîtrait fausse hors contexte vaut son pesant d'or. Un commentaire qui traduit le code en français, ligne par ligne, est une chose de plus qui périmera la prochaine fois que quelqu'un modifiera la ligne sans toucher à la note au-dessus.
