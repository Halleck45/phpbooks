# Laravel: Scout With Meilisearch or Algolia ($)

Scout adds full-text search to Eloquent models. **Every time a model is saved, updated or deleted, Scout updates the search index for you**, so the synchronisation code you would otherwise write does not exist.

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

The typo in "wireles" still returns the mouse. Typo tolerance and relevance ranking are the search engine's job, and a SQL `LIKE` never did either.

**Meilisearch** is open source and self-hosted: a single binary with sensible defaults.

```bash
docker run -p 7700:7700 getmeili/meilisearch
```

**Algolia** is the managed, paid alternative. Same Scout driver, no infrastructure to run.

```bash
composer require algolia/scout-extended
```

```php
// config/scout.php
return [
    'driver' => env('SCOUT_DRIVER', 'algolia'),
];
```

## Pricing

Meilisearch is free to self-host. Algolia bills by search volume and records indexed, with a free tier for small projects. The same Scout code works against either, so the choice comes down to running it yourself or paying someone else to.

## When to reach for this

Any Laravel app with a search box over more than a trivial amount of data: a product catalog, a documentation site, a directory of listings.

## When it's the wrong fit

A search need simple enough that an indexed column and a basic `LIKE` query do the job. Adding a search engine there is infrastructure without a problem.

> **Under the hood:** Scout's driver system is a plain PHP interface; Meilisearch and Algolia drivers both implement the same handful of methods (`update`, `delete`, `search`). Swapping between them is a config change because Scout was designed against that interface rather than either engine's API.
