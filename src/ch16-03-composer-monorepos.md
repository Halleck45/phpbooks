# Composer Path Repositories and Monorepos

<img src="images/ch16-icon.svg" alt="Composer Path Repositories and Monorepos illustration" width="72">

Publishing to Packagist, from the previous section, assumes your package is finished enough to hand to strangers. Plenty of real work happens before that point: specifically, the stretch where you're developing two or more related packages *together*, and changes to one need to be visible in the other immediately, without a publish-and-reinstall cycle in between. Composer has a repository type built for exactly this: the path repository.

## The problem it solves

Say you're splitting `phpgrep` into two packages: a core library, `phpgrep/core`, and the CLI wrapper around it, `phpgrep/cli`, which depends on the core. Without publishing `phpgrep/core` anywhere, `composer require phpgrep/core` in the CLI package has nothing to install: Packagist has never heard of it, and neither has any other registry. You could publish an early, half-finished version just to unblock local development, but that's backwards: you'd be publishing code for the sole purpose of testing it locally.

## Pointing Composer at a local folder instead

A path repository tells Composer, for one project, "when you see this package name, don't look on Packagist, look in this folder on disk instead":

```json
{
    "repositories": [
        {
            "type": "path",
            "url": "../phpgrep-core"
        }
    ],
    "require": {
        "phpgrep/core": "*"
    }
}
```

Given a directory layout like:

```console
projects/
├── phpgrep-core/
│   └── composer.json     ("name": "phpgrep/core")
└── phpgrep-cli/
    └── composer.json     (the file above)
```

running `composer install` inside `phpgrep-cli` resolves `phpgrep/core` to `../phpgrep-core` and, by default, creates a *symlink* in `vendor/phpgrep/core` pointing back at the real folder, not a copy. Edit a file in `phpgrep-core`, and `phpgrep-cli` sees the change instantly, with no reinstall, no re-publish, nothing to run in between. It behaves, for local development purposes, exactly like a single package would, while still being two genuinely separate packages with their own `composer.json`, their own version constraints, and their own eventual path to Packagist once they're ready.

## Where this leads: monorepos

Take that same idea and put several related packages in *one* Git repository, each with its own `composer.json`, wired together with path repositories pointing at each other's subfolders: that's the shape most PHP monorepos take. There's no special "monorepo mode" in Composer; a monorepo is just an ordinary directory tree of packages that happen to share one repository and use path repositories to reference each other during development. Some projects stay that way permanently, treating the monorepo as the real, shipped structure. Others use it purely as a development convenience and split packages out to their own repositories, and publish each to Packagist independently, once they've stabilized. Both are legitimate; which one fits depends more on your team's release process than on anything Composer itself enforces.
