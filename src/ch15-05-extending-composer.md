# Extending Composer with Scripts and Plugins

You've seen `"scripts"` used for commands you run yourself: `composer test`, `composer check`. Composer scripts have a second, quieter use: hooking into Composer's *own* lifecycle, so something runs automatically at the right moment, without you having to remember to run it.

## Lifecycle events

Composer fires a named event at each stage of its own work (before and after an install, before and after an update, and several others) and you can attach a script to any of them by name, instead of inventing a name of your own:

```json
{
    "scripts": {
        "post-install-cmd": "@php artisan-like-thing:setup",
        "post-update-cmd": [
            "@php bin/generate-config.php"
        ]
    }
}
```

`post-install-cmd` runs automatically every time someone runs `composer install`: a fresh clone getting its dependencies for the first time, a CI job setting up before tests, a new developer setting up their machine. That's the point: nobody has to remember an extra manual step buried in a README, because Composer runs it for them, in the right order, every time. `post-update-cmd` is the equivalent hook for `composer update`. Other events exist for narrower moments (before a package is installed or removed, and so on) but `post-install-cmd` and `post-update-cmd` cover the overwhelming majority of real setups: regenerating a config file, warming a cache, printing a reminder about an environment variable that still needs setting.

The `@php` prefix runs a PHP script using the same PHP binary Composer itself is running under, which matters on machines with more than one PHP version installed: it removes any ambiguity about which `php` gets used.

## Where scripts stop, and plugins start

Lifecycle scripts are shell commands (or PHP scripts) that Composer runs at fixed points: useful, but limited to "run this command when this event fires." Sometimes that's not enough: you want to change how Composer itself behaves, add a new command, alter how packages get installed, react to events with actual PHP logic instead of a fire-and-forget shell command. That's what Composer plugins are for: ordinary Composer packages that hook into Composer's internals directly, written in PHP, distributed and installed exactly like any other dependency. Tools you've likely encountered without realizing it (automatic `.env` file handling in some frameworks, for instance) are often implemented as Composer plugins under the hood.

Writing one is a legitimate thing to do, and worth knowing exists, but it's real Composer-internals territory (event subscriber classes, Composer's own plugin API) and squarely beyond what this book covers. If lifecycle scripts stop being enough for something you're building, that's the door to walk through next; the [official Composer documentation](https://getcomposer.org/doc/articles/plugins.md) is the right place to start.
