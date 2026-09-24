# Evaluating a New Stack in a Day

A new client, a new tool, a framework you have never shipped anything in. This book covers the options that exist today; new ones will exist tomorrow, and clients do not wait for the next edition. **One day, four steps, and you know whether to commit project time to it.**

## Morning: scaffold and orient

Run the tool's own quickstart, as documented, no shortcuts. Note how long it took, how much was decided for you, and how much freedom is left. [Scaffolding a First Project in Under a Minute](ch01-02-scaffolding-a-first-project.md) shows what this looked like for the frameworks and CMSes in this book.

## Midday: build one real, small thing

Not a "hello world." A login form, a data table, a single API endpoint. Time it, and note where you got stuck in the documentation. That friction is the most honest signal you will get about what a project in this tool will feel like.

## Afternoon: check the edges

Look for what every chapter of this book treats as decision-relevant. Is there an official, maintained path for testing (see [Shipping Confidence](ch14-00-shipping-confidence.md))? For deployment (see [Shipping to Production](ch16-00-shipping-to-production.md))? Does a stuck question get answered in hours rather than weeks (see [Communities Worth Joining](ch17-02-communities-worth-joining.md))?

## Evening: decide against the brief, not the marketing

Every tool's homepage claims to be fast, modern and developer-friendly. None of that matters as much as the question [Chapter 1](ch01-01-framework-cms-or-headless.md) asked first: framework, CMS or headless? And does this option fit the feature you were asked to build?

> **Under the hood:** The same practice (quickstart, then a small feature, then the edges) evaluates tools outside PHP too. What is specific to this book is the list of edges: PHP's ecosystem has mature answers for testing, deployment and community support, so a new tool lacking any of them deserves to be treated as a yellow flag, not a minor gap.
