try:
    integer_input = int(input("Enter Words : "))
    print("added" ,1 + integer_input)
except (TypeError , ValueError) :
    print("Only can numbers")
else:
    print("No errors")
finally:
    print("Executed no matter what (finally block)")