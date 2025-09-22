def validate_inputs(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Inputs must be numeric")

def fun1(x, y):
    validate_inputs(x, y)
    """Adds two numbers"""
    return x + y

def fun2(x, y):
    validate_inputs(x, y)
    """Subtracts y from x"""
    return x - y

def fun3(x, y):
    validate_inputs(x, y)
    """Multiplies two numbers"""
    return x * y

def fun4(x, y):
    validate_inputs(x, y)
    """Returns the sum of results from fun1, fun2, and fun3"""
    return fun1(x, y) + fun2(x, y) + fun3(x, y)

def fun5(x, y):
    validate_inputs(x, y)
    if y == 0:
        raise ZeroDivisionError("Division by zero not allowed")
    return x / y

def fun6(x, y):
    validate_inputs(x, y)
    return x ** y