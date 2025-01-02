def calculator():
    def get_number(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")

    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the number of the operation (1/2/3/4): ")

    if operation not in ('1', '2', '3', '4'):
        print("Invalid operation choice. Please restart the program.")
        return

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    if operation == '1':
        result = num1 + num2
        operator = '+'
    elif operation == '2':
        result = num1 - num2
        operator = '-'
    elif operation == '3':
        result = num1 * num2
        operator = '*'
    elif operation == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        operator = '/'

    print(f"{num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    calculator()
