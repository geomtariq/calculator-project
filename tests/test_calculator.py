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
        (Decimal("2"), Decimal("3"), Decimal("5")),          # Positive integers
        (Decimal("-1"), Decimal("-1"), Decimal("-2")),       # Negative integers
        (Decimal("-5"), Decimal("5"), Decimal("0")),         # Mixed sign
        (Decimal("1.5"), Decimal("2.5"), Decimal("4.0")),    # Decimals
        (Decimal("0"), Decimal("0"), Decimal("0")),          # Zeros
    ])
    def test_add(self, calc, a, b, expected):
        """Test the add method."""
        assert calc.add(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (Decimal("5"), Decimal("3"), Decimal("2")),          # Positive integers
        (Decimal("-1"), Decimal("-1"), Decimal("0")),        # Negative integers
        (Decimal("5"), Decimal("-5"), Decimal("10")),        # Mixed sign
        (Decimal("4.5"), Decimal("2.5"), Decimal("2.0")),    # Decimals
        (Decimal("0"), Decimal("0"), Decimal("0")),          # Zeros
    ])
    def test_subtract(self, calc, a, b, expected):
        """Test the subtract method."""
        assert calc.subtract(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (Decimal("2"), Decimal("3"), Decimal("6")),          # Positive integers
        (Decimal("-2"), Decimal("-3"), Decimal("6")),        # Negative integers
        (Decimal("-2"), Decimal("3"), Decimal("-6")),        # Mixed sign
        (Decimal("1.5"), Decimal("2"), Decimal("3.0")),      # Decimals
        (Decimal("10"), Decimal("0"), Decimal("0")),         # With zero
    ])
    def test_multiply(self, calc, a, b, expected):
        """Test the multiply method."""
        assert calc.multiply(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (Decimal("6"), Decimal("3"), Decimal("2")),          # Positive integers
        (Decimal("-6"), Decimal("-3"), Decimal("2")),        # Negative integers
        (Decimal("-6"), Decimal("3"), Decimal("-2")),        # Mixed sign
        (Decimal("7.5"), Decimal("2.5"), Decimal("3.0")),    # Decimals
        (Decimal("0"), Decimal("5"), Decimal("0")),          # Zero dividend
    ])
    def test_divide(self, calc, a, b, expected):
        """Test the divide method."""
        assert calc.divide(a, b) == expected
