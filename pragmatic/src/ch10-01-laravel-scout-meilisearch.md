# Laravel: Scout With Meilisearch or Algolia ($)

Scout adds full-text search to Eloquent models by keeping a search index in sync automatically, every time a model is saved, updated, or deleted, without writing that synchronization logic yourself.

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

That typo in "wireles" still returns the mouse; typo tolerance and relevance ranking are exactly what the underlying search engine handles that a SQL `LIKE` query never could.

**Meilisearch** is open source and self-hosted, a single binary with sensible defaults out of the box:

```bash
docker run -p 7700:7700 getmeili/meilisearch
```

**Algolia** is a managed, paid alternative, same Scout driver, no infrastructure to run:

```bash
composer require algolia/scout-extended
```

```php
// config/scout.php
'driver' => env('SCOUT_DRIVER', 'algolia'),
```

## Pricing

Meilisearch is free to self-host. Algolia bills by search volume and records indexed, with a free tier for small projects, which is what earns it the `$`: the same Scout code works against either, so the choice is genuinely just "run it yourself or pay someone else to."

## When to reach for this

Any Laravel app with a search box over more than a trivial amount of data: a product catalog, a documentation site, a directory of listings.

## When it's the wrong fit

Search needs simple enough that an indexed database column and a basic `LIKE` query genuinely suffice, where adding a search engine is unnecessary infrastructure for the problem at hand.

> **Under the hood:** Scout's driver system is a plain PHP interface; Meilisearch and Algolia drivers both implement the same handful of methods (`update`, `delete`, `search`). Swapping between them is a config change specifically because Scout was designed against that interface rather than either engine's specific API.
