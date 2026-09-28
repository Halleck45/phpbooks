# Nextcloud Talk: Real-Time Built Into a Larger Platform

Nextcloud Talk is a chat and video calling system at production scale, built as an app inside a PHP application rather than as a product from scratch. You may never touch Nextcloud's code, and it still teaches something. **"PHP can't do real-time" was never true; the trick is knowing what to keep in PHP and what to hand off.**

Talk installs as an app inside any Nextcloud instance:

```bash
php occ app:install spreed
php occ app:enable spreed
```

For chat, Talk relies on the same polling and Server-Sent Event techniques as the rest of this chapter. For audio and video calls at scale, it hands off to a dedicated High-Performance Backend, a separate signaling server, instead of forcing media through PHP's request lifecycle:

```bash
php occ talk:signaling:add wss://signaling.example.com "shared-secret-here"
```

That split is the pattern to borrow. PHP owns accounts, permissions, and chat history. A dedicated service owns the media stream.

## When to reach for this

Not as a package you install into your own project, but as a reference architecture the day your real-time feature starts wanting video or audio and not only data updates: keep PHP as the source of truth for accounts and permissions, and delegate the media transport to a service built for it.

## When it's the wrong fit

If the question is whether to self-host Nextcloud for your organization (see [Shipping File Storage and Collaboration](ch08-01-nextcloud-ready-made-drive.md)), Talk is one of the apps that comes with it, not a separate decision.

> **Under the hood:** Nextcloud's app system lets a feature like Talk be installed, updated, and disabled independently of the core, using PHP's own package and autoloading conventions. It is the same instinct as WordPress plugins or Symfony bundles: a stable core, and functionality layered on as discrete, swappable units.
