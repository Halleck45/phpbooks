# TYPO3 : intégration Solr et Elasticsearch

Un gros site TYPO3 (voir [Du contenu structuré à l'échelle d'une institution](ch03-02-typo3-structured-content.md)) a précisément le problème de recherche pour lequel les moteurs spécialisés existent. Des milliers de pages, plusieurs langues, et des rédacteurs qui attendent que les résultats respectent les mêmes droits d'accès et la même arborescence que le reste du site.

**L'extension Solr indexe l'arborescence avec ses restrictions d'accès : une recherche ne fait jamais remonter une page que le visiteur n'a pas le droit de voir.**

```bash
composer require apache-solr-for-typo3/solr
```

```yaml
plugin.tx_solr {
  solr {
    host = solr.example.com
    port = 8983
    scheme = https
  }
  search {
    faceting = 1
    faceting.facets {
      contentType {
        field = type
      }
    }
  }
}
```

La recherche à facettes, où le visiteur filtre les résultats par type de contenu, par service ou par date, n'est plus que de la configuration une fois Solr branché. Pas de PHP sur mesure.

## Quand le choisir

Les sites TYPO3 d'entreprise ou d'institution où la justesse de la recherche compte pour l'organisation : contenu multilingue, droits par page, filtres à facettes. Pas un champ de recherche posé là pour faire joli.

## Quand ce n'est pas le bon outil

Un site TYPO3 plus modeste où l'extension de recherche indexée fournie suffit. Un cluster Solr ou Elasticsearch à part, c'est de l'infrastructure dont le projet n'a pas encore besoin.

> **Sous le capot :** l'intégration Solr reproduit le modèle de droits de TYPO3 au moment de l'indexation, en enregistrant pour chaque document les groupes d'utilisateurs autorisés à le voir, à côté de son contenu. C'est ce qui empêche la recherche de devenir une fuite involontaire de contenu restreint, un détail que les intégrations de recherche génériques oublient parfois.
