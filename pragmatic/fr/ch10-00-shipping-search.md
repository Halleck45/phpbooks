# Livrer une recherche qui répond du tac au tac

« Est-ce que la recherche trouve le produit même si je fais une faute de frappe ? » Un champ de recherche posé sur un `WHERE title LIKE '%query%'` répond non. Il ne tolère aucune coquille, ne classe rien par pertinence, et parcourt toute la table dès que les données grossissent. **Une recherche qui répond du tac au tac est un problème résolu depuis longtemps : votre travail consiste à brancher vos données sur l'outil qui le résout, pas à en construire un.**

<img src="images/ch10-librarian.png" alt="Un comptoir de bibliothèque. Une personne remplit une fiche de demande où un gribouillis est barré. De l'autre côté du comptoir, un petit éléphant à lunettes tend déjà le bon livre, devant un mur de tiroirs de fichier" width="560">

- [Laravel : Scout avec Meilisearch ou Algolia ($)](ch10-01-laravel-scout-meilisearch.md) : un index de recherche tenu à jour avec vos modèles, sur un serveur à vous ou loué.
- [TYPO3 : intégration Solr et Elasticsearch](ch10-02-typo3-solr-elasticsearch.md) : une recherche sur des milliers de pages qui respecte les droits d'accès et les langues.
- [WordPress : extensions de recherche, et quand passer à Elasticsearch](ch10-03-wordpress-search-plugins.md) : ce qui est déjà là, et les deux extensions qui le remplacent quand ça ne suffit plus.
