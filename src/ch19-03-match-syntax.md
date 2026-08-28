# `match` Pattern Syntax

Chapter 6 introduced `match` alongside enums, where it earns its keep the most. Before we leave `match` behind for good, three syntax details are worth pinning down: they don't come up in the simplest examples, but you'll want all three the first time you write a `match` expression with more than two or three arms.

## Multiple conditions per arm

An arm doesn't have to test a single value. Separate several with commas, and the arm matches if *any* of them equals the subject:

```php
<?php

$dayNumber = 6;

$dayType = match ($dayNumber) {
    1, 2, 3, 4, 5 => 'Weekday',
    6, 7 => 'Weekend',
    default => 'Invalid',
};

echo $dayType; // Weekend
```

Read the comma as "or": `1, 2, 3, 4, 5 =>` means "if the subject is 1, or 2, or 3, or 4, or 5." Without this, you'd need five separate arms all returning the same value, which is exactly the kind of repetition `match` exists to eliminate.

## Order matters: first match wins

`match` checks its arms from top to bottom and stops at the first one that matches. That's not usually something you have to think about, because well-designed conditions don't overlap. But combine `match (true)` (matching against boolean conditions rather than a single value, as you saw back in [Chapter 3](ch03-05-control-flow.md)) with conditions that *can* overlap, and order becomes a real decision, not a formality:

```php
<?php

$score = 85;

$grade = match (true) {
    $score >= 90 => 'A',
    $score >= 80 => 'B',
    $score >= 70 => 'C',
    default => 'F',
};

echo $grade; // B
```

Put `$score >= 70` first, and every score of 85 or above would also satisfy it, and you'd never reach the `A` or `B` arms at all; they'd be unreachable code, silently. Ordering the conditions from most specific to least specific, as above, is what makes this pattern work. It's a small trap, but a common one: when your arms can overlap, always order the most restrictive condition first.

## Arms are expressions, not just values

Every arm of a `match` is a full expression, evaluated and returned when that arm is chosen: it doesn't have to be a bare literal. You can call a function, construct an object, or run any expression PHP allows:

```php
<?php

enum LogLevel
{
    case Info;
    case Warning;
    case Error;
}

function formatMessage(string $level, string $text): string
{
    return "[" . strtoupper($level) . "] {$text}";
}

$level = LogLevel::Warning;

$output = match ($level) {
    LogLevel::Info => formatMessage('info', 'Request completed'),
    LogLevel::Warning => formatMessage('warning', 'Disk usage above 80%'),
    LogLevel::Error => (new RuntimeException('Disk full'))->getMessage(),
};

echo $output; // [WARNING] Disk usage above 80%
```

That last arm constructs an exception object and immediately calls a method on it, all inside a single `match` arm; parentheses around `new RuntimeException(...)` are needed there so PHP knows to call `getMessage()` on the constructed object rather than trying to parse it some other way. There's no rule that arms have to be short or trivial; they just have to be expressions, which in PHP covers almost everything. This is what makes `match` a genuine replacement for a lot of small helper functions, not just a tidier `switch`.
