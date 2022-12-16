import time


# This function adds two numbers
def add(x, y):
    if type(x) is not int or type(y) is not int:
        raise TypeError("Cannot perform addition on strings")
    return x + y


def add_slow(x, y):
    time.sleep(4)
    if type(x) is not int or type(y) is not int:
        raise TypeError("Cannot perform addition on strings")
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y

