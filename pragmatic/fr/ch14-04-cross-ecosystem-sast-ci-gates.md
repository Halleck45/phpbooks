# Tous écosystèmes : SAST, analyse des dépendances et barrières en CI

Tout ce qui précède dans ce chapitre dépend du framework. Cette page traite de ce qui fonctionne à l'identique quelle que soit la stack que vous livrez, et de la façon de le câbler pour qu'**un build cassé ou vulnérable n'atteigne jamais la production en silence.**

**L'analyse statique comme SAST léger** : PHPStan et Psalm, déjà vus framework par framework, servent aussi de première ligne de test de sécurité statique (SAST). Ils repèrent une requête SQL construite à partir d'une entrée non assainie, ou une variable utilisée avant d'être garantie définie.

**GitHub CodeQL** va plus loin. Il suit le chemin d'une entrée non fiable à travers le code jusqu'à un point dangereux, une requête SQL brute, un `eval()`, une sortie non échappée, au lieu de vérifier des types.

```yaml
# .github/workflows/codeql.yml
- uses: github/codeql-action/init@v3
  with:
    languages: php
- uses: github/codeql-action/analyze@v3
```

**Dependabot** surveille votre `composer.lock` et ouvre une pull request dès qu'une dépendance a une vulnérabilité connue avec un correctif disponible.

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "composer"
    directory: "/"
    schedule: { interval: "weekly" }
```

**Snyk ($)** couvre le même terrain avec le vernis d'un produit payant : un tableau de bord, des contrôles de conformité des licences et une couverture qui dépasse les dépendances Composer, contre un abonnement au-delà de l'offre gratuite.

## Le câbler dans la CI

Le but de tout cela est une barrière, pas un rapport que personne ne lit :

```yaml
# .github/workflows/ci.yml
jobs:
  quality:
    steps:
      - run: composer audit
      - run: vendor/bin/phpstan analyse
      - run: vendor/bin/pest # or php bin/phpunit
```

Si une étape échoue, la pull request ne peut pas être fusionnée. Voilà la fonctionnalité. Pas que les outils existent, mais que personne n'ait à se souvenir de les lancer.

> **Sous le capot :** CodeQL modélise les flux de données. Il suit une valeur depuis son entrée dans le programme (un paramètre `$_GET`, un champ de formulaire) jusqu'à son utilisation, au lieu de vérifier chaque ligne isolément. C'est une analyse d'une autre nature, et plus coûteuse, que la vérification de types de PHPStan et Psalm.
