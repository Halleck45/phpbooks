# Laravel : Scout avec Meilisearch ou Algolia ($)

Scout ajoute la recherche plein texte aux modèles Eloquent. **À chaque enregistrement, mise à jour ou suppression d'un modèle, Scout met l'index de recherche à jour à votre place.** Le code de synchronisation que vous auriez écrit n'existe pas.

```bash
composer require laravel/scout meilisearch/meilisearch-php
```

```php
class Product extends Model
{
    use Searchable;

    public function toSearchableArray(): array
    {
        return ['name' => $this->name, 'description' => $this->description];
    }
}

// searching
$results = Product::search('wireles mouse')->get();
```

La coquille dans « wireles » ramène quand même la souris. Tolérer les fautes et classer par pertinence, c'est le métier du moteur de recherche, et un `LIKE` SQL n'a jamais su faire ni l'un ni l'autre.

**Meilisearch** est open source et s'héberge chez vous : un seul binaire, avec des réglages par défaut raisonnables.

```bash
docker run -p 7700:7700 getmeili/meilisearch
```

**Algolia** est l'équivalent hébergé et payant. Même driver Scout, aucune infrastructure à faire tourner.

```bash
composer require algolia/scout-extended
```

```php
// config/scout.php
return [
    'driver' => env('SCOUT_DRIVER', 'algolia'),
];
```

## Tarif

Meilisearch est gratuit à héberger soi-même. Algolia facture au volume de recherches et au nombre d'enregistrements indexés, avec un palier gratuit pour les petits projets. Le même code Scout fonctionne avec l'un comme avec l'autre : la question se résume à faire tourner le moteur vous-même ou payer quelqu'un pour le faire.

## Quand le choisir

Toute application Laravel avec un champ de recherche sur un volume de données qui dépasse l'anecdotique : un catalogue de produits, un site de documentation, un annuaire.

## Quand ce n'est pas le bon outil

Un besoin de recherche assez simple pour qu'une colonne indexée et un `LIKE` fassent l'affaire. Ajouter un moteur de recherche à cet endroit, c'est de l'infrastructure sans problème à résoudre.

> **Sous le capot :** le système de drivers de Scout est une simple interface PHP ; les drivers Meilisearch et Algolia implémentent la même poignée de méthodes (`update`, `delete`, `search`). Passer de l'un à l'autre tient dans la configuration parce que Scout a été conçu contre cette interface, et non contre l'API de l'un ou l'autre moteur.
