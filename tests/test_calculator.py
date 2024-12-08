import pytest

from precheck.calculator import add, subtract, multiply, divide

def test_add():
    """Tests addition."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    """Tests subtraction."""
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2

def test_multiply():
    """Tests multiplication."""
    assert multiply(3, 4) == 12
    assert multiply(-1, 5) == -5

def test_divide():
    """Tests division."""
    assert divide(10, 2) == 5
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)

