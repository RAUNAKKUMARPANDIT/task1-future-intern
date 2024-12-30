#  addition function
def add(x, y):
    return x + y

#  subtraction function
def subtract(x, y):
    return x - y

#  multiplication Function
def multiply(x, y):
    return x * y

#    division Function
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Main program  calculator
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # enter input
    choice = input("Enter choice(1/2/3/4): ")

    # verify condition true or false
    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform calculation based on the user's choice
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid choice! Please select a valid operation (1/2/3/4).")

# Run the calculator
if __name__ == "__main__":
    calculator()


