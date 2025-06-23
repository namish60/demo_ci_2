# test_calculator.py
from calculator import add, sub, mul, div

def test_operations():
    assert add(2, 3) == 5
    assert sub(5, 3) == 2
    assert mul(4, 3) == 12
    assert div(10, 2) == 5
    assert div(10, 0) is None  # Because you return None on division by zero
