# Installing Global Tools with Composer

<img src="images/ch16-icon.svg" alt="Installing Global Tools with Composer illustration" width="72">

Not everything you install with Composer is a dependency of a specific project. Static analysis tools like PHPStan, code formatters like PHP-CS-Fixer, and similar command-line utilities are things you want available everywhere, run against whatever project you happen to be sitting in, not bundled into that project's own `composer.json`. Composer has a separate command for exactly that case.

## `require --dev` vs. `global require`

You've already used `require-dev`: a dependency needed only during development, like PHPUnit, listed in a project's own `composer.json` and installed into that project's own `vendor/` folder:

```console
$ composer require --dev phpunit/phpunit
```

That's the right call for anything the project's tests or build process genuinely depend on: everyone who clones the repository and runs `composer install` gets the same version, which matters for reproducibility. It's the wrong call for a tool you personally like to run across every project you touch, regardless of what any one of them declares: installing PHPStan into ten different projects' `vendor/` folders, one copy per project, at one version per project, is a lot of duplication for a tool that doesn't actually belong to any of them.

`composer global require` solves that:

```console
$ composer global require phpstan/phpstan
```

This installs PHPStan once, into a global Composer directory entirely separate from any project (`~/.config/composer` on Linux, `~/.composer` on macOS by default, though the exact path is worth confirming with `composer global config home`) rather than into a project's `vendor/` folder. From then on, `phpstan` is a single, shared install, available no matter which project directory you're standing in.

## Getting it on your `PATH`

A global install alone doesn't make the `phpstan` command work from anywhere: your shell still needs to know where to find it. The binary lands in a `vendor/bin` folder inside that global Composer directory, and that folder needs to be on your `PATH`:

```console
$ export PATH="$HOME/.composer/vendor/bin:$PATH"
```

Add that line to your shell's startup file (`~/.zshrc`, `~/.bashrc`, or equivalent) so it takes effect in every new terminal, not just the current one. Confirm it worked:

```console
$ phpstan --version
PHPStan - PHP Static Analysis Tool 1.11.5
```

If that command isn't found, the `PATH` line above is almost always the culprit: either it's missing, pointing at the wrong directory for your platform, or you edited the startup file but haven't reloaded it (`source ~/.zshrc`, or just open a new terminal).

## Choosing between the two

The rule of thumb: if a tool needs to run identically for everyone on the team and in CI, at a version pinned in version control, it belongs in `require-dev`. If it's a personal preference you run across every project regardless of what that project declares, and you're comfortable it might drift a version or two out of sync with a teammate's copy, `composer global require` is the better fit. Plenty of real setups use both at once: PHPStan pinned per-project via `require-dev` so CI is reproducible, and something like PHP-CS-Fixer installed globally for quick, ad hoc formatting while you're editing.
