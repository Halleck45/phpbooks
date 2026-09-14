# Security and Performance

## Security

[Chapter 10](ch10-02-validation-and-xss.md) dealt with XSS and SQL injection properly, and named CSRF without defending against it. **That is the beginning of web application security, not the whole of it.** A few more directions are worth knowing about.

Authentication and authorization answer two different questions: who is making this request, and what are they allowed to do. `password_hash()` and `password_verify()` are PHP's built-in, correctly salted way to store passwords. Sessions keep track of a logged-in user across requests, despite the shared-nothing model of [Chapter 18](ch18-01-request-model.md). OAuth covers "log in with an account from somewhere else".

**A codebase is only as secure as the packages it pulls in**, and [Chapter 16](ch16-00-more-about-composer.md) taught you to pull in many. `composer audit` checks the packages you have installed against a database of known vulnerabilities, and Roave Security Advisories blocks installing a package version with a known issue in the first place.

The OWASP Top 10 is a standard, regularly updated list of the most common web application vulnerabilities, XSS and SQL injection among them. Read it once, as a map of what to defend against beyond what this book covered.

Secrets are the last direction: never commit a credential to a repository. Environment variables, the mechanism from [Chapter 14](ch14-05-working-with-environment-variables.md), are the floor. A dedicated secrets store (Vault, or a cloud provider's secrets manager) is the ceiling for anything that handles real user data.

## Performance and observability

By default, PHP compiles your source code to bytecode on every single request, then throws the result away. **Opcache keeps that compiled bytecode between requests.** Turning it on in production is not so much optional as assumed.

Caching layers such as Redis and Memcached give you a place to store data that is expensive to recompute or refetch. The shared-nothing model of [Chapter 18](ch18-01-request-model.md) means nothing survives between requests unless you deliberately put it somewhere, which is the same reason [Chapter 10](ch10-03-talking-to-a-database.md) reached for a database at all.

Profiling in production needs different tools. The Xdebug profiler from [Chapter 13](ch13-02-xdebug.md) is for development, far too slow to leave running under real traffic. Production leans on lighter instruments: Blackfire, or general application performance monitoring products like Datadog and New Relic.

**Knowing what a request did after the fact matters more in PHP than in a long-running server**, precisely because each request's state disappears the moment it ends. Structured logs, request-level metrics and distributed tracing are how you reconstruct what happened once "add a `var_dump()` and rerun it" stops being an option.

Both directions share a theme. The guestbook of Chapter 10 and the final project of Chapter 21 were built to teach the underlying model correctly. Neither was built to survive a hostile internet or serious traffic, and that is fine. That is what this section is for.
