# Espaces de noms, paquets et Composer

Jusqu'ici, chaque exemple tenait dans un fichier. C'est fini. Depuis le [chapitre 5](ch05-00-classes.md) et le [chapitre 6](ch06-00-enums.md), vous avez des classes et des énumérations, et un projet qui en compte une dizaine n'a rien à faire dans un script unique. Il vous faut répartir le code entre plusieurs fichiers, et faire en sorte que ces fichiers ne se marchent pas dessus.

Le piège, c'est le nommage. Le jour où vous installez un paquet avec Composer, le gestionnaire de paquets de PHP, vous partagez votre projet avec du code que vous n'avez pas écrit et que vous ne pouvez pas renommer. Si ce paquet définit une classe `Product` et que vous en avez une aussi, PHP n'a aucun moyen de les distinguer. **Un espace de noms est un préfixe devant un nom, et c'est ce préfixe qui empêche `App\Models\Product` et `Vendor\Package\Product` de se télescoper.** Deux noms différents, rien à deviner.

Composer vient en premier, parce que c'est lui qui justifie tout le reste. Vous donnez ensuite un espace de noms à vos propres classes, vous les importez avec `use` pour continuer à écrire des noms courts, et vous rangez le tout dans un dossier `src/` qui reflète ces espaces de noms, comme dans les vrais projets PHP. PSR-4 noue le tout : une convention qui permet à Composer de retrouver n'importe quelle classe à partir de son seul nom.

Cette dernière pièce est la récompense. La ligne `require 'vendor/autoload.php'` trouve et charge déjà chaque paquet que vous installez. À la fin du chapitre, elle trouvera aussi *vos propres* classes. Vous ajoutez un fichier, vous utilisez la classe, et elle est là, tout simplement. Aucune liste de `require` à entretenir en tête de chaque fichier.

<img src="images/ch07-one-key.png" alt="Une seule clé étiquetée vendor/autoload.php ouvre deux portes à la fois, l'une marquée vendor/ pour les paquets installés et l'autre marquée src/ pour vos propres classes" width="560">
