# B - Glossary of Ecosystem Terms

Defined by what each one does for you, not by its formal definition.

**Adapter**
A small piece of code that makes one thing (a storage backend, a search engine) speak the interface your application expects, so swapping the underlying service doesn't mean rewriting the application. See [League/Flysystem](ch02-06-league-flysystem-standalone.md).

**Attribute**
A piece of metadata written directly above a PHP class or method (`#[ApiResource]`, `#[IsGranted('ROLE_ADMIN')]`) that a framework reads at runtime to decide how to treat it, replacing what used to require separate configuration files.

**Bundle**
Symfony's word for an installable package that adds a feature to an application: the Security Bundle, the AI Bundle. Roughly equivalent to a Laravel package or a WordPress plugin.

**Facade**
A Laravel convention: a simple, static-looking call (`Storage::get(...)`) that's actually backed by a real, swappable object underneath, giving you a short, memorable syntax without losing the flexibility of dependency injection.

**Fiber**
A PHP 8.1 feature that lets a single process pause and resume execution at will, holding many things "in flight" at once without needing a thread per task. What makes [Reverb's WebSocket server](ch07-01-laravel-reverb-livewire.md) possible.

**Hook / Filter**
WordPress's extension mechanism: a named point in core code where a plugin can run its own function (`add_action`), or modify a value as it passes through (`add_filter`), without editing WordPress core itself.

**Migration**
A version-controlled, incremental change to a database schema, written in code rather than applied by hand, so every developer and every environment ends up with the same database structure by running the same migration files.

**ORM (Object-Relational Mapper)**
The layer that turns database rows into PHP objects and back (Eloquent in Laravel, Doctrine in Symfony), so most day-to-day code works with `$product->price` instead of hand-written SQL.

**Provider (Service Provider / Service Container)**
The part of a framework responsible for constructing objects and handing them to whatever needs them, so a class can simply declare "I need a logger" in its constructor without knowing how that logger gets built or configured.

**PSR**
A PHP Standards Recommendation: an agreed-upon interface (PSR-3 for logging, PSR-7 for HTTP messages) that lets independently built packages, from different vendors, work together without one needing to know the other's internals.

**Resource**
In an API context, a single type of thing your API exposes (a `Product`, an `Order`), along with the operations available on it. Also used more narrowly in Laravel for the class that shapes a model into JSON.

**Webhook**
A callback: instead of your app repeatedly asking a service "did anything happen yet," the service sends your app an HTTP request the moment something does. How [Stripe](ch09-03-laravel-cashier-stripe.md) tells your app a payment succeeded.

**Worker**
A long-running process that pulls tasks off a queue and executes them, separate from the process handling web requests, so slow work doesn't block a user waiting for a page to load. See [Shipping Background Work](ch11-00-shipping-background-work.md).
