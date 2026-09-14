# More About Composer and Packagist

Since [Chapter 7](ch07-01-hello-composer.md), Composer has been doing one job for you: read `composer.json`, fetch the packages listed in it, and find your classes by name thanks to a PSR-4 line. That covers most of a working day. **It is not all Composer can do, though, and the rest becomes useful the day your project stops being "one package, one repository".**

The first two additions live in the `composer.json` you already have. A `"scripts"` section turns the commands you type all day into short Composer subcommands, and a second flavor of autoloading, `"files"`, takes care of the function files PSR-4 has no way to find.

Then the view widens. Packagist is the public registry behind every `composer require`, and it is worth knowing how a package gets there. Spoiler: nobody uploads anything. Right after come path repositories, the mechanism for developing two local packages side by side before either is published, and the shape most PHP monorepos are built on.

Two last stops sit slightly outside any single project: installing command line tools once, globally, instead of one copy per project, and a short, honest look at the hooks Composer fires around its own lifecycle, with the door it leaves open for plugins.
