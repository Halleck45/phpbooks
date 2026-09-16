# Shipping User Accounts

Sign-up, login, "forgot password," and knowing who's currently looking at the screen: nearly every application needs this, and almost none of them need to write it from scratch. Password hashing, session handling, and the dozen small security details around them (timing attacks, session fixation, rate limiting) are exactly the kind of code you want to inherit from a well-maintained package, not reinvent under a deadline.

- [Laravel: Breeze, Fortify, and Jetstream](ch04-01-laravel-breeze-fortify.md) covers Laravel's layered set of official starter kits, from "just the views" to a full team-based SaaS scaffold.
- [Symfony: The Security Bundle](ch04-02-symfony-security-bundle.md) covers Symfony's configuration-driven approach to authentication and authorization.
- [WordPress: Roles, Capabilities, and Application Passwords](ch04-03-wordpress-roles-capabilities.md) covers what's already built into WordPress core, and when it's enough.
