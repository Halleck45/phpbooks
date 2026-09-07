# A - Keywords

The following words are reserved by PHP. You can't use any of them as the name of a variable, function, class, constant, or namespace: the parser has already claimed them for something else.

## Control flow

`if` · `else` · `elseif` · `endif` · `while` · `endwhile` · `do` · `for` · `endfor` · `foreach` · `endforeach` · `as` · `switch` · `endswitch` · `case` · `default` · `match` · `break` · `continue` · `goto` · `return` · `yield`

## Class-related

`class` · `interface` · `trait` · `enum` · `extends` · `implements` · `new` · `clone` · `instanceof` · `abstract` · `final` · `public` · `protected` · `private` · `readonly` · `static` · `const` · `var` · `function` · `fn` · `use`

## Error handling

`try` · `catch` · `finally` · `throw`

## Namespaces and includes

`namespace` · `use` · `require` · `require_once` · `include` · `include_once`

## Other

`echo` · `print` · `declare` · `enddeclare` · `global` · `list` · `array` · `isset` · `unset` · `empty` · `exit` · `die` · `and` · `or` · `xor` · `not` · `int` · `float` · `bool` · `string` · `null` · `true` · `false` · `void` · `mixed` · `never` · `self` · `parent`

That last group of type names (`int`, `string`, `null`, `true`, `false`, and the rest) deserves a note: they only became reserved gradually, as PHP added them as proper type declarations. Older code sometimes used `String` or `Int` as class names, back when that was still legal. It isn't anymore.

`use` shows up in two groups above because it does two unrelated jobs: importing names from a namespace ([Chapter 7](ch07-04-use-keyword.md)) and capturing variables into a closure ([Chapter 15](ch15-01-closures.md)). Same word, same reservation, different context.

None of these can be repurposed, no matter how well the name would otherwise fit your code. Try to name a variable `$class`: that one's fine, actually, keywords only block *bare* identifiers, not variable names after the `$`. Try to name a function `list()` or a class `Match`, and PHP will stop you at parse time, not at runtime. Better there than in production.
