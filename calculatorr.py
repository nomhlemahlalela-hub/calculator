# Simple Calculator without try-except

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Check if the inputs are numbers
if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():
    num1 = float(num1)
    num2 = float(num2)

    print("Choose operator: +, -, *, /")
    operator = input("Enter operator: ")

    if operator == '+':
        print("Result:", num1 + num2)
    elif operator == '-':
        print("Result:", num1 - num2)
    elif operator == '*':
        print("Result:", num1 * num2)
    elif operator == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)
    else:
        print("Error: Invalid operator!")
else:
    print("Error: Please enter valid numbers only!")


