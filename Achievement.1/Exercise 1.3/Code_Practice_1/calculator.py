
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+ or -): ")

if operator == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")
else:
    print("Unknown operator")
