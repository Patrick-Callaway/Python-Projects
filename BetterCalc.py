# Get input

num1 = float(input("Enter a number: "))
op = input("Enter an operator: +, -, *, /: ")
num2 = float(input("Enter a number: "))

# If statements - Calculations

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    print("Invalid Operator")