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
    if a == 0 and b < 0:
        raise ValueError("Cannot raise zero to a negative power!")
    if a < 0 and isinstance(b, float) and not b.is_integer():
        raise ValueError("Cannot calculate power with negative base and fractional exponent (non-real result)!")
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number!")
    return math.sqrt(a)

def percentage(value, percent):
    return (value * percent) / 100

def main():
    print("--- Simple Calculator (Advanced) ---")
    print("Operations: +, -, *, /, power, sqrt, %")
    print("Type 'exit' to quit.")

    while True:
        try:
            choice = input("\nEnter operation (or 'exit'): ").strip().lower()
            if choice == 'exit':
                break

            if choice == 'sqrt':
                num = float(input("Enter number: "))
                print(f"Result: {square_root(num)}")
            elif choice == '%':
                val = float(input("Enter value: "))
                per = float(input("Enter percentage: "))
                print(f"Result: {percentage(val, per)}")
            elif choice in ['+', '-', '*', '/', 'power']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '+': print(f"Result: {add(num1, num2)}")
                elif choice == '-': print(f"Result: {subtract(num1, num2)}")
                elif choice == '*': print(f"Result: {multiply(num1, num2)}")
                elif choice == '/': print(f"Result: {divide(num1, num2)}")
                elif choice == 'power': print(f"Result: {power(num1, num2)}")
            else:
                print("Invalid operation! Please try again.")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
