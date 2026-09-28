# TYPO3 : du contenu structuré à l'échelle d'une institution

Certains sites de contenu ne sont pas un blog et quelques pages. Ce sont quelques milliers de pages, une douzaine de services, six langues, et un circuit de validation avant que quoi que ce soit ne soit publié. **TYPO3 est un CMS conçu pour cette échelle** : un arbre de contenu, des permissions fines et une prise en charge du multilingue (voir [Livrer du multilingue et du multisite](ch13-00-shipping-multi-language-multi-site.md)) pensés dès le départ, pas greffés après coup.

```bash
composer create-project typo3/cms-base-distribution my-site
cd my-site
./vendor/bin/typo3 setup
```

Le contenu vit dans un arbre de pages. Chaque page se compose d'« éléments de contenu », des blocs structurés (texte, images, formulaire, plugin) que les rédacteurs agencent sans toucher au code. Quand le jeu fourni ne suffit pas, vous ajoutez un élément sur mesure :

```php
<?php
// Configuration/TCA/Overrides/tt_content.php
use TYPO3\CMS\Core\Utility\ExtensionManagementUtility;

ExtensionManagementUtility::addTcaSelectItem(
    'tt_content',
    'CType',
    ['label' => 'Team Member Card', 'value' => 'teammember_card'],
);
```

Les permissions se règlent par page et par groupe d'utilisateurs. Un rédacteur régional gère la branche de son service dans l'arbre et ne peut toucher à celle de personne d'autre.

## Quand le choisir

Les grands sites institutionnels ou d'entreprise : universités, administrations, multinationales. Le contenu appartient à plusieurs équipes, et le circuit éditorial est une exigence, pas un confort.

## Quand ce n'est pas le bon outil

Un site de petite entreprise ou un blog à un seul rédacteur. La structure de TYPO3 fait toute sa valeur à grande échelle et n'est que du poids mort en dessous. WordPress livre le même résultat plus vite pour un brief plus simple.

> **Sous le capot :** le TCA de TYPO3 (Table Configuration Array) est un grand tableau PHP qui décrit le comportement de chaque type de contenu : ses champs, leur validation, leur rendu dans le backend. C'est de l'interface générée depuis des métadonnées, le même motif que [l'administration d'API Platform](ch05-03-api-platform-auto-admin.md), appliqué à du contenu éditorial plutôt qu'à des ressources d'API.
