import calcart

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiplication (n1, n2):
    return n1 * n2
def division (n1, n2):
    return n1 / n2

operants = {
    "+": add,
    "-": subtract,
    "*": multiplication,
    "/": division
}

def calculator():
    print(calcart.logo)
    continuation = True
    num1 = float(input("Enter first number: "))

    while continuation:
        for symbol in operants:
            print(symbol)
        operation_symbol = input("Enter operation: ")
        num2 = float(input("Enter second number: "))
        answer = operants[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue1= (input(f'Do you want to continue calculation with {answer}? '
                          f'Type "y" to continue or "n" to start a new calculation: '))

        if continue1 == "y":
            num1 = answer
            print("\n" * 20)
        else:
            continuation = False
            calculator()

calculator()