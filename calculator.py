

###  main function to run the calculator
def simplecalculator():
    print("choise operation:")
    print("1. Addition")
    print("2. subtraction")
    print("3. Multiplication")
    print("4. Division")

    # enter the input 
    choice = input("Enter choice(1/2/3/4): ")

    # Check condition is vlaid or not
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {addition(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtraction(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiplication(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {division(num1, num2)}")
    else:
        print("Invalid input number")


simplecalculator()
