# Symfony: The AI Bundle

Symfony's AI Bundle brings the "talk to a model behind a clean interface" idea into Symfony's own conventions. **The agent is configured, not constructed by hand, so the model provider never gets hard-wired into your business logic.**

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

Swapping the model or provider for a feature is a YAML change. In tests, Symfony's own tooling (see [Shipping Confidence](ch14-02-symfony-phpunit-phpstan-rector.md)) substitutes a fake agent, and no real API is ever called.

## When to reach for this

A Symfony project adding an AI feature, where consistency with the app's configuration and dependency injection matters, or where the team wants an easy way to swap providers or mock the call in tests.

## When it's the wrong fit

A tiny script or a non-Symfony project. There, the bundle's configuration layer is more setup than calling the provider's HTTP API with [Guzzle](ch02-02-guzzle-http-client.md).

> **Under the hood:** The bundle's `AgentInterface` is, again, ordinary interface-based dependency injection: Symfony's service container hands your controller whatever concrete agent implementation is configured, the same mechanism it uses to inject a database connection or a logger.
