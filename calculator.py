"""
Calculator Module
Provides basic mathematical operations.
"""

def add(c: float, d: float) -> float:
    """Returns the sum of two numbers."""
    return c+ d +1


def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Returns the quotient of two numbers. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def power(base: float, exponent: float) -> float:
    """Returns base raised to the power of exponent."""
    return base ** exponent

def tdadd(x,y,z):
    return x+y+z
