# Quickstart: Calculator Library

## Installation

This library is a local package. To use it, ensure you are in the root directory of the `calculator-project`.

## Library Usage

Here's how to use the `Calculator` class in your Python code:

```python
from src.calculator.calculator import Calculator
from decimal import Decimal

# Initialize the calculator
calc = Calculator(precision=10)

# Perform some calculations
sum_result = calc.add(Decimal('0.1'), Decimal('0.2'))
print(f"Sum: {sum_result}")  # Output: Sum: 0.3

diff_result = calc.subtract(10, 3.5)
print(f"Difference: {diff_result}")  # Output: Difference: 6.5

# Handle exceptions
try:
    calc.divide(5, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Output: Error: Cannot divide by zero.
```

## Command-Line Interface (CLI) Usage

The CLI provides a simple way to perform calculations from your terminal.

```bash
# Addition
python -m src.calculator.cli add 5 3
# Output: 8

# Subtraction
python -m src.calculator.cli subtract 10 4.5
# Output: 5.5

# Multiplication
python -m src.calculator.cli multiply 7 2
# Output: 14

# Division
python -m src.calculator.cli divide 10 2
# Output: 5

# Power
python -m src.calculator.cli power 2 3
# Output: 8

# Square Root
python -m src.calculator.cli sqrt 16
# Output: 4
```
