# A - Coming from Python, JavaScript, or Java

One row per construct, the spelling you know on the left, the modern PHP spelling on the right. Where PHP offers an old form and a new one, only the new one is listed.

| Concept | Python | JavaScript | Java | PHP |
|---|---|---|---|---|
| Variable | `x = 1` | `let x = 1` | `int x = 1;` | `$x = 1;` |
| Constant | `X = 1` (convention) | `const X = 1` | `static final int X = 1;` | `const X = 1;` |
| String interpolation | `f"hi {name}"` | `` `hi ${name}` `` | `"hi " + name` | `"hi {$name}"` |
| String concat | `a + b` | `a + b` | `a + b` | `$a . $b` |
| Multi-line string | `"""..."""` | `` `...` `` | `"""..."""` | `<<<TXT ... TXT;` |
| Integer division | `a // b` | `Math.trunc(a / b)` | `a / b` | `intdiv($a, $b)` |
| Exponent | `a ** b` | `a ** b` | `Math.pow(a, b)` | `$a ** $b` |
| Strict equality | `a == b` | `a === b` | `a.equals(b)` | `$a === $b` |
| Null coalescing | `a if a is not None else b` | `a ?? b` | `Optional.ofNullable(a).orElse(b)` | `$a ?? $b` |
| Ternary | `a if c else b` | `c ? a : b` | `c ? a : b` | `$c ? $a : $b` |
| List literal | `[1, 2]` | `[1, 2]` | `List.of(1, 2)` | `[1, 2]` |
| Dict literal | `{"k": 1}` | `{k: 1}` | `Map.of("k", 1)` | `['k' => 1]` |
| List append | `xs.append(v)` | `xs.push(v)` | `xs.add(v)` | `$xs[] = $v;` |
| Dict lookup with default | `d.get("k", 0)` | `d.k ?? 0` | `d.getOrDefault("k", 0)` | `$d['k'] ?? 0` |
| Length | `len(xs)` | `xs.length` | `xs.size()` | `count($xs)` |
| String length | `len(s)` | `s.length` | `s.length()` | `mb_strlen($s)` |
| Slice | `xs[1:3]` | `xs.slice(1, 3)` | `xs.subList(1, 3)` | `array_slice($xs, 1, 2)` |
| Iterate list | `for v in xs:` | `for (const v of xs)` | `for (var v : xs)` | `foreach ($xs as $v)` |
| Iterate dict | `for k, v in d.items():` | `for (const [k, v] of Object.entries(d))` | `for (var e : d.entrySet())` | `foreach ($d as $k => $v)` |
| Map | `[f(v) for v in xs]` | `xs.map(f)` | `xs.stream().map(f)` | `array_map($f, $xs)` |
| Filter | `[v for v in xs if p(v)]` | `xs.filter(p)` | `xs.stream().filter(p)` | `array_filter($xs, $p)` |
| Lambda | `lambda x: x * 2` | `x => x * 2` | `x -> x * 2` | `fn($x) => $x * 2` |
| Closure capture | by reference | by reference | effectively final | by value (`use ($x)` or `fn`) |
| Default argument | `def f(x=1):` | `function f(x = 1)` | overload | `function f(int $x = 1)` |
| Named argument | `f(x=1)` | `f({x: 1})` | none | `f(x: 1)` |
| Variadic | `def f(*xs):` | `function f(...xs)` | `void f(int... xs)` | `function f(int ...$xs)` |
| Class | `class A:` | `class A {}` | `class A {}` | `class A {}` |
| Constructor | `def __init__(self, x):` | `constructor(x) {}` | `A(int x) {}` | `public function __construct(public int $x) {}` |
| Instance member | `self.x` | `this.x` | `this.x` | `$this->x` |
| Static member | `A.x` | `A.x` | `A.x` | `A::$x` |
| Interface | `Protocol` | none (TS: `interface`) | `interface A {}` | `interface A {}` |
| Enum | `class C(Enum):` | none (TS: `enum`) | `enum C { A, B }` | `enum C { case A; case B; }` |
| Catch exception | `except E as e:` | `catch (e)` | `catch (E e)` | `catch (E $e)` |
| Safe navigation | none | `a?.b` | `Optional.map` | `$a?->b` |
| String to int | `int(s)` | `parseInt(s)` | `Integer.parseInt(s)` | `(int) $s` |
| Type check | `isinstance(x, A)` | `x instanceof A` | `x instanceof A` | `$x instanceof A` |
| Print | `print(x)` | `console.log(x)` | `System.out.println(x)` | `echo $x;` |
| Import | `from a import B` | `import { B } from 'a'` | `import a.B;` | `use A\B;` |
| Package manager | pip, `pyproject.toml` | npm, `package.json` | Maven, `pom.xml` | Composer, `composer.json` |
| Test runner | pytest | Jest, Vitest | JUnit | PHPUnit, Pest |
| Formatter | black, ruff | Prettier | google-java-format | PHP-CS-Fixer, PHP_CodeSniffer |
| Static analysis | mypy, pyright | tsc | the compiler | PHPStan, Psalm |
| Run a script | `python a.py` | `node a.js` | `java A.java` | `php a.php` |
| REPL | `python` | `node` | `jshell` | `php -a` |

## Four things that are different, not just spelled differently

- **A request starts from nothing and ends with nothing.** No process stays alive between two requests. [How PHP Runs](ch01-how-php-runs.md).
- **Arrays are values.** Assign or pass one and you get a copy. Objects are handles. [Arrays](ch04-arrays.md).
- **Closures capture by value, at creation time.** A later change to the outer variable is not seen. [Functions and Closures](ch05-functions-and-closures.md).
- **Strict typing is a per-file switch.** `declare(strict_types=1)` governs the calls made from that file, and only that file. [Types](ch03-types.md).
