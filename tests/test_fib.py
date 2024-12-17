from mypkg.fib import fib
import pytest


def test_fib():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(5) == 8


def test_fib_exception():
    with pytest.raises(ValueError):
        fib(-1)


def test_github_actions_ruff_lint():
    pass


def test_github_actions_ruff_format():
    fib(1)
