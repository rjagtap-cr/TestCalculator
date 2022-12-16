import pytest
from pytest_mock import mocker
from basic_calculations import add, subtract, multiply, divide, add_slow


@pytest.mark.parametrize('a, b, val', [
    (5, 5, 10), (2, 3, 5), (1, -5, -4)
])
def test_add(a, b, val):
    assert add(a, b) == val


@pytest.mark.parametrize('a, b, val', [
    ("Hi ", "Hello", "Hi Hello"),
    (1.2, 2.3, 3.5),
    # (1, 2, 3) This is fail
])
def test_add_fails(a, b, val):
    with pytest.raises(TypeError, match="Cannot perform addition on strings"):
        assert add(a, b) == val


def test_subtract():
    assert subtract(5, 5) == 0
    assert subtract(-2, 2) == -4


def test_multiply():
    assert multiply(5, 5) == 25
    assert multiply(-2, 2) == -4


def test_divide():
    assert divide(5, 5) == 1
    assert divide(-2, 2) == -1
