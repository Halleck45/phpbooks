# B - Glossary of Ecosystem Terms

Each term is defined by what it does for you, not by its formal definition.

**Adapter**
A small piece of code that makes one thing (a storage backend, a search engine) speak the interface your application expects, so swapping the service underneath does not mean rewriting the application. See [League/Flysystem](ch02-06-league-flysystem-standalone.md).

**Attribute**
Metadata written directly above a PHP class or method (`#[ApiResource]`, `#[IsGranted('ROLE_ADMIN')]`) that a framework reads at runtime to decide how to treat it. It replaces what used to need separate configuration files.

**Bundle**
Symfony's word for an installable package that adds a feature to an application: the Security Bundle, the AI Bundle. Roughly a Laravel package or a WordPress plugin.

**Facade**
A Laravel convention: a short, static-looking call (`Storage::get(...)`) backed by a real, swappable object underneath. You get a memorable syntax without losing the flexibility of dependency injection.

**Fiber**
A PHP 8.1 feature that lets a single process pause and resume execution at will, holding many things in flight at once without a thread per task. It is what makes [Reverb's WebSocket server](ch07-01-laravel-reverb-livewire.md) possible.

**Hook / Filter**
WordPress's extension mechanism: a named point in core code where a plugin runs its own function (`add_action`) or modifies a value on its way through (`add_filter`), without editing WordPress core.

**Migration**
A version-controlled, incremental change to a database schema, written in code rather than applied by hand. Every developer and every environment ends up with the same structure by running the same migration files.

**ORM (Object-Relational Mapper)**
The layer that turns database rows into PHP objects and back (Eloquent in Laravel, Doctrine in Symfony), so day-to-day code reads `$product->price` instead of hand-written SQL.

**Provider (Service Provider / Service Container)**
The part of a framework that builds objects and hands them to whatever needs them. A class declares "I need a logger" in its constructor and never learns how that logger was built or configured.

**PSR**
A PHP Standards Recommendation: an agreed interface (PSR-3 for logging, PSR-7 for HTTP messages) that lets packages from different vendors work together without knowing each other's internals.

**Resource**
In an API, one type of thing the API exposes (a `Product`, an `Order`) with the operations available on it. Laravel also uses the word, more narrowly, for the class that shapes a model into JSON.

**Webhook**
A callback. Instead of your app asking a service "did anything happen yet?" over and over, the service sends your app an HTTP request the moment something does. It is how [Stripe](ch09-03-laravel-cashier-stripe.md) tells your app a payment succeeded.

**Worker**
A long-running process that pulls tasks off a queue and runs them, separate from the process serving web requests, so slow work never blocks a user waiting for a page. See [Shipping Background Work](ch11-00-shipping-background-work.md).
