import pytest

# def my_func(x, y, z):
#     return x + y + z
#
# def test_result1():
#     assert (1, 2, 3) == 5

def my_exeption():
    div = 10 / 0
    return div

def test_result2():
    with pytest.raises(ZeroDivisionError):
        my_exeption()


