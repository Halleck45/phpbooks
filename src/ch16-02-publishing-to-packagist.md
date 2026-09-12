# Publishing a Package to Packagist

<img src="images/ch16-icon.svg" alt="Publishing a Package to Packagist illustration" width="72">

Every `composer require` you've run has quietly relied on [Packagist](https://packagist.org/), the public package registry Composer checks by default whenever you ask it to install something. It's the reason `composer require nunomaduro/termwind` in Chapter 1 didn't need you to specify a URL, a server, or anything beyond a name: Packagist already knew where that package lived. Publishing your own package there is more approachable than it sounds, and understanding the mechanism removes a fair bit of mystery around what "publishing a PHP package" actually means.

## What a publishable `composer.json` needs

At minimum, four things:

```json
{
    "name": "yourname/phpgrep",
    "description": "A small line-searching CLI tool, built as a learning project.",
    "license": "MIT",
    "require": {
        "php": ">=8.1"
    },
    "autoload": {
        "psr-4": {
            "PhpGrep\\": "src/"
        }
    }
}
```

`"name"` follows a fixed shape: `vendor/package`, both lowercase, hyphen-separated, where `vendor` is usually your GitHub username or organization, not a formal company name; plenty of published packages belong to individuals. `"description"` and `"license"` are what show up on your package's Packagist page, and `"license"` matters for a practical reason too: without one, you're leaving the terms under which anyone can use your code legally ambiguous, which is exactly the kind of thing that quietly scares off potential users. `"MIT"` is the common, permissive default if you have no particular reason to choose otherwise.

## You don't upload anything

This is the part that surprises people coming from ecosystems with a `publish` command. Composer packages aren't uploaded to Packagist at all: Packagist doesn't host your code. It hosts *metadata about* your code, and reads the actual source straight from your Git repository, GitHub included. Publishing a package is, mechanically:

1. Push a `composer.json` like the one above to a public Git repository.
2. Go to [packagist.org](https://packagist.org/), sign in, and click "Submit," pointing it at your repository's URL.
3. Packagist reads your `composer.json`, indexes the package under the `"name"` you gave it, and, this is the important part, sets up a webhook so it's notified automatically every time you push.

From that point on, there's no separate "release" step, no build artifact to hand over. Packagist watches your repository directly.

## Versions come from Git tags

If Packagist reads straight from your repository, where do version numbers like `1.2.0` come from? From ordinary Git tags, using [semantic versioning](https://semver.org/): `MAJOR.MINOR.PATCH`:

```console
$ git tag v1.0.0
$ git push origin v1.0.0
```

Push that tag, and Packagist's webhook picks it up and lists `1.0.0` as an installable version within moments. Increment the patch number for backward-compatible fixes, the minor number for backward-compatible new features, and the major number the moment you break something a consumer might be relying on. That last rule is the one that actually matters to anyone depending on your package, since it's what lets them write a version constraint like `^1.0` in their own `composer.json` and trust that anything satisfying it won't break their code. There's no separate step to "publish" `1.0.0` beyond tagging and pushing it; the tag *is* the release.
