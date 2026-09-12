# Security and Performance

<img src="images/ch22-icon.svg" alt="Security and Performance illustration" width="72">

## Security

[Chapter 10](ch10-02-validation-and-xss.md) covered XSS and SQL injection properly, and named CSRF without defending against it. That's the beginning of web application security, not the whole of it. A few directions worth knowing exist:

- **Authentication and authorization**: verifying who's making a request and what they're allowed to do. `password_hash()` and `password_verify()` are PHP's built-in, correctly-salted way to store passwords; sessions track a logged-in user across requests despite [Chapter 18](ch18-01-request-model.md)'s shared-nothing model; OAuth handles "log in with an account from somewhere else."
- **Dependency security**: `composer audit` checks your installed packages against a database of known vulnerabilities, and Roave Security Advisories can block installing a package version with a known issue in the first place. A codebase is only as secure as the packages [Chapter 16](ch16-00-more-about-composer.md) pulled in.
- **The OWASP Top 10**: a standard, regularly updated checklist of the most common web application vulnerabilities, XSS and SQL injection among them. Worth reading once as a map of what to defend against beyond what this book covered.
- **Secrets management**: never committing credentials to a repository. Environment variables, the same mechanism from [Chapter 14](ch14-05-working-with-environment-variables.md), are the floor; dedicated secrets stores (Vault, a cloud provider's secrets manager) are the ceiling for anything handling real user data.

## Performance and observability

- **Opcache**: PHP compiles source code to bytecode on every single request by default. Opcache caches that compiled bytecode between requests, and turning it on in production isn't optional so much as assumed.
- **Caching layers** (Redis, Memcached): a place to store data that's expensive to recompute or refetch, given that [Chapter 18](ch18-01-request-model.md)'s shared-nothing model means nothing survives between requests unless you deliberately put it somewhere, the same reason [Chapter 10](ch10-03-talking-to-a-database.md) reached for a database at all.
- **Profiling in production**: Xdebug's profiler, from [Chapter 13](ch13-02-xdebug.md), is a development-time tool, too slow to leave running under real traffic. Production observability leans on lighter tools instead: Blackfire, or general application performance monitoring products like Datadog and New Relic.
- **Logging, metrics, and tracing**: knowing what a request actually did after the fact matters more in PHP than in a long-running server process, precisely because each request's local state disappears the moment it ends. Structured logs, request-level metrics, and distributed tracing are how you reconstruct what happened once "just add a `var_dump()` and rerun it" isn't an option anymore.

Both directions share a theme: the guestbook from Chapter 10 and the final project from Chapter 21 were built to teach the underlying model correctly. Neither was built to survive a hostile internet or serious traffic, and that's fine; that's what this section is for.
