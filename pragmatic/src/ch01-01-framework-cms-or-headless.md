# Framework, CMS, or Headless: What Are You Actually Building?

Most briefs describe one of three shapes, whether or not the person who wrote the brief knows it.

## "We need an application"

A booking system, an internal dashboard, a marketplace: something with custom logic, where the behavior is the product. This is framework territory. Laravel or Symfony gives you routing, a database layer, and a place to put your own logic, and no opinion about what your app does. You write that part.

**Reach for a framework when the value of the product is the custom behavior itself**, and no off-the-shelf tool already does what the brief describes.

## "We need a site people can edit"

A marketing site, a blog, a documentation portal, most small business websites: the value is the content, and non-technical people will add, edit, and reorganize it after launch. This is CMS territory. WordPress or TYPO3 gives you an editing interface, a content structure, and a plugin ecosystem on day one, and you never write an admin panel from scratch.

Reach for a CMS when the client's real request is "and then our marketing team should be able to update this themselves." That is most content briefs, whether they say it out loud or not.

## "We need an API for something else to consume"

A mobile app, a separate front end, another team's service: something that feeds a consumer, with no server-rendered page at all. This is headless territory. A tool like API Platform exists to turn a data model into a documented, versioned API without hand-writing every endpoint.

Reach for a headless approach when you already know the consumer is a JavaScript front end, a mobile app, or another backend team, and any page you rendered would be thrown away.

## When the brief is both

Plenty of real projects are two of these at once: a marketing site that also needs a booking system, an app that also needs an editable content section. Start from the shape closest to the primary value of the project, and bolt the other capability on afterward. A WordPress site with a custom plugin for the booking logic ships faster than a Laravel app that reimplements a content editor. A Laravel app with a `posts` table and a simple admin screen ships faster than custom booking logic wedged into WordPress hooks.

> **Under the hood:** None of this is about PHP itself. Frameworks, CMSes, and API tools are built from the same language features (a router that matches a URL to code, an ORM that turns rows into objects), packaged around a different assumption about who will use the result and how often the content changes without a deploy.
