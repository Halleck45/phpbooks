# Rust Book → PHP Book: chapter mapping

Source: `rust-lang/book` `src/SUMMARY.md` (main branch, fetched 2026-08-24).
Target: `src/SUMMARY.md` in this repo.

Legend: **kept** (1:1, light adaptation) · **adapted** (reframed around a PHP-native concept) · **dropped** (no PHP equivalent, or not beginner-relevant) · **expanded** (PHP-specific content added beyond the Rust source)

| Rust chapter | Decision | Notes |
|---|---|---|
| 1 Getting Started | kept | Cargo → Composer in 1.3 |
| 2 Guessing Game | kept | Direct port, good first CLI project either language |
| 3 Common Programming Concepts | kept | All five subsections map cleanly |
| 4 Understanding Ownership | **dropped → adapted** | Ownership/borrowing/the borrow checker/lifetimes have no PHP equivalent — PHP is garbage-collected. Replaced with a much shorter chapter on copy-on-write arrays and `&$ref` semantics, since that's the actual place PHP beginners get surprised, without pretending it's the same problem Rust solves. |
| 5 Structs | adapted | "Structs" → PHP classes (PHP has no bare struct type) |
| 6 Enums and Pattern Matching | kept | Strong fit: PHP 8.1 added real enums, and `match` (8.0) is PHP's version of Rust's `match` |
| 7 Packages, Crates, and Modules | adapted | Crates → Composer packages, modules → namespaces + PSR-4 autoloading |
| 8 Common Collections | adapted | Vectors → indexed arrays, hash maps → associative arrays (PHP arrays are both, taught separately for clarity) |
| 9 Error Handling | adapted | `panic!`/`Result<T,E>` → fatal errors/`Error` vs. exceptions/`try`/`catch`. PHP has no `Result` idiom, so 9.3 is reframed as exceptions vs. return-null/false, not a port of Rust's guidance. |
| 10 Generics, Traits, Lifetimes | **adapted, lifetimes dropped** | Traits chapter kept but retitled — note PHP's `trait` keyword is a different mechanism (compile-time mixin) than Rust's `trait` (interface-like). Generics don't exist at the language level in PHP; covered only as a docblock/PHPStan-Psalm convention. Lifetimes dropped entirely — no analog. |
| 11 Writing Automated Tests | kept | PHPUnit stands in for `cargo test` |
| 12 I/O Project (CLI grep clone) | kept | `$argv`, `file_get_contents`, `getenv`, `STDERR` are direct analogs |
| 13 Iterators and Closures | adapted | Rust iterators → PHP generators (`yield`) and array functions (`array_map`, etc.); closures map directly, arrow functions (`fn() =>`) added since Rust has no equivalent split |
| 14 More about Cargo and Crates.io | kept | Packagist stands in for crates.io |
| 15 Smart Pointers | **dropped** | `Box`, `Rc`, `RefCell`, `Drop`, reference cycles are all about manual heap management under a borrow checker. PHP has neither manual allocation nor a borrow checker; its GC (refcounting + cycle collector) already does this invisibly. No replacement chapter — flagged as an explicit non-topic in the intro instead. |
| 16 Fearless Concurrency | **adapted, trimmed, marked advanced** | PHP's shared-nothing, (usually) single-threaded-per-request model makes threads/message-passing/`Send`+`Sync` a poor beginner topic. Replaced with a short, explicitly-advanced chapter on the request model plus pointers to queues/Fibers/ReactPHP/Swoole rather than teaching primitives beginners won't use. |
| 17 Async, Await, Futures, Streams | **dropped → folded into ch16** | Not core-language in PHP the way `async fn` is in Rust (it lives in userland: Fibers/ReactPHP/Swoole/AMPHP). A full 6-subsection chapter would misrepresent it as a language feature; reduced to one subsection in the concurrency chapter. |
| 18 OOP Features | **expanded, merged with 15/structs content** | Inverted emphasis: Rust's OOP chapter argues PHP-style OOP is achievable via traits, because Rust has no inheritance. PHP has real classes and inheritance as first-class citizens, so this became a full chapter (ch15) covering inheritance/polymorphism/magic methods/design patterns — more central to PHP than to Rust. |
| 19 Patterns and Matching | kept, trimmed | PHP's pattern matching is narrower (`match`, list destructuring) — three subsections still fit, just smaller in scope |
| 20 Advanced Features | **adapted, unsafe & macros dropped** | Unsafe Rust: no equivalent (no raw pointers in PHP). Macros: no true equivalent — PHP Attributes (8.0) are the nearest analog (declarative metadata, not code generation) and replace this subsection. Advanced traits/types → built-in interfaces (`Countable`, `ArrayAccess`, `IteratorAggregate`) and reflection, which are the PHP mechanisms beginners actually reach for at this level. |
| 21 Final Project: Multithreaded Web Server | adapted | Reframed around PHP's built-in dev server and per-request lifecycle instead of hand-rolling a thread pool, which would fight PHP's execution model rather than teach it |
| Appendix A–G | kept, C/E retitled | C "Derivable Traits" → "Built-in Interfaces and Magic Methods"; E "Editions" → "PHP Versions and Backward Compatibility" (PHP has no edition system, but the versioning/BC concern is analogous) |

## Net structure change

19 numbered chapters instead of Rust's 21 (16+17 merged into one trimmed, clearly-marked-advanced chapter; 15+18 merged into one expanded OOP chapter). Appendix unchanged at A–G.
