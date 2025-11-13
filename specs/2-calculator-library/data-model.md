# Data Model: Calculator Library

## Entity: Calculator

This class encapsulates the core logic and state of the calculator.

### Fields

- `precision` (int): The number of decimal places for calculations. Defaults to 28.

### Methods

- `add(a: Decimal, b: Decimal) -> Decimal`: Returns the sum of `a` and `b`.
- `subtract(a: Decimal, b: Decimal) -> Decimal`: Returns the difference of `a` and `b`.
- `multiply(a: Decimal, b: Decimal) -> Decimal`: Returns the product of `a` and `b`.
- `divide(a: Decimal, b: Decimal) -> Decimal`: Returns the quotient of `a` and `b`.
- `power(base: Decimal, exponent: Decimal) -> Decimal`: Returns `base` raised to the power of `exponent`.
- `sqrt(number: Decimal) -> Decimal`: Returns the square root of `number`.

### Validation Rules

- All input parameters to the calculation methods (`a`, `b`, `base`, `exponent`, `number`) must be of type `Decimal`. The public-facing library functions will handle the conversion from `int` and `float` to `Decimal`.
- The `divide` method will raise a `ZeroDivisionError` if `b` is zero.
- The `power` method will raise a `ValueError` if `base` and `exponent` are both zero.
- The `sqrt` method will raise a `ValueError` if `number` is negative.
