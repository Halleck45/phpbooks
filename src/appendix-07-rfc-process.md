# G - How PHP Is Made (the RFC Process)

At some point, reading through enums, `match`, attributes, and readonly properties, it's worth asking: who decided PHP should work this way? The answer is public, documented, and more interesting than "a company decided."

PHP's language evolution happens through RFCs (Request for Comments), proposed and discussed on the `internals@lists.php.net` mailing list. Anyone can write one. The process, roughly:

1. Someone drafts an RFC describing a proposed change (new syntax, a new function, a change to existing behavior) with motivation and, usually, a working implementation to point at.
2. It's posted to the mailing list and discussed publicly, often for weeks, sometimes for months. Discussion is not a formality; RFCs get substantially reworked, or abandoned, based on it.
3. Once discussion settles, it goes to a vote among PHP's voting members: established core contributors, not the general public.
4. Most language-level RFCs need a two-thirds majority to pass. Some narrower changes need only a simple majority; the RFC process page specifies which threshold applies to which category of change.

Every finished RFC lives at [wiki.php.net/rfc](https://wiki.php.net/rfc), vote tally and all. Enums, `match`, attributes, readonly properties: everything this book has leaned on that didn't exist before PHP 8 went through exactly this process, usually after real public disagreement about whether it was the right idea.

Worth reading through if you're curious, and worth remembering the next time a piece of PHP syntax seems arbitrary. Somebody had to argue for it, in public, against people arguing the other way.
