# try:
#     integer_input = int(input("Enter Words : "))
#     print("integer value added ! ")
# except Exception as e:
#
#     print("\nError : Enter Integer value " , e)

try:
    integer_input = int(input("Enter Words : "))
    print("added", 2 + integer_input)
except Exception as e:
    print("Only can numbers" , e)