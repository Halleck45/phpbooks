# Frameworks and the Tooling Around Them

## Frameworks

[Chapter 21](ch21-00-final-project-web-app.md) had you write a router, controllers and a view layer by hand, on purpose, so that none of it would ever feel like magic. **A framework is that same shape, already built**, exercised by thousands of projects, with an ecosystem of packages assembled around it. Reaching for one is not admitting defeat. It is skipping work that has already been done well.

Two frameworks dominate the PHP world, and they make different bets.

**Laravel comes with batteries included.** An ORM (Eloquent), a templating engine (Blade), a command line tool (Artisan), queues, authentication scaffolding, and more, all designed to work together out of the box. It is the most common entry point for a new PHP project today.

**Symfony is built components first.** Its pieces (routing, dependency injection, the HTTP abstraction) can each be used on their own, and it favors explicitness over convention. It is often the choice for larger, longer-lived codebases, and parts of it quietly power other projects, Laravel included.

Smaller frameworks such as Slim and Mezzio exist for the cases where a full framework is more than a project needs, an API with no views, say. Pick based on what the project and the team actually need, not on which name is loudest online. Because you have built the pieces by hand, none of them should look opaque: open a Laravel controller or a Symfony route and you will recognize the shape.

> A framework is Chapter 21, done before you by a thousand people.

## Tooling

[Appendix D](appendix-04-useful-development-tools.md) covered the tools you run while writing PHP: Composer, PHPUnit, static analysis, a debugger. **The next layer of tooling is about what happens after the code is written**: carrying it safely from your machine into production, and keeping it healthy once it is there.

Continuous integration (GitHub Actions, GitLab CI) runs your test suite, PHPStan and your style checker on every push, so a broken change is caught before a human has to notice it. Containers (Docker) package PHP, its extensions and its dependencies into something that runs identically on your laptop, in CI and in production, which ends the "works on my machine" conversation. Deployment tools (Deployer, or managed platforms like Laravel Forge and Platform.sh) automate "get the new code onto the server correctly", a job that by hand involves more steps than it should.

Two tools go a step further. **Rector refactors code mechanically**, including upgrading a whole codebase across PHP versions in bulk rather than file by file, which matters the moment the compatibility concerns of [Appendix E](appendix-05-php-versions.md) stop being theoretical. **Infection tests your tests.** It deliberately plants small bugs in your code and checks whether the suite from [Chapter 12](ch12-00-testing.md) notices, a sharper question than "do the tests pass".

None of these ideas is PHP-specific. What is PHP-specific is how well they fit: the ecosystem has mature, boring, well-documented tooling for every one of them, and boring is a real advantage over flashier ecosystems with thinner tooling underneath.
