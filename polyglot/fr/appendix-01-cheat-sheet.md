# A - Venir de Python, JavaScript ou Java

Une ligne par construction, l'écriture que vous connaissez à gauche, l'écriture PHP moderne à droite. Quand PHP propose une ancienne forme et une nouvelle, seule la nouvelle figure ici.

| Concept | Python | JavaScript | Java | PHP |
|---|---|---|---|---|
| Variable | `x = 1` | `let x = 1` | `int x = 1;` | `$x = 1;` |
| Constante | `X = 1` (convention) | `const X = 1` | `static final int X = 1;` | `const X = 1;` |
| Interpolation de chaîne | `f"hi {name}"` | `` `hi ${name}` `` | `"hi " + name` | `"hi {$name}"` |
| Concaténation | `a + b` | `a + b` | `a + b` | `$a . $b` |
| Chaîne multiligne | `"""..."""` | `` `...` `` | `"""..."""` | `<<<TXT ... TXT;` |
| Division entière | `a // b` | `Math.trunc(a / b)` | `a / b` | `intdiv($a, $b)` |
| Puissance | `a ** b` | `a ** b` | `Math.pow(a, b)` | `$a ** $b` |
| Égalité stricte | `a == b` | `a === b` | `a.equals(b)` | `$a === $b` |
| Coalescence de null | `a if a is not None else b` | `a ?? b` | `Optional.ofNullable(a).orElse(b)` | `$a ?? $b` |
| Ternaire | `a if c else b` | `c ? a : b` | `c ? a : b` | `$c ? $a : $b` |
| Littéral de liste | `[1, 2]` | `[1, 2]` | `List.of(1, 2)` | `[1, 2]` |
| Littéral de dictionnaire | `{"k": 1}` | `{k: 1}` | `Map.of("k", 1)` | `['k' => 1]` |
| Ajout en fin de liste | `xs.append(v)` | `xs.push(v)` | `xs.add(v)` | `$xs[] = $v;` |
| Lecture avec valeur par défaut | `d.get("k", 0)` | `d.k ?? 0` | `d.getOrDefault("k", 0)` | `$d['k'] ?? 0` |
| Longueur | `len(xs)` | `xs.length` | `xs.size()` | `count($xs)` |
| Longueur d'une chaîne | `len(s)` | `s.length` | `s.length()` | `mb_strlen($s)` |
| Tranche | `xs[1:3]` | `xs.slice(1, 3)` | `xs.subList(1, 3)` | `array_slice($xs, 1, 2)` |
| Parcourir une liste | `for v in xs:` | `for (const v of xs)` | `for (var v : xs)` | `foreach ($xs as $v)` |
| Parcourir un dictionnaire | `for k, v in d.items():` | `for (const [k, v] of Object.entries(d))` | `for (var e : d.entrySet())` | `foreach ($d as $k => $v)` |
| Map | `[f(v) for v in xs]` | `xs.map(f)` | `xs.stream().map(f)` | `array_map($f, $xs)` |
| Filtre | `[v for v in xs if p(v)]` | `xs.filter(p)` | `xs.stream().filter(p)` | `array_filter($xs, $p)` |
| Lambda | `lambda x: x * 2` | `x => x * 2` | `x -> x * 2` | `fn($x) => $x * 2` |
| Capture des closures | par référence | par référence | effectivement finale | par valeur (`use ($x)` ou `fn`) |
| Argument par défaut | `def f(x=1):` | `function f(x = 1)` | surcharge | `function f(int $x = 1)` |
| Argument nommé | `f(x=1)` | `f({x: 1})` | aucun | `f(x: 1)` |
| Variadique | `def f(*xs):` | `function f(...xs)` | `void f(int... xs)` | `function f(int ...$xs)` |
| Classe | `class A:` | `class A {}` | `class A {}` | `class A {}` |
| Constructeur | `def __init__(self, x):` | `constructor(x) {}` | `A(int x) {}` | `public function __construct(public int $x) {}` |
| Membre d'instance | `self.x` | `this.x` | `this.x` | `$this->x` |
| Membre statique | `A.x` | `A.x` | `A.x` | `A::$x` |
| Interface | `Protocol` | aucune (TS : `interface`) | `interface A {}` | `interface A {}` |
| Énumération | `class C(Enum):` | aucune (TS : `enum`) | `enum C { A, B }` | `enum C { case A; case B; }` |
| Rattraper une exception | `except E as e:` | `catch (e)` | `catch (E e)` | `catch (E $e)` |
| Navigation sûre | aucune | `a?.b` | `Optional.map` | `$a?->b` |
| Chaîne vers entier | `int(s)` | `parseInt(s)` | `Integer.parseInt(s)` | `(int) $s` |
| Test de type | `isinstance(x, A)` | `x instanceof A` | `x instanceof A` | `$x instanceof A` |
| Afficher | `print(x)` | `console.log(x)` | `System.out.println(x)` | `echo $x;` |
| Import | `from a import B` | `import { B } from 'a'` | `import a.B;` | `use A\B;` |
| Gestionnaire de paquets | pip, `pyproject.toml` | npm, `package.json` | Maven, `pom.xml` | Composer, `composer.json` |
| Lanceur de tests | pytest | Jest, Vitest | JUnit | PHPUnit, Pest |
| Formateur | black, ruff | Prettier | google-java-format | PHP-CS-Fixer, PHP_CodeSniffer |
| Analyse statique | mypy, pyright | tsc | le compilateur | PHPStan, Psalm |
| Exécuter un script | `python a.py` | `node a.js` | `java A.java` | `php a.php` |
| REPL | `python` | `node` | `jshell` | `php -a` |

## Les différences qui ne sont pas qu'une question d'écriture

- **Une requête part de rien et finit sans rien**, parce qu'aucun processus ne reste en vie entre deux requêtes. Voir [Comment PHP s'exécute](ch01-how-php-runs.md).
- **Les tableaux sont des valeurs** : affecter ou passer un tableau en produit une copie, alors que les objets circulent par identifiant. Voir [Les tableaux](ch04-arrays.md).
- **Les closures capturent par valeur, au moment de leur création**, et une modification ultérieure de la variable extérieure ne leur parvient pas. Voir [Fonctions et closures](ch05-functions-and-closures.md).
- **Le typage strict est un interrupteur par fichier** : `declare(strict_types=1)` régit les appels faits depuis ce fichier, et seulement lui. Voir [Le système de types](ch03-types.md).
