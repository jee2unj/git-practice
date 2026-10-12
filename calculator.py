"""Basic arithmetic operations for a small calculator."""


def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of two numbers."""
    return a + b


def sub(a: int | float, b: int | float) -> int | float:
    """Return the difference between two numbers."""
    return a - b


def mul(a: int | float, b: int | float) -> int | float:
    """Return the product of two numbers."""
    return a * b


def div(a: int | float, b: int | float) -> float:
    """Return the quotient of two numbers.

    Raises:
        ZeroDivisionError: If the divisor is zero.
    """
    return a / b


def main() -> None:
    """Run a short demonstration of the calculator functions."""
    examples = (
        ("3 * 4", mul(3, 4)),
        ("3 + 4", add(3, 4)),
        ("4 - 3", sub(4, 3)),
        ("4 / 2", div(4, 2)),
    )
    for expression, result in examples:
        print(f"{expression} = {result}")


if __name__ == "__main__":
    main()
