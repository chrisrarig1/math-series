import pytest
from math_series.series import fibonacci,lucas

def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_eight():
    actual = fibonacci(8)
    expected = 21
    assert actual == expected


def test_luctwo():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucfive():
    actual = lucas(5)
    expected = 11
    assert actual == expected