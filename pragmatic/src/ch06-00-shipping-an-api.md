# Shipping an API Other Teams Can Use

At some point, someone else needs to talk to your data: a mobile app, a partner's system, a frontend built by a different team. That means REST or GraphQL endpoints, request validation, consistent error responses, and ideally documentation that doesn't go stale the moment the code changes. Hand-writing all of that per resource is exactly the kind of repetitive work modern PHP tooling exists to eliminate.

- [API Platform: A Full API From One PHP Class](ch06-01-api-platform-from-one-class.md) generates REST, GraphQL, and OpenAPI docs from a single annotated class.
- [Laravel: Sanctum, Resources, and API Versioning](ch06-02-laravel-sanctum-resources.md) covers Laravel's lighter-weight, more manual, and more common approach.
- [WordPress: The Built-In REST API](ch06-03-wordpress-rest-api.md) shows what's already exposed without installing anything.
