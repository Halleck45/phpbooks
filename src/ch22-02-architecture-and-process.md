# Architecture and the Development Process

## Architecture

Once a program grows past a handful of files, "where does this piece of code live, and why there" stops being obvious and becomes its own discipline. You've already practiced the smallest version of this instinct: the Strategy pattern in [Chapter 17](ch17-04-oop-design-patterns.md) pulled varying behavior out behind an interface so a class using it didn't need to know which version it received. Architecture is that same instinct, applied to an entire codebase instead of one class.

A few names worth recognizing:

- **Layered architecture**: separating concerns the way [Chapter 21](ch21-02-mvc-structure.md)'s router, controllers, and views did, formalized into explicit layers (presentation, domain logic, persistence) with rules about which layer is allowed to depend on which.
- **Domain-Driven Design (DDD)**: naming classes and methods after the concepts the business actually uses, not after the framework's folder structure, so the code reads like the problem it solves.
- **Hexagonal architecture (ports and adapters)**: keeping your core logic ignorant of the database and framework at its edges, so that logic can be tested and reasoned about without either one in the room.
- **Monolith versus microservices**: a well-organized monolith stays the right choice for longer than internet conventional wisdom suggests. Splitting a system into services solves organizational problems (many teams shipping independently), not technical ones, and introduces real new problems of its own, coordination across a network instead of within one process, which is [Chapter 18](ch18-01-request-model.md)'s shared-nothing model repeated at a much larger scale.

None of these are rules to apply everywhere. They're vocabulary: names for shapes of code organization, so that when a codebase's structure starts causing pain, you have a name for what to look up.

## The software development lifecycle

Architecture organizes code. The rest of the practices around a project organize the *people* changing that code, and how a change gets from an idea to something running safely in production:

- **Branching and code review**: a shared workflow for proposing a change and having someone else look at it before it merges, catching problems a test suite doesn't.
- **Versioning and releases**: semantic versioning, the same MAJOR.MINOR.PATCH scheme [Appendix E](appendix-05-php-versions.md) used to describe PHP's own backward-compatibility guarantees, applies equally to any package you publish through [Chapter 16](ch16-02-publishing-to-packagist.md).
- **Environments**: keeping local, staging, and production meaningfully similar, built on the environment variables from [Chapter 14](ch14-05-working-with-environment-variables.md) rather than hardcoded differences.
- **Issue tracking and changelogs**: a record of what changed and why, separate from the commit history, that a teammate (or you, in six months) can actually read.

None of this is PHP-specific. What's worth flagging is that PHP's fast edit-and-reload loop, no compile step, no build wait, makes it unusually easy to skip this discipline early on and feel nothing go wrong, right up until a project has enough history and enough contributors that skipping it finally costs something.
