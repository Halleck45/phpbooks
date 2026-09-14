# Frameworks and the Tooling Around Them

## Frameworks

[Chapter 21](ch21-00-final-project-web-app.md) built a router, controllers, and a view layer by hand, on purpose: so none of it would feel like magic. A framework gives you that same shape, already built, tested by thousands of other projects, with an ecosystem of packages assembled around it. Reaching for one isn't admitting defeat; it's skipping work that's already been done well.

Two dominate the PHP world, and they make different trade-offs:

- **Laravel**: batteries-included. An ORM (Eloquent), a templating engine (Blade), a command-line tool (Artisan), queues, authentication scaffolding, and more, all designed to work together out of the box. The most common entry point for a new PHP project today.
- **Symfony**: components-first. Its pieces (routing, dependency injection, the HTTP abstraction) are usable individually, and it favors explicitness over convention. Often the choice for larger, longer-lived codebases, and parts of it quietly power other projects, Laravel included.

Smaller frameworks (Slim, Mezzio) exist for cases where a full framework is more than a project needs, an API with no views, say. Pick based on what the project and team actually need, not which one is loudest online; because you've already built the pieces by hand, none of the big ones should feel opaque.

## Tooling

[Appendix D](appendix-04-useful-development-tools.md) covered the tools you run while writing PHP: Composer, PHPUnit, static analysis, a debugger. The next layer of tooling is about what happens after you write the code: carrying it safely from your machine into production, and keeping it healthy once it's there.

- **Continuous integration** (GitHub Actions, GitLab CI): running your test suite, PHPStan, and your style checker automatically on every push, so a broken change is caught before a human has to notice it.
- **Containers** (Docker): packaging PHP, its extensions, and its dependencies into something that runs identically on your laptop, in CI, and in production, ending the "works on my machine" conversation.
- **Deployment tooling** (Deployer, or managed platforms like Laravel Forge and Platform.sh): automating "get the new code onto the server correctly," which by hand involves more steps than it looks like it should.
- **Rector**: automated, mechanical refactoring, including upgrading a codebase across PHP versions in bulk rather than by hand, relevant the moment [Appendix E](appendix-05-php-versions.md)'s backward-compatibility concerns stop being theoretical.
- **Infection**: mutation testing. It goes one step past what [Chapter 12](ch12-00-testing.md) covered by deliberately introducing small bugs into your code and checking whether your test suite actually notices, which is a sharper question than "do the tests pass."

None of these are PHP-specific ideas. What's PHP-specific is how well they fit around it: PHP's ecosystem has mature, boring, well-documented tooling for all of the above, which is a genuine advantage over flashier ecosystems with thinner tooling underneath them.
