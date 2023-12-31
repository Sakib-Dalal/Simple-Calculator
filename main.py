# Calculator

# Addition
def addition(n1, n2):
    return n1 + n2


# Subtraction
def subtraction(n1, n2):
    return n1 - n2


# Multiplication
def multiplication(n1, n2):
    return n1 * n2


# Division
def division(n1, n2):
    return n1 / n2


operations = {"+": addition, "-": subtraction, "*": multiplication, "/": division}

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from above list: ")

calculator_function = operations[operation_symbol]
answer = calculator_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")