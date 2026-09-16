# Shipping Without a Framework: Standalone Components

Not everything needs a framework. A one-off import script doesn't need Laravel. A cron job that pings three APIs and writes a report doesn't need Symfony. Sometimes the fastest way to ship isn't picking a framework or a CMS at all, it's running `composer require` for the one library built for exactly this job, and writing forty lines around it.

Every package in this chapter is genuinely independent: no framework underneath, nothing to configure beyond the one thing it does. Several of them are worth knowing for another reason too: they're the literal engines running inside the frameworks covered later in this book. Knowing them standalone makes the "under the hood" boxes in later chapters a lot less mysterious.

- [Command-Line Tools: Symfony/Console](ch02-01-symfony-console-standalone.md)
- [Talking to Other APIs: Guzzle](ch02-02-guzzle-http-client.md)
- [Templating Without a Framework: League/Plates](ch02-03-league-plates-standalone.md)
- [Logging That Just Works: Monolog](ch02-04-monolog-standalone.md)
- [Validating Input: Respect/Validation](ch02-05-respect-validation.md)
- [File Storage Without Buying Into a Framework: League/Flysystem](ch02-06-league-flysystem-standalone.md)
