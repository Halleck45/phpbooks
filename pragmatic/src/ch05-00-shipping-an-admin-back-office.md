# Shipping an Admin Back Office

"Can we get a screen to edit the products ourselves?" Sooner or later every application needs one: a place where someone who is not a developer edits records, approves orders, or fixes a typo in a settings table. Building it form by form is one of the least valuable ways to spend a sprint. **The data model you already have describes that screen well enough for a tool to generate it.**

<img src="images/ch05-generated-desk.png" alt="A small elephant feeds a single sheet of paper into a box-shaped machine with a crank. Out of the other side rolls a complete office desk with drawers, a filing cabinet, a form and a table of rows. A person with a coffee mug watches it arrive" width="560">

The pick depends on what already describes the data: an Eloquent model, a Doctrine entity, an API resource, or a WordPress post type.

- [Laravel: Filament in an Afternoon](ch05-01-laravel-filament.md) generates a full admin panel from Eloquent models, with almost no boilerplate.
- [Symfony: EasyAdmin and Sonata](ch05-02-symfony-easyadmin.md) is the light and the heavy option for a Doctrine project.
- [API Platform: An Admin Generated From Your API](ch05-03-api-platform-auto-admin.md) turns the API you already expose into a panel, for free.
- [WordPress: Custom Post Types and ACF as a CRUD Engine](ch05-04-wordpress-cpt-as-crud.md) shows how far the WordPress admin stretches before you need anything else.
- [Laravel Nova ($): The Official, Supported Alternative to Filament](ch05-05-laravel-nova.md) trades an open-source panel for first-party support and a roadmap.
