# Shipping an AI Feature This Sprint

"Can we add a chatbot?" "Can search understand plain language?" "Can it summarise this for the user?" AI features arrive as small bolt-on requests far more often than as a rewrite of the product. **Adding one to an existing PHP app almost never means running a model. It means calling an API and handling the answer well.**

<img src="images/ch12-helpline.png" alt="A small elephant at an office desk holds a telephone to its ear and writes on a form. The cord runs out of the picture toward a distant building with a spark on its roof. A stack of filled forms sits on the desk" width="560">

- [Laravel: Prism and the OpenAI/Anthropic PHP Clients](ch12-01-laravel-prism-llm-clients.md): one API for several model providers, swappable in a line.
- [Symfony: The AI Bundle](ch12-02-symfony-ai-bundle.md): the same idea in Symfony's own conventions, configured rather than constructed.
- [WordPress: AI Plugins and When to Call an API Instead](ch12-03-wordpress-ai-plugins.md): the fastest path for a WordPress site, and where it stops being enough.
