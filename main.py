# Calculator

from art import logo


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


def calculator():
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation from above list: ")

    calculator_function = operations[operation_symbol]
    answer = calculator_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")


is_calculation_stop = False

print(logo)
calculator()

while not is_calculation_stop:
    end_or_not = input("Enter 'yes' to end the calculator, or 'no' for new calculation: ").lower()
    if end_or_not == 'no':
        is_calculation_stop = False
        calculator()  # use of recursion in function
    else:
        is_calculation_stop = True
