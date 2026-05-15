import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number!")
    return math.sqrt(a)

def percentage(value, percent):
    return (value * percent) / 100

if __name__ == "__main__":
    print("Simple Calculator (Advanced)")
    print("1 + 2 =", add(1, 2))
    print("2 ^ 3 =", power(2, 3))
    print("sqrt(16) =", square_root(16))
    print("20% of 500 =", percentage(500, 20))
