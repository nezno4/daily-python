# -*- coding: utf-8 -*-
def add(a: float, b: float) -> float:
    """Adds two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtracts the second number from the first."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divides first number by second. Exception if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
