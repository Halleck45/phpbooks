# Symfony : l'AI Bundle

L'AI Bundle de Symfony reprend l'idée « parler à un modèle derrière une interface propre » dans les conventions de Symfony. **L'agent est configuré, pas construit à la main, et le fournisseur de modèle ne se retrouve jamais câblé en dur dans votre logique métier.**

```bash
composer require symfony/ai-bundle
```

```yaml
# config/packages/ai.yaml
ai:
  platform:
    anthropic:
      api_key: '%env(ANTHROPIC_API_KEY)%'
  agent:
    support_assistant:
      model: 'claude-sonnet'
      system_prompt: 'You are a concise, friendly support assistant.'
```

```php
final class TicketSummaryController
{
    public function __construct(private AgentInterface $supportAssistant) {}

    public function summarize(Ticket $ticket): Response
    {
        $result = $this->supportAssistant->call(
            new UserMessage("Summarize this ticket:\n\n{$ticket->getBody()}"),
        );

        return new JsonResponse(['summary' => $result->getContent()]);
    }
}
```

Changer de modèle ou de fournisseur pour une fonctionnalité, c'est une ligne de YAML. Dans les tests, l'outillage de Symfony (voir [Livrer de la confiance](ch14-02-symfony-phpunit-phpstan-rector.md)) substitue un faux agent, et aucune vraie API n'est jamais appelée.

## Quand le choisir

Un projet Symfony qui ajoute une fonctionnalité IA, quand la cohérence avec la configuration et l'injection de dépendances de l'application compte, ou quand l'équipe veut pouvoir changer de fournisseur ou simuler l'appel dans les tests sans y passer la journée.

## Quand ce n'est pas le bon outil

Un petit script, ou un projet qui n'est pas sous Symfony. Là, la couche de configuration du bundle demande plus de mise en place qu'un appel direct à l'API HTTP du fournisseur avec [Guzzle](ch02-02-guzzle-http-client.md).

> **Sous le capot :** l'`AgentInterface` du bundle, c'est encore de l'injection de dépendances par interface : le conteneur de services de Symfony fournit à votre contrôleur l'implémentation d'agent configurée, par le même mécanisme qu'il utilise pour injecter une connexion à la base ou un logger.
