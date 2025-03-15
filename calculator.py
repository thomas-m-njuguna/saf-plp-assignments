# Get user inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+ - / * or x): ")

# Perform calculation based on operator
if operator == "+":
    result = num1 + num2
    print("The sum of the two numbers is:", result)

elif operator == "-":
    result = abs(num1 - num2)  # Always show positive difference
    print("The difference of the two numbers is:", result)

elif operator == "/":
    if num2 != 0:  # Prevent division by zero
        result = num1 / num2
        print("The division of the two numbers is:", result)

    else:
        print("Error: Cannot divide by zero!")
elif operator == "*" or operator == "x":
    result = num1 * num2
    print("The product of the two numbers is:", result)

else:
    print("Invalid operator entered!")
