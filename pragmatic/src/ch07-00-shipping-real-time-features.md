# Shipping Real-Time Features

Live notifications, a presence indicator, a chat widget, a dashboard number that updates itself: any feature where "the page just knows" something changed without a manual refresh. PHP's traditional request/response model doesn't naturally hold an open connection to push updates, but the modern ecosystem has closed that gap from several directions, some requiring you to run your own WebSocket server, some handing that job to someone else entirely.

- [Laravel: Reverb and Livewire Without Writing JavaScript](ch07-01-laravel-reverb-livewire.md) covers Laravel's first-party, self-hosted WebSocket server paired with a reactive component model.
- [Symfony: UX Turbo and Mercure](ch07-02-symfony-ux-turbo-mercure.md) covers Symfony's approach, built on an open real-time protocol rather than a custom server.
- [Nextcloud Talk: Real-Time Built Into a Larger Platform](ch07-03-nextcloud-talk.md) looks at how a mature, real-world PHP application handles chat and calls at scale.
- [Pusher ($): Managed WebSockets Without Running Your Own Server](ch07-04-pusher-managed-websockets.md) trades infrastructure for a subscription.
