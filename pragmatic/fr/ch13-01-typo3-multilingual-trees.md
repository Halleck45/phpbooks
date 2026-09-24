# TYPO3 : des arbres de contenu multilingues bien faits

TYPO3 traite les langues comme une dimension à part entière de son arborescence depuis bien avant la plupart de ses concurrents. **Une traduction n'est pas une copie du site, mais un enregistrement relié à son original, à l'intérieur de la même structure.**

```yaml
# config/sites/main/config.yaml
languages:
  - title: English
    languageId: 0
    locale: en_US.UTF-8
    base: /
  - title: French
    languageId: 1
    locale: fr_FR.UTF-8
    base: /fr/
    fallbackType: strict
```

Les rédacteurs traduisent page par page depuis la vue par langue du backend. Elle montre quelles traductions sont complètes, lesquelles sont périmées parce que l'original a changé depuis, et lesquelles manquent :

```bash
./vendor/bin/typo3 language:update
```

`fallbackType: strict` signifie qu'une page non traduite n'existe pas en français, au lieu d'afficher discrètement le contenu anglais. C'est un choix assumé, pas un réglage par défaut qui livre aux visiteurs des pages à moitié traduites.

## Quand le choisir

Les grands sites institutionnels avec une vraie gestion de contenu multilingue : des rédacteurs qui gèrent chacun leur langue dans leur région, et un lien entre l'original et ses traductions qui doit survivre à des années de modifications par des personnes différentes.

## Quand ce n'est pas le bon outil

Un petit site qui a besoin de deux ou trois pages statiques traduites. [WPML sur WordPress](ch13-02-wordpress-multisite-wpml.md), ou une extension de traduction plus simple, y arrive avec beaucoup moins de mise en place.

> **Sous le capot :** TYPO3 enregistre le contenu traduit dans des enregistrements distincts, reliés par un identifiant commun (`l10n_parent`), plutôt que dans un seul enregistrement avec une colonne par langue. C'est ce choix de structure qui permet à une page d'avoir en même temps trois traductions terminées et deux manquantes, suivies proprement au lieu d'être entassées dans les colonnes d'une seule ligne.
