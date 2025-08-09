def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Can't "

def floor_divide(a , b):
    if b != 0:
        return a // b
    else:
        return "Can't "

def modulus(a , b):
    if b != 0:
        return a % b
    else:
        return "Can't "

def power(a, b):
    return a ** b


def calculator(a, b, op):
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "//": floor_divide,
        "%": modulus,
        "**": power
    }

    if op in operations:
        return operations[op](a, b)
    else:
        return "Not a valid operation"


num1 = int(input("Enter first Number  : "))
num2 = int(input("Enter second Number : "))
operator = input("Enter Operation : ")

result = calculator(num1, num2, operator)
print(f"Result: {result}")


