# More About Composer and Packagist

<img src="images/ch16-icon.svg" alt="More About Composer and Packagist illustration" width="72">

You've used Composer since [Chapter 7](ch07-01-hello-composer.md): `composer install`, a `composer.json` with an `autoload` block, PSR-4 mapping a namespace to a folder. That's enough to build and structure a real project, and it's most of what you'll do with Composer day to day. It is not, however, everything Composer does, and this chapter fills in the rest of the picture: the parts you'll reach for once your project grows past "one package, one repository."

We'll start close to home, with two features of `composer.json` you've been living next to without using: the `"scripts"` section, which turns shell commands into short, memorable Composer subcommands, and a second kind of autoloading, `"files"`, for the plain function files that don't fit PSR-4's one-class-per-file assumption.

From there we widen out. Packagist is the public registry every `composer require` pulls from by default, and it's worth understanding how a package actually gets there. Spoiler: nobody "uploads" anything. We'll also look at what happens once you're not working on a single package anymore: developing two or more local packages side by side, before either is published, using Composer's path repositories, the mechanism that makes monorepo-style PHP projects work.

Finally, two things that live slightly outside any one project: installing command-line tools globally with Composer, so you have one copy of PHPStan or PHP-CS-Fixer available everywhere instead of a dozen per-project copies, and a brief, honest look at the automation hooks Composer offers around its own lifecycle, and the door it leaves open, via plugins, for going further than that.
