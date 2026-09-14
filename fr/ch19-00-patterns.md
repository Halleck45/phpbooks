# Motifs et correspondance

Pour sortir trois valeurs d'un tableau à l'ancienne, vous écrivez trois lignes : `$name = $row[0];`, puis `$age = $row[1];`, puis `$city = $row[2];`. Chaque ligne répète le même geste, et aucune ne dit au lecteur à quoi ressemble le tableau. **La déstructuration fait le même travail en une seule affectation, en dessinant à gauche du signe égal la forme que vous attendez.** C'est l'outil de motifs le plus discret de PHP, on en parle bien moins qu'il ne le mérite, et c'est le sujet de ce chapitre.

L'outil bruyant, vous le connaissez déjà. `match` est arrivé au [chapitre 6](ch06-02-match.md), aux côtés des énumérations, comme remplaçant propre de `switch`. Sur la page, `match` et la déstructuration ne se ressemblent pas. Dessous, ils règlent le même genre de problème : vous tenez une forme (un tableau, une valeur qui peut être l'une parmi plusieurs) et vous voulez que PHP la démonte pour vous, plutôt que d'écrire à la main les index ou les comparaisons.

La déstructuration se glisse dans plus d'endroits qu'on ne le croit : l'affectation simple, `foreach`, les cases qu'on saute exprès. Vient ensuite la syntaxe elle-même, imbriquée et par clé, là où elle gagne sa place dans le code de tous les jours. Le chapitre se termine sur trois détails de `match` que le chapitre 6 n'avait pas la place d'aborder : plusieurs conditions dans un même bras, pourquoi l'ordre des bras compte, et des bras qui sont des expressions complètes plutôt que de simples valeurs.

Rien d'exotique là-dedans. C'est du PHP ordinaire, idiomatique, et une fois que vous l'aurez en main, `$row[0]`, `$row[1]`, `$row[2]` sur trois lignes vous paraîtra aussi daté qu'un `switch` avec six `break`.
