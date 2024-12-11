def fib(n: int) -> int:
    """
    Calculate the nth Fibonacci number.

    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
    usually starting with 1 and 1. This function uses a recursive approach to calculate the nth number
    in the sequence.

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


def test_fib():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(5) == 8


def test_fib_exception():
    import pytest

    with pytest.raises(ValueError):
        fib(-1)


def test_github_actions_ruff_lint():
    pass


def test_github_actions_ruff_format():
    fib(1)
