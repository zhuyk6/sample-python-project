import pytest
import mypkg.fib as fib


def test_fib():
    assert fib.fib(0) == 1
    assert fib.fib(1) == 1
    assert fib.fib(5) == 8

    with pytest.raises(ValueError):
        fib.fib(-1)
