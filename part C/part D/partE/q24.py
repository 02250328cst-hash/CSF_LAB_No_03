def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

while True:
    # Display menu
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ").strip()

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            # Take two numbers in a single line separated by space
            num1, num2 = map(float, input("Enter two numbers: ").split())
        except ValueError:
            print("Invalid input! Please enter two numbers separated by space.")
            continue

        if choice == '1':
            print("Sum =", add(num1, num2))
        elif choice == '2':
            print("Difference =", subtract(num1, num2))
        elif choice == '3':
            print("Product =", multiply(num1, num2))
        elif choice == '4':
            result = divide(num1, num2)
            if result == "Error: Division by zero":
                print(result)
            else:
                print("Quotient =", result)
    else:
        print("Invalid choice! Please select 1-5 only.")