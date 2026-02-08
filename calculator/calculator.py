import json


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def load_config(path="config.json"):
    with open(path, "r") as file:
        return json.load(file)


if __name__ == "__main__":
    print("=== Simple CLI Calculator ===")

    # Load allowed operations from config.json
    try:
        config = load_config()
        allowed_ops = config.get("operations", [])
    except FileNotFoundError:
        print("config.json not found.")
        exit(1)

    # Input numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        exit(1)

    # Input operation
    print(f"Allowed operations: {allowed_ops}")
    op = input("Choose operation: ")

    if op not in allowed_ops:
        print("Invalid operation selected.")
        exit(1)

    # Perform calculation
    try:
        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)
        else:
            print("Operation not supported.")
            exit(1)

        print(f"Result: {result}")

    except ValueError as e:
        print(f"Error: {e}")
