import pytest
from math_series.series import fibonacci,lucas,sum_series

# fibonacci tests
def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_not20():
    actual = fibonacci(9)
    expected = 20
    assert actual != expected


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

# Lucas tests

def test_luctwo():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucfive():
    actual = lucas(5)
    expected = 11
    assert actual == expected

# Sum Function Tests

def test_sumfib():
    actual = sum_series(2)
    expected = 1
    assert actual == expected

def test_sumlucas():
    actual = sum_series(2, 2,1)
    expected = 3
    assert actual == expected

def test_sum6():
    actual = sum_series(6, 3,5)
    expected = 55
    assert actual == expected