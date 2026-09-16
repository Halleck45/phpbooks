# Framework, CMS, or Headless: What Are You Actually Building?

Most briefs describe one of three shapes, whether or not the person writing the brief knows it.

## "We need an application"

Something with custom logic: a booking system, an internal dashboard, a marketplace, anything where the behavior is the product. This is framework territory. A framework like Laravel or Symfony gives you routing, a database layer, and a place to put your own logic, but no opinion about what your app actually does. You write that part.

Reach for a framework when the value of the product is the custom behavior itself, and no off-the-shelf tool already does what you're describing.

## "We need a site people can edit"

Something where the value is the content, and non-technical people need to add, edit, or reorganize it after launch: a marketing site, a blog, a documentation portal, most small business websites. This is CMS territory. A CMS like WordPress or TYPO3 gives you an editing interface, content structure, and a plugin ecosystem, on day one, without you writing an admin panel from scratch.

Reach for a CMS when the client's real request is "and then our marketing team should be able to update this themselves," which is most content-driven briefs whether they say it out loud or not.

## "We need an API for something else to consume"

Something feeding a mobile app, a separate front end, or another team's service, where there's no server-rendered page at all. This is headless API territory. Tools like API Platform exist specifically to turn a data model into a documented, versioned API without hand-writing every endpoint.

Reach for a headless approach when you already know the consumer is a JavaScript front end, a mobile app, or another backend team, and a server-rendered page would just be thrown away.

## When it's genuinely unclear

Plenty of real projects are two of these at once: a marketing site that also needs a booking system, an app that also needs an editable content section. When that happens, this book generally recommends starting from whichever shape is closer to the *primary* value of the project, and bolting the other capability on afterward. A WordPress site with a custom plugin for the booking logic ships faster than a Laravel app that reimplements a content editor. A Laravel app with a `posts` table and a simple admin screen ships faster than wedging custom booking logic into WordPress hooks.

> **Under the hood:** None of this is really about PHP itself. Frameworks, CMSes, and API-only tools are almost always built from the same underlying language features (a router matching a URL to code, an ORM turning rows into objects), just packaged around a different assumption about who will use the result and how often the content changes without a deploy.
