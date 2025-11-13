from decimal import Decimal, getcontext, InvalidOperation
from typing import Union

class Calculator:
    """
    A calculator for high-precision arithmetic using the decimal module.
    """
    def __init__(self, precision: int = 28):
        """
        Initializes the Calculator with a specified precision.

        Args:
            precision: The number of decimal places for calculations.
        """
        getcontext().prec = precision
        self.precision = precision

    def _to_decimal(self, number: Union[int, float, str, Decimal]) -> Decimal:
        """Converts a number to a Decimal object, raising TypeError for invalid inputs."""
        if not isinstance(number, (int, float, str, Decimal)):
            raise TypeError("All inputs must be numeric (int, float, str, or Decimal)")
        try:
            return Decimal(number)
        except InvalidOperation:
            raise TypeError(f"Invalid numeric string: {number}")

    def add(self, a: Union[int, float, str, Decimal], b: Union[int, float, str, Decimal]) -> Decimal:
        """
        Adds two numbers.

        Args:
            a: The first number.
            b: The second number.

        Returns:
            The sum of a and b as a Decimal object.
        """
        return self._to_decimal(a) + self._to_decimal(b)

    def subtract(self, a: Union[int, float, str, Decimal], b: Union[int, float, str, Decimal]) -> Decimal:
        """
        Subtracts the second number from the first.

        Args:
            a: The first number.
            b: The second number.

        Returns:
            The difference of a and b as a Decimal object.
        """
        return self._to_decimal(a) - self._to_decimal(b)

    def multiply(self, a: Union[int, float, str, Decimal], b: Union[int, float, str, Decimal]) -> Decimal:
        """
        Multiplies two numbers.

        Args:
            a: The first number.
            b: The second number.

        Returns:
            The product of a and b as a Decimal object.
        """
        return self._to_decimal(a) * self._to_decimal(b)

    def divide(self, a: Union[int, float, str, Decimal], b: Union[int, float, str, Decimal]) -> Decimal:
        """
        Divides the first number by the second.

        Args:
            a: The dividend.
            b: The divisor.

        Returns:
            The quotient of a and b as a Decimal object.

        Raises:
            ZeroDivisionError: If the divisor (b) is zero.
        """
        b_dec = self._to_decimal(b)
        if b_dec == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self._to_decimal(a) / b_dec

    def power(self, base: Union[int, float, str, Decimal], exponent: Union[int, float, str, Decimal]) -> Decimal:
        """
        Raises a number to a power.

        Args:
            base: The base number.
            exponent: The exponent.

        Returns:
            The result of base raised to the power of exponent as a Decimal object.

        Raises:
            ValueError: If base and exponent are both 0 (0**0 is undefined).
        """
        base_dec = self._to_decimal(base)
        exponent_dec = self._to_decimal(exponent)

        if base_dec == 0 and exponent_dec == 0:
            raise ValueError("0 to the power of 0 is undefined")

        result = base_dec ** exponent_dec
        return result

    def sqrt(self, number: Union[int, float, str, Decimal]) -> Decimal:
        """
        Calculates the square root of a number.

        Args:
            number: The number to calculate the square root of.

        Returns:
            The square root as a Decimal object.

        Raises:
            ValueError: If the number is negative.
        """
        number_dec = self._to_decimal(number)
        if number_dec < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return number_dec.sqrt()
