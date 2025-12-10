def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def perform_calculation():
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ").strip()
        b = float(input("Enter second number: "))

        if op == "+":
            return add(a, b)
        elif op == "-":
            return subtract(a, b)
        elif op == "*":
            return multiply(a, b)
        elif op == "/":
            return divide(a, b)
        else:
            print(" Invalid operator!")
            return None

    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return None
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None

def calculator():
    while True:
        print("\n======= Simple Calculator =======")
        print("1. Calculate")
        print("2. Clear")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            result = perform_calculation()
            if result is not None:
                print(f"Result: {result}")

        elif choice == "2":
            print("Calculator cleared!")

        elif choice == "3":
            print("Exiting calculator...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    calculator()