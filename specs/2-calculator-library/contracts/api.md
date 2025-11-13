# API Contract: Calculator Library

This document defines the public API for the Calculator Library.

## Class: `Calculator`

### Initialization

`__init__(self, precision: int = 28)`

- **Description**: Initializes a new `Calculator` instance.
- **Parameters**:
  - `precision` (int, optional): The number of decimal places for calculations. Defaults to 28.

### Methods

#### `add(self, a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> Decimal`

- **Description**: Adds two numbers.
- **Parameters**: `a` and `b` (numeric).
- **Returns**: The sum as a `Decimal` object.

#### `subtract(self, a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> Decimal`

- **Description**: Subtracts the second number from the first.
- **Parameters**: `a` and `b` (numeric).
- **Returns**: The difference as a `Decimal` object.

#### `multiply(self, a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> Decimal`

- **Description**: Multiplies two numbers.
- **Parameters**: `a` and `b` (numeric).
- **Returns**: The product as a `Decimal` object.

#### `divide(self, a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> Decimal`

- **Description**: Divides the first number by the second.
- **Parameters**: `a` and `b` (numeric).
- **Returns**: The quotient as a `Decimal` object.
- **Raises**: `ZeroDivisionError` if `b` is 0.

#### `power(self, base: Union[int, float, Decimal], exponent: Union[int, float, Decimal]) -> Decimal`

- **Description**: Raises a number to a power.
- **Parameters**: `base` and `exponent` (numeric).
- **Returns**: The result as a `Decimal` object.
- **Raises**: `ValueError` if `base` and `exponent` are both 0.

#### `sqrt(self, number: Union[int, float, Decimal]) -> Decimal`

- **Description**: Calculates the square root of a number.
- **Parameters**: `number` (numeric).
- **Returns**: The square root as a `Decimal` object.
- **Raises**: `ValueError` if `number` is negative.
