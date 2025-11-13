import pytest
from decimal import Decimal, getcontext
from src.calculator.calculator import Calculator

# Set precision for consistency in tests
getcontext().prec = 28

@pytest.fixture
def calc():
    """Provides a Calculator instance for tests."""
    return Calculator()

class TestBasicArithmetic:
    @pytest.mark.parametrize("a, b, expected", [
        (Decimal("2"), Decimal("3"), Decimal("5")),
        (Decimal("-1"), Decimal("-1"), Decimal("-2")),
        (Decimal("-5"), Decimal("5"), Decimal("0")),
        (Decimal("1.5"), Decimal("2.5"), Decimal("4.0")),
        (Decimal("0"), Decimal("0"), Decimal("0")),
    ])
    def test_add(self, calc, a, b, expected):
        """Test the add method."""
        assert calc.add(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (Decimal("5"), Decimal("3"), Decimal("2")),
        (Decimal("-1"), Decimal("-1"), Decimal("0")),
        (Decimal("5"), Decimal("-5"), Decimal("10")),
        (Decimal("4.5"), Decimal("2.5"), Decimal("2.0")),
        (Decimal("0"), Decimal("0"), Decimal("0")),
    ])
    def test_subtract(self, calc, a, b, expected):
        """Test the subtract method."""
        assert calc.subtract(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (Decimal("2"), Decimal("3"), Decimal("6")),
        (Decimal("-2"), Decimal("-3"), Decimal("6")),
        (Decimal("-2"), Decimal("3"), Decimal("-6")),
        (Decimal("1.5"), Decimal("2"), Decimal("3.0")),
        (Decimal("10"), Decimal("0"), Decimal("0")),
    ])
    def test_multiply(self, calc, a, b, expected):
        """Test the multiply method."""
        assert calc.multiply(a, b) == expected

    @pytest.mark.parametrize("base, exponent, expected", [
        (Decimal("2"), Decimal("3"), Decimal("8")),
        (Decimal("2"), Decimal("-1"), Decimal("0.5")),
        (Decimal("9"), Decimal("0.5"), Decimal("3")),
        (Decimal("0"), Decimal("5"), Decimal("0")),
        (Decimal("5"), Decimal("0"), Decimal("1")),
    ])
    def test_power(self, calc, base, exponent, expected):
        """Test the power method."""
        assert calc.power(base, exponent) == expected

    @pytest.mark.parametrize("number, expected", [
        (Decimal("9"), Decimal("3")),
        (Decimal("0"), Decimal("0")),
        (Decimal("0.25"), Decimal("0.5")),
    ])
    def test_sqrt(self, calc, number, expected):
        """Test the sqrt method."""
        assert calc.sqrt(number) == expected

class TestErrorHandling:
    def test_invalid_string_input_raises_type_error(self, calc):
        """Test that non-numeric string input raises a TypeError."""
        with pytest.raises(TypeError, match="Invalid numeric string: a"):
            calc.add("a", 5)

    def test_non_numeric_input_raises_type_error(self, calc):
        """Test that non-numeric, non-string input raises a TypeError."""
        with pytest.raises(TypeError, match="All inputs must be numeric"):
            calc.add([1, 2], 5)

    def test_divide_by_zero_raises_zero_division_error(self, calc):
        """Test that division by zero raises a ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            calc.divide(Decimal("5"), Decimal("0"))

    def test_power_zero_to_zero_raises_value_error(self, calc):
        """Test that 0^0 raises a ValueError."""
        with pytest.raises(ValueError, match="0 to the power of 0 is undefined"):
            calc.power(Decimal("0"), Decimal("0"))

    def test_sqrt_negative_number_raises_value_error(self, calc):
        """Test that sqrt of a negative number raises a ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
            calc.sqrt(Decimal("-4"))