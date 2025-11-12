
# Ask the user for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Ask the user to choose an operator
operator = input("Enter an operator (+, -, *, /): ")

# Perform the operation using if statements
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    result = "Invalid operator"

# Print the result
print("Result:", result)
