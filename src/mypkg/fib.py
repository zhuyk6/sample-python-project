"""
This module provides functions to calculate Fibonacci numbers.
"""


def fib(n: int) -> int:
    """Calculate the nth Fibonacci number using the recursive approach.

    The Fibonacci sequence is defined as follows:
    - F(0) = 1
    - F(1) = 1
    - F(n) = F(n-1) + F(n-2) for n > 1

    Args:
        n (int): The position in the Fibonacci sequence to calculate. Must be a non-negative integer.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.

    Examples:
        >>> fib(0)
        1
        >>> fib(1)
        1
        >>> fib(5)
        8
    """
    if n < 0:
        raise ValueError(f"n must be a non-negative, but {n} is given.")
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_iter(n: int) -> int:
    """Calculate the nth Fibonacci number using an iterative approach.

    Args:
        n (int): Nth Fibonacci number to calculate.

    Raises:
        ValueError: If n is a negative integer.

    Returns:
        int: The nth Fibonacci number.
    """
    if n < 0:
        raise ValueError(f"n must be a non-negative, but {n} is given.")
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        f0, f1 = 1, 1
        for i in range(2, n + 1):
            f0, f1 = f1, f0 + f1
        return f1
