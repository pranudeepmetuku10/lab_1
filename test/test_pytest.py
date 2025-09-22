import pytest
from src import calculator

# Test fun1 (addition) with multiple inputs
@pytest.mark.parametrize("x,y,expected", [
    (2, 3, 5),
    (-1, 5, 4),
    (0, 0, 0),
    (2.5, 3.5, 6.0)
])
def test_fun1(x, y, expected):
    assert calculator.fun1(x, y) == expected

# Test fun2 (subtraction)
def test_fun2():
    assert calculator.fun2(10, 4) == 6
    assert calculator.fun2(-2, -3) == 1

# Test fun3 (multiplication)
def test_fun3():
    assert calculator.fun3(3, 4) == 12
    assert calculator.fun3(0, 5) == 0

# Test fun4 (combination)
def test_fun4():
    # fun4 should now accept 3 arguments if you updated it
    assert calculator.fun4(2, 3, 5) == calculator.fun1(2, 3) + calculator.fun2(2, 3) + calculator.fun3(2, 3) + 5

# Test fun5 (division)
def test_fun5_division():
    assert calculator.fun5(10, 2) == 5

def test_fun5_zero_division():
    with pytest.raises(ZeroDivisionError):
        calculator.fun5(5, 0)

# Test fun6 (power)
def test_fun6_power():
    assert calculator.fun6(2, 3) == 8
    assert calculator.fun6(5, 0) == 1

# Test invalid inputs for type checking
def test_invalid_inputs():
    with pytest.raises(TypeError):
        calculator.fun1("a", 3)
    with pytest.raises(TypeError):
        calculator.fun2(2, "b")