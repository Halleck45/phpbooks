# Evaluating a New Stack in a Day

A new client, a new tool, a new framework you haven't personally shipped anything in yet: this book's chapters cover the options that exist today, but new ones will exist tomorrow, and clients don't wait for the next edition. Here's a repeatable way to size one up before committing real project time to it.

## Morning: scaffold and orient

Run the tool's own quickstart, exactly as documented, no shortcuts. Note how long it took, how much was decided for you automatically, and how much freedom you have left. (See [Scaffolding a First Project in Under a Minute](ch01-02-scaffolding-a-first-project.md) for what this looked like across the frameworks and CMSes covered in this book.)

## Midday: build one real, small thing

Not a "hello world," an actual feature: a login form, a data table, a single API endpoint. Time how long it takes and note where you got stuck searching documentation. That friction is the most honest signal you'll get about what a real project in this tool will actually feel like.

## Afternoon: check the edges

Look specifically for what this book calls out as decision-relevant in every chapter: is there an official, maintained path for testing (see [Shipping Confidence](ch14-00-shipping-confidence.md))? For deployment (see [Shipping to Production](ch16-00-shipping-to-production.md))? Is the community active enough that a stuck question gets answered in hours, not weeks (see [Communities Worth Joining](ch17-02-communities-worth-joining.md))?

## Evening: decide against the actual brief, not the tool's marketing

Every tool's homepage claims to be fast, modern, and developer-friendly. None of that matters as much as whether it matches what [Chapter 1](ch01-01-framework-cms-or-headless.md) asked first: framework, CMS, or headless, and does this specific option fit the feature you were actually asked to build.

> **Under the hood:** This same practice, quickstart then a small real feature then the edges, works for evaluating tools outside PHP entirely. What's specific to this book is only the list of edges worth checking: PHP's ecosystem has enough mature, well-trodden answers for testing, deployment, and community support that a new tool lacking any of them is worth treating as a real yellow flag, not a minor gap.
