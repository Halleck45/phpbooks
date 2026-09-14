# The PHP Book: Writing Philosophy

This is a specification for how *The PHP Book* is written and maintained, distilled from the book's own foreword and introduction, from `RUST-TO-PHP-MAPPING.md` (its structural source), and from the editorial conventions applied while building it. Anyone editing, extending, or reorganizing the book should read this first.

## 1. Audience and purpose

- Written for new to PHP readers: people who already have some coding experience, either old PHP or another similar language.
- The goal is understanding, not snippet-copying. Explain each idea once, properly, rather than leaving the reader to reconstruct it from scattered examples. If a concept is explained, it earns a real explanation, not a rule to memorize.
- The book takes PHP's reputation head-on instead of ignoring it: acknowledge the old, deserved criticisms, then show the reader the language as it actually is now (real types, a serious error model, enums, first-class functions). No relitigating, no pretending the history didn't happen.

## 2. Structural philosophy

The book's chapter structure originated is based on industry best practices for onboarding documentations:

- **Adapt, don't force-fit.** A source concept is *kept* only where it maps cleanly onto a real PHP idea. Where PHP has no equivalent (ownership, the borrow checker, lifetimes, smart pointers, unsafe code, macros), the topic is dropped rather than stretched into a false analogy.
- **Expand where PHP is actually different.** Where PHP's own model is richer or more central than the source material assumed (real inheritance and OOP, PHP-specific web request handling), the book gives it more room than a mechanical port would, not less.
- **Mark advanced or narrow topics honestly.** Content most PHP developers will never touch in ordinary work (concurrency primitives, Fibers, reflection-heavy metaprogramming) is explicitly flagged as optional and skippable in its own text, rather than presented with the same weight as core material. A reader should never have to guess whether something is foundational or a detour.
- **Front-load fundamentals.** Variables, types, control flow, and functions come first and are grounded in one small worked example (the guessing game) before being named formally. Projects then grow progressively larger: a CLI tool with real error handling, then a small web application built without a framework, so nothing stands between the reader and what's actually happening.
- **Chapters should stand on their own where reasonably possible.** The book is meant to be readable start to finish *or* dipped into as a reference. When a chapter leans on something covered elsewhere, it links back rather than assuming the reader read every prior page in order.

## 3. Content and example philosophy

- Examples are deliberately unimpressive: no framework, no build step, no JavaScript unless the topic requires it. The smallest form that could possibly matter is the right size for an example. Keeping the surrounding technology plain keeps the lesson about PHP itself, not about tooling.
- A chapter should not depend on material that comes *after* it. If an idea needs a concept from a later chapter, either explain that concept briefly inline, or point forward explicitly ("Chapter N covers this properly") rather than silently assuming knowledge the reader doesn't have yet.
- Don't claim adjacency ("the next chapter") unless it's literally true. Chapter order changes over the life of this project; phrases that assume a fixed neighbor go stale the moment a chapter moves. Prefer "later in the book" / "the book's final project" style phrasing for anything that isn't guaranteed to stay adjacent.

## 4. Prose style

- No em dashes (—) or en dashes (–) anywhere in the prose. Use commas, periods, or restructured sentences instead.
- Direct, plainspoken explanation over cleverness. Say what something is and why it matters, not just how to type it.
- It's fine, even preferred, for the book to state its own opinions plainly (what to reach for first, what to avoid, what's overkill) rather than hedging everything into a feature-list.

## 5. Structural conventions (mechanical)

- `src/SUMMARY.md` is the single source of truth for chapter order and numbering. Every other file that mirrors the table of contents (`src/llms.txt`, the "Covered PHP Features" appendix) must be kept in sync with it, in both numbering *and* section order, not just numbering.
- Chapter files follow `chNN-MM-descriptive-name.md`: `NN` is the chapter number, `MM` is the subsection (`00` is the chapter's own overview page). Appendices follow `appendix-NN-name.md`.
- When chapters are renumbered or reordered as a mechanical consequence of restructuring, only filenames, links, and numbers should normally change. If a move breaks a chapter's actual internal logic (a forward reference that's no longer true, an assumed prerequisite that's no longer in place), that's a real content bug introduced by the move and gets a targeted prose fix, not just a renumbering.
- `src/sitemap.xml` is generated from `SUMMARY.md`'s link list, not hand-maintained; regenerate it whenever chapters are added, removed, or reordered.

## 6. Verification discipline

Before considering a structural or content change to the book complete:

- No em dashes or en dashes were introduced (`grep` check).
- All internal chapter links resolve.
- `mdbook build` runs clean, with no warnings.
- `book/llms.txt` and `book/sitemap.xml` still match `src/` byte-for-byte (mdBook copies these verbatim; a mismatch means one was edited without regenerating the other correctly).
