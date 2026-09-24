# Nextcloud Talk: Real-Time Built Into a Larger Platform

Nextcloud Talk is worth studying even if you never touch Nextcloud's codebase, because it's a real-time chat and video calling system, at genuine production scale, built as a PHP application's app rather than a from-scratch product. It's proof that "PHP can't do real-time" was never really true, just underused.

Talk ships as an installable app inside any Nextcloud instance:

```bash
php occ app:install spreed
php occ app:enable spreed
```

For basic chat, Talk relies on the same kind of polling and Server-Sent Event techniques covered elsewhere in this chapter. For audio and video calls at scale, it hands off to a dedicated High-Performance Backend (a separate signaling server), rather than trying to do everything inside PHP's request lifecycle:

```bash
php occ talk:signaling:add wss://signaling.example.com "shared-secret-here"
```

That split (PHP handling accounts, permissions, and chat history; a dedicated service handling the actual media stream) is a pattern worth borrowing directly: let PHP do what it's good at, and hand off the genuinely specialized real-time media work to a tool built for exactly that.

## When to reach for this

Not something you'll `composer require` into your own project, but a useful reference architecture when your own real-time feature starts wanting video or audio, not just data updates: keep PHP as the source of truth for accounts and permissions, and delegate the media transport to a dedicated service rather than forcing it through PHP.

## When it's the wrong fit

If you're evaluating whether to self-host Nextcloud itself for your organization's needs (see [Shipping File Storage and Collaboration](ch08-01-nextcloud-ready-made-drive.md)), Talk is simply one of the apps that come with it, not a separate decision.

> **Under the hood:** Nextcloud's app system lets features like Talk be installed, updated, and disabled independently of Nextcloud core, using PHP's own package and autoloading conventions internally. It's the same instinct behind WordPress plugins or Symfony bundles: a stable core, with functionality layered on as discrete, swappable units.
