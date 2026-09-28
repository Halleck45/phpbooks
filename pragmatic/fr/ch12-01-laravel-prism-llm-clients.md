# Laravel : Prism et les clients PHP OpenAI et Anthropic

Prism est un paquet pensé pour Laravel qui parle aux grands modèles de langage (OpenAI, Anthropic et d'autres) derrière une seule API. **Une fonctionnalité écrite contre un fournisseur n'est pas enchaînée à lui.**

```bash
composer require prism-php/prism
```

```php
use Prism\Prism\Prism;
use Prism\Prism\Enums\Provider;

$response = Prism::text()
    ->using(Provider::Anthropic, 'claude-sonnet')
    ->withPrompt("Summarize this support ticket in two sentences:\n\n{$ticket->body}")
    ->generate();

echo $response->text;
```

Comparer le coût ou la qualité de deux fournisseurs sur la même fonctionnalité tient en une ligne :

```php
Prism::text()->using(Provider::OpenAI, 'gpt-4o')->withPrompt($prompt)->generate();
```

Quand le résultat doit repartir dans votre base plutôt que s'afficher à l'écran, demandez une sortie structurée. Vous fournissez un schéma au lieu de découper du texte à la main :

```php
$response = Prism::structured()
    ->using(Provider::Anthropic, 'claude-sonnet')
    ->withSchema($ticketClassificationSchema)
    ->withPrompt("Classify this ticket: {$ticket->body}")
    ->generate();

$category = $response->structured['category'];
```

Pour une couche plus mince, les paquets officiels `openai-php/client` et `anthropic-php` appellent directement l'API de chaque fournisseur. Ils conviennent à une fonctionnalité qui n'aura jamais besoin que d'un seul fournisseur.

## Quand le choisir

Une fonctionnalité précise et bornée (résumé, classification, chatbot de support, suggestions de contenu) ajoutée à une application qui reste, pour le reste, un produit Laravel ordinaire.

## Quand ce n'est pas le bon outil

Une fonctionnalité où le modèle doit agir sur des données privées et vivantes au moment de la requête, ce qu'un appel d'API seul ne fournit pas. Cela pointe en général vers une étape de recherche préalable (chercher dans vos propres données, puis les glisser dans le prompt), pas vers une raison d'écarter l'approche.

> **Sous le capot :** l'abstraction de fournisseur de Prism est une interface PHP, le même motif que [les adaptateurs de stockage de Flysystem](ch02-06-league-flysystem-standalone.md) : un contrat, plusieurs implémentations interchangeables, et un code applicatif qui dépend du contrat plutôt que du SDK d'un éditeur.
