# G - Comment PHP se fabrique (le processus des RFC)

À un moment, en parcourant les enums, `match`, les attributs et les propriétés readonly, une question finit par venir : qui a décidé que PHP fonctionnerait comme ça ? La réponse est publique, documentée, et plus intéressante que « une entreprise en a décidé ».

Le langage évolue par RFC (Request for Comments), proposées et discutées sur la liste de diffusion `internals@lists.php.net`. N'importe qui peut en écrire une. Le processus, dans les grandes lignes :

1. Quelqu'un rédige une RFC décrivant un changement (une nouvelle syntaxe, une nouvelle fonction, une modification d'un comportement existant), avec sa motivation et, le plus souvent, une implémentation qui fonctionne.
2. Elle est publiée sur la liste et discutée en public, souvent pendant des semaines, parfois des mois. La discussion n'est pas une formalité : des RFC sont largement remaniées, ou abandonnées, à cause d'elle.
3. Une fois la discussion apaisée, elle passe au vote des membres votants de PHP : des contributeurs établis du cœur du langage, pas le grand public.
4. La plupart des RFC qui touchent au langage exigent une majorité des deux tiers. Certains changements plus étroits se contentent d'une majorité simple ; la page décrivant le processus précise quel seuil s'applique à quelle catégorie de changement.

Chaque RFC terminée vit sur [wiki.php.net/rfc](https://wiki.php.net/rfc), décompte des votes inclus. Enums, `match`, attributs, propriétés readonly : tout ce sur quoi ce livre s'est appuyé et qui n'existait pas avant PHP 8 est passé par exactement ce chemin, en général après un vrai désaccord public sur le bien-fondé de l'idée.

Ça vaut la lecture si vous êtes curieux, et ça vaut d'être gardé en tête la prochaine fois qu'un bout de syntaxe PHP vous semblera arbitraire. Quelqu'un a dû le défendre, en public, contre des gens qui défendaient l'inverse.
