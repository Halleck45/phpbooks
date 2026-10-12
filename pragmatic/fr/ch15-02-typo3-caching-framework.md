# TYPO3 : le framework de cache intégré

Le framework de cache de TYPO3 mérite un regard même hors d'un projet TYPO3, parce qu'**il traite le cache comme un problème en couches et non comme un interrupteur.** Le rendu des pages, chaque élément de contenu, les résultats de requêtes en base et la configuration ont chacun leur cache, avec leurs propres règles d'invalidation.

```php
# config/system/settings.php
$GLOBALS['TYPO3_CONF_VARS']['SYS']['caching']['cacheConfigurations']['pages'] = [
    'backend' => \TYPO3\CMS\Core\Cache\Backend\Typo3DatabaseBackend::class,
    'options' => ['defaultLifetime' => 86400],
];
```

Les rédacteurs ne gèrent jamais l'invalidation. Quand un contenu change, TYPO3 vide les caches qui en dépendent et rien d'autre, au lieu d'un brutal « tout vider » après chaque modification :

```php
$cacheManager = GeneralUtility::makeInstance(CacheManager::class);
$cacheManager->getCache('pages')->flushByTag('pageId_' . $pageId);
```

L'invalidation par étiquettes est ce qui rend un cache agressif sûr sur un grand site. Corriger une faute de frappe sur une page n'oblige pas à régénérer toutes les autres.

Pour les sites à fort trafic, TYPO3 ajoute devant tout cela un cache de proxy inverse, Varnish le plus souvent. Un visiteur anonyme qui demande une page inchangée la reçoit entièrement rendue, sans que PHP ne s'exécute.

## Quand le choisir

Les grands sites TYPO3 sous charge, où la génération des pages pèse à l'échelle de milliers de pages et où le contenu change assez souvent pour que vider tout le cache en annule l'intérêt.

## Quand ce n'est pas le bon outil

Un site à faible trafic, où le cache par défaut suffit déjà. Régler des durées de vie et des étiquettes pour un site que personne ne sollicite résout un problème qui n'existe pas encore.

> **Sous le capot :** L'invalidation par étiquettes associe à chaque élément mis en cache une ou plusieurs étiquettes (un identifiant de page, un type de contenu) au moment de l'écriture. Vider « tout ce qui porte `pageId_42` » devient alors une opération ciblée, pas une purge complète. La plupart des systèmes de cache bien conçus, en PHP ou ailleurs, reposent sur le même principe.
