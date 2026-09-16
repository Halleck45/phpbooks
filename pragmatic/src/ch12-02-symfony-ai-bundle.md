# Symfony: The AI Bundle

Symfony's AI Bundle brings the same "talk to a model behind a clean interface" idea into Symfony's own conventions: configuration-driven setup, dependency injection, and a platform abstraction so the underlying model provider isn't hard-wired into your business logic.

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

Because the agent is configured, not constructed by hand, swapping the model or provider for a given feature is a YAML change, and Symfony's own testing tools (see [Shipping Confidence](ch14-02-symfony-phpunit-phpstan-rector.md)) can substitute a fake agent in tests without ever calling a real API.

## When to reach for this

A Symfony project adding an AI-powered feature where consistency with the rest of the app's configuration and dependency injection conventions matters, or where the team wants an easy path to swap providers or mock the AI call entirely in tests.

## When it's the wrong fit

A tiny script or a non-Symfony project, where pulling in the bundle's configuration layer is more setup than calling a provider's HTTP API directly with [Guzzle](ch02-02-guzzle-http-client.md).

> **Under the hood:** The bundle's `AgentInterface` is, again, ordinary interface-based dependency injection: Symfony's service container hands your controller whatever concrete agent implementation is configured, which is exactly the same mechanism it uses to inject a database connection or a logger.
