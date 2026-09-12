# Methods and Constructor Promotion

<img src="images/ch05-icon.svg" alt="Methods and Constructor Promotion illustration" width="72">

A **method** is just a function that lives inside a class. You've already written one, `totalPrice()` on `Product`, in the previous section, but it's worth looking at what makes it different from an ordinary function, and then at PHP's shortest, most modern way of writing the constructor that so often accompanies one.

## `$this`

Inside a method, `$this` refers to the specific object the method was called on. It's how a method reaches the data that belongs to *this particular instance*, as opposed to some other instance of the same class:

```php
<?php
declare(strict_types=1);

class Product
{
    public string $name;
    public float $price;
    public int $quantity;

    public function __construct(string $name, float $price, int $quantity)
    {
        $this->name = $name;
        $this->price = $price;
        $this->quantity = $quantity;
    }

    public function totalPrice(): float
    {
        return $this->price * $this->quantity;
    }

    public function applyDiscount(float $percentage): void
    {
        $this->price -= $this->price * ($percentage / 100);
    }
}

$mug = new Product('Coffee mug', 8.50, 3);
$mug->applyDiscount(10);

echo $mug->price; // 7.65
```

`applyDiscount()` doesn't take the product as a parameter; it doesn't need to, because `$this` already *is* the product it was called on. Call `$mug->applyDiscount(10)`, and inside the method, `$this` is `$mug`; call the same method on a different `Product`, and `$this` is that one instead. It's implicit, always available inside any non-static method, and it's how an object's methods stay in sync with that same object's data without you having to pass the object into every one of its own methods by hand.

## The constructor, the long way

Look back at `Product`'s constructor above. It's a common shape: three parameters in, three matching property assignments, one line each, no logic beyond "put this where it belongs." This pattern is common enough in PHP, and repetitive enough, that it earned its own shorthand.

## Constructor property promotion

PHP 8 lets you declare a property and assign it from a constructor parameter in a single spot, by adding a visibility keyword directly to the parameter itself:

```php
<?php
declare(strict_types=1);

class Product
{
    public function __construct(
        public string $name,
        public float $price,
        public int $quantity,
    ) {
    }

    public function totalPrice(): float
    {
        return $this->price * $this->quantity;
    }
}

$mug = new Product('Coffee mug', 8.50, 3);
echo $mug->totalPrice(); // 25.5
```

Compare this directly against the version at the top of this section. Both classes behave identically from the outside: same properties, same types, same constructor signature. But the promoted version has no separate property declarations, no `$this->name = $name;` repeated three times, and an empty constructor body. Writing `public string $name` as a constructor parameter does three things at once: declares the property, sets its type, and assigns the incoming argument to it, all in the one place you'd otherwise have written it twice.

This is the idiomatic, modern way to write a constructor whose only job is "store what I was given," which describes a large share of the constructors you'll write in real PHP code. You'll see it constantly from here on in this book.

## `readonly` properties, briefly

One more keyword worth knowing now that you've seen promotion, since the two are so often paired: mark a promoted property `readonly`, and it can be set once, during construction, and never reassigned after:

```php
<?php
declare(strict_types=1);

class Product
{
    public function __construct(
        public readonly string $name,
        public float $price,
        public int $quantity,
    ) {
    }
}

$mug = new Product('Coffee mug', 8.50, 3);
$mug->name = 'Travel mug'; // Error: Cannot modify readonly property Product::$name
```

A product's price and quantity are expected to change (that's the whole point of `applyDiscount()`), but there's rarely a good reason for its name to change after it's created. `readonly` lets you say so directly in the class definition, and PHP enforces it, rather than that guarantee living only as a comment or a convention someone eventually forgets. We'll lean on `readonly` again once enums and value objects enter the picture in the next chapter.
