# Les collections courantes

Une liste de courses, un annuaire, une boîte de fiches, une ligne d'une base de données. Dans la plupart des langages, ce sont quatre types différents. En PHP, c'est une seule et même chose : un tableau.

Vous utilisez des tableaux depuis le [chapitre 3](ch03-02-data-types.md), un `$fruits = ["apple", "banana"]` par-ci, un `foreach` par-là, juste assez pour faire avancer un exemple. C'était à crédit. **Les tableaux sont la structure dont les programmes PHP sont faits**, et ils méritent d'être compris pour de bon, une fois, plutôt qu'attrapés au passage.

<img src="images/ch08-one-array-many-hats.png" alt="Un seul tableau PHP dessiné en couteau suisse dont les lames s'appellent liste, dictionnaire, pile et fiche : une structure qui fait le travail de plusieurs" width="520">

Si une seule structure suffit à tant de choses, la raison tient en une phrase, et c'est la clé de tout le chapitre. **Un tableau PHP est toujours une table ordonnée** : des clés, chacune pointant vers une valeur, conservées dans l'ordre où vous les avez ajoutées. Prenez 0, 1, 2 comme clés et cela ressemble à une liste. Prenez des mots et cela ressemble à un dictionnaire. En dessous, rien n'a changé. Gardez ce fait en tête et bien des comportements déroutants (pourquoi l'ordre est conservé, pourquoi `array_filter()` laisse des trous dans les clés, pourquoi `count()` est instantané) deviennent évidents.

> Une liste et un dictionnaire, c'est le même tableau PHP avec d'autres clés.

Le chapitre fait aussi halte sur les chaînes de caractères, et ce n'est pas un changement de sujet. Chaînes et tableaux vivent côte à côte dans le PHP de tous les jours : on découpe l'une en l'autre et on recolle des tableaux de chaînes à longueur de journée. Et dès qu'une chaîne contient autre chose que de l'anglais sans accent (un prénom accentué, un symbole monétaire, un emoji), vous rencontrez UTF-8, que PHP gère bien, à condition de le lui demander correctement.

Les [tableaux indexés](ch08-01-indexed-arrays.md) ouvrent le bal, puisque vous avez déjà l'intuition des listes. Puis les [chaînes de caractères](ch08-02-strings.md), avec un regard honnête sur les octets et les caractères, la distinction qui piège presque tout le monde une fois. Puis les [tableaux associatifs](ch08-03-associative-arrays.md), où des clés choisies par vous transforment la même structure en une petite fiche souple.
