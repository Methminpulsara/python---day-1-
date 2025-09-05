
try:
    integer_input = int(input("Enter Words : "))
    print("added" + integer_input)
except TypeError :
    print("Type Error")
except ValueError:
    print("Value Error")


try:
    integer_input = int(input("Enter Words : "))
    print("added" + integer_input)
except (TypeError , ValueError) :
    print("Only can numbers")
