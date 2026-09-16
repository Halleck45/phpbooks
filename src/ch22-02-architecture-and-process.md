# Architecture and the Development Process

## Architecture

Past a handful of files, "where does this piece of code live, and why there" stops being obvious. It becomes a discipline of its own. You have already practiced its smallest form: the Strategy pattern in [Chapter 17](ch17-04-oop-design-patterns.md) pulled varying behavior out behind an interface, so the class using it never needed to know which version it received. **Architecture is that same instinct, applied to a whole codebase instead of one class.**

A few names are worth recognizing.

**Layered architecture** separates concerns the way the router, controllers and views of [Chapter 21](ch21-02-mvc-structure.md) did, made formal: explicit layers (presentation, domain logic, persistence), and rules about which layer may depend on which.

**Domain-Driven Design**, DDD for short, names classes and methods after the concepts the business actually uses rather than after the framework's folder structure, so the code reads like the problem it solves.

**Hexagonal architecture**, also called ports and adapters, keeps your core logic ignorant of the database and the framework at its edges, so that logic can be tested and reasoned about without either one in the room.

**Monolith versus microservices** is the debate you will hear most often. A well-organized monolith stays the right choice for longer than internet wisdom suggests. Splitting a system into services solves organizational problems (many teams shipping independently), not technical ones, and it brings real new problems of its own: coordination across a network instead of within one process, the shared-nothing model of [Chapter 18](ch18-01-request-model.md) repeated at a much larger scale.

None of these is a rule to apply everywhere. They are vocabulary. When the structure of a codebase starts to hurt, you will have a name for what to look up.

> Architecture names are vocabulary, not orders.

## The software development lifecycle

Architecture organizes code. **The rest of the practices around a project organize the people changing that code**, and the path a change takes from an idea to something running safely in production.

Branching and code review give a team a shared way to propose a change and have someone else look at it before it merges, which catches the problems a test suite cannot. Versioning gives releases a meaning: the same MAJOR.MINOR.PATCH scheme that [Appendix E](appendix-05-php-versions.md) used for PHP's own compatibility promises applies to any package you publish through [Chapter 16](ch16-02-publishing-to-packagist.md). Environments keep local, staging and production meaningfully similar, built on the environment variables of [Chapter 14](ch14-05-working-with-environment-variables.md) rather than on hardcoded differences. Issue tracking and changelogs keep a record of what changed and why, separate from the commit history, that a teammate (or you, in six months) can actually read.

None of this is PHP-specific either. What deserves a flag is that PHP makes it unusually easy to skip. No compile step, no build wait: edit, reload, done. You can go a long time without this discipline and feel nothing go wrong, right up until the project has enough history and enough contributors that skipping it finally costs something.
